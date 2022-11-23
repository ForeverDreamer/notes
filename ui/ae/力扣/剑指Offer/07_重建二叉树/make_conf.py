import json
from pprint import pprint as pp
import re

BASE_DIR = 'D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/'
IMPORT_AS_TYPE = ('COMP_CROPPED_LAYERS', 'FOOTAGE', 'COMP', 'PROJECT')

codes = """
class Solution:
    def buildTree(self, preorder, inorder):
        # left和right均包含首尾元素
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None
            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点，左子树数据：前序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归地构造右子树，并连接到根节点，右子树数据：前序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)


print(Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
"""
lines = codes.strip().split('\n')
pairs = []
i = 0
while i < len(lines):
# for i in range(0, len(lines)):
    line = lines[i]
    indent = 4
    if '#' in line:
        # idx = line.find('#')
        offset0 = (len(line) - len(line.lstrip())) // indent
        offset1 = (len(lines[i+1]) - len(lines[i+1].lstrip())) // indent
        pair = [[line.strip(), offset0], [lines[i+1].strip(), offset1]]
        i += 2
    else:
        offset = (len(line) - len(line.lstrip())) // indent
        pair = [['', 0], [line.strip(), offset]]
        i += 1
    pairs.append(pair)
# pp(pairs)

# with open("D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/transcript.txt", 'r', encoding='utf-8') as f:
#     for line in f.readlines():
#         if line.startswith('#'):
#             continue
#         annotations = re.findall(r'[\S]', line)



data = {
    'queues': [
        {
            'name': 'preorder', 'pos': [100, 100, 0], 'elems': [3, 9, 20, 15, 7],
            'effects': [{'name': 'ADBE Drop Shadow'}],
            'keyframes': [{'Opacity': [[0, 1, 2], [0, 0, 100]]}]},
        {
            'name': 'inorder', 'pos': [100, 200, 0], 'elems': [9, 3, 15, 20, 7],
            'effects': [],
            'keyframes': [{'Opacity': [[0, 1, 2], [0, 0, 100]]}]
         },
    ],
    'codes': pairs,
    'files': [
        {'path': f'{BASE_DIR}代码.jpg', 'import_as_type': IMPORT_AS_TYPE[1], 'pos': [1398, 540, 0]}
    ],
    'transcript': [
        # Opacity属性可通过Python音频库分析配音后自动生成
        {'text': '大家好，我是IT学长，今天跟大家分享的是力扣 "剑指 Offer 07. 重建二叉树"', 'keyframes': [{'Opacity': [[0, 0.5, 3, 3.5], [0, 100, 100, 0]]}]},
        {'text': '题目链接已打在屏幕下方，有兴趣的同学可以去力扣官网提交代码测试运行结果', 'keyframes': [{'Opacity': [[4, 4.5, 7, 7.5], [0, 100, 100, 0]]}]},
    ],
    'annotations': [
        {'text': 'https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/', 'pos': [85, 800, 0], 'keyframes': [{'Opacity': [[4, 4.5, 7, 7.5], [0, 100, 100, 0]]}]},
    ],
}

# Serializing json
obj = json.dumps(data, indent=4)
# print(obj)
with open("D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/conf.json", 'w', encoding='utf-8') as f:
    f.write(obj)