//share_util.head
#includepath "../utils/jsx";
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


var project = app.project;
var comp = shareUtil.findItemByName("s0", "s0");

var i = 2
var keyTime = comp.layer("s0.算法").marker.keyTime(i)
$.writeln(keyTime)

var marker = comp.layer("s0.主标题").marker
var mv = marker.keyValue(i);
marker.setValueAtTime(keyTime, mv);
marker.removeKey(i)

var marker = comp.layer("s0.数据结构").marker
var mv = marker.keyValue(i);
marker.setValueAtTime(keyTime, mv);
marker.removeKey(i)