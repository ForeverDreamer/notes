function BinaryTree() {

}

// BinaryTree.prototype._btTraverseSelectedDropQueue = function (key, traverse) {
//     var times = this.times
//
//     var selectedKeyframes = {
//         "Transform.Opacity": [null, [0, 100], { "spatial": [{ "type": 'HOLD' }] }]
//     }
//
//     var dropTmp = binaryTree.dropTmp;
//     var dropKeyframes = {
//         "Transform.Opacity": [null, [0, 100, 0]],
//         "Transform.Position": [null, null, { "temporal": [[[0, 0.1], [1000, 100]], [[0, 75], [0, 0.1]]] }],
//         "Transform.Rotation": [null, [0, 45]],
//         "Contents.Group 1.Contents.Path 1.Path": [
//             null,
//             [
//                 {
//                     "vertices": [[0, -50], [50, 0], [0, 50], [-50, 0]],
//                     "inTangents": [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0],
//                     [0, 27.6142425537109]],
//                     "outTangents": [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0],
//                     [0, -27.6142425537109]],
//                     "closed": 'true'
//                 },
//                 {
//                     "vertices": [[0, -57.5], [57.5, 0], [0, 57.5], [-57.5, 0]],
//                     // "inTangents": [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0], [0, 27.6142425537109]],
//                     // "outTangents": [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0], [0, -27.6142425537109]],
//                     "closed": true
//                 }
//             ]
//         ]
//     }
//     // 选中
//     var selectedLayer = this.nodeLayers[key]["selectedLayer"]
//     if (selectedLayer("Transform")("Opacity").numKeys === 0) {
//         selectedKeyframes["Transform.Opacity"][0] = times - [0.5, 0.5];
//         shareUtil.configKeyframes(selectedLayer, selectedKeyframes);
//         // 掉落
//         var dropLayer = this.nodeLayers[key]["dropLayer"]
//         dropKeyframes["Transform.Opacity"][0] = [times[0], times[1], times[1] + 0.5]
//         dropTmp["Position"] = dropLayer("Transform")("Position").value
//         dropKeyframes["Transform.Position"][0] = times
//         dropKeyframes["Transform.Position"][1] = [dropTmp["Position"], [50 + dropTmp["sn"] * 80, 810]]
//         dropKeyframes["Transform.Rotation"][0] = times
//         dropKeyframes["Contents.Group 1.Contents.Path 1.Path"][0] = times
//         shareUtil.configKeyframes(dropLayer, dropKeyframes);
//         shareUtil.configKeyframes(
//             this.nodeLayers[key]["dropTextLayer"],
//             { "Transform.Rotation": [times, [0, -45]], "Transform.Opacity": [[times[0], times[1], times[1] + 0.5], [0, 100, 0]] }
//         )
//         dropTmp["sn"] += 1
//
//         // 队列
//         var queueKeyframes = { "Transform.Opacity": [times + [0.5, 0.5], [0, 100]] }
//         // var elemLayers = precompUtil.queueLayers[traverse][key]
//         var elemLayers = binaryTree.queueLayers[traverse][key]
//         shareUtil.configKeyframes(elemLayers["shapeLayer"], queueKeyframes)
//         shareUtil.configKeyframes(elemLayers["textLayer"], queueKeyframes)
//         // if (traverse === "preorder" && key === '3') {
//         //     shareUtil.configKeyframes(selectedLayer, {
//         //         "Contents.Group 1.Contents.Fill 1.Color": [
//         //             [times[0], times[1]+0.5],
//         //             [
//         //                 colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["default"]),
//         //                 colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["root"])
//         //             ],
//         //             {"spatial": [{"type": 'HOLD'}, {"type": 'HOLD'}]}
//         //         ]
//         //     });
//         //     shareUtil.configKeyframes(elemLayers["shapeLayer"], {
//         //         "Contents.Group 1.Contents.Fill 1.Color": [
//         //             [times[0], times[1]+0.5],
//         //             [
//         //                 colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["default"]),
//         //                 colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["root"])
//         //             ],
//         //             {"spatial": [{"type": 'HOLD'}, {"type": 'HOLD'}]}]
//         //     });
//         // }
//         // for (var kQueue in precompUtil.queueLayers) {
//         //     $.writeln(kQueue)
//         //     var queue = precompUtil.queueLayers[kQueue]
//         //     for (var kElem in queue) {
//         //         $.writeln(kElem)
//         //     }
//         //     $.writeln('===============================')
//         // }
//     }
// }
//
// BinaryTree.prototype._btTraverseForwardPath = function (traverse, forwardPath) {
//     var times = binaryTree.times
//     var nodePathKeyframes = {
//         'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [50, 0]],
//         'Contents.Group 1.Contents.Trim Paths 1.End': [times, [50, 100]],
//     }
//     var edgePathKeyframes = {
//         'Contents.Group 1.Contents.Trim Paths 1.End': [times, [0, 100]],
//     }
//
//     for (var i = 0; i < forwardPath.length; i++) {
//         if (forwardPath[i].name.indexOf("Node") !== -1) {
//             // if (!keys[forwardPath[i].name]) {
//             //     shareUtil.configKeyframes(forwardPath[i],  {
//             //         'Contents.Group 1.Contents.Trim Paths 1.Start': [[0, times[0]-1/FRAME_RATE], [50, 50]],
//             //         'Contents.Group 1.Contents.Trim Paths 1.End': [[0, times[0]-1/FRAME_RATE], [50, 50]],
//             //     });
//             // }
//             shareUtil.configKeyframes(forwardPath[i], nodePathKeyframes);
//             if (traverse === 'preorder') {
//                 var key = forwardPath[i].name.split('.').slice(-1)[0]
//                 // this._btTraverseSelectedDropQueue(key, traverse)
//             }
//         } else {
//             // if (!keys[forwardPath[i].name]) {
//             //     shareUtil.configKeyframes(forwardPath[i],  {
//             //         'Contents.Group 1.Contents.Trim Paths 1.End': [[0, times[0]-1/FRAME_RATE], [0, 0]],
//             //     });
//             // }
//             shareUtil.configKeyframes(forwardPath[i], edgePathKeyframes);
//         }
//         // keys[forwardPath[i].name] = true
//         times[0] += 1
//         times[1] = times[0] + 0.5
//     }
//     if (traverse === 'inorder') {
//         var key = forwardPath[i - 1].name.split('.').slice(-1)[0]
//         // this._btTraverseSelectedDropQueue(key, traverse)
//     }
//     forwardPath.length = 0;
// }
//
// BinaryTree.prototype._btTraverseBackwardPath = function (traverse, backwardPath) {
//     var times = binaryTree.times
//     var nodePathKeyframes = {
//         'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [0, 50]],
//         'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 50]],
//     }
//     var edgePathKeyframes = {
//         'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 0]],
//     }
//     var length;
//     switch (traverse) {
//         case 'preorder':
//             length = backwardPath.length
//             break;
//         case 'inorder':
//             length = 2
//             break;
//     }
//     for (var i = 0; i < length; i++) {
//         if (backwardPath[0].name.indexOf("Edge") !== -1) {
//             shareUtil.configKeyframes(backwardPath[0], edgePathKeyframes);
//         }
//         else {
//             shareUtil.configKeyframes(backwardPath[0], nodePathKeyframes);
//         }
//         times[0] += 1
//         times[1] = times[0] + 0.5
//         backwardPath.shift()
//     }
//     if (traverse === 'inorder') {
//         var key = backwardPath.shift().name.split('.').slice(-1)[0]
//         // this._btTraverseSelectedDropQueue(key, traverse)
//     }
// }
//
// BinaryTree.prototype._btTraverse = function (traverse, nodePath, edgePath) {
//
//     function processNode(node) {
//         // $.writeln("==================================")
//     }
//
//     function preorder(traverse, root, func, forwardPath, backwardPath) {
//         func(root)
//         forwardPath.push(root["pathLayer"])
//         backwardPath.unshift(root["pathLayer"])
//         var direction = "left"
//         if (root[direction]) {
//             forwardPath.push(root["edgeLayers"]["down"][direction]["pathLayer"])
//             backwardPath.unshift(root["edgeLayers"]["down"][direction]["pathLayer"])
//             preorder(traverse, root[direction], func, forwardPath, backwardPath)
//         }
//         direction = "right"
//         if (root[direction]) {
//             forwardPath.push(root["edgeLayers"]["down"][direction]["pathLayer"])
//             backwardPath.unshift(root["edgeLayers"]["down"][direction]["pathLayer"])
//             preorder(traverse, root[direction], func, forwardPath, backwardPath)
//         }
//     }
//
//     // 对动画路径来说其实是前序遍历
//     function inorder(traverse, root, func, forwardPath, backwardPath) {
//         forwardPath.push(root["pathLayer"])
//         var direction = "left"
//         if (root[direction]) {
//             forwardPath.push(root["edgeLayers"]["down"][direction]["pathLayer"])
//             backwardPath.unshift(root["pathLayer"])
//             backwardPath.unshift(root["edgeLayers"]["down"][direction]["pathLayer"])
//             backwardPath.unshift(root[direction]["pathLayer"])
//             inorder(traverse, root[direction], func, forwardPath, backwardPath)
//         }
//         func(root)
//         direction = "right"
//         if (root[direction]) {
//             forwardPath.push(root["edgeLayers"]["down"][direction]["pathLayer"])
//             backwardPath.unshift(root["pathLayer"])
//             backwardPath.unshift(root["edgeLayers"]["down"][direction]["pathLayer"])
//             backwardPath.unshift(root[direction]["pathLayer"])
//             inorder(traverse, root[direction], func, forwardPath, backwardPath)
//         }
//         if (!root["left"] && !root["right"]) {
//             // 配置路径动画
//             binaryTree._btTraverseForwardPath(traverse, forwardPath)
//             if (backwardPath.length > 0) {
//                 binaryTree._btTraverseBackwardPath(traverse, backwardPath)
//             }
//         }
//     }
//
//     function doTraverse(traverse, root, func) {
//         binaryTree.dropTmp = { "Position": null, "sn": 0 };
//         var times = binaryTree.times
//         var forwardPath = []
//         var backwardPath = []
//
//         if (traverse === 'preorder') {
//             preorder(traverse, root, func, forwardPath, backwardPath)
//             binaryTree._btTraverseForwardPath(traverse, forwardPath)
//             binaryTree._btTraverseBackwardPath(traverse, backwardPath)
//         } else if (traverse === 'inorder') {
//             inorder(traverse, root, func, forwardPath, backwardPath)
//             binaryTree._btTraverseBackwardPath(traverse, backwardPath)
//             shareUtil.configKeyframes(root["pathLayer"], {
//                 'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [0, 50]],
//                 'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 50]],
//             });
//         }
//
//     }
//
//     doTraverse(traverse, this.rootNode, processNode)
//
//     // 音效
//     if (nodePath["sound"]) {
//         var soundItem = shareUtil.findItemByName(node["Path"]["sound"]["name"])
//         var startTimes = node["Path"]["sound"]["startTimes"]
//         for (var i = 0; i < startTimes.length; i++) {
//             var soundLayer = comp.layers.add(soundItem);
//             soundLayer.startTime = startTimes[i];
//         }
//     }
//
//     if (edgePath["sound"]) {
//         var soundItem = shareUtil.findItemByName(edge["Path"]["sound"]["name"])
//         var startTimes = edge["Path"]["sound"]["startTimes"]
//         for (var i = 0; i < startTimes.length; i++) {
//             var soundLayer = comp.layers.add(soundItem);
//             soundLayer.startTime = startTimes[i];
//         }
//     }
// }

