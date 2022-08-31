from .utils import *


def main():
    # df = load_from_directory()
    # save_to_pickle(df, 'origin')
    # df = load_from_pickle('zhichi_dropna')
    # df = df.groupby('会话ID')[['消息内容', 'MsgLen']].transform(flag_invalid)
    # df = flag_invalid(df.groupby('会话ID'))
    # df.sort_values(by=['会话ID', '消息时间'])
    # df.to_excel('zhichi_processed.xlsx')
    # xiaorui_match_all()
    # missing_index_assign_test()
    df = load_from_pickle('zhichi_vs_xiaorui')
    df = (df.pipe(remove_unnamed_columns)
          .pipe(fill_unknown)
          .pipe(reformat_answers)
          .pipe(add_zhichi_answer)
          .pipe(column_rename, {'XrAnswer': '小睿答案'})
          .pipe(column_reorder, ['会话ID', '消息时间', '来源类型', '目标类型', 'MsgLen', 'IsFirstQ', '消息内容', '智齿答案', '小睿答案']))
    df = df[df['IsFirstQ'] == 1]
    save_to_excel(df, 'zhichi_vs_xiaorui')
    # df = load_from_excel('zhichi_vs_xiaorui')
    # save_to_pickle(df, 'zhichi_vs_xiaorui')


if __name__ == "__main__":
    main()

# 已看完5000行
# invalid_questions = {
#     'hi', '您好', '不会', '您好！', '3', '20238200620027', '人工客服', '人工', '不是', '2', '都不是', '你好', 'aa', '人工服务',
#     '转人工', '1', '没有答案', '人工咨询', '9443', '留言', '5', '您有人工服务吗？', '请问这是什么平台', '客服', '热线', '咨询热线',
#     '回答不错', '再见', '人工？', '否', '无法登录', '咨询电话', '联系电话', '查询', '我有录音', '电话', '有人工座机电话吗',
#     'dianhuahaoma', '电话号码', '你能处理啥事', '真失望', '进不了', '怎么敏感了？！', '是人工服务吗', '六日上班吗', '在吗', '？',
#     '5', '您好(?▽?)', 'ni?hao', '人工吗', '不懂', '这不是我想要的答案', '好', '回', '697723', '高', '？？？', '贪污的人', '我要举报',
#     '投诉', '0', '三年高达五万', '我不是企业', '我是个人', '有人吗', '打扰国委了', '政务大厅电话', '服务电话', '你', '发改委电话', '回答呀',
#     '4', '太难', '讨新', '丨讨讨二', 'h', '怎么样不敏感', '不晓得问什么', '不是这个', '算了吧不问了没意义', '能看到吗？', '|', '13946361172',
#     '想', '没有', '这不是我想要的答案', '此默你留言', '请问有人工吗？'
# }
