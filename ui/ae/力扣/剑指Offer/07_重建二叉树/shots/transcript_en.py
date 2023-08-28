# 开场白/过渡语/结束语，录制成单独的音频文件，方便重复使用

subtitles = {
    0: [
        # 开场白start
        'Write the code, change the world!',
        'Hello everyone, I am an IT Xuezhang',
        # 开场白end
        'What I share with you today is "LeetCode剑指Offer 07. rebuild binary tree"',
        'The topic link has been typed at the bottom of the screen, interested students can go to LeetCode official website to submit the code and test the running results',
        "Let's look at the topic description"
    ],
    1: [
        'Input the results of preorder traversal and inorder traversal of a binary tree, please build the binary tree and return its root node',
        'Assume that neither the input preorder traversal nor the inorder traversal results contain duplicate numbers',
    ],
    2: [
        'The question gave two examples to help understand the meaning of the question',
        'Example 1',
        'The result of preorder traversal is[3,9,20,15,7], The result of inorder traversal is[9,3,15,20,7]',
        'The reconstructed binary tree is serialized as, [3,9,20,null,null,15,7]',
        # 停顿5秒
        'drawn like this',
    ],
    3: [
        'Example 2',
        'If the results of preorder traversal and inorder traversal are both[-1]',
        'Empty tree, Serialization is represented by [-1]',
    ],
    4: [
        'Restrictions: the number of nodes is between 0 and 5000',
        'When we implement the algorithm, we need to consider the time and space complexity according to the constraints',
        'Otherwise, even if the local debugging is passed and submitted to Likou, it will still fail to pass all test cases because of the complexity',
    ],
    5: [
        'Before solving the problem, we must know the meaning of the two traversal methods',
        'Preorder traversal is performed in the order of [root node -> left subtree -> right subtree]',
        'The animation of the process looks like this',
        # 停顿5秒
        'The traversal results are sorted according to [root node | left subtree | right subtree]',
        'Therefore, the first element of the result of the preorder traversal is the root node of the tree',
        'But at this time, it is impossible to determine the distribution area of the left subtree and the right subtree',
    ],
    6: [
        'Inorder traversal is performed in the order of [left subtree -> root node -> right subtree]',
        'The animation of the process looks like this',
        # 停顿5秒
        'The traversal results are sorted according to [left subtree | root node | right subtree]',
        'As long as you find the position of the root node, the left and right are the data of the left and right subtrees respectively',
        'But the root node cannot be located only by its own traversal results'
    ],
    7: [
        'The title description contains the setting that "the results of preorder traversal and inorder traversal do not contain repeated numbers"',
    ],
    8: [
        'The root node of the preorder traversal is [3]',
        'So the position of the root node of the in-order traversal is the position of [3]',
        '[9] is the left subtree, the number of nodes is 1, [15,20,7] is the right subtree, the number of nodes is 3',
        'Knowing the number of nodes in the left and right subtrees, you can locate the distribution of the left and right subtrees of the preorder traversal results',
        'Moving the root node to the right by 1 unit is the area of the left subtree',
        'Continue to move to the right 3 units is the area of the right subtree',
        'Repeating the above analysis can recursively divide the node distribution of the left and right subtrees and the subtrees of the subtrees',
        'Then rebuild the binary tree back',
    ],
    9: [
        # 过渡语start
        'The creator of Linux and Git, two artifacts in the programming world',
        'Linus Torvalds once said：Talk is cheap, show me the code!',
        "Let's not talk much, go to the code!",
        # 过渡语end
    ],
    10: [
        'First instantiate and call the main function',
        'Define a recursive reconstruction function',
        'Initialize the left and right boundaries of the traversal result array',
        'Build a hash dictionary to help us quickly locate the root node',
        'Then recursively rebuild the tree nodes',
        'First compare the left and right boundary positions, if the left boundary is greater than the right boundary',
        'If the current subtree is empty, return directly',
        'If it is not empty, locate the root node index first, that is, the first node of the preorder traversal result',
        'Then use the value of the node to find the index of the root node in the inorder traversal in the hash dictionary',
        'Create the root node',
        'Calculate the number of nodes in the left and right subtrees according to the position of the root node in the inorder traversal',
        'Then locate the distribution of the left and right subtrees in the preorder traversal',
        'Then pass the left and right subtree boundaries of the preorder traversal and inorder traversal into the recursive reconstruction function respectively',
        'By repeating the above analysis and operations, all nodes can be recursively rebuilt',
        # 播放背景音乐（自己用Logic pro x的apple loop创建一段重复使用）和剩余动画
    ],
    11: [
        # 结束语start
        "That's all for this video",
        'Thanks for watching, see you next time!',
        # 结束语end
    ],
}
