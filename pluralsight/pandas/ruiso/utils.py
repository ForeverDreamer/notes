from collections import OrderedDict
import contextlib
import sys

import pandas as pd
from pymongo import MongoClient

LOG_COLLS = ('log_search', 'log_recommend')


@contextlib.contextmanager
def mongo_client():
    # <ENTER>
    client = MongoClient('')
#     print('clr数据库连接成功！')
    try:
        # Like __enter__()'s return statement
        yield client
        # <NORMAL EXIT>
        client.close()
#         print('clr关闭数据库！')
    except Exception:
        # <EXCEPTIONAL EXIT>
        print('mongo_client: exceptional exit', sys.exc_info())
        raise


# def top_search_transform_trend():
#     with mongo_client() as mongo:
#         d = mongo.get_default_database()
#         docs = d[LOG_COLLS[0]].find(
#             {'cmd': 'search_global'},
#             ('tokens', 'user_actions', 'result.docs._id', 'create_time')
#         )
#         records = []
#         dic = {}
#         for doc in docs:
#             tokens = doc.pop('tokens', None)
#             # 搜索量趋势
#             if not tokens:
#                 continue
#             for token in tokens:
#                 if token in dic:
#                     dic[token] += 1
#                 else:
#                     dic[token] = 1
#             dic_list = list(dic.items())
#             dic_list.sort(key=lambda elem: elem[1], reverse=True)
#             # 转化率趋势
#             user_actions = doc.get('user_actions')
#             if not user_actions:
#                 continue
#             for token in tokens:
#                 for doc_id, actions in user_actions.items():
#                     records.append({'token': token, 'doc_id': doc_id, 'time': doc['create_time'], 'click': 1, 'stay': 1 if actions.get('stay') else 0})
#         df = pd.DataFrame(records)
#
#     df['time'] = df['time'].dt.date
#     df = df.set_index('time')
#     # df = df.sort_index()
#     group_df = df.groupby(by=['token', 'time']).agg({'click': 'sum', 'stay': 'sum'})
#     group_df = group_df.sort_index(level=['token', 'time'])
#     dic = {}
#     for index, rate in round(group_df['stay'] / group_df['click'], 2).to_dict().items():
#         token = index[0]
#         date = str(index[1])
#         if token in dic:
#             dic[token][date] = rate
#         else:
#             dic[token] = {}
#             dic[token][date] = rate
#
#     return {'top_n': dic_list, 'transform': dic}


def stats_top_search():
    with mongo_client() as mongo:
        d = mongo.get_default_database()
        docs = d[LOG_COLLS[0]].find(
            {'cmd': 'search_global'},
            ('tokens', 'user_actions', 'result.docs._id', 'create_time')
        )
        records = []
        dic = {}
        for doc in docs:
            tokens = doc.pop('tokens', None)
            # 搜索量趋势
            if not tokens:
                continue
            for token in tokens:
                if token in dic:
                    dic[token] += 1
                else:
                    dic[token] = 1
            dic_list = list(dic.items())
            dic_list.sort(key=lambda elem: elem[1], reverse=True)
            # 转化率趋势
            user_actions = doc.get('user_actions')
            if not user_actions:
                continue
            for token in tokens:
                for doc_id, actions in user_actions.items():
                    records.append({'token': token, 'doc_id': doc_id, 'time': doc['create_time'], 'click': 1, 'stay': 1 if actions.get('stay') else 0})
        df = pd.DataFrame(records)

    df = df.set_index('time')
    df = df.groupby(by=["token"]).resample('1D').agg({'click': 'sum', 'stay': 'sum'})

    start = '2022-10-11'
    end = '2022-11-10'
    delta = pd.to_datetime(end) - pd.to_datetime(start) + pd.to_timedelta('1D')
    length = delta.days
    default = pd.DataFrame([{'click': 0, 'stay': 0}] * length, index=pd.date_range(start=start, end=end))
    dfs = []
    keys = set()
    for index, row in df.iterrows():
        if index[0] in keys:
            continue
        _df = (df.loc[index[0]] + default).fillna(0).astype('int32').assign(
            token=pd.Series([index[0]] * length, index=default.index))
        #         print(_df)
        dfs.append(_df)
        keys.add(index[0])
    df = pd.concat(dfs)
    df = df.reset_index().set_index(['token', 'index']).sort_index(level=['token', 'index'])
    dic = {}
    for index, rate in round((df['stay'] / df['click']).fillna(0), 2).to_dict().items():
        token = index[0]
        date = str(index[1])
        if token in dic:
            dic[token][date] = rate
        else:
            dic[token] = {}
            dic[token][date] = rate

    return {'top_n': dic_list, 'transform': dic}
