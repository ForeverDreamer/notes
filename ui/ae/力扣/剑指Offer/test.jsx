#includepath "../../utils/jsx;";
#include "constants.jsx";
#include "json.jsx";
#include "animation.jsx";
#include "share.jsx";
#include "color.jsx";
#include "effects.jsx";
#include "presets.jsx";
#include "text.jsx";
#include "shape.jsx";
#include "precomp.jsx"

var project = app.project;
var mainComp = project.activeItem;
var layer = mainComp.layer(1)
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

// var path = layer("Contents")("Ellipse 1")("Contents")("Path 1")("Path").value
// var path = layer("Contents")("Group 1")("Contents")("Path 1")("Path").value
// var path = layer("Masks")("Mask 1")("Mask Path").value
// $.writeln(path.vertices)
// $.writeln(path.inTangents)
// $.writeln(path.outTangents)
// $.writeln("============================================")
// $.writeln(path.featherSegLoc)
// $.writeln(path.featherRelSegLoc)
// $.writeln(path.featherRadii)

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
// $.writeln(effects.length)
// for (var i = 0; i < effects.length; i++) {
//     $.writeln(effects[i].category + ',' + effects[i].displayName + ',' + effects[i].matchName)
// }

// var taskId = app.scheduleTask('$.writeln(app.findMenuCommandId("AtomX"))', 1000, true)
// $.writeln(taskId)
// $.writeln(app.findMenuCommandId("AtomX"))
// $.writeln(app.findMenuCommandId("Animation Composer 3"))
// app.executeCommand(5020);

// var shapeLayer = comp.layers.addShape();
// shapeLayer.name = 'Node.Path.3'
// var shapeGroup = shapeLayer("Contents").addProperty("ADBE Vector Group");
// var pathGroup = shapeGroup("Contents").addProperty("ADBE Vector Shape - Group")
// var myShape = new Shape();
// // myShape.vertices = path.vertices;
// // myShape.inTangents = path.inTangents;
// // myShape.outTangents = path.outTangents;
// // edge的顶点坐标
// myShape.vertices = path.vertices;
// myShape.vertices = [[0,-50],[50,0],[0,50],[-50,0]];
// myShape.inTangents = [[-27.6142425537109,0], [0,-27.6142425537109], [27.6142425537109,0], [0,27.6142425537109]];
// myShape.outTangents = [[27.6142425537109,0], [0,27.6142425537109], [-27.6142425537109,0], [0,-27.6142425537109]];
// myShape.closed = true;
// pathGroup("Path").setValue(myShape);
// trimGroup = shapeGroup("Contents").addProperty("ADBE Vector Filter - Trim")
// // trimGroup("start").setValue(5)
// // trimGroup("end").setValue(5)
// strokeGroup = shapeGroup("Contents").addProperty("ADBE Vector Graphic - Stroke")
// strokeGroup("Color").setValue(colorUtil.hexToRgb1("#FF0000"))
// strokeGroup("Stroke Width").setValue(5)
// var anchorPoint = shareUtil.setAnchorPoint(shapeLayer)
// shapeGroup("Transform")("Anchor Point").setValue([187, 60])
// shapeGroup("Transform")("Position").setValue([187, 60])
// shapeLayer("Transform")("Position").setValue([187, 60])
// // nodeLayer("Transform")("Position").setValue(myShape.vertices)
// shareUtil.configKeyframes(shapeLayer, {"Contents.Group 1.Contents.Trim Paths 1.Start": [[0, 0.5], [50, 0]]})
// shareUtil.configKeyframes(shapeLayer, {"Contents.Group 1.Contents.Trim Paths 1.End": [[0, 0.5], [50, 100]]})
// shapeLayer("Contents")("Group 1")("Contents")("Trim Paths 1")("Offset").setValue(-135)


// var shapeLayer = comp.layers.addShape();
// shapeLayer.name = 'Edge.Path.3'
// var shapeGroup = shapeLayer("Contents").addProperty("ADBE Vector Group");
// var pathGroup = shapeGroup("Contents").addProperty("ADBE Vector Shape - Group")
// var myShape = new Shape();
// // myShape.vertices = path.vertices;
// // myShape.inTangents = path.inTangents;
// // myShape.outTangents = path.outTangents;
// // edge的顶点坐标
// // myShape.vertices = path.vertices;
// myShape.vertices = [[153, 95], [88, 211]];
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
// shareUtil.configKeyframes(shapeLayer, {"Contents.Group 1.Contents.Trim Paths 1.End": [[0.5, 1], [0, 100]]})

// 需要手动导入之后，找到precomp名字(可以重命名)再用代码操作
// var atomxCompItem = shareUtil.findItemByName("Shape - Basic 75-1")
// var compLayer = mainComp.layers.add(atomxCompItem);
// compLayer("Transform")("Scale").setValue([50, 50])
// compLayer("Transform")("Position").setValue([328, 350])

var dic = {"a": 1, "nested": {"b": 1, "c": 2}}
$.writeln(dic["a"])
// 注意：此处并没有清空原变量的数据，"a"和"nested"仍然可以正常访问，坑！！！
var dic;
$.writeln(dic["a"])
dic["a"] = 2
$.writeln(dic["a"])
$.writeln(dic["nested"])