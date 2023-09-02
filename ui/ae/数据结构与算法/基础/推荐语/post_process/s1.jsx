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

var sn = 1

// 第一次创建
// var shot = conf["shots"][sn]
// shot['width'] = WIDTH
// shot['height'] = HEIGHT
// compUtil.addOne(shot, mainComp, project)

var parentName = "s1"
var color = COLORS["text"]

// 副标题：数据结构
var parentComp = shareUtil.findItemByName(parentName, parentName)
var compName = "s1.数据结构"
var comp = shareUtil.findItemByName(compName)
atomxTypographyUtil.titleMinimal_94(
    {
        "text": "数据结构：\n数据结构是以有效且有组织的方式在计算机内存中组织和存储数据的方法\n它们为存储、访问和操作数据提供了基础\n数据结构的示例包括数组、链表、堆栈、队列、树和图",
        "leading": 35,
        "textColor": color,
        "elementColor": color,
        "Scale": [28.8, 56],
        // "Scale": [28.8, 12],
        "Position": [-7.3, 46.7],
    },
    comp
)

var layer2 = parentComp.layer(compName)
layer2("Scale").setValue([41, 41])
// layer2("Scale").setValue([50, 50])
layer2("Position").setValue([463.6, 217])
layer2.startTime = 0;
