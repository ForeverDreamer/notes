function PrecompUtil() { 
    this.queueLayers = {}
}

PrecompUtil.prototype.stack = function (nodeLayer, edgeLayer, elems) {

}

PrecompUtil.prototype.stack = function (comp, conf) {

}

PrecompUtil.prototype.queue = function (comp, conf) {
    var name = conf["name"]
    this.queueLayers[name] = {}
    var elems = conf['elems']
    var unit = conf["unit"];

    var queueComp = project.items.addComp('队列.' + name, conf['width'], conf['height'], PIXEL_ASPECT, conf['duration'], FRAME_RATE);

    var elemHeight = unit["pathGroup"]["Size"][0]
    var elemWidth = unit["pathGroup"]["Size"][1]
	// var height = layer.sourceRectAtTime(startTime, false).height
    for (var i = 0; i < elems.length; i++) {
        unit["layerName"] = "Shape" + "." + elems[i]
        unit["Position"] = [elemWidth / 2 + elemWidth * i, elemHeight / 2]
        // var shapeLayer = shareUtil.addLayer(queueComp, unit);
        var shapeLayer = shapeUtil.add(queueComp, unit)
        var textLayer = textUtil.overlay(
            queueComp, shapeLayer, "Text" + "." + elems[i],
            {"text": elems[i], "font": "Arial-BoldItalicMT", "fontSize": 40, "Position": [elemWidth/2, elemHeight/2]}
        );
        this.queueLayers[name][elems[i]] = {'shapeLayer': shapeLayer, "textLayer": textLayer}
    }
    shareUtil.addLayer(comp, conf, queueComp);
    // effectsUtil.add(queueLayer, "ADBE Drop Shadow", {"Distance": 10, "Softness": 30, "Opacity": 255});
}

