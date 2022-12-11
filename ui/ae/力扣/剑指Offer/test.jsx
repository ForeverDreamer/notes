#includepath "../../utils/jsx;";
#include "json.jsx";
#include "share.jsx";
#include "color.jsx";

var project = app.project;
var comp = project.activeItem;
var layer = comp.layer(14)
// $.writeln(shapeLayer.name)
// var left = shapeLayer.sourceRectAtTime(0, true).left
// var top = shapeLayer.sourceRectAtTime(0, true).top
// var width = shapeLayer.sourceRectAtTime(0, true).width
// var height = shapeLayer.sourceRectAtTime(0, true).height
// $.writeln(left)
// $.writeln(top)
// $.writeln(width)
// $.writeln(height)
// var aiLayer = comp.layer(7)
// $.writeln(aiLayer("Transform")("Anchor Point").value)
// var preorderLayer = comp.layer(5)
// $.writeln(preorderLayer("Masks").numProperties)
// newMask = preorderLayer.Masks.addProperty("Mask");
// newMask.inverted = true;
// myMaskShape = newMask("maskShape");
// myShape = myMaskShape.value;
// myShape.vertices = [[5,5],[5,45],[45,45],[45,5]];
// myShape.closed = true;
// myMaskShape.setValue(myShape);
// var shapeLayer = comp.layer(1)
// shapeLayer.selected = true;

// var path = layer("Contents")("Polystar 1")("Contents")("Path 1")("Path").value
var path = layer("Masks")("Mask 1")("Mask Path").value
$.writeln(path)
$.writeln(path.vertices)
$.writeln(path.inTangents)
$.writeln(path.outTangents)
$.writeln(path.featherSegLoc)
$.writeln(path.featherRelSegLoc)
$.writeln(path.featherRadii)
// path.selected = true;
// app.executeCommand(19); //Copy
// shapeLayer.selected = false;

// var inorderLayer = comp.layer(5)
// inorderLayer.selected = true;
// var posPorp = inorderLayer("Transform")("Position")
// posPorp.selected = true;
// app.executeCommand(20); //Paste
// inorderLayer.selected = false;

// var myShape = new Shape();
// myShape.vertices = [[300,50], [200,150],[300,250],[400,150]];
// myShape.inTangents = [[55.23,0],[0,-55.23],[-55.23,0],[0,55.23]];
// myShape.outTangents = [[-55.23,0],[0,55.23],[55.23,0],[0,-55.23]];
// path.setValue(myShape);
// $.writeln(myShape.vertices)
// [colorUtil.hexToRgb("#FF0000", true), colorUtil.hexToRgb("#00FF18", true), colorUtil.hexToRgb("#005FB8", true)]
// $.writeln(colorUtil.hexToRgb("#005FB8", true))
// var effects = app.effects
// // $.writeln(effects.length)
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
// var pathGroup = shapeGroup("Contents").addProperty("ADBE Vector Shape - Group")
// var myShape = new Shape();
// // myShape.vertices = path.vertices;
// // myShape.inTangents = path.inTangents;
// // myShape.outTangents = path.outTangents;
// // myShape.featherRelSegLoc = path.featherRelSegLoc;
// // edge的顶点坐标
// myShape.vertices = [[146,82], [78,203]];
// // myShape.inTangents = path.inTangents;
// // myShape.outTangents = path.outTangents;
// // myShape.featherRelSegLoc = path.featherRelSegLoc;
// myShape.closed = false;
// pathGroup("Path").setValue(myShape);
// trimGroup = shapeGroup("Contents").addProperty("ADBE Vector Filter - Trim")
// // trimGroup("start").setValue(5)
// // trimGroup("end").setValue(5)

// strokeGroup = shapeGroup("Contents").addProperty("ADBE Vector Graphic - Stroke")
// strokeGroup("Color").setValue(colorUtil.hexToRgb1("#FF0000"))
// strokeGroup("Stroke Width").setValue(5)
// var anchorPoint = shareUtil.setAnchorPoint(shapeLayer, "RIGHT_TOP")
// shapeGroup("Transform")("Anchor Point").setValue([anchorPoint[0], anchorPoint[1]])
// shapeGroup("Transform")("Position").setValue([anchorPoint[0], anchorPoint[1]])
// shapeLayer("Transform")("Position").setValue([anchorPoint[0], anchorPoint[1]])
// // nodeLayer("Transform")("Position").setValue(myShape.vertices)