BinaryTree.prototype.add = function (conf, parentComp, parentObj) {
    var comp = parentObj.items.addComp(conf["layerName"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE);
    comp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])
    comp.resolutionFactor = RESOLUTION_FACTOR

    var elems = conf["elems"];

    var selected = conf["node"]["selected"];
    var drop = conf["node"]["drop"];
    var nodeShape = conf["node"]["shape"];
    var nodePath = conf["node"]["path"];

    var edgeShape = conf["edge"]["shape"];

    var edgePath = conf["edge"]["path"];

    var NODE_SCALE = nodeShape["Scale"][0] / 100
    var ROTATION = edgeShape["Rotation"]

    binaryTree.times = [0, 0.5]
    var STEP = [0.5, 0.5]
    var NODE_PREFIX = "Node"
    var EDGE_PREFIX = "Edge"

    var ROOT_NODE_POS = conf["rootNodePos"]
    var EDGE_OFFSET = 45 * NODE_SCALE
    var HORIZONTAL_DIST = 160 * NODE_SCALE
    var VERTICAL_DIST = 240 * NODE_SCALE

    // binaryTree.verticalDist *= NODE_SCALE
    binaryTree.nodeLayers = {}
    binaryTree.edgeLayers = {}
    var offset = null
    if (nodePath) {
        offset = nodePath["Trim Paths"]["Offset"]
    }

    function addNode(elem, parentNode, direction, selected, drop, upEdge) {
        var key = elem["key"]
        var layerName = elem["layerName"] ? elem["layerName"] : key

        if (parentNode) {
            var parentPos = parentNode["Position"]
        }

        switch (direction) {
            case 'left':
                nodeShape["Position"] = [parentPos[0] - HORIZONTAL_DIST, parentPos[1] + VERTICAL_DIST]
                if (nodePath) {
                    nodePath["Trim Paths"]["Offset"] = offset
                }
                break;
            case 'right':
                nodeShape["Position"] = [parentPos[0] + HORIZONTAL_DIST, parentPos[1] + VERTICAL_DIST]
                if (nodePath) {
                    nodePath["Trim Paths"]["Offset"] = -offset
                }
                break;
            case null:
                nodeShape["Position"] = ROOT_NODE_POS
                break;
            default:
                throw new TypeError("参数[direction]类型错误")
        }

        var shapeKeyframes = {
            "Transform.Opacity": [binaryTree.times, [0, 100], { "temporal": [[[0, 0.1], [200, 100]], [[0, 75], [0, 0.1]]] }]
        }
        nodeShape["layerName"] = NODE_PREFIX + "." + "Shape" + "." + layerName
        var shapeTextProps = { "text": key }
        if (conf["animation"]) {
            nodeShape["keyframes"] = shapeKeyframes
            shapeTextProps["keyframes"] = shapeKeyframes
            binaryTree.times += STEP
        }
        if (elem["keyframes"]) {
            nodeShape["keyframes"] = elem["keyframes"]
            shapeTextProps["keyframes"] = elem["keyframes"]
            if (upEdge) {
                shareUtil.configKeyframes(upEdge["shapeLayer"], elem["keyframes"])
            }
        }
        var shapeLayer = shareUtil.addLayer(nodeShape, comp);

        if (selected) {
            selected["Position"] = nodeShape["Position"]
            selected["layerName"] = NODE_PREFIX + "." + "Selected" + "." + layerName
            if (elem["Color"]) {
                selected["Fill"]["Color"] = colorUtil.hexToRgb1(elem["Color"])
            }
            var selectedLayer = shapeUtil.addOne(selected, comp)
            // selectedLayers[selected["layerName"]] = selectedLayer
        }
        shapeTextProps["layerName"] = NODE_PREFIX + "." + "Text" + "." + layerName
        var shapeTextLayer = textUtil.overlay(shapeTextProps, comp, shapeLayer);

        if (drop) {
            // drop["Fill"]["Color"] = drop["Fill"]["Color"]
            drop["layerName"] = NODE_PREFIX + "." + "Drop" + "." + layerName
            drop["Position"] = nodeShape["Position"]
            var dropLayer = shapeUtil.addOne(drop, comp)
            // dropLayers[drop["layerName"]] = dropLayer
            var dropTextLayer = textUtil.overlay(
                { "layerName": NODE_PREFIX + "." + "Drop" + '.' + "Text" + "." + key,  "text": key, "Opacity": 0 },
                comp, dropLayer
            )
        }

        if (nodePath) {
            nodePath["pathGroup"]["type"] = "Group"
            nodePath["layerName"] = NODE_PREFIX + "." + "Path" + "." + layerName;
            // path["Position"] = shapeLayer("Transform")("Position").value.slice(0, 2)
            nodePath["Position"] = nodeShape["Position"]
            var pathLayer = shapeUtil.addOne(nodePath, comp)
            // nodePathLayers.push(pathLayer)
        }

        binaryTree.nodeLayers[layerName] = {
            "layerName": layerName,
            "key": key,
            "Position": shapeLayer("Transform")("Position").value,
            "shapeLayer": shapeLayer, "shapeTextLayer": shapeTextLayer, "selectedLayer": selectedLayer, "dropLayer": dropLayer, "dropTextLayer": dropTextLayer, "pathLayer": pathLayer,
            "edgeLayers": {
                "down": { "left": null, "right": null },
                "up": upEdge ? upEdge : null,
            },
            "left": null, "right": null
        }
        if (parentNode) {
            parentNode[direction] = binaryTree.nodeLayers[layerName]
        }

        return binaryTree.nodeLayers[layerName]
    }

    function addEdge(elem, upNode, direction) {
        var key = elem["key"]
        var layerName = elems["layerName"] ? elems["layerName"] : key
        var upLayerName = upNode["layerName"];
        var upPos = upNode["Position"];

        if (direction === "left") {
            edgeShape["Position"] = [upPos[0] - EDGE_OFFSET, upPos[1] + EDGE_OFFSET]
            edgeShape["Rotation"] = ROTATION
            if (edgePath) {
                edgePath["Rotation"] = 0
            }
        } else if (direction === "right") {
            edgeShape["Position"] = [upPos[0] + EDGE_OFFSET, upPos[1] + EDGE_OFFSET]
            edgeShape["Rotation"] = -ROTATION
            if (edgePath) {
                edgePath["Rotation"] = -ROTATION * 2
            }
        } else {
            throw new TypeError("参数[direction]类型错误")
        }

        var edgeKeyframes = {
            // "Transform.Scale": [times, [[0, 0, 0], edgeShape["Scale"]], {"temporal": [[[0, 0.1], [200, 100]], [[0, 75], [0, 0.1]]]}]
            "Transform.Scale": [binaryTree.times, [[0, 0, 0], edgeShape["Scale"]], { "temporal": [[[0, 0.1], [300, 100]], [[0, 75], [0, 0.1]]] }]
        }
        edgeShape["layerName"] = EDGE_PREFIX + "." + "Shape" + "." + upLayerName + '.' + layerName
        if (conf["animation"]) {
            edgeShape["keyframes"] = edgeKeyframes
            binaryTree.times += STEP
        }
        var shapeLayer = shareUtil.addLayer(edgeShape, comp)

        if (edgePath) {
            edgePath["pathGroup"]["type"] = "Group"
            edgePath["layerName"] = EDGE_PREFIX + "." + "Path" + "." + upLayerName + '.' + layerName
            edgePath["Position"] = edgeShape["Position"]
            var pathLayer = shapeUtil.addOne(edgePath, comp)
        }

        binaryTree.edgeLayers[layerName] = {
            "layerName": layerName,
            "key": key,
            "shapeLayer": shapeLayer, "pathLayer": pathLayer,
            "nodeLayers": {
                "up": upNode ? upNode : null,
                "down": null,
            }
        }
        upNode["edgeLayers"]["down"][direction] = binaryTree.edgeLayers[layerName]

        return binaryTree.edgeLayers[layerName]
    }

    this.rootNode = addNode(elems[0], null, null, selected, drop)

    var i = 1;
    var nodeQueue = [this.rootNode]

    while (nodeQueue.length > 0) {
        var treeNode = nodeQueue.shift();
        if (elems[i] && elems[i]["key"]) {
            var edgeLayer = addEdge(elems[i], treeNode, "left")
            var nodeLayer = addNode(elems[i], treeNode, "left", selected, drop, edgeLayer)
            nodeQueue.push(nodeLayer)
        }
        i += 1;
        if (elems[i] && elems[i]["key"]) {
            var edgeLayer = addEdge(elems[i], treeNode, "right")
            var nodeLayer = addNode(elems[i], treeNode, "right", selected, drop, edgeLayer)
            nodeQueue.push(nodeLayer)
        }
        i += 1;
    }

    // if (conf["traverse"]) {
    //     this._btTraverse(conf["traverse"], nodePath, edgePath)
    // }

    conf["item"] = comp
    var compLayer = shareUtil.addLayer(conf, parentComp)
    return { 'comp': comp, 'compLayer': compLayer };
}

var binaryTree = new BinaryTree();