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
#include "utils.jsx"

var START_TIME = 7.5
var INTERVAL = 0.5
// 二叉树
var btComp = shareUtil.findItemByName("s6.二叉树")
var pathLayerKeyframes = {
    '3': {'times': [START_TIME, START_TIME+INTERVAL], 'values': {'start': [50, 0], 'end': [50, 100]}},
    '3.9': {'times': [START_TIME+INTERVAL, START_TIME+INTERVAL*2, START_TIME+INTERVAL*4, START_TIME+INTERVAL*5], 'values': {'end': [0, 100, 100, 0]}},
    '9': {'times': [START_TIME+INTERVAL*2, START_TIME+INTERVAL*3, START_TIME+INTERVAL*4], 'values': {'start': [50, 0, 50], 'end': [50, 100, 50]}},
    '3.20': {'times': [START_TIME+INTERVAL*5, START_TIME+INTERVAL*6], 'values': {'end': [0, 100]}},
    '20': {'times': [START_TIME+INTERVAL*6, START_TIME+INTERVAL*7], 'values': {'start': [50, 0], 'end': [50, 100]}},
    '20.15': {'times': [START_TIME+INTERVAL*7, START_TIME+INTERVAL*8, START_TIME+INTERVAL*10, START_TIME+INTERVAL*11], 'values': {'end': [0, 100, 100, 0]}},
    '15': {'times': [START_TIME+INTERVAL*8, START_TIME+INTERVAL*9, START_TIME+INTERVAL*10], 'values': {'start': [50, 0, 50], 'end': [50, 100, 50]}},
    '20.7': {'times': [START_TIME+INTERVAL*11, START_TIME+INTERVAL*12], 'values': {'end': [0, 100]}},
    '7': {'times': [START_TIME+INTERVAL*12, START_TIME+INTERVAL*13], 'values': {'start': [50, 0], 'end': [50, 100]}}
}

var nodeStart = 'Contents.Group 1.Contents.Trim Paths 1.Start'
var nodeEnd = 'Contents.Group 1.Contents.Trim Paths 1.End'
var edgeEnd = 'Contents.Group 1.Contents.Trim Paths 1.End'
var nodePathKeyframes = {}
var edgePathKeyframes = {}
var opacityKeyframes = {
    'Opacity': [[START_TIME+INTERVAL*14, START_TIME+INTERVAL*15], [100, 0]]
}

for (var layerName in pathLayerKeyframes) {
    var keyframes = pathLayerKeyframes[layerName]
    var nodePathLayer = null
    var edgePathLayer = null
    if (layerName.split('.').length === 1) {
        nodePathLayer = btComp.layer('Node.Path.' + layerName)
        nodePathKeyframes[nodeStart] = propertyKeyframes(keyframes['times'], keyframes['values']['start'])
        nodePathKeyframes[nodeEnd] = propertyKeyframes(keyframes['times'], keyframes['values']['end'])
        shareUtil.configKeyframes(nodePathLayer, nodePathKeyframes)
        shareUtil.configKeyframes(nodePathLayer, opacityKeyframes)
    } else {
        edgePathLayer = btComp.layer('Edge.Path.' + layerName)
        edgePathKeyframes[edgeEnd] = propertyKeyframes(keyframes['times'], keyframes['values']['end'])
        shareUtil.configKeyframes(edgePathLayer, edgePathKeyframes)
        shareUtil.configKeyframes(edgePathLayer, opacityKeyframes)
    }
}

var selectedLayerKeyframes = {
    '9': {'times': [START_TIME+INTERVAL*2, START_TIME+INTERVAL*3]},
    '3': {'times': [START_TIME+INTERVAL*4, START_TIME+INTERVAL*5]},
    '15': {'times': [START_TIME+INTERVAL*8, START_TIME+INTERVAL*9]},
    '20': {'times': [START_TIME+INTERVAL*10, START_TIME+INTERVAL*11]},
    '7': {'times': [START_TIME+INTERVAL*12, START_TIME+INTERVAL*13]}
}
var selectedColor = "Contents.Group 1.Contents.Fill 1.Color"
var selectedKeyframes = {}
for (var layerName in selectedLayerKeyframes) {
    var keyframes = selectedLayerKeyframes[layerName]
    var selectedLayer = btComp.layer('Node.Selected.' + layerName)
    selectedKeyframes[selectedColor] = propertyKeyframes(
        keyframes["times"],
        [
            colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["default"]),
            colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["pathColor"])
        ],
        procSpatial(keyframes["times"]),
    )
    shareUtil.configKeyframes(selectedLayer, selectedKeyframes)
}


// 队列
var queueComp = shareUtil.findItemByName("s6.队列")
var queueLayerKeyframes = {
    '9': {'times': [START_TIME+INTERVAL*2, START_TIME+INTERVAL*3]},
    '3': {'times': [START_TIME+INTERVAL*4, START_TIME+INTERVAL*5]},
    '15': {'times': [START_TIME+INTERVAL*8, START_TIME+INTERVAL*9]},
    '20': {'times': [START_TIME+INTERVAL*10, START_TIME+INTERVAL*11]},
    '7': {'times': [START_TIME+INTERVAL*12, START_TIME+INTERVAL*13]}
}
var queueShapeKeyframes = {}
for (var layerName in queueLayerKeyframes) {
    var keyframes = queueLayerKeyframes[layerName]
    var shapeLayer = queueComp.layer('Shape.' + layerName)
    queueShapeKeyframes[selectedColor] = propertyKeyframes(
        keyframes["times"],
        [
            colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["default"]),
            colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["pathColor"])
        ],
        procSpatial(keyframes["times"]),
    )
    shareUtil.configKeyframes(shapeLayer, queueShapeKeyframes)
}

// 选中顺序动画
var RIGHT = {
    'times': [START_TIME + INTERVAL * 18, START_TIME + INTERVAL * 19],
    'values': [
        colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["pathColor"]),
        colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["right"])
    ]
}
var queueLayerKeyframes = {
    '9': {
        'times': [START_TIME+INTERVAL*14, START_TIME+INTERVAL*15],
        'values': [
            colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["pathColor"]),
            colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["left"])
        ]
    },
    '3': {
        'times': [START_TIME+INTERVAL*16, START_TIME+INTERVAL*17],
        'values': [
            colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["pathColor"]),
            colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["root"])
        ]
    },
    '15': RIGHT,
    '20': RIGHT,
    '7': RIGHT
}
var queueShapeKeyframes = {}
for (var layerName in queueLayerKeyframes) {
    var keyframes = queueLayerKeyframes[layerName]
    var shapeLayer = queueComp.layer('Shape.' + layerName)
    queueShapeKeyframes[selectedColor] = propertyKeyframes(
        keyframes["times"],
        keyframes["values"],
        procSpatial(keyframes["times"]),
        null,
        false
    )
    shareUtil.configKeyframes(shapeLayer, queueShapeKeyframes)
}

var selectedKeyframes = {}
for (var layerName in queueLayerKeyframes) {
    var keyframes = queueLayerKeyframes[layerName]
    var selectedLayer = btComp.layer('Node.Selected.' + layerName)
    selectedKeyframes[selectedColor] = propertyKeyframes(
        keyframes["times"],
        keyframes["values"],
        procSpatial(keyframes["times"]),
        null,
        false
    )
    shareUtil.configKeyframes(selectedLayer, selectedKeyframes)
}