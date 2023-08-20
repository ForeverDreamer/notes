//share_util.head
#includepath "../../../utils_v0/jsx";
#include "json.jsx";
var BASE_DIR = "D:/data_files/notes/ui/Ae/"
var conf = jsonUtil.read(BASE_DIR + "力扣/剑指Offer/07_重建二叉树/conf.json");
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

function printArray(array) {
    for (var i = 0; i < array.length; i++) {
        $.writeln(array[i])
    }
}

function dataPositions(data, parentFolderName) {
    var params = {
        "itemName": "数据",
        "parentFolderName": parentFolderName
    }
    var parentPosition = shareUtil.getPosition({"layerName": "数据", "itemName": parentFolderName, "parentFolderName": parentFolderName})
    var positions = []
    for (var i = 0; i < data.length; i++) {
        params["layerName"] = "Shape." + data[i]
        var position = shareUtil.getPosition(params)
        position[0] += parentPosition[0]
        // $.writeln(position)
        positions.push(position)
    }
    return positions
}
// printArray(dataPositions('s11_s11.队列.前序_数据'))
// $.writeln("================")
// printArray(dataPositions('s11_s11.队列.中序_数据'))

preorderPositions = dataPositions([3, 9, 20, 15, 7], 's11.前序遍历结果')
inorderPositions = dataPositions([9, 3, 15, 20, 7], 's11.中序遍历结果')
printArray(preorderPositions)
$.writeln("================")
printArray(inorderPositions)

var preorderDataComp = shareUtil.findItemByName("s11.前序遍历结果", "s11.前序遍历结果")
var rootSelectedLayer = preorderDataComp.layer('根选中框')
var leftSelectedLayer = preorderDataComp.layer('左选中框')
var rightSelectedLayer = preorderDataComp.layer('右选中框')
var codeComp = shareUtil.findItemByName("s11.代码", "s11.代码")
var currentLineLayer = codeComp.layer('currentLine')
var currentLinePosition = currentLineLayer("Transform")("Position");

var Keyframes = {
    "Transform.Position": [
        [
            currentLinePosition.keyTime(9), currentLinePosition.keyTime(15), currentLinePosition.keyTime(21),
            currentLinePosition.keyTime(23), currentLinePosition.keyTime(25),
        ],
        [
            // preorderPositions[0], preorderPositions[1], preorderPositions[2],
            // preorderPositions[1], preorderPositions[2],
        ],
        {"spatial": [{"type": 'HOLD'}, {"type": 'HOLD'}, {"type": 'HOLD'}, {"type": 'HOLD'}, {"type": 'HOLD'}]}
    ]
}

for (var i = 0; i < preorderPositions.length; i++) {
    preorderPositions[i][1] = 103.5
}

// var positions = []
// var idxes = [0, 1, 2, 1, 2]
// for (var i = 0; i < idxes.length; i++) {
//     positions.push(preorderPositions[idxes[i]])
// }
// Keyframes["Transform.Position"][1] = positions

// shareUtil.configKeyframes(rootSelectedLayer, Keyframes)


// 此段重复代码封装成函数
for (var i = 0; i < preorderPositions.length; i++) {
    preorderPositions[i][1] = 52.5
}

// 此段重复代码封装成函数
var positions = []
var idxes = [0, 1, 2, 1, 2]
for (var i = 0; i < idxes.length; i++) {
    positions.push(preorderPositions[idxes[i]])
}
Keyframes["Transform.Position"][1] = positions

shareUtil.configKeyframes(leftSelectedLayer, Keyframes)

var positions = []
var idxes = [4, 1, 1, 1, 1]
for (var i = 0; i < idxes.length; i++) {
    positions.push(preorderPositions[idxes[i]])
}
Keyframes["Transform.Position"][1] = positions

shareUtil.configKeyframes(rightSelectedLayer, Keyframes)

