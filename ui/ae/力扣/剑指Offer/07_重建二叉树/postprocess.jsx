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

function dataPositions(parentPath, data) {
    var parentPosition = shareUtil.getPosition(parentPath)
    // $.writeln(parentPosition)

    var paths = []
    for (var i = 0; i < data.length; i++) {
        paths.push(parentPath + '_Shape.' + data[i])
    }
    
    var positions = []
    for (var i = 0; i < paths.length; i++) {
            // parentComp.layers.byName("数据")("Transform")("Position").value
        var position = shareUtil.getPosition(paths[i])
        position[0] += parentPosition[0]
        // $.writeln(position)
        positions.push(position)
    }

    return positions
}
// printArray(dataPositions('s11_s11.队列.前序_数据'))
// $.writeln("================")
// printArray(dataPositions('s11_s11.队列.中序_数据'))

preorderPositions = dataPositions('s11_s11.队列.前序_数据', [3, 9, 20, 15, 7])
inorderPositions = dataPositions('s11_s11.队列.中序_数据', [9, 3, 15, 20, 7])

var preorderQueueComp = shareUtil.findItemByName("s11.队列.前序")
var leftSelectedLayer = preorderQueueComp.layer('左边界.选中框')
var codeComp = shareUtil.findItemByName("代码")
var currentLineLayer = codeComp.layer('currentLine')
var currentLinePosition = currentLineLayer("Transform")("Position");

var leftSelectedKeyframes = {
    "Transform.Position": [
        [
            currentLinePosition.keyTime(9), currentLinePosition.keyTime(15), currentLinePosition.keyTime(21),
            currentLinePosition.keyTime(23), currentLinePosition.keyTime(25),
        ],
        [
            preorderPositions[0], preorderPositions[1], preorderPositions[2],
            preorderPositions[1], preorderPositions[2],
        ],
        {"spatial": [{"type": 'HOLD'}, {"type": 'HOLD'}, {"type": 'HOLD'}, {"type": 'HOLD'}, {"type": 'HOLD'}]}
    ]
}

shareUtil.configKeyframes(leftSelectedLayer, leftSelectedKeyframes)

