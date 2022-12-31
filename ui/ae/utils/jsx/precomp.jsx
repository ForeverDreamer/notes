function PrecompUtil() {
    this.queueLayers = {}
}

PrecompUtil.prototype.stack = function (comp, conf) {

}

PrecompUtil.prototype.queue = function (comp, conf) {
    var traverse = conf["traverse"]
    this.queueLayers[traverse] = {}
    var elems = conf['elems']
    var unit = conf["unit"];

    var queueComp = project.items.addComp(conf["name"], conf['width'], conf['height'], PIXEL_ASPECT, conf['duration'], FRAME_RATE);

    var elemHeight = unit["pathGroup"]["Size"][0]
    var elemWidth = unit["pathGroup"]["Size"][1]
	// var height = layer.sourceRectAtTime(startTime, false).height
    for (var i = 0; i < elems.length; i++) {
        var key = elems[i]["key"]
        unit["layerName"] = "Shape" + "." + key
        unit["Position"] = [elemWidth / 2 + elemWidth * i, elemHeight / 2]
        if (elems[i]["Color"]) {
            unit["Fill"]["Color"] = colorUtil.hexToRgb1(elems[i]["Color"])
        }
        // var shapeLayer = shareUtil.addLayer(queueComp, unit);
        var shapeLayer = shapeUtil.create_one(queueComp, unit)
        if (elems[i]["keyframes"]) {
            shareUtil.configKeyframes(shapeLayer, elems[i]["keyframes"])
        }
        var textLayer = textUtil.overlay(
            queueComp, shapeLayer, "Text" + "." + key,
            {"text": key, "font": "Arial-BoldItalicMT", "fontSize": 40, "Position": [elemWidth/2, elemHeight/2]}
        );
        this.queueLayers[traverse][key] = {'shapeLayer': shapeLayer, "textLayer": textLayer}
    }
    shareUtil.addLayer(comp, conf, queueComp);
    // effectsUtil.add(queueLayer, "ADBE Drop Shadow", {"Distance": 10, "Softness": 30, "Opacity": 255});
}

