function PrecompUtil() { }

PrecompUtil.prototype.stack = function (nodeLayer, edgeLayer, elems) {

}

PrecompUtil.prototype.stack = function (comp, conf) {

}

PrecompUtil.prototype.queue = function (comp, conf) {
    this.queueInorderLayers = {}
    var height = conf['height']
    var elems = conf['elems']
    var startTime = conf["startTime"]
    var unit = conf["unit"];
    var effects = conf['effects']
    var keyframes = conf['keyframes']

    var queueComp = project.items.addComp('队列.' + conf["name"], conf['width'], conf['height'], PIXEL_ASPECT, conf['duration'], FRAME_RATE);

    var originalWidth = 108
    var elemWidth = originalWidth * unit["scale"][0]/100
	// var height = layer.sourceRectAtTime(startTime, false).height
    for (var i = 0; i < elems.length; i++) {
        unit["pos"] = [elemWidth / 2 + elemWidth * i, height / 2, 0]
        unit["Size"] =  [elemWidth, height]
        var shapeLayer = shareUtil.addLayer(queueComp, unit);
        shapeLayer.name = "Shape" + "." + elems[i]
        var textLayer = textUtil.overlay(
            queueComp, shapeLayer, "Text" + "." + elems[i],
            {"text": elems[i], "font": "Arial-BoldItalicMT", "fontSize": 40, "pos": [elemWidth/2, height/2]}
        );
        this.queueInorderLayers[elems[i].toString()] = {'shape': shapeLayer, "text": textLayer}
    }
    var queueLayer = mainComp.layers.add(queueComp);
    queueLayer.startTime = startTime;
    shareUtil.setAnchorPoint(queueLayer, 'LEFT')
    queueLayer("Transform")("Position").setValue(conf["pos"]);
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
    
        drop["Fill"]["Color"] = drop["Fill"]["Color"]
        drop["layerName"] = NODE_PREFIX + "." + "Drop" + "." + key
        drop["Position"] = nodeShape["Position"]
        var dropLayer = shapeUtil.add(comp, drop)
        // dropLayers[drop["layerName"]] = dropLayer
    
        var textLayer = textUtil.overlay(comp, shapeLayer, NODE_PREFIX + "." + "Text" + "." + key, {"text": key, "pos": textPos});

        nodePath["pathGroup"]["type"] = "Group"
        nodePath["layerName"] = NODE_PREFIX + "."  + "Path" + "." + key;
        // path["Position"] = shapeLayer("Transform")("Position").value.slice(0, 2)
        nodePath["Position"] = nodeShape["Position"]
        
        var pathLayer = shapeUtil.add(comp, nodePath)
        // nodePathLayers.push(pathLayer)

        nodeLayers[key] = {
            "key": key,
            "Position": shapeLayer("Transform")("Position").value,
            "shapeLayer": shapeLayer, "textLayer": textLayer, "selectedLayer": selectedLayer, "dropLayers": dropLayer, "pathLayer": pathLayer,
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
    var nodeKeyframes;
    var edgeKeyframes;
    var forwardPath = []
    var backwardPath = []

    function configforwardPath() {
        nodeKeyframes = {
            'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [50, 0]],
            'Contents.Group 1.Contents.Trim Paths 1.End': [times, [50, 100]],
        }
        edgeKeyframes = {
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
                shareUtil.configKeyframes(forwardPath[i], nodeKeyframes);
            } else {
                // if (!keys[forwardPath[i].name]) {
                //     shareUtil.configKeyframes(forwardPath[i],  {
                //         'Contents.Group 1.Contents.Trim Paths 1.End': [[0, times[0]-1/FRAME_RATE], [0, 0]],
                //     });
                // }
                shareUtil.configKeyframes(forwardPath[i], edgeKeyframes);
            }
            // keys[forwardPath[i].name] = true
            times[0] += 1
            times[1] = times[0] + 0.5
        }
        var key = forwardPath[i-1].name.split('.').slice(-1)
        shareUtil.configKeyframes(nodeLayers[key]["selectedLayer"], {"Transform.Opacity": [times, [0, 100], {"spatial": [{"type": 'HOLD'}]}]});
        forwardPath = [];
    }

    function configBackwardPath() {
        nodeKeyframes = {
            'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [0, 50]],
            'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 50]],
        }
        edgeKeyframes = {
            'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 0]],
        }

        for (var i = 0; i < 2; i++) {
            if (backwardPath[0].name.indexOf("Edge") !== -1) {
                shareUtil.configKeyframes(backwardPath[0], edgeKeyframes);
            }
            else {
                shareUtil.configKeyframes(backwardPath[0], nodeKeyframes);
            }
            times[0] += 1
            times[1] = times[0] + 0.5
            backwardPath.shift()
        }
        var key = backwardPath.shift().name.split('.').slice(-1)
        if (nodeLayers[key]["selectedLayer"]("Transform")("Opacity").numKeys === 0) {
            shareUtil.configKeyframes(nodeLayers[key]["selectedLayer"], {"Transform.Opacity": [times, [0, 100], {"spatial": [{"type": 'HOLD'}]}]});
        }
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

    // $.writeln("二叉树前序==================================")
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
            $.writeln("配置路径动画==================================")
            // keys = {}
            // 配置路径动画
            configforwardPath()

            $.writeln("==================================")
            if (backwardPath.length > 0) {
                configBackwardPath()
            }
        }
    }

    $.writeln("二叉树中序==================================")
    inorder(rootNode, inorderProcess)
    configBackwardPath()
    shareUtil.configKeyframes(rootNode["pathLayer"], nodeKeyframes);

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