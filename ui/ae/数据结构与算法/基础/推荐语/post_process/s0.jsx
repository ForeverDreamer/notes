#includepath "../../../../utils/jsx";
#include "json.jsx";
var conf = jsonUtil.read("D:/data_files/notes/ui/Ae/数据结构与算法/基础/推荐语/conf.json");
#include "constants.jsx";
#include "color.jsx";
#include "text.jsx";
#include "shape.jsx";
#include "share.jsx";
#include "effects.jsx";
#include "presets.jsx";
#include "camera.jsx";
#include "comp.jsx";
#include "dsa/binarytree.jsx"
#include "dsa/codes.jsx"
#include "dsa/queue.jsx"
#include "dsa/stack.jsx"
#include "dsa/dsa.jsx"
#include "atomx/typography.jsx"


var sn = 0

// 第一次创建
// var shot = conf["shots"][sn]
// shot['width'] = WIDTH
// shot['height'] = HEIGHT
// compUtil.addOne(shot, mainComp, project)


// 配置镜头中的各个元素，配置复杂就用python生成json文件，给jsx读取使用
var parentName = "s0"
// 副标题：数据结构
var compName = "s0.数据结构"
atomxTypographyUtil.config(
    {
        "text": "数据结构：\n数据结构是以有效且有组织的方式在计算机内存中组织和存储数据的方法\n它们为存储、访问和操作数据提供了基础\n数据结构的示例包括数组、链表、堆栈、队列、树和图",
        "leading": 35,
        "textColor": COLORS["subtitle"],
        "elementColor": COLORS["subtitle"],
        "Scale": [28.8, 56],
        "Position": [-7.3, 46.1]},
    shareUtil.findItemByName(compName)
)

var parentComp = shareUtil.findItemByName(parentName, parentName)
parentComp.layer(compName)("Scale").setValue([41, 41])
parentComp.layer(compName)("Position").setValue([780, 217])

// 副标题：算法
var compName = "s0.算法"
atomxTypographyUtil.config(
    {
        "text": "算法：\n算法是解决特定问题所遵循的分步过程或指令\n它们是一组定义明确的规则，可将输入数据转换为所需的输出\n算法决定了解决问题的效率，并在软件开发中发挥着至关重要的作用",
        "leading": 35,
        "textColor": COLORS["subtitle"],
        "elementColor": COLORS["subtitle"],
        "Scale": [28.8, 56],
        "Position": [-7.3, 46.1]},
    shareUtil.findItemByName(compName)
)
parentComp.layer(compName)("Scale").setValue([41, 41])
parentComp.layer(compName)("Position").setValue([780, 760])

// 主标题：什么是数据结构和算法？
var compName = "s0.主标题"
atomxTypographyUtil.config(
    {
        "text": "什么是数据结构和算法？",
        "leading": 35,
        "textColor": COLORS["subtitle"],
        "elementColor": COLORS["subtitle"],
        "Scale": [28.8, 12],
        "Position": [-7.3, -8.3]},
    shareUtil.findItemByName(compName)
)
parentComp.layer(compName)("Scale").setValue([50, 50])
parentComp.layer(compName)("Position").setValue([201, 540])