PrecompUtil.prototype._btTraverseSelectedDropQueue = function (key, traverse) {
    var times = this.times

    var selectedKeyframes = {
        "Transform.Opacity": [null, [0, 100], {"spatial": [{"type": 'HOLD'}]}]
    }

    var dropTmp = precompUtil.dropTmp;
    var dropKeyframes = {
        "Transform.Opacity": [null, [0, 100, 0]],
        "Transform.Position": [null, null, {"temporal": [[[0, 0.1], [1000, 100]], [[0, 75], [0, 0.1]]]}],
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
    // 选中
    var selectedLayer = this.nodeLayers[key]["selectedLayer"]
    if (selectedLayer("Transform")("Opacity").numKeys === 0) {
        selectedKeyframes["Transform.Opacity"][0] = times-[0.5, 0.5];
        shareUtil.configKeyframes(selectedLayer, selectedKeyframes);
        // 掉落
        var dropLayer = this.nodeLayers[key]["dropLayer"]
        dropKeyframes["Transform.Opacity"][0] = [times[0], times[1], times[1]+0.5]
        dropTmp["Position"] = dropLayer("Transform")("Position").value
        dropKeyframes["Transform.Position"][0] = times
        dropKeyframes["Transform.Position"][1] = [dropTmp["Position"], [50+dropTmp["sn"]*80, 810]]
        dropKeyframes["Transform.Rotation"][0] = times
        dropKeyframes["Contents.Group 1.Contents.Path 1.Path"][0] = times
        shareUtil.configKeyframes(dropLayer, dropKeyframes);
        shareUtil.configKeyframes(
            this.nodeLayers[key]["dropTextLayer"],
            {"Transform.Rotation": [times, [0, -45]], "Transform.Opacity": [[times[0], times[1], times[1]+0.5], [0, 100, 0]]}
        )
        dropTmp["sn"] += 1

        // 队列
        var queueKeyframes = {"Transform.Opacity": [times+[0.5, 0.5], [0, 100]]}
        // var elemLayers = precompUtil.queueLayers[traverse][key]
        var elemLayers = this.queueLayers[traverse][key]
        shareUtil.configKeyframes(elemLayers["shapeLayer"], queueKeyframes)
        shareUtil.configKeyframes(elemLayers["textLayer"], queueKeyframes)
        if (traverse === "preorder" && key === '3') {
            shareUtil.configKeyframes(selectedLayer, {
                "Contents.Group 1.Contents.Fill 1.Color": [[times[0], times[1]+17.5], [colorUtil.hexToRgb1('#FFFFFF'), colorUtil.hexToRgb1('#0573E1')], {"spatial": [{"type": 'HOLD'}]}]
            });
            shareUtil.configKeyframes(elemLayers["shapeLayer"], {
                "Contents.Group 1.Contents.Fill 1.Color": [[times[0], times[1]+17.5], [colorUtil.hexToRgb1('#FFFFFF'), colorUtil.hexToRgb1('#0573E1')], {"spatial": [{"type": 'HOLD'}]}]
            });
        }
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

PrecompUtil.prototype._btTraverseForwardPath = function (traverse, forwardPath) {
    var times = this.times
    var nodePathKeyframes = {
        'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [50, 0]],
        'Contents.Group 1.Contents.Trim Paths 1.End': [times, [50, 100]],
    }
    var edgePathKeyframes = {
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
            if (traverse === 'preorder') {
                var key = forwardPath[i].name.split('.').slice(-1)[0]
                this._btTraverseSelectedDropQueue(key, traverse)
            }
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
    if (traverse === 'inorder') {
        var key = forwardPath[i-1].name.split('.').slice(-1)[0]
        this._btTraverseSelectedDropQueue(key, traverse)
    }
    forwardPath.length = 0;
}

PrecompUtil.prototype._btTraverseBackwardPath = function (traverse, backwardPath) {
    var times = this.times
    var nodePathKeyframes = {
        'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [0, 50]],
        'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 50]],
    }
    var edgePathKeyframes = {
        'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 0]],
    }
    var length;
    switch (traverse) {
		case 'preorder':
			length = backwardPath.length
			break;
		case 'inorder':
			length = 2
			break;
	}
    for (var i = 0; i < length; i++) {
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
    if (traverse === 'inorder') {
        var key = backwardPath.shift().name.split('.').slice(-1)[0]
        this._btTraverseSelectedDropQueue(key, traverse)
    }
}

PrecompUtil.prototype._btTraverse = function (traverse, nodePath, edgePath) {

    function processNode(node) {
        // $.writeln("==================================")
    }

    function preorder(traverse, root, func, forwardPath, backwardPath) {
        func(root)
        forwardPath.push(root["pathLayer"])
        backwardPath.unshift(root["pathLayer"])
        var direction = "left"
        if (root[direction]) {
            forwardPath.push(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root["edgeLayers"]["down"][direction]["pathLayer"])
            preorder(traverse, root[direction], func, forwardPath, backwardPath)
        }
        direction = "right"
        if (root[direction]) {
            forwardPath.push(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root["edgeLayers"]["down"][direction]["pathLayer"])
            preorder(traverse, root[direction], func, forwardPath, backwardPath)
        }
    }

    // 对动画路径来说其实是前序遍历
    function inorder(traverse, root, func, forwardPath, backwardPath) {
        forwardPath.push(root["pathLayer"])
        var direction = "left"
        if (root[direction]) {
            forwardPath.push(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root["pathLayer"])
            backwardPath.unshift(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root[direction]["pathLayer"])
            inorder(traverse, root[direction], func, forwardPath, backwardPath)
        }
        func(root)
        direction = "right"
        if (root[direction]) {
            forwardPath.push(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root["pathLayer"])
            backwardPath.unshift(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root[direction]["pathLayer"])
            inorder(traverse, root[direction], func, forwardPath, backwardPath)
        }
        if (!root["left"] && !root["right"]) {
            // 配置路径动画
            precompUtil._btTraverseForwardPath(traverse, forwardPath)
            if (backwardPath.length > 0) {
                precompUtil._btTraverseBackwardPath(traverse, backwardPath)
            }
        }
    }

    function doTraverse(traverse, root, func) {
        precompUtil.dropTmp = {"Position": null, "sn": 0};
        var times = precompUtil.times
        var forwardPath = []
        var backwardPath = []

        if (traverse === 'preorder') {
            preorder(traverse, root, func, forwardPath, backwardPath)
            precompUtil._btTraverseForwardPath(traverse, forwardPath)
            precompUtil._btTraverseBackwardPath(traverse, backwardPath)
        } else if (traverse === 'inorder') {
            inorder(traverse, root, func, forwardPath, backwardPath)
            precompUtil._btTraverseBackwardPath(traverse, backwardPath)
            shareUtil.configKeyframes(root["pathLayer"], {
                'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [0, 50]],
                'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 50]],
            });
        }

    }

    doTraverse(traverse, this.rootNode, processNode)

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
}

PrecompUtil.prototype.binaryTree = function (parentComp, conf) {
    var comp = project.items.addComp(conf["name"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE);

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

    var NODE_PREFIX = "Node";
    var EDGE_PREFIX = "Edge";

    var rootNodePos = [235*nodeScale, 75*nodeScale]
    this.nodeLayers = {}
    this.edgeLayers = {}

    if (nodePath) {
        var offset = nodePath["Trim Paths"]["Offset"]
    }
    var rotation = edgeShape["Rotation"]

    this.times = [0, 0.5]
    var step = [0.5, 0.5]

    function addNode(elem, parentNode, direction, selected, drop, upEdge) {
        var times = precompUtil.times
        var nodeLayers = precompUtil.nodeLayers
        var key = elem["key"]

        if (parentNode) {
            var parentPos = parentNode["Position"]
        }

        switch (direction) {
            case 'left':
                nodeShape["Position"] = [parentPos[0]-horizontalDist, parentPos[1]+verticalDist]
                if (nodePath) {
                    nodePath["Trim Paths"]["Offset"] = offset
                }
                break;
            case 'right':
                nodeShape["Position"] = [parentPos[0]+horizontalDist, parentPos[1]+verticalDist]
                if (nodePath) {
                    nodePath["Trim Paths"]["Offset"] = -offset
                }
                break;
            case null:
                nodeShape["Position"] = rootNodePos
                break;
            default:
                throw new TypeError("参数[direction]类型错误")
        }

        var shapeKeyframes = {
            "Transform.Opacity": [times, [0, 100], {"temporal": [[[0, 0.1], [200, 100]], [[0, 75], [0, 0.1]]]}]
        }
        nodeShape["layerName"] = NODE_PREFIX + "." + "Shape" + "." + key
        var shapeTextProps = {"text": key}
        if (js_bool(conf["animation"])) {
            nodeShape["keyframes"] = shapeKeyframes
            shapeTextProps["keyframes"] = shapeKeyframes
            precompUtil.times += step
        }
        var shapeLayer = shareUtil.addLayer(comp, nodeShape);

        if (selected) {
            selected["Position"] = nodeShape["Position"]
            selected["layerName"] = NODE_PREFIX + "." + "Selected" + "." + key
            if (elem["Color"]) {
                selected["Fill"]["Color"] = colorUtil.hexToRgb1(elem["Color"])
            }
            var selectedLayer = shapeUtil.create_one(comp, selected)
            // selectedLayers[selected["layerName"]] = selectedLayer
        }
        var shapeTextLayer = textUtil.overlay(comp, shapeLayer, NODE_PREFIX + "." + "Text" + "." + key, shapeTextProps);

        if (drop) {
            // drop["Fill"]["Color"] = drop["Fill"]["Color"]
            drop["layerName"] = NODE_PREFIX + "." + "Drop" + "." + key
            drop["Position"] = nodeShape["Position"]
            var dropLayer = shapeUtil.create_one(comp, drop)
            // dropLayers[drop["layerName"]] = dropLayer
            var dropTextLayer = textUtil.overlay(comp, dropLayer, NODE_PREFIX + "." + "Drop" + '.' + "Text" + "." + key, {"text": key, "Opacity": 0});
        }

        if (nodePath) {
            nodePath["pathGroup"]["type"] = "Group"
            nodePath["layerName"] = NODE_PREFIX + "."  + "Path" + "." + key;
            // path["Position"] = shapeLayer("Transform")("Position").value.slice(0, 2)
            nodePath["Position"] = nodeShape["Position"]
            var pathLayer = shapeUtil.create_one(comp, nodePath)
            // nodePathLayers.push(pathLayer)
        }

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

    function addEdge(elem, upNode, direction) {
        var times = precompUtil.times
        var edgeLayers = precompUtil.edgeLayers

        var key = elem[0]
        var upKey = upNode["key"];
        var upPos = upNode["Position"];

        if (direction === "left") {
            edgeShape["Position"] = [upPos[0]-edgeOffset,upPos[1]+edgeOffset]
            edgeShape["Rotation"] = rotation
            if (edgePath) {
                edgePath["Rotation"] = 0
            }
        } else if (direction === "right") {
            edgeShape["Position"] = [upPos[0]+edgeOffset, upPos[1]+edgeOffset]
            edgeShape["Rotation"] = -rotation
            if (edgePath) {
                edgePath["Rotation"] = -rotation*2
            }
        } else {
            throw new TypeError("参数[direction]类型错误")
        }

        var edgeKeyframes = {
            // "Transform.Scale": [times, [[0, 0, 0], edgeShape["Scale"]], {"temporal": [[[0, 0.1], [200, 100]], [[0, 75], [0, 0.1]]]}]
            "Transform.Scale": [times, [[0, 0, 0], edgeShape["Scale"]], {"temporal": [[[0, 0.1], [300, 100]], [[0, 75], [0, 0.1]]]}]
        }
        edgeShape["layerName"] = EDGE_PREFIX + "." + direction + "." + "Shape" + "." + upKey + '.' + key
        if (js_bool(conf["animation"])) {
            edgeShape["keyframes"] = edgeKeyframes
            precompUtil.times += step
        }
        var shapeLayer = shareUtil.addLayer(comp, edgeShape)

        if (edgePath) {
            edgePath["pathGroup"]["type"] = "Group"
            edgePath["layerName"] = EDGE_PREFIX + "." + direction + "." + "Path" + "." + upKey + '.' + key
            edgePath["Position"] = edgeShape["Position"]
            var pathLayer = shapeUtil.create_one(comp, edgePath)
        }

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

    if (conf["traverse"]) {
        this._btTraverse(conf["traverse"], nodePath, edgePath)
    }

    var compLayer = parentComp.layers.add(comp);
    compLayer("Transform")("Position").setValue(conf["Position"])
    compLayer.startTime = conf["startTime"]
    if (conf['3D']) {
		compLayer.threeDLayer = true;
	}
    shareUtil.configMasks(compLayer, conf["Masks"])
    shareUtil.configKeyframes(compLayer, conf["keyframes"])
    return {'comp': comp, 'compLayer': compLayer};
}

PrecompUtil.prototype.graph = function (nodeLayer, edgeLayer, elems) {

}

PrecompUtil.prototype.createOne = function (parentComp, conf) {
    var comp;
    if (conf["type"] === "STACK") {
        comp = this.stack(parentComp, conf)
    } else if (conf["type"] === "QUEUE") {
        comp = this.queue(parentComp, conf)
    } else if (conf["type"] === "LINKED_LIST") {

    } else if (conf["type"] === "BINARY_TREE") {
        comp = this.binaryTree(parentComp, conf)
    } else if (conf["type"] === "GRAPH") {
        comp = this.graph(conf)
    } else if (conf["type"] === "CODE") {

    }
    if (conf["children"]) {
        for (var j = 0; j < conf["children"].length; j++) {
            this.createOne(comp, conf["children"][j])
        }
    }
    return comp
}

PrecompUtil.prototype.createMany = function (precomps) {
    for (var i = 0; i < precomps.length; i++) {
        this.createOne(mainComp, precomps[i])
    }
}

var precompUtil = new PrecompUtil();