scenes = {
    's0': [
        [
            '大家好，我是IT学长，今天跟大家分享的是力扣 "剑指 Offer 07. 重建二叉树"',
            '题目链接已打在屏幕下方，有兴趣的同学可以去力扣官网提交代码测试运行结果',
            '我们看一下题目描述'
        ],
    ],
    's1': [
        [
            '输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点',
            '假设输入的前序遍历和中序遍历的结果中都不含重复的数字',
        ],
        [
            '题目举了两个例子帮助理解题意',
            '示例 1',
            '前序遍历的结果是[3,9,20,15,7]，中序遍历的结果是[9,3,15,20,7]',
            '重建出来的二叉树为[3,9,20,null,null,15,7]',
            '画出来是这个样子的',
        ],
        [
            '示例 2',
            '如果前序遍历的结果是[-1]，中序遍历的结果是[-1]',
            '重建出来的二叉树为[-1]',
            '此种为空树情况',
        ],
        [
            '限制条件：0 <= 节点个数 <= 5000',
            '我们实现算法时需要根据限制条件考虑时间复杂度和空间复杂度问题',
            '否则即使本地调试通过，提交到力扣依然会因为复杂度太高而无法通过全部测试用例',
        ]
    ],
    's2': [
        [
            '解题之前我们必须要知道两种遍历方式的含义',
            '前序遍历任何一个节点，都是按照根节点->左子树->右子树的顺序进行',
            '过程用动画演示出来是这样的',
            '遍历结果按照[根节点|左子树|右子树]排序',
            '因此前序遍历结果的第一个元素即为树的根节点',
            '但无法确定左子树和右子树',
        ],
    ],
    's3': [
        [
            '中序遍历任何一个节点，都是按照左子树->根节点->右子树的顺序进行',
            '过程用动画演示出来是这样的',
            '遍历结果按照[左子树|根节点|右子树]排序',
            '只要找到根节点，就能确定左子树和右子树'
        ],
    ],
    's4': [
        [
            '题目描述中包含前序遍历和中序遍历的结果中都不含重复的数字假设',
        ],
    ],
    's5': [
        [
            '因此前序遍历的根节点key和中序遍历中的key是一样的，都是3',
            '由此可以定位中序遍历结果中根节点的位置',
            '根据中序遍历结果[左子树|根节点|右子树]排序的性质',
            '可以进一步定位左子树和右子树的分布区域',
            '最后根据两者长度定位前序遍历结果中左子树和右子树的分布区域',
            '根据这种方式就可以递归地划分出左右所有子树的数据排列',
            '然后把二叉树重建回来'
        ],
    ],
}