from redis.commands.json.path import Path

root = Path.root_path()

from utils import *

name = 'xr'

xr = {
    "_id": "xr1",
    "name": "政务咨询机器人",
    "customer": "客",
    "desc": "机器人描",
    "avatar": "avatar",
    "kb": "fgw",
    "qe": "version0.pickle",
    "answer": {
        "feedback": "引导留言文案",
        "outside": "此问题不在当前业务范围内，请尝试切换其他机器人或咨询客服人员",
        "sensitive": "您的问题较为敏感，暂无法答复。",
        "welcome": "您好，政务咨询机器人为您服务",
        "timeout": "超时下线文案",
        "unknown": "抱歉没能找到相关答案，您可以换个问法试试！"
    },
    "advanced": {
        "size": 15,
        "autocomplete": {
            "length": 3,
            "ignore": [
                "你好",
                "我想问下"
            ]
        },
        "threshold": 0.55,
        "jg": 0.04
    },
    "train": {
        "immediate": True,
        "timing": "23:04:01"
    },
    "chat_active": True,
    "active": True
}

# print(json_set(name, root, xr))
# print(json_get(name, root))
# print(json_get(name, 'name'))
# print(json_get(name, 'answer.feedback'))
# print(json_get(name, 'advanced.autocomplete.ignore'))

# print(json_type(name))

# print(json_strlen(name, 'desc'))

# print(json_strappend(name, '_appended', 'desc'))
# print(json_get(name, 'desc'))

# print(json_objlen(name, root))
# print(json_objlen(name, 'train'))

# print(json_objkeys(name, root))
# print('==========================================')
# print(json_objkeys(name, 'train'))


# print(json_numincrby(name, 'advanced.size', 1))
# print('==========================================')
# print(json_numincrby(name, 'advanced.jg', 0.1))

# print(json_delete(name, 'avatar'))
# print(json_delete(name, 'train.timing'))

# print(json_debug(name, root))
# print(json_debug(name, 'advanced'))

# print(json_arrlen(name, 'advanced.autocomplete.ignore'))
# print(json_arrinsert(name, 'advanced.autocomplete.ignore', 2, '测试'))
print(json_arrpop(name, 'advanced.autocomplete.ignore', 2))
