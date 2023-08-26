#includepath "../../../../utils_v0/jsx";
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
// printArray(dataPositions('s10_s10.队列.前序_数据'))
// $.writeln("================")
// printArray(dataPositions('s10_s10.队列.中序_数据'))

var preorderPositions = dataPositions([3, 9, 20, 15, 7], 's10.前序遍历结果')
var lastOne = preorderPositions[preorderPositions.length-1]
preorderPositions.push([lastOne[0]+39, lastOne[1]])
var inorderPositions = dataPositions([9, 3, 15, 20, 7], 's10.中序遍历结果')
var lastOne = inorderPositions[inorderPositions.length-1]
inorderPositions.push([lastOne[0]+39, lastOne[1]])
// printArray(preorderPositions)
// $.writeln("================")
// printArray(inorderPositions)

// 前序遍历结果
var preorderDataComp = shareUtil.findItemByName("s10.前序遍历结果", "s10.前序遍历结果")
var rootSelectedLayer = preorderDataComp.layer('根选中框')
var leftSelectedLayer = preorderDataComp.layer('左选中框')
var rightSelectedLayer = preorderDataComp.layer('右选中框')
var codeComp = shareUtil.findItemByName("s10.代码", "s10.代码")
var currentLineLayer = codeComp.layer('currentLine')
var currentLinePosition = currentLineLayer("Transform")("Position");

var Keyframes = {}

function procSpatial(key, times) {
    var spatial = []
    for (var i = 0; i < times.length; i++) {
        spatial.push({"type": 'HOLD'})
    }
    Keyframes[key][2] = {"spatial": spatial}
    Keyframes[key][3] = true
}

function procSourceText(times, texts) {
    var key = "Source Text"
    Keyframes[key] = []
    Keyframes[key][0] = times
    Keyframes[key][1] = texts
    procSpatial(key, times)
}

function procOpacity(times, opacities) {
    var key = "Opacity"
    Keyframes[key] = []
    Keyframes[key][0] = times
    Keyframes[key][1] = opacities
    procSpatial(key, times)
}

function procPosition(times, idxes, posY) {
    var key = "Position"
    Keyframes[key] = []
    Keyframes[key][0] = times

    var positions = []
    for (var i = 0; i < idxes.length; i++) {
        var pos = null
        if (!preorderPositions[idxes[i]]) {
            pos = [preorderPositions[0][0]-39, posY]
        } else {
            pos = preorderPositions[idxes[i]]
        }
        positions.push(pos)
    }
    Keyframes[key][1] = positions

    for (var i = 0; i < preorderPositions.length; i++) {
        preorderPositions[i][1] = posY
    }

    procSpatial(key, times)
}

// 左右选择框
var times = [
    currentLinePosition.keyTime(9), currentLinePosition.keyTime(15), currentLinePosition.keyTime(21),
    currentLinePosition.keyTime(23), currentLinePosition.keyTime(25), currentLinePosition.keyTime(27),
    currentLinePosition.keyTime(29), currentLinePosition.keyTime(31), currentLinePosition.keyTime(37),
    currentLinePosition.keyTime(43), currentLinePosition.keyTime(45), currentLinePosition.keyTime(47),
    currentLinePosition.keyTime(49), currentLinePosition.keyTime(51), currentLinePosition.keyTime(53), 
    currentLinePosition.keyTime(59),currentLinePosition.keyTime(61), currentLinePosition.keyTime(63), 
    currentLinePosition.keyTime(65), currentLinePosition.keyTime(67), currentLinePosition.keyTime(69)
]

var idxes = [
    0, 1, 2, 
    1, 2, 1, 
    0, 2, 3, 
    4, 3, 4,
    3, 2, 4, 
    5, 4, 5, 
    4, 2, 0
]

procOpacity([currentLinePosition.keyTime(1), currentLinePosition.keyTime(9)], [0, 100])
procPosition(times, idxes, 52.5)
shareUtil.configKeyframes(leftSelectedLayer, Keyframes)

