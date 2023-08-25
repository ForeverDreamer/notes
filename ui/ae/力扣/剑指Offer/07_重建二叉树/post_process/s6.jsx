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


// 二叉树
var btComp = shareUtil.findItemByName("s6.二叉树")
var pathLayerKeyframes = {
    '3': {'times': [7.5, 8], 'values': {'start': [50, 0], 'end': [50, 100]}}, 
    '3.9': {'times': [8, 8.5, 9.5, 10], 'values': {'end': [0, 100, 100, 0]}},  
    '9': {'times': [8.5, 9, 9.5], 'values': {'start': [50, 0, 50], 'end': [50, 100, 50]}},  
    '3.20': {'times': [10, 10.5], 'values': {'end': [0, 100]}},
    '20': {'times': [10.5, 11], 'values': {'start': [50, 0], 'end': [50, 100]}}, 
    '20.15': {'times': [11, 11.5, 12.5, 13], 'values': {'end': [0, 100, 100, 0]}},  
    '15': {'times': [11.5, 12, 12.5], 'values': {'start': [50, 0, 50], 'end': [50, 100, 50]}},  
    '20.7': {'times': [13, 13.5], 'values': {'end': [0, 100]}},
    '7': {'times': [13.5, 14], 'values': {'start': [50, 0], 'end': [50, 100]}}
}
var times = [7.35, 7.85]
var step = [0.5, 0.5]
var nodeStart = 'Contents.Group 1.Contents.Trim Paths 1.Start'
var nodeEnd = 'Contents.Group 1.Contents.Trim Paths 1.End'
var edgeEnd = 'Contents.Group 1.Contents.Trim Paths 1.End'
var nodePathKeyframes = {}
var edgePathKeyframes = {}

for (var layerName in pathLayerKeyframes) {
    var keyframes = pathLayerKeyframes[layerName]
    var nodePathLayer = null
    var edgePathLayer = null
    if (layerName.split('.').length === 1) {
        nodePathLayer = btComp.layer('Node.Path.' + layerName)
        nodePathKeyframes[nodeStart] = propertyKeyframes(keyframes['times'], keyframes['values']['start'])
        nodePathKeyframes[nodeEnd] = propertyKeyframes(keyframes['times'], keyframes['values']['end'])
        shareUtil.configKeyframes(nodePathLayer, nodePathKeyframes)
    } else {
        edgePathLayer = btComp.layer('Edge.Path.' + layerName)
        edgePathKeyframes[edgeEnd] = propertyKeyframes(keyframes['times'], keyframes['values']['end'])
        shareUtil.configKeyframes(edgePathLayer, edgePathKeyframes)
    }
}

var selectedLayerKeyframes = {
    '9': {'times': [8.5, 9]},
    '3': {'times': [9.5, 10]},
    '15': {'times': [11.5, 12]},
    '20': {'times': [12.5, 13]},
    '7': {'times': [13.5, 14]}
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
    '9': {'times': [8.5, 9]},
    '3': {'times': [9.5, 10]},
    '15': {'times': [11.5, 12]},
    '20': {'times': [12.5, 13]},
    '7': {'times': [13.5, 14]}
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