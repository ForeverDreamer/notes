#includepath "./utils;";
#include "json.jsx";
#include "share.jsx";
#include "color.jsx";

var project = app.project;
var comp = project.activeItem;
// var shapeLayer = comp.layer(1)
// shapeLayer.selected = true;

var path = shapeLayer("Contents")("Group 1")("Contents")("Path 1")("Path")
path.selected = true;
app.executeCommand(19); //Copy
shapeLayer.selected = false;

var inorderLayer = comp.layer(5)
inorderLayer.selected = true;
var posPorp = inorderLayer("Transform")("Position")
posPorp.selected = true;
app.executeCommand(20); //Paste
inorderLayer.selected = false;

// var myShape = new Shape();
// myShape.vertices = [[300,50], [200,150],[300,250],[400,150]];
// myShape.inTangents = [[55.23,0],[0,-55.23],[-55.23,0],[0,55.23]];
// myShape.outTangents = [[-55.23,0],[0,55.23],[55.23,0],[0,-55.23]];
// path.setValue(myShape);
// $.writeln(myShape.vertices)
// [colorUtil.hexToRgb("#FF0000", true), colorUtil.hexToRgb("#00FF18", true), colorUtil.hexToRgb("#005FB8", true)]
// $.writeln(colorUtil.hexToRgb("#005FB8", true))
// var effects = app.effects
// for (var i = 0; i < effects.length; i++) {
//     $.writeln(effects[i].category + ',' + effects[i].displayName + ',' + effects[i].matchName)
// }

// var taskId = app.scheduleTask('$.writeln(app.findMenuCommandId("AtomX"))', 1000, true)
// $.writeln(taskId)
// $.writeln(app.findMenuCommandId("AtomX"))
// $.writeln(app.findMenuCommandId("Animation Composer 3"))
// app.executeCommand(5020);

// var shapeLayer = comp.layers.addShape();
// var shapeGroup = shapeLayer("Contents").addProperty("ADBE Vector Group");
// pathGroup = shapeGroup("Contents").addProperty("ADBE Vector Shape - Group")
// var myShape = new Shape();
// myShape.vertices = [[300,50], [200,150],[300,250],[400,150]];
// myShape.inTangents = [[55.23,0],[0,-55.23],[-55.23,0],[0,55.23]];
// myShape.outTangents = [[-55.23,0],[0,55.23],[55.23,0],[0,-55.23]];
// myShape.closed = true;
// pathGroup("Path").setValue(myShape);
// strokeProp = shapeGroup("Contents").addProperty("ADBE Vector Graphic - Stroke")
// strokeProp("Color").setValue([0, 0, 0])