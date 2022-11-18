import json

BASE_DIR = 'D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/'
IMPORT_AS_TYPE = ('COMP_CROPPED_LAYERS', 'FOOTAGE', 'COMP', 'PROJECT')

data = {
    'queues': [
        {'name': 'preorder', 'pos': [100, 100, 0], 'elems': [3, 9, 20, 15, 7]},
        {'name': 'inorder', 'pos': [100, 200, 0], 'elems': [9, 3, 15, 20, 7]}
    ],
    'files': [
        {'path': f'{BASE_DIR}代码.jpg', 'import_as_type': IMPORT_AS_TYPE[1], 'pos': [1398, 540, 0]}
    ],
}

# Serializing json
obj = json.dumps(data, indent=4)
print(obj)
with open("D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/conf.json", 'w', encoding='utf-8') as f:
    f.write(obj)