var idxes = [
    4, 1, 1, 
    1, 1, 1, 
    4, 4, 3, 
    3, 3, 3,
    3, 4, 4,
    4, 4, 4,
    4, 4, 4
]

procOpacity([currentLinePosition.keyTime(1), currentLinePosition.keyTime(9)], [0, 100])
procPosition(times, idxes, 104.5)
shareUtil.configKeyframes(rightSelectedLayer, Keyframes)

// 根选择框
var times = [
    currentLinePosition.keyTime(11), currentLinePosition.keyTime(17), currentLinePosition.keyTime(33),
    currentLinePosition.keyTime(39), currentLinePosition.keyTime(55),
]

var idxes = [
    0, 1, 2,
    3, 4
]

procOpacity([currentLinePosition.keyTime(1), currentLinePosition.keyTime(11)], [0, 100])
procPosition(times, idxes, 78.5)
shareUtil.configKeyframes(rootSelectedLayer, Keyframes)

// 中序遍历结果
var inorderDataComp = shareUtil.findItemByName("s10.中序遍历结果", "s10.中序遍历结果")
var rootSelectedLayer = inorderDataComp.layer('根选中框')
var leftSelectedLayer = inorderDataComp.layer('左选中框')
var rightSelectedLayer = inorderDataComp.layer('右选中框')

// 左右选择框
var times = [
    currentLinePosition.keyTime(9), currentLinePosition.keyTime(15), currentLinePosition.keyTime(21),
    currentLinePosition.keyTime(23), currentLinePosition.keyTime(25), currentLinePosition.keyTime(27),
    currentLinePosition.keyTime(29), currentLinePosition.keyTime(31), currentLinePosition.keyTime(37),
    currentLinePosition.keyTime(43), currentLinePosition.keyTime(45), currentLinePosition.keyTime(47),
    currentLinePosition.keyTime(49), currentLinePosition.keyTime(51), currentLinePosition.keyTime(53), 
    currentLinePosition.keyTime(59), currentLinePosition.keyTime(61), currentLinePosition.keyTime(63),
    currentLinePosition.keyTime(65), currentLinePosition.keyTime(67), currentLinePosition.keyTime(69)
]

var idxes = [
    0, 0, 0, 
    0, 1, 0, 
    0, 2, 2, 
    2, 2, 3,
    2, 2, 4,
    4, 4, 5,
    4, 2, 0
]

procOpacity([currentLinePosition.keyTime(1), currentLinePosition.keyTime(9)], [0, 100])
procPosition(times, idxes, 52.5)
shareUtil.configKeyframes(leftSelectedLayer, Keyframes)

var idxes = [
    4, 0, -1, 
    0, 0, 0, 
    4, 4, 2, 
    1, 2, 2,
    2, 4, 4,
    3, 4, 4,
    4, 4, 4
]

procOpacity([currentLinePosition.keyTime(1), currentLinePosition.keyTime(9)], [0, 100])
procPosition(times, idxes, 104.5)
shareUtil.configKeyframes(rightSelectedLayer, Keyframes)

// 根选择框
var times = [
    currentLinePosition.keyTime(12), currentLinePosition.keyTime(18), currentLinePosition.keyTime(34),
    currentLinePosition.keyTime(40), currentLinePosition.keyTime(56),
]

var idxes = [
    1, 0, 3,
    2, 4
]

procOpacity([currentLinePosition.keyTime(1), currentLinePosition.keyTime(12)], [0, 100])
procPosition(times, idxes, 78.5)
shareUtil.configKeyframes(rootSelectedLayer, Keyframes)

