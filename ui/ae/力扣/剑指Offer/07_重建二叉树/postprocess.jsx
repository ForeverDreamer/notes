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

var preorderPositions = dataPositions([3, 9, 20, 15, 7], 's11.前序遍历结果')
var lastOne = preorderPositions[preorderPositions.length-1]
preorderPositions.push([lastOne[0]+39, lastOne[1]])
var inorderPositions = dataPositions([9, 3, 15, 20, 7], 's11.中序遍历结果')
var lastOne = inorderPositions[inorderPositions.length-1]
inorderPositions.push([lastOne[0]+39, lastOne[1]])
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
        [],
        [],
        {}
    ]
}

function procOpacity(idxes) {

}

function procPosition(times, idxes, posY) {
    Keyframes["Transform.Position"][0] = times

    var positions = []
    for (var i = 0; i < idxes.length; i++) {
        positions.push(preorderPositions[idxes[i]])
    }
    Keyframes["Transform.Position"][1] = positions

    for (var i = 0; i < preorderPositions.length; i++) {
        preorderPositions[i][1] = posY
    }
}

var times = [
    currentLinePosition.keyTime(9), currentLinePosition.keyTime(15), currentLinePosition.keyTime(21),
    currentLinePosition.keyTime(23), currentLinePosition.keyTime(25), currentLinePosition.keyTime(27),
    currentLinePosition.keyTime(29), currentLinePosition.keyTime(31), currentLinePosition.keyTime(37),
    currentLinePosition.keyTime(43), currentLinePosition.keyTime(45), currentLinePosition.keyTime(47),
    currentLinePosition.keyTime(49), currentLinePosition.keyTime(53), currentLinePosition.keyTime(59),
    currentLinePosition.keyTime(61), currentLinePosition.keyTime(63), currentLinePosition.keyTime(65),
    currentLinePosition.keyTime(67), currentLinePosition.keyTime(69)
]

var spatial = []

for (var i = 0; i < times.length; i++) {
    spatial.push({"type": 'HOLD'})
}

Keyframes["Transform.Position"][2] = {"spatial": spatial}

var idxes = [
    0, 1, 2, 
    1, 2, 1, 
    0, 2, 3, 
    4, 3, 4,
    3, 4, 5,
    4, 5, 4,
    2, 0
]

procPosition(times, idxes, 52.5)
shareUtil.configKeyframes(leftSelectedLayer, Keyframes)

idxes = [
    4, 1, 1, 
    1, 1, 1, 
    4, 4, 3, 
    3, 3, 3,
    3, 4, 4,
    4, 4, 4,
    4, 4
]

procPosition(times, idxes, 104.5)
shareUtil.configKeyframes(rightSelectedLayer, Keyframes)