PrecompUtil.prototype.binaryTree = function (parentComp, conf) {
    var comp = project.items.addComp("二叉树." + conf["name"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE); 

    var elems = conf["elems"];
    
    var nodeShape = conf["node"]["shape"];
    var selected = conf["node"]["selected"];
    var drop = conf["node"]["drop"];
    var nodePath = conf["node"]["path"];

    var edgeShape = conf["edge"]["shape"];
    var edgePath = conf["edge"]["path"];

    var nodeScale = nodeShape["Scale"][0]/100
    var edgeOffset = 45*nodeScale;
    var horizontalDist = 160*nodeScale;
    var verticalDist = 240*nodeScale;
    var textPos = [64, 66, 0];

    var NODE_PREFIX = "Node";
    var EDGE_PREFIX = "Edge";

    var rootNodePos = [235*nodeScale, 75*nodeScale]
    var nodeLayers = {}
    var edgeLayers = {}

    var offset = nodePath["Trim Paths"]["Offset"]
    var rotation = edgeShape["Rotation"]

    function addNode(key, parentNode, direction, selected, drop, upEdge) {
        if (parentNode) {
            var parentPos = parentNode["Position"]
        }
        switch (direction) {
            case 'left':
                nodeShape["Position"] = [parentPos[0]-horizontalDist, parentPos[1]+verticalDist]
                nodePath["Trim Paths"]["Offset"] = offset
                break;
            case 'right':
                nodeShape["Position"] = [parentPos[0]+horizontalDist, parentPos[1]+verticalDist]
                nodePath["Trim Paths"]["Offset"] = -offset
                break;
            case null:
                nodeShape["Position"] = rootNodePos
                break;
            default:
                throw new TypeError("参数[direction]类型错误")
        }
        nodeShape["layerName"] = NODE_PREFIX + "." + "Shape" + "." + key
        var shapeLayer = shareUtil.addLayer(comp, nodeShape);
    
        selected["Position"] = nodeShape["Position"]
        selected["layerName"] = NODE_PREFIX + "." + "Selected" + "." + key
        var selectedLayer = shareUtil.addLayer(comp, selected);
        // selectedLayers[selected["layerName"]] = selectedLayer
        var shapeTextLayer = textUtil.overlay(comp, shapeLayer, NODE_PREFIX + "." + "Text" + "." + key, {"text": key});

        // drop["Fill"]["Color"] = drop["Fill"]["Color"]
        drop["layerName"] = NODE_PREFIX + "." + "Drop" + "." + key
        drop["Position"] = nodeShape["Position"]
        var dropLayer = shapeUtil.add(comp, drop)
        // dropLayers[drop["layerName"]] = dropLayer
        var dropTextLayer = textUtil.overlay(comp, dropLayer, NODE_PREFIX + "." + "Drop" + '.' + "Text" + "." + key, {"text": key, "Opacity": 0});


        nodePath["pathGroup"]["type"] = "Group"
        nodePath["layerName"] = NODE_PREFIX + "."  + "Path" + "." + key;
        // path["Position"] = shapeLayer("Transform")("Position").value.slice(0, 2)
        nodePath["Position"] = nodeShape["Position"]
        
        var pathLayer = shapeUtil.add(comp, nodePath)
        // nodePathLayers.push(pathLayer)

        nodeLayers[key] = {
            "key": key,
            "Position": shapeLayer("Transform")("Position").value,
            "shapeLayer": shapeLayer, "shapeTextLayer": shapeTextLayer, "selectedLayer": selectedLayer, "dropLayer": dropLayer, "dropTextLayer": dropTextLayer, "pathLayer": pathLayer,
            "edgeLayers": {
                "down": {"left": null, "right": null},
                "up": upEdge ? upEdge : null,
            },
            "left": null, "right": null
        }
        if (parentNode) {
            parentNode[direction] = nodeLayers[key]
        }

        return nodeLayers[key]
    }

    function addEdge(key, upNode, direction) {
        var upKey = upNode["key"];
        var upPos = upNode["Position"];

        if (direction === "left") {
            edgeShape["Position"] = [upPos[0]-edgeOffset,upPos[1]+edgeOffset]
            edgeShape["Rotation"] = rotation
            edgePath["Rotation"] = 0
        } else if (direction === "right") {
            edgeShape["Position"] = [upPos[0]+edgeOffset, upPos[1]+edgeOffset]
            edgeShape["Rotation"] = -rotation
            edgePath["Rotation"] = -rotation*2
        } else {
            throw new TypeError("参数[direction]类型错误")
        }

        edgeShape["layerName"] = EDGE_PREFIX + "." + direction + "." + "Shape" + "." + upKey + '->' + key
        var shapeLayer = shareUtil.addLayer(comp, edgeShape)

        edgePath["pathGroup"]["type"] = "Group"
        edgePath["layerName"] = EDGE_PREFIX + "." + direction + "." + "Path" + "." + upKey + '->' + key
        edgePath["Position"] = edgeShape["Position"]
        var pathLayer = shapeUtil.add(comp, edgePath)

        edgeLayers[key] = {
            "key": key,
            "shapeLayer": shapeLayer, "pathLayer": pathLayer,
            "nodeLayers": {
                "up": upNode ? upNode : null,
                "down": null,
            }
        }
        upNode["edgeLayers"]["down"][direction] = edgeLayers[key]

        return edgeLayers[key]
    }

    var rootNode = addNode(elems[0], null, null, selected, drop)

    var i = 1;
    var nodeQueue = [rootNode]

    while (nodeQueue.length > 0) {
        var treeNode = nodeQueue.shift();
        if (js_null(elems[i])) {
            var edgeLayer = addEdge(elems[i], treeNode, "left")
            var nodeLayer = addNode(elems[i], treeNode, "left", selected, drop, edgeLayer)
            nodeQueue.push(nodeLayer)
        }
        i += 1;
        if (js_null(elems[i])) {
            var edgeLayer = addEdge(elems[i], treeNode, "right")
            var nodeLayer = addNode(elems[i], treeNode, "right", selected, drop, edgeLayer)
            nodeQueue.push(nodeLayer)
        }
        i += 1;
    }

    var times = [1, 1.5]

    var selectedKeyframes;
    var dropKeyframes;
    var dropTmp = {"Position": null, "sn": 0};
    var nodePathKeyframes;
    var edgePathKeyframes;
    var forwardPath = []
    var backwardPath = []
    var temporal = [[[0, 0.1], [1000, 100]], [[0, 75], [0, 0.1]]]

    selectedKeyframes = {
        "Transform.Opacity": [null, [0, 100], {"spatial": [{"type": 'HOLD'}]}]
    }

    dropKeyframes = {
        "Transform.Opacity": [null, [0, 100, 0]],
        "Transform.Position": [null, null, {"temporal": temporal}],
        "Transform.Rotation": [null, [0, 45]],
        "Contents.Group 1.Contents.Path 1.Path": [
            null,
            [
                {
                    "vertices": [[0, -50], [50, 0], [0, 50], [-50, 0]],
                    "inTangents": [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0],
                    [0, 27.6142425537109]],
                    "outTangents": [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0],
                    [0, -27.6142425537109]],
                    "closed": 'true'
                },
                {
                    "vertices": [[0, -57.5], [57.5, 0], [0, 57.5], [-57.5, 0]],
                    // "inTangents": [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0], [0, 27.6142425537109]],
                    // "outTangents": [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0], [0, -27.6142425537109]],
                    "closed": true
                }
            ]
        ]
    }

    function configSelectedDrop(key) {
        var selectedLayer = nodeLayers[key]["selectedLayer"]
        if (selectedLayer("Transform")("Opacity").numKeys === 0) {
            selectedKeyframes["Transform.Opacity"][0] = times-[0.5, 0.5]; 
            shareUtil.configKeyframes(selectedLayer, selectedKeyframes);

            var dropLayer = nodeLayers[key]["dropLayer"]
            dropKeyframes["Transform.Opacity"][0] = [times[0], times[1], times[1]+0.5]
            dropTmp["Position"] = dropLayer("Transform")("Position").value
            dropKeyframes["Transform.Position"][0] = times
            dropKeyframes["Transform.Position"][1] = [dropTmp["Position"], [50+dropTmp["sn"]*84, 750]]
            dropKeyframes["Transform.Rotation"][0] = times
            dropKeyframes["Contents.Group 1.Contents.Path 1.Path"][0] = times
            shareUtil.configKeyframes(dropLayer, dropKeyframes);
            shareUtil.configKeyframes(
                nodeLayers[key]["dropTextLayer"], 
                {"Transform.Rotation": [times, [0, -45]], "Transform.Opacity": [[times[0], times[1], times[1]+0.5], [0, 100, 0]]}
            )
            dropTmp["sn"] += 1

            // 配置遍历结果队列动画
            var queueKeyframes = {"Transform.Opacity": [times+[0.5, 0.5], [0, 100]]}
            var elemLayers = precompUtil.queueLayers["inorder"][key]
            shareUtil.configKeyframes(elemLayers["shapeLayer"], queueKeyframes)
            shareUtil.configKeyframes(elemLayers["textLayer"], queueKeyframes)
            // for (var kQueue in precompUtil.queueLayers) {
            //     $.writeln(kQueue)
            //     var queue = precompUtil.queueLayers[kQueue]
            //     for (var kElem in queue) {
            //         $.writeln(kElem)
            //     }
            //     $.writeln('===============================')
            // }
        }
    }

    function configforwardPath() {
        nodePathKeyframes = {
            'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [50, 0]],
            'Contents.Group 1.Contents.Trim Paths 1.End': [times, [50, 100]],
        }
        edgePathKeyframes = {
            'Contents.Group 1.Contents.Trim Paths 1.End': [times, [0, 100]],
        }

        for (var i = 0; i < forwardPath.length; i++) {
            if (forwardPath[i].name.indexOf("Node") !== -1) {
                // if (!keys[forwardPath[i].name]) {
                //     shareUtil.configKeyframes(forwardPath[i],  {
                //         'Contents.Group 1.Contents.Trim Paths 1.Start': [[0, times[0]-1/FRAME_RATE], [50, 50]],
                //         'Contents.Group 1.Contents.Trim Paths 1.End': [[0, times[0]-1/FRAME_RATE], [50, 50]],
                //     });
                // }
                shareUtil.configKeyframes(forwardPath[i], nodePathKeyframes);
            } else {
                // if (!keys[forwardPath[i].name]) {
                //     shareUtil.configKeyframes(forwardPath[i],  {
                //         'Contents.Group 1.Contents.Trim Paths 1.End': [[0, times[0]-1/FRAME_RATE], [0, 0]],
                //     });
                // }
                shareUtil.configKeyframes(forwardPath[i], edgePathKeyframes);
            }
            // keys[forwardPath[i].name] = true
            times[0] += 1
            times[1] = times[0] + 0.5
        }
        var key = forwardPath[i-1].name.split('.').slice(-1)
        configSelectedDrop(key)
        forwardPath = [];
    }

    function configBackwardPath() {
        nodePathKeyframes = {
            'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [0, 50]],
            'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 50]],
        }
        edgePathKeyframes = {
            'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 0]],
        }

        for (var i = 0; i < 2; i++) {
            if (backwardPath[0].name.indexOf("Edge") !== -1) {
                shareUtil.configKeyframes(backwardPath[0], edgePathKeyframes);
            }
            else {
                shareUtil.configKeyframes(backwardPath[0], nodePathKeyframes);
            }
            times[0] += 1
            times[1] = times[0] + 0.5
            backwardPath.shift()
        }
        var key = backwardPath.shift().name.split('.').slice(-1)
        configSelectedDrop(key)
    }

    function inorderProcess(node) {
        // $.writeln("==================================")
        // var nodeLayer = node["nodeLayer"]
        // $.writeln(nodeLayer.name)
        // var nodePathLayer = node["nodePathLayer"]
        // $.writeln(nodePathLayer.name)
        // shareUtil.configKeyframes(nodePathLayer, inorderKeyframe);
        // for (var k in inorderKeyframe) {
        //     inorderKeyframe[k][0][0] += 1
        //     inorderKeyframe[k][0][1] = inorderKeyframe[k][0][0] + 0.5
        // }
    }


    function preorder(root, func) {
        // $.writeln(root["key"])
        func(root["data"]);
        if (root["left"]) {
            preorder(root["left"], func);
        }
        if (root["right"]) {
            preorder(root["right"], func);
        }
    }

    // preorder(rootNode, processNode)

    // 对动画路径来说其实是前序遍历
    function inorder(root, func) {
        forwardPath.push(root["pathLayer"])
        var direction = "left"
        if (root[direction]) {
            forwardPath.push(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root["pathLayer"])
            backwardPath.unshift(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root[direction]["pathLayer"])
            inorder(root[direction], func)
        }
        func(root)
        var direction = "right"
        if (root[direction]) {
            forwardPath.push(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root["pathLayer"])
            backwardPath.unshift(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root[direction]["pathLayer"])
            inorder(root[direction], func)
        }
        if (!root["left"] && !root["right"]) {
            // 配置路径动画
            configforwardPath()
            if (backwardPath.length > 0) {
                configBackwardPath()
            }
        }
    }

    inorder(rootNode, inorderProcess)
    configBackwardPath()
    shareUtil.configKeyframes(rootNode["pathLayer"], nodePathKeyframes);

    // 音效
    if (nodePath["sound"]) {
        var soundItem = shareUtil.findItemByName(node["Path"]["sound"]["name"])
        var startTimes = node["Path"]["sound"]["startTimes"]
        for (var i = 0; i < startTimes.length; i++) {
            var soundLayer = comp.layers.add(soundItem);
            soundLayer.startTime = startTimes[i];
        }
    }

    if (edgePath["sound"]) {
        var soundItem = shareUtil.findItemByName(edge["Path"]["sound"]["name"])
        var startTimes = edge["Path"]["sound"]["startTimes"]
        for (var i = 0; i < startTimes.length; i++) {
            var soundLayer = comp.layers.add(soundItem);
            soundLayer.startTime = startTimes[i];
        }
    }

    var compLayer = parentComp.layers.add(comp);
    compLayer("Transform")("Position").setValue(conf["Position"])
    compLayer.startTime = conf["startTime"]
    if (conf['3D']) {
		compLayer.threeDLayer = true;
	}
    return {'comp': comp, 'compLayer': compLayer};
}

PrecompUtil.prototype.graph = function (nodeLayer, edgeLayer, elems) {

}

var precompUtil = new PrecompUtil();