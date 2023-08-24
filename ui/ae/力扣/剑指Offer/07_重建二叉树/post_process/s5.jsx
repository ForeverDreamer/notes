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
var btComp = shareUtil.findItemByName("s5.二叉树")
var layerNames = ['3', '3.9', '9', '3.20', '20', '20.15', '15', '20.7', '7']
var times = [10.33, 10.83]
var step = [0.5, 0.5]
var nodeStart = 'Contents.Group 1.Contents.Trim Paths 1.Start'
var nodeEnd = 'Contents.Group 1.Contents.Trim Paths 1.End'
var edgeEnd = 'Contents.Group 1.Contents.Trim Paths 1.End'
var nodePathKeyframes = {}
var edgePathKeyframes = {}

var selectedColor = "Contents.Group 1.Contents.Fill 1.Color"
var selectedKeyframes = {}
for (var i = 0; i < layerNames.length; i++) {
    var layerName = layerNames[i]
    var selectedLayer = null
    var nodePathLayer = null
    var edgePathLayer = null
    if (layerName.split('.').length === 1) {
        selectedLayer = btComp.layer('Node.Selected.' + layerName)
        selectedKeyframes[selectedColor] = propertyKeyframes(
            times,
            [
                colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["default"]),
                colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["pathColor"])
            ],
            procSpatial(times),
        )
        shareUtil.configKeyframes(selectedLayer, selectedKeyframes)

        nodePathLayer = btComp.layer('Node.Path.' + layerName)
        nodePathKeyframes[nodeStart] = propertyKeyframes(times,[50, 0])
        nodePathKeyframes[nodeEnd] = propertyKeyframes(times,[50, 100])
        shareUtil.configKeyframes(nodePathLayer, nodePathKeyframes)
    } else {
        edgePathLayer = btComp.layer('Edge.Path.' + layerName)
        edgePathKeyframes[edgeEnd] = propertyKeyframes(times,[0, 100])
        shareUtil.configKeyframes(edgePathLayer, edgePathKeyframes)
    }
    times += step
}


// 队列
var times = [10.33, 10.83]
var step = [1, 1]
var queueComp = shareUtil.findItemByName("s5.队列")
var layerNames = ['3', '9', '20', '15', '7']
var quequeShapeKeyframes = {}
for (var i = 0; i < layerNames.length; i++) {
    var layerName = layerNames[i]
    var shapeLayer = queueComp.layer('Shape.' + layerName)
    quequeShapeKeyframes[selectedColor] = propertyKeyframes(
        times,
        [
            colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["default"]),
            colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["pathColor"])
        ],
        procSpatial(times),
    )
    shareUtil.configKeyframes(shapeLayer, quequeShapeKeyframes)
    times += step
}