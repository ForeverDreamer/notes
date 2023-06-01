#includepath "./utils/jsx";
#include "constants.jsx";
#include "misc.jsx";
#include "shape.jsx";


// 脚本创建的doc坐标Y系统是反的，需要先手动创建doc
var doc = app.activeDocument
var line = doc.pathItems.add();
var p1 = line.pathPoints.add();
p1.anchor = p1.rightDirection = p1.leftDirection = [700.499999999999,-417.5];
var p2 = line.pathPoints.add();
p2.anchor = p2.rightDirection = p2.leftDirection = [581.500000000001,-400.5];
line.setEntirePath([p1.anchor, p2.anchor]);
// line.left = 581
// line.top = -397

var artItems = app.activeDocument.selection
// brush从库里选出来使用一下会添加到当前文档，name在鼠标移到相应得brush会显示
app.activeDocument.brushes.getByName("Arrow 1.18").applyTo(line)
line.strokeWidth = 0.5


// var brushes = app.activeDocument.brushes
// for (var i = 0; i < brushes.length; i++) {
//     $.writeln(i + ', ' + brushes[i].name)
//     brushes[i].applyTo(line)
//     break
// }