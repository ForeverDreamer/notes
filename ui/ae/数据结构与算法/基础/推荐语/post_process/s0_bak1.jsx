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

var project = app.project;

var sn = 0

// 第一次创建
// var shot = conf["shots"][sn]
// shot['width'] = WIDTH
// shot['height'] = HEIGHT
// compUtil.addOne(shot, mainComp, project)


// 配置镜头中的各个元素，配置复杂就用python生成json文件，给jsx读取使用
var parentName = "s0"
var startTime = 0
var color = COLORS["markBox"]

// 主标题：什么是数据结构和算法？
var parentComp = shareUtil.findItemByName(parentName, parentName)
var compName = "s0.主标题"
var comp = shareUtil.findItemByName(compName)
atomxTypographyUtil.titleBig_20(
    {
        "text": "什么是数据结构和算法？",
        "textColor": color,
        "elementColor": color,
    },
    comp
)
var layer1 = parentComp.layer(compName)
layer1("Scale").setValue([30, 30])
layer1("Position").setValue([250, 540])
layer1.startTime = 0;
// startTime += layer1.outPoint - layer2.inPoint

// 副标题：数据结构
var compName = "s0.数据结构"
var comp = shareUtil.findItemByName(compName)
atomxTypographyUtil.titleCalloutL1(
    {
        // "text": "数据结构：\n数据结构是以有效且有组织的方式在计算机内存中组织和存储数据的方法\n它们为存储、访问和操作数据提供了基础\n数据结构的示例包括数组、链表、堆栈、队列、树和图",
        "text": "数据结构",
        "textColor": color,
        "lineColor": color,
        "dotColor": color,
    },
    comp
)

var layer2 = parentComp.layer(compName)
layer2("Scale").setValue([55, 55])
layer2("Position").setValue([780, 217])
layer2.startTime = 5;
// startTime += layer2.outPoint - layer2.inPoint

// // 副标题：算法
var compName = "s0.算法"
var comp = shareUtil.findItemByName(compName)
atomxTypographyUtil.titleCalloutL1(
    {
        // "text": "数据结构：\n数据结构是以有效且有组织的方式在计算机内存中组织和存储数据的方法\n它们为存储、访问和操作数据提供了基础\n数据结构的示例包括数组、链表、堆栈、队列、树和图",
        "text": "算法",
        "textScale": [65.6, -65.6],
        "textColor": color,
        "lineColor": color,
        "dotColor": color,
    },
    comp
)

var layer3 = parentComp.layer(compName)
layer3("Scale").setValue([55, -55])
layer3("Position").setValue([780, 760])
layer3.startTime = 10;