// 函数调用栈
var funcCallStackComp = shareUtil.findItemByName("函数调用栈", "s10.代码调试")
var moduleShapeLayer = funcCallStackComp.layer("Shape.<module>")
var moduleTextLayer = funcCallStackComp.layer("Text.<module>")
var buildTreeLayer = funcCallStackComp.layer("Shape.buildTree( )")
var buildTreeTextLayer = funcCallStackComp.layer("Text.buildTree( )")
var rebuild0Layer = funcCallStackComp.layer("Shape.rebuild( ).0")
var rebuild0TextLayer = funcCallStackComp.layer("Text.rebuild( ).0")
var rebuild1Layer = funcCallStackComp.layer("Shape.rebuild( ).1")
var rebuild1TextLayer = funcCallStackComp.layer("Text.rebuild( ).1")
var rebuild2Layer = funcCallStackComp.layer("Shape.rebuild( ).2")
var rebuild2TextLayer = funcCallStackComp.layer("Text.rebuild( ).2")
var rebuild3Layer = funcCallStackComp.layer("Shape.rebuild( ).3")
var rebuild3TextLayer = funcCallStackComp.layer("Text.rebuild( ).3")

var Keyframes = {}
procOpacity([0, 1], [0, 100])
shareUtil.configKeyframes(moduleShapeLayer, Keyframes)
shareUtil.configKeyframes(moduleTextLayer, Keyframes)

var times = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(2), currentLinePosition.keyTime(72)
]
var opacities = [
    0, 100, 0
]
procOpacity(times, opacities)
shareUtil.configKeyframes(buildTreeLayer, Keyframes)
shareUtil.configKeyframes(buildTreeTextLayer, Keyframes)

var times = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(9), currentLinePosition.keyTime(71)
]
var opacities = [
    0, 100, 0
]
procOpacity(times, opacities)
shareUtil.configKeyframes(rebuild0Layer, Keyframes)
shareUtil.configKeyframes(rebuild0TextLayer, Keyframes)

var times = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(15), currentLinePosition.keyTime(29),
    currentLinePosition.keyTime(31), currentLinePosition.keyTime(69)
]
var opacities = [
    0, 100, 0,
    100, 0
]
procOpacity(times, opacities)
shareUtil.configKeyframes(rebuild1Layer, Keyframes)
shareUtil.configKeyframes(rebuild1TextLayer, Keyframes)

var times = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(21), currentLinePosition.keyTime(23),
    currentLinePosition.keyTime(25), currentLinePosition.keyTime(27), currentLinePosition.keyTime(37),
    currentLinePosition.keyTime(51), currentLinePosition.keyTime(53), currentLinePosition.keyTime(67)
]
var opacities = [
    0, 100, 0,
    100, 0, 100,
    0, 100, 0
]
procOpacity(times, opacities)
shareUtil.configKeyframes(rebuild2Layer, Keyframes)
shareUtil.configKeyframes(rebuild2TextLayer, Keyframes)

var times = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(43), currentLinePosition.keyTime(45),
    currentLinePosition.keyTime(47), currentLinePosition.keyTime(49), currentLinePosition.keyTime(59),
    currentLinePosition.keyTime(61), currentLinePosition.keyTime(63), currentLinePosition.keyTime(65)
]
var opacities = [
    0, 100, 0,
    100, 0, 100,
    0, 100, 0
]
procOpacity(times, opacities)
shareUtil.configKeyframes(rebuild3Layer, Keyframes)
shareUtil.configKeyframes(rebuild3TextLayer, Keyframes)

// 变量文本
var Keyframes = {}
var codeDebugComp = shareUtil.findItemByName("s10.代码调试", "s10.代码调试")

var idx_plLayer = codeDebugComp.layer("idx_pl")
var times = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(4), currentLinePosition.keyTime(9), 
    currentLinePosition.keyTime(71), currentLinePosition.keyTime(72), 
]
var opacities = [
    0, 100, 0,
    100, 0
]
procOpacity(times, opacities)
shareUtil.configKeyframes(idx_plLayer, Keyframes)

var idx_prLayer = codeDebugComp.layer("idx_pr")
var times = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(5), currentLinePosition.keyTime(9),
    currentLinePosition.keyTime(71), currentLinePosition.keyTime(72),
]
var opacities = [
    0, 100, 0,
    100, 0
]
procOpacity(times, opacities)
shareUtil.configKeyframes(idx_prLayer, Keyframes)

