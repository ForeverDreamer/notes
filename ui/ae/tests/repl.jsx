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

// 注意字符串拼接时的引号问题，还有注释文字里边的符号问题，否则会导致莫名其妙的错误

// Eval Error (#4): "Unterminated string constant" in 'D:\data_files\notes\ui\ae\utils\jsx\precomp.jsx' [58:30] in host 'aftereffects-18.0 (main)'.
// "var comp = items.addComp("二叉树." + conf["name"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE);" 

// Eval Error (#14): "No matching closing brace found"
// 手动创建的Shape, prop.propertyValueType === PropertyValueType.ThreeD_SPATIAL，所以array需要传三个值

// app.cancelTask(4)
app.beginUndoGroup("设置路径");

var project = app.project;
var comp = project.activeItem;
var layer1 = comp.layer(1)

var path = layer1("Contents")("Shape 1")("Contents")("Path 1")("Path").value
var vertices = path.vertices
var inTangents = path.inTangents
var outTangents = path.outTangents

var layer2 = comp.layer(2)
var prop = layer2("Transform")("Position")
var value = prop.value
for (var i = 0; i < vertices.length; i++) {
    vertices[i] += value
}

shareUtil.configKeyframes(layer2, {"Transform.Position": [[0, 1, 2, 3, 4, 5, 6, 7], vertices]})

for (var i = 1; i <= prop.numKeys; i++) {
	prop.setInterpolationTypeAtKey(i, KeyframeInterpolationType.BEZIER)
    // 手动创建的Shape, prop.propertyValueType === PropertyValueType.ThreeD_SPATIAL，所以array需要传三个值
    prop.setSpatialTangentsAtKey(i, inTangents[i-1].concat([0]), outTangents[i-1].concat([0]))
}

app.endUndoGroup();
