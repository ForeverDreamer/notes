//share_util.head
#includepath "utils/jsx";
#include "json.jsx";
var BASE_DIR = "D:/data_files/notes/ui/ae/"
var conf = jsonUtil.read(BASE_DIR + "基础/树/b-tree/conf.json");
#include "constants.jsx";
#include "color.jsx";
#include "text.jsx";
#include "shape.jsx";
#include "share.jsx";
#include "effects.jsx";
#include "precomp.jsx";
#include "presets.jsx";
#include "camera.jsx";
#include "ac.jsx";

var DURATION = 3
// app.purge(PurgeTarget.ALL_CACHES);
var project = app.project;
shareUtil.delItems(project.items);
var mainComp = project.items.addComp(NAME, WIDTH, HEIGHT, PIXEL_ASPECT, DURATION, FRAME_RATE);
mainComp.openInViewer();
var bL = textUtil.addOne(mainComp, "字幕", {"text": "你好世界", "Position": [960, 540], "font": FONTS["subtitle"], "fontSize": 100, "fillColor": COLORS["subtitle"]});

acUtil.add(bL, "D:/Program Files/Adobe/Adobe After Effects 2021/Support Files/Presets/User/Untitled.ffx", 0.5, 2.5)

$.writeln(bL.marker.numKeys)

// var m = bL1.marker.keyValue(1);
// var p = m.getParameters();
// $.writeln(p)
// var m = bL1.marker.keyValue(2);
// var p = m.getParameters();
// $.writeln(p)

// var m = bL2.marker.keyValue(1);
// var p = m.getParameters();
// $.writeln(p)
// var m = bL2.marker.keyValue(2);
// var p = m.getParameters();
// $.writeln(p)