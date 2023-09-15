# 开场白/过渡语/结束语，录制成单独的音频文件，方便重复使用

subtitles = {
    0: [
        '我们在创作短视频的过程中经常需要用Pr对原始视频素材进行剪辑',
        '然后将剪辑片段单独导出来，导入Ae进行二次创作',
        '但是Pr不能把所有剪辑好的片段一次性导出来，需要用户一个个手动导出，非常浪费时间'
        '所以我希望写一个Pr插件，可以选择需要导出的序列，一键自动导出所有剪辑片段',
        '减少重复性工作，节省时间，提升创作效率'
    ],
    # 每一步的操作步骤捡重要的演示一遍，代码重新敲一遍，录制屏幕，鼠标尺寸选2，点击时加图形动画comp特效
    # 使用方框，下划线，箭头等图形元素、镜头移动和放大缩小等方式强调重点，文字注释帮助理解
    # 每句字幕都尽量配上准确、形象的可视化元素（视频、图片、动画、图形、特效等）
    1: [
        '第一步：查阅Adobe-CEP文档，学习怎么为Pr编写插件',
        'Adobe CEP（通用扩展性平台）是Adobe开发的一个技术平台',
        '用于为 Adobe 应用程序（如 Premiere Pro、After Effectc、 Photoshop、Illustrator等）创建扩展和插件。'
        '在浏览器地址栏输入Adobe-CEP官方代码仓库地址，来到文档首页',
        '文档是全英文的，英文不太好的同学可以借助浏览器的翻译功能翻译成自己的母语', # YouTube
        '通读一遍之后感觉一脸蒙圈，还得先动动手才能明白',
    ],
    2: [
        '第二步：根据Getting-Started-guides，一步步实现可以运行的插件',
        '我们点击开始链接，来到开发示例教程页面',
        '按照指南开始动手实现',
        '1.确定文件夹结构，创建必要的目录和文件',
        '2.配置您的扩展manifest.xml，配置插件的各项参数',
        '3.下载CSInterface.js，这个文件是与Adobe应该沟通的桥梁',
        '4.编写前端代码，设计插件在Adobe应用里的展示界面和交互逻辑',
        '5.编写ExtendScript代码，实现需要的功能代码',
        '6.把代码目录复制到Adobe插件目录，然后再应用程序中就可以打开了',
    ],
    3: [
        '第三步：优化插件的UI界面，根据需要优化配置参数',
        '示例代码是针对Ps的，我们要增加对Pr的支持',
        '插件Id、名字等也不专业，改成有意义的名字',
        '插件界面的文字也改一下',
        '功能代码改成Pr支持的操作，比如：弹出一个消息框',
        '更新代码，查看一下效果，点击按钮，看看有没有反应',
    ],
    4: [
        '第四步：编写Extend Script实现批量导出功能'， # 播放背景音乐，主要步骤用文字标注解释
    ],
    5: [
        '第五步：在Pr界面中进行最终测试',
        '更新代码，插件面板关闭后再重新打开，新代码才会生效',
        '打开Media Encoder，点击"导出剪辑片段"按钮',
        '等待所有视频片段渲染结束',
        '检查一下导出结果',
        '导入Ae进行二次创作', # 打开Ae导入视频片段，按clips编号拖动layer出现顺序
    ],
}
