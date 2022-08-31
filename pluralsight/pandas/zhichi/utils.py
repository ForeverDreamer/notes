import pandas as pd
import os
from datetime import datetime as dt

import requests as http

from .constants import *


# def load():
#     df = pd.read_csv(CSV_PATH, encoding='gbk', usecols=['来源类型', '消息内容'])
#     senders = df['来源类型'].to_list()
#     messages = df['消息内容'].to_list()
#     print(len(senders))
#     print(len(messages))
#     with open("访客消息_50字内.txt", "wt", encoding='utf-8') as f:
#         for sender, message in zip(senders, messages):
#             if sender == '访客' and len(message) <= 50:
#                 f.write(f'{message}\n')


def load_from_directory(directory=ROOT_PATH):
    dfs = []
    for root, directories, files in os.walk(directory):
        for f in files:
            if f.endswith('csv'):
                dfs.append(pd.read_csv(os.path.join(root, f), encoding='gbk'))
            else:
                dfs.append(pd.read_excel(os.path.join(root, f)))
    return pd.concat(dfs)


def load_from_excel(name):
    return pd.read_excel(os.path.join(ROOT_PATH, f'{name}.xlsx'))


def save_to_excel(df, name):
    df.to_excel(os.path.join(ROOT_PATH, f'{name}.xlsx'))


def load_from_pickle(name):
    return pd.read_pickle(os.path.join(ROOT_PATH, f'{name}.pickle'))


def save_to_pickle(df, name):
    df.to_pickle(os.path.join(ROOT_PATH, f'{name}.pickle'))


# def flag_invalid(df):
#     cond1 = (df['来源类型'] == '访客')
#     cond2 = (df['MsgLen'] <= 5)
#     cond3 = (df['消息内容'].str.contains('^[你您]好'))
#     cond4 = (df['消息内容'].str.contains('^[^\u4e00-\u9fa5]*$'))
#     cond5 = (df['消息内容'].str.contains('人工|客服'))
#     # cond6 = (df['消息内容'].str.contains('电话|热线|座机'))
#     cond6 = (df['消息内容'].str.contains('有人吗|在吗|不是|谢谢|再见'))
#     cond7 = (df['MsgLen'] <= 1)
#     cond = df[~((cond1 & cond2) & (cond3 | cond4 | cond5 | cond6 | cond7))].filter(['来源类型', '消息内容'])
#     return df


def flag_invalid(groups):
    group_dfs = []
    for _id, df in groups:
        cond1 = (df['来源类型'] == '访客')
        cond2 = (df['MsgLen'] <= 5)
        cond3 = (df['消息内容'].str.contains('^[你您]好'))
        cond4 = (df['消息内容'].str.contains('^[^\u4e00-\u9fa5]*$'))
        cond5 = (df['消息内容'].str.contains('人工|客服'))
        cond6 = (df['消息内容'].str.contains('有人吗|在吗|不是|谢谢|再见'))
        cond7 = (df['MsgLen'] <= 1)
        cond8 = (df['MsgLen'] > 200)
        cond_series = ~(cond4 | cond7 | cond8 | (cond2 & (cond3 | cond5 | cond6))) & cond1
        found = False
        flags = {}
        for idx, value in cond_series.items():
            if found:
                flags[idx] = 0
                continue
            if value:
                flags[idx] = 1
                found = True
            else:
                flags[idx] = 0
        group_dfs.append(df.assign(IsFirstQ=pd.Series(flags, dtype='int32')))
    return pd.concat(group_dfs)


def xiaorui_match_all():
    rv = http.post(XIAORUI_URL, json={'cmd': 'open_session', 'params': {'xrid': 'xr1', 'userid': '123'}})
    sessionid = rv.json()['data']['sessionid']
    df = load_from_pickle('zhichi_processed')
    answers = {}
    count = 0
    for idx, q in df[df['来源类型'] == '访客']['消息内容'].items():
        if pd.isnull(q):
            continue
        rv = http.post(
            XIAORUI_URL,
            json={
                'cmd': 'match',
                'params': {
                    'sessionid': sessionid, 'q': q
                }
            }
        )
        if rv.status_code != 200:
            print()
            print('错误：', rv.text)
            continue
        try:
            docs = rv.json()['data']['qas']['docs']
            answers[idx] = '\n'.join([doc['answer']['text'] for doc in docs])
        except TypeError:
            print(rv.json()['data']['qas']['docs'])
        except KeyError:
            # print(rv.json()['data'])
            words = rv.json()['data']['words']
            answers[idx] = '敏感词：' + ', '.join([word for word in words])
        count += 1
        if count % 100 == 0:
            print(f'{dt.now()}已发送：{count}条请求，idx: {idx}')
            # break
    df = df.assign(XrAnswer=pd.Series(answers))
    save_to_excel(df, 'zhichi')


def missing_index_assign_test():
    df = load_from_pickle('zhichi_processed')[:10]
    answers = {}
    count = 0
    for idx, q in df['消息内容'].items():
        if count % 2 == 0:
            count += 1
            continue
        answers[idx] = '测试答案'
        count += 1
    df = df.assign(XrAnswer=pd.Series(answers))
    save_to_excel(df, 'missing_index_assign_test')


def remove_unnamed_columns(df):
    return df.loc[:, ~df.columns.str.contains('^Unnamed')]


def fill_unknown(df):
    def _fill(_df):
        # cond = _df['IsFirstQ'] == 1
        cond = _df['来源类型'] == '访客'
        return _df[cond]['XrAnswer'].transform(lambda answer: '抱歉没能找到相关答案，您可以换个问法试试！' if pd.isnull(answer) else answer)
    # df.loc[:, 'XrAnswer'] = df.pipe(_fill)
    df = df.assign(XrAnswer=df.pipe(_fill))
    return df


def reformat_answers(df):
    def _reformat(_df):
        def _split_answer(answer):
            if pd.isnull(answer):
                return answer
            lines = answer.split('\n')[:5]
            lines = [f'{(idx+1)}-{line}' for idx, line in enumerate(lines)]
            return '\n'.join(lines)
        return _df['XrAnswer'].transform(_split_answer)
    # df.loc[:, 'XrAnswer'] = df.pipe(_reformat)
    df = df.assign(XrAnswer=df.pipe(_reformat))
    return df


def shift_index(df, step):
    df['XrAnswer'].index = df['XrAnswer'].index + step
    # df.loc[:, 'XrAnswer'] = df['XrAnswer']
    df = df.assign(XrAnswer=df['XrAnswer'])
    return df


def add_zhichi_answer(df):
    cond = df['来源类型'] == '机器人'
    zhichi_answers = df[cond]['消息内容']
    zhichi_answers.index = zhichi_answers.index - 1
    # df.loc[:, '智齿答案'] = zhichi_answers
    df = df.assign(智齿答案=zhichi_answers)
    return df


def column_rename(df, columns):
    return df.rename(columns=columns)


def column_reorder(df, columns):
    return df.loc[:, columns]
