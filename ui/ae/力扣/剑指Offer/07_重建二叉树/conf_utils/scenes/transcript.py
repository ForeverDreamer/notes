# 开场白/过渡语/结束语，录制成单独的音频文件，方便重复使用
scenes = {
    's0': [
        [
            # 开场白start
            'Write the code, change the world!',
            '大家好，我是IT学长',
            # 开场白end
            '今天跟大家分享的是 "力扣剑指Offer 07. 重建二叉树"',
            '题目链接已打在屏幕下方，有兴趣的同学可以去力扣官网提交代码，测试运行结果',
            '我们看一下题目描述'
        ],
    ],
    's1': [
        [
            '输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点',
            '假设输入的前序遍历和中序遍历结果中都不包含重复数字',
        ],
        [
            '题目举了两个例子帮助理解题意',
            '示例 1',
            '前序遍历的结果是[3,9,20,15,7]，中序遍历的结果是[9,3,15,20,7]',
            '重建出来的二叉树用序列化表示为，[3,9,20,null,null,15,7]',
            # 停顿5秒
            '画出来是这样子的',
        ],
        [
            '示例 2',
            '如果前序遍历和中序遍历的结果都是[-1]',
            '则为空树，序列化用[-1]表示',
        ],
        [
            '限制条件：节点个数在0到5000之间',
            '我们实现算法时需要根据限制条件考虑时间和空间复杂度',
            '否则即使本地调试通过，提交到力扣依然会因为复杂度太高，而无法通过全部测试用例',
        ]
    ],
    's2': [
        [
            '解题之前我们必须要知道两种遍历方式的含义',
            '前序遍历按照根节点->左子树->右子树的顺序进行',
            '过程动画演示出来是这样子的',
            # 停顿5秒
            '遍历结果按照[根节点|左子树|右子树]排序',
            '因此前序遍历结果的第一个元素就是树的根节点',
            '但此时无法确定左子树和右子树的分布区域',
        ],
    ],
    's3': [
        [
            '中序遍历按照左子树->根节点->右子树的顺序进行',
            '过程动画演示出来是这样子的',
            # 停顿5秒
            '遍历结果按照[左子树|根节点|右子树]排序',
            '只要找到根节点的位置，左边和右边就分别是左右子树的数据'
        ],
    ],
    's4': [
        [
            '题目描述中包含“前序遍历和中序遍历的结果都不包含重复数字”的设定',
        ],
    ],
    's5': [
        [
            '因此前序遍历的根节点key和中序遍历的根节点key是相同的，都是[3]',
            '所以[3]所在的位置就是中序遍历根节点的位置',
            '[9]为左子树，长度为1，[15,20,7]为右子树，长度为3',
            '知道了左右子树的长度，就能定位前序遍历左右子树的分布了',
            '根节点往后移动左子树长度个单位就是左子树的数据',
            '继续往后移动右子树长度个单位就是右子树的数据',
        ],
        [
            '重复以上分析就可以递归地划分出左右子树以及子树的子树的数据分布',
            '然后把二叉树重建回来',
        ]
    ],
    's6': [
        [
            # 过渡语start
            '程序世界两大神器：Linux和Git 的创造者',
            'Linus Torvalds曾经曰过：Talk is cheap, show me the code!',
            '咱们话不多说，上代码！',
            # 过渡语end
        ],
    ],
    's7': [
        [
            '首先实例化并调用主函数',
            '定义递归重建函数',
            '初始化遍历结果数组的左右边界',
            '构建哈希字典，帮助我们快速定位根节点',
            '然后对树节点进行递归重建',
            '先比较左右边界位置，如果左边界大于右边界',
            '则当前子树为空，直接返回',
            '不空则先定位根节点索引，即前序遍历结果的第一个节点',
            '然后通过该节点的数值，在哈希字典中找到中序遍历根节点的索引',
            '把根节点创建出来',
            '根据中序遍历根节点的位置计算出左子树的长度',
            '就可以定位前序遍历左右子树的分布',
            '接着把前序遍历和中序遍历的左右子树边界，再分别传入递归重建函数',
            '不断重复以上分析和操作，就能递归地创建出所有树节点',
            # 播放背景音乐（自己用Logic pro x的apple loop创建一段重复使用）和剩余动画
            # 结束语start
            '以上就是本期视频的全部内容',
            '感谢收看，下次见！',
            # 结束语end
        ],
    ],
}