var idx_ilLayer = codeDebugComp.layer("idx_il")
var times = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(6), currentLinePosition.keyTime(9),
    currentLinePosition.keyTime(71), currentLinePosition.keyTime(72),
]
var opacities = [
    0, 100, 0,
    100, 0
]
procOpacity(times, opacities)
shareUtil.configKeyframes(idx_ilLayer, Keyframes)

var idx_irLayer = codeDebugComp.layer("idx_ir")
var times = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(7), currentLinePosition.keyTime(9),
    currentLinePosition.keyTime(71), currentLinePosition.keyTime(72),
]
var opacities = [
    0, 100, 0,
    100, 0
]
procOpacity(times, opacities)
shareUtil.configKeyframes(idx_irLayer, Keyframes)

var idx_dicLayer = codeDebugComp.layer("idx_dic")
var times = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(8), currentLinePosition.keyTime(72),
]
var opacities = [
    0, 100, 0,
]
procOpacity(times, opacities)
shareUtil.configKeyframes(idx_dicLayer, Keyframes)

var piLayer = codeDebugComp.layer("idx_pl.idx_pr.idx_il.idx_ir")
var timesOpacities = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(9), currentLinePosition.keyTime(71)
]
var opacities = [
    0, 100, 0
]
var timesSourceTexts = [
    currentLinePosition.keyTime(9), currentLinePosition.keyTime(15),
    currentLinePosition.keyTime(21), currentLinePosition.keyTime(23),
    currentLinePosition.keyTime(25), currentLinePosition.keyTime(27),
    currentLinePosition.keyTime(29), currentLinePosition.keyTime(31),
    currentLinePosition.keyTime(37), currentLinePosition.keyTime(43),
    currentLinePosition.keyTime(45), currentLinePosition.keyTime(47),
    currentLinePosition.keyTime(49), currentLinePosition.keyTime(51),
    currentLinePosition.keyTime(53), currentLinePosition.keyTime(59),
    currentLinePosition.keyTime(61), currentLinePosition.keyTime(63),
    currentLinePosition.keyTime(65), currentLinePosition.keyTime(67),
    currentLinePosition.keyTime(69),
]
var sourceTexts = [
    'idx_pl: 0  idx_pr: 4  idx_il: 0  idx_ir: 4', 'idx_pl: 1  idx_pr: 1  idx_il: 0  idx_ir: 0',
    'idx_pl: 2  idx_pr: 1  idx_il: 0  idx_ir: -1', 'idx_pl: 1  idx_pr: 1  idx_il: 0  idx_ir: 0',
    'idx_pl: 2  idx_pr: 1  idx_il: 1  idx_ir: 0', 'idx_pl: 1  idx_pr: 1  idx_il: 0  idx_ir: 0',
    'idx_pl: 0  idx_pr: 4  idx_il: 0  idx_ir: 4', 'idx_pl: 2  idx_pr: 4  idx_il: 2  idx_ir: 4',
    'idx_pl: 3  idx_pr: 3  idx_il: 2  idx_ir: 2', 'idx_pl: 4  idx_pr: 3  idx_il: 2  idx_ir: 1',
    'idx_pl: 3  idx_pr: 3  idx_il: 2  idx_ir: 2', 'idx_pl: 4  idx_pr: 3  idx_il: 3  idx_ir: 2',
    'idx_pl: 3  idx_pr: 3  idx_il: 2  idx_ir: 2', 'idx_pl: 2  idx_pr: 4  idx_il: 2  idx_ir: 4',
    'idx_pl: 4  idx_pr: 4  idx_il: 4  idx_ir: 4', 'idx_pl: 5  idx_pr: 4  idx_il: 4  idx_ir: 3',
    'idx_pl: 4  idx_pr: 4  idx_il: 4  idx_ir: 4', 'idx_pl: 5  idx_pr: 4  idx_il: 5  idx_ir: 4',
    'idx_pl: 4  idx_pr: 4  idx_il: 4  idx_ir: 4', 'idx_pl: 2  idx_pr: 4  idx_il: 2  idx_ir: 4',
    'idx_pl: 0  idx_pr: 4  idx_il: 0  idx_ir: 4',
]
procOpacity(timesOpacities, opacities)
procSourceText(timesSourceTexts, sourceTexts)
shareUtil.configKeyframes(piLayer, Keyframes)

var idx_p_rootLayer = codeDebugComp.layer("idx_p_root")
var timesOpacities = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(11), currentLinePosition.keyTime(15),
    currentLinePosition.keyTime(17), currentLinePosition.keyTime(21), currentLinePosition.keyTime(23),
    currentLinePosition.keyTime(25), currentLinePosition.keyTime(27), currentLinePosition.keyTime(31),
    currentLinePosition.keyTime(33), currentLinePosition.keyTime(37), currentLinePosition.keyTime(39),
    currentLinePosition.keyTime(43), currentLinePosition.keyTime(45), currentLinePosition.keyTime(47),
    currentLinePosition.keyTime(49), currentLinePosition.keyTime(53), currentLinePosition.keyTime(55),
    currentLinePosition.keyTime(59), currentLinePosition.keyTime(61), currentLinePosition.keyTime(63),
    currentLinePosition.keyTime(65), currentLinePosition.keyTime(71),
]
var opacities = [
    0, 100, 0,
    100, 0, 100,
    0, 100, 0,
    100, 0, 100,
    0, 100, 0,
    100, 0, 100,
    0, 100, 0,
    100, 0
]
var timesSourceTexts = [
    currentLinePosition.keyTime(11), currentLinePosition.keyTime(17), currentLinePosition.keyTime(29),
    currentLinePosition.keyTime(33), currentLinePosition.keyTime(39), currentLinePosition.keyTime(51),
    currentLinePosition.keyTime(55), currentLinePosition.keyTime(67), currentLinePosition.keyTime(69),
]
var sourceTexts = [
    "idx_p_root: 0", "idx_p_root: 1", "idx_p_root: 0",
    "idx_p_root: 2", "idx_p_root: 3", "idx_p_root: 2",
    "idx_p_root: 4", "idx_p_root: 2", "idx_p_root: 0"
]
procOpacity(timesOpacities, opacities)
procSourceText(timesSourceTexts, sourceTexts)
shareUtil.configKeyframes(idx_p_rootLayer, Keyframes)

var idx_i_rootLayer = codeDebugComp.layer("idx_i_root")
var timesOpacities = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(12), currentLinePosition.keyTime(15),
    currentLinePosition.keyTime(18), currentLinePosition.keyTime(21), currentLinePosition.keyTime(23),
    currentLinePosition.keyTime(25), currentLinePosition.keyTime(27), currentLinePosition.keyTime(31),
    currentLinePosition.keyTime(34), currentLinePosition.keyTime(37), currentLinePosition.keyTime(40),
    currentLinePosition.keyTime(43), currentLinePosition.keyTime(45), currentLinePosition.keyTime(47),
    currentLinePosition.keyTime(49), currentLinePosition.keyTime(53), currentLinePosition.keyTime(56),
    currentLinePosition.keyTime(59), currentLinePosition.keyTime(61), currentLinePosition.keyTime(63),
    currentLinePosition.keyTime(65), currentLinePosition.keyTime(71),
]
var opacities = [
    0, 100, 0,
    100, 0, 100,
    0, 100, 0,
    100, 0, 100,
    0, 100, 0,
    100, 0, 100,
    0, 100, 0,
    100, 0
]
var timesSourceTexts = [
    currentLinePosition.keyTime(12), currentLinePosition.keyTime(18), currentLinePosition.keyTime(29),
    currentLinePosition.keyTime(34), currentLinePosition.keyTime(40), currentLinePosition.keyTime(51),
    currentLinePosition.keyTime(56), currentLinePosition.keyTime(67), currentLinePosition.keyTime(69),
]
var sourceTexts = [
    "idx_i_root: 1", "idx_i_root: 0", "idx_i_root: 1",
    "idx_i_root: 3", "idx_i_root: 2", "idx_i_root: 3",
    "idx_i_root: 4", "idx_i_root: 3", "idx_i_root: 1",
]
procOpacity(timesOpacities, opacities)
procSourceText(timesSourceTexts, sourceTexts)
shareUtil.configKeyframes(idx_i_rootLayer, Keyframes)

var rootLayer = codeDebugComp.layer("root")
var timesOpacities = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(13), currentLinePosition.keyTime(15),
    currentLinePosition.keyTime(19), currentLinePosition.keyTime(21), currentLinePosition.keyTime(23),
    currentLinePosition.keyTime(25), currentLinePosition.keyTime(27), currentLinePosition.keyTime(31),
    currentLinePosition.keyTime(35), currentLinePosition.keyTime(37), currentLinePosition.keyTime(41),
    currentLinePosition.keyTime(43), currentLinePosition.keyTime(45), currentLinePosition.keyTime(47),
    currentLinePosition.keyTime(49), currentLinePosition.keyTime(53), currentLinePosition.keyTime(57),
    currentLinePosition.keyTime(59), currentLinePosition.keyTime(61), currentLinePosition.keyTime(63),
    currentLinePosition.keyTime(65), currentLinePosition.keyTime(71),
]
var opacities = [
    0, 100, 0,
    100, 0, 100,
    0, 100, 0,
    100, 0, 100,
    0, 100, 0,
    100, 0, 100,
    0, 100, 0,
    100, 0
]
var timesSourceTexts = [
    currentLinePosition.keyTime(13), currentLinePosition.keyTime(19), currentLinePosition.keyTime(29),
    currentLinePosition.keyTime(35), currentLinePosition.keyTime(41), currentLinePosition.keyTime(51),
    currentLinePosition.keyTime(57), currentLinePosition.keyTime(67), currentLinePosition.keyTime(69),
]
var sourceTexts = [
    "root: 3", "root: 9", "root: 3",
    "root: 20", "root: 15", "root: 20",
    "root: 7", "root: 20", "root: 3",
]
procOpacity(timesOpacities, opacities)
procSourceText(timesSourceTexts, sourceTexts)
shareUtil.configKeyframes(rootLayer, Keyframes)

var size_leftLayer = codeDebugComp.layer("size_left")
var timesOpacities = [
    currentLinePosition.keyTime(1), currentLinePosition.keyTime(14), currentLinePosition.keyTime(15),
    currentLinePosition.keyTime(20), currentLinePosition.keyTime(21), currentLinePosition.keyTime(23),
    currentLinePosition.keyTime(25), currentLinePosition.keyTime(27), currentLinePosition.keyTime(31),
    currentLinePosition.keyTime(36), currentLinePosition.keyTime(37), currentLinePosition.keyTime(42),
    currentLinePosition.keyTime(43), currentLinePosition.keyTime(45), currentLinePosition.keyTime(47),
    currentLinePosition.keyTime(49), currentLinePosition.keyTime(53), currentLinePosition.keyTime(58),
    currentLinePosition.keyTime(59), currentLinePosition.keyTime(61), currentLinePosition.keyTime(63),
    currentLinePosition.keyTime(65), currentLinePosition.keyTime(71),
]
var opacities = [
    0, 100, 0,
    100, 0, 100,
    0, 100, 0,
    100, 0, 100,
    0, 100, 0,
    100, 0, 100,
    0, 100, 0,
    100, 0
]
var timesSourceTexts = [
    currentLinePosition.keyTime(14), currentLinePosition.keyTime(20), currentLinePosition.keyTime(29),
    currentLinePosition.keyTime(36), currentLinePosition.keyTime(42), currentLinePosition.keyTime(51),
    currentLinePosition.keyTime(58), currentLinePosition.keyTime(67), currentLinePosition.keyTime(69),
]
var sourceTexts = [
    "size_left: 1", "size_left: 0", "size_left: 1",
    "size_left: 1", "size_left: 0", "size_left: 1",
    "size_left: 0", "size_left: 1", "size_left: 1",
]
procOpacity(timesOpacities, opacities)
procSourceText(timesSourceTexts, sourceTexts)
shareUtil.configKeyframes(size_leftLayer, Keyframes)