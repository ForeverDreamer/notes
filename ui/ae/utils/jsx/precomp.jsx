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

PrecompUtil.prototype.addNodePath = function (comp, conf) {
    var shapeLayer = comp.layers.addShape();
    shapeLayer.name = conf['layerName'];
    var shapeGroup = shapeLayer("Contents").addProperty("ADBE Vector Group");
    var pathGroup = shapeGroup("Contents").addProperty("ADBE Vector Shape - Group")
    var shape = new Shape();
    shape.vertices = conf["vertices"];
    shape.inTangents = conf["inTangents"];
    shape.outTangents = conf["outTangents"];
    shape.closed = conf["closed"];
    pathGroup("Path").setValue(shape);
    trimGroup = shapeGroup("Contents").addProperty("ADBE Vector Filter - Trim");
    strokeGroup = shapeGroup("Contents").addProperty("ADBE Vector Graphic - Stroke");
    strokeGroup("Color").setValue(colorUtil.hexToRgb1(conf["Color"]));
    strokeGroup("Stroke Width").setValue(conf["Stroke Width"]);
    shapeGroup("Transform")("Anchor Point").setValue([0, 0]);
    shapeGroup("Transform")("Position").setValue([0, 0]);
    var anchorPoint = shareUtil.setAnchorPoint(shapeLayer);
    shapeLayer("Transform")("Position").setValue(conf["Position"]);
    // shareUtil.configKeyframes(shapeLayer, conf["keyframes"]);
    shapeLayer("Contents")("Group 1")("Contents")("Trim Paths 1")("Start").setValue(conf["Start"]);
    shapeLayer("Contents")("Group 1")("Contents")("Trim Paths 1")("End").setValue(conf["End"]);
    shapeLayer("Contents")("Group 1")("Contents")("Trim Paths 1")("Offset").setValue(conf["Offset"]);
    if (conf["effects"]) {
        for (var i = 0; i < conf["effects"].length; i++) {
            effectsUtil.add(shapeLayer, conf["effects"][i]);
        }
    }
    return shapeLayer
}

PrecompUtil.prototype.addEdgePath = function (comp, conf) {
    var shapeLayer = comp.layers.addShape();
    shapeLayer.name = conf['layerName'];
    var shapeGroup = shapeLayer("Contents").addProperty("ADBE Vector Group");
    var pathGroup = shapeGroup("Contents").addProperty("ADBE Vector Shape - Group");
    var shape = new Shape();
    shape.vertices = conf["vertices"];
    shape.closed = conf["closed"];
    pathGroup("Path").setValue(shape);
    trimGroup = shapeGroup("Contents").addProperty("ADBE Vector Filter - Trim");
    strokeGroup = shapeGroup("Contents").addProperty("ADBE Vector Graphic - Stroke");
    strokeGroup("Color").setValue(colorUtil.hexToRgb1(conf["Color"]));
    strokeGroup("Stroke Width").setValue(conf["Stroke Width"]);
    var anchorPoint = shareUtil.setAnchorPoint(shapeLayer, "RIGHT_TOP");
    shapeGroup("Transform")("Anchor Point").setValue(conf["Position"]);
    shapeGroup("Transform")("Position").setValue(conf["Position"]);
    shapeLayer("Transform")("Position").setValue(conf["Position"]);
    if (conf["Rotation"]) {
        shapeLayer("Transform")("Rotation").setValue(conf["Rotation"]);
    }
    shapeLayer("Contents")("Group 1")("Contents")("Trim Paths 1")("End").setValue(conf["End"]);
    if (conf["effects"]) {
        for (var i = 0; i < conf["effects"].length; i++) {
            effectsUtil.add(shapeLayer, conf["effects"][i]);
        }
    }
    // shareUtil.configKeyframes(shapeLayer, conf["keyframes"]);
    return shapeLayer
}

PrecompUtil.prototype.binaryTree = function (parentComp, conf) {
    var comp = project.items.addComp("二叉树." + conf["name"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE); 
    var selected = conf["selected"];
    var node = conf["node"];
    var edge = conf["edge"];
    var elems = conf["elems"];

    var scale = node["scale"][0]/100
    var edgeOffset = 45*scale;
    var horizontalDist = 160*scale;
    var verticalDist = 240*scale;
    var textPos = [64, 66, 0];

    var NODE_PATH_PREFIX = "Node.Path";
    var EDGE_PATH_PREFIX = "Edge.Path";
    var NODE_PREFIX = "Node";
    var EDGE_PREFIX = "Edge";

    var rootNodePos = [235*scale, 75*scale, 0]
    var nodePathLayers = []
    var edgePathLayers = []
    var selectedLayers = {}

    // var tracker = conf["tracker"];
    // if (tracker) {
    //     tracker["pos"] = rootNodePos
    //     tracker["layerName"] = "Tracker"
    //     var trackerLayer = shareUtil.comp(layers, tracker);
    //     shareUtil.configKeyframes(trackerLayer, tracker["keyframes"])
    //     // var effectsProp = trackerLayer.Effects.addProperty("PEDG");
    //     // effectsProp("Radius").expression = "random() * 50 + 10"
    //     // trackerLayer.moveToEnd()
    // }

    node["pos"] = rootNodePos
    node["layerName"] = NODE_PREFIX + "." + "Shape" + "." + elems[0]
    var nodeLayer = shareUtil.addLayer(comp, node);

    selected["pos"] = node["pos"]
    selected["layerName"] = NODE_PREFIX + "." + "Selected" + "." + elems[0]
    var selectedLayer = shareUtil.addLayer(comp, selected);
    selectedLayers[selected["layerName"]] = selectedLayer

    textUtil.overlay(comp, nodeLayer, NODE_PREFIX + "." + "Text" + "." + elems[0], {"text": elems[0], "pos": textPos});


    var path = node["Path"]
    path["layerName"] = NODE_PATH_PREFIX + "." + elems[0];
    path["Position"] = nodeLayer("Transform")("Position").value.slice(0, 2)
    var nodePathLayer = this.addNodePath(comp, path)
    nodePathLayers.push(nodePathLayer)

    var rootNode = {"key": elems[0], "data": {"nodeLayer": nodeLayer, "selectedLayer": selectedLayer, "nodePathLayer": nodePathLayer, "edgePathLayer": {}}, "left": null, "right": null}

    var i = 1;
    var offset = node["Path"]["Offset"]
    var rotation = edge["rotation"]
    var queue = [nodeLayer];
    var treeNodeQueue = [rootNode]
    // $.writeln(elems)
    while (queue.length > 0) {
        var parentNodeLayer = queue.shift();
        var treeNode = treeNodeQueue.shift();
        var parentPos = parentNodeLayer("Transform")("Position").value;
        var nodeLayer;
        var edgePathLayer;
        if (js_null(elems[i])) {
            edge["pos"] = [parentPos[0]-edgeOffset, parentPos[1]+edgeOffset, parentPos[2]];
            edge["rotation"] = rotation
            edge["layerName"] = EDGE_PREFIX + "." + "Left" + "." + elems[i]
            shareUtil.addLayer(comp, edge);

            path = edge["Path"];
            path["layerName"] = EDGE_PATH_PREFIX + "." + elems[i];
            path["Position"] = edge["pos"].slice(0, 2);
            path["Rotation"] = 0;
            // $.writeln(path["Position"]);
            edgePathLayer = this.addEdgePath(comp, path)
            edgePathLayers.push(edgePathLayer);

            node["pos"] = [parentPos[0]-horizontalDist, parentPos[1]+verticalDist, parentPos[2]];
            node["layerName"] = NODE_PREFIX + "." + "Shape" + "." + elems[i]
            nodeLayer = shareUtil.addLayer(comp, node);

            selected["pos"] = node["pos"]
            selected["layerName"] = NODE_PREFIX + "." + "Selected" + "." + elems[i]
            var selectedLayer = shareUtil.addLayer(comp, selected);
            selectedLayers[selected["layerName"]] = selectedLayer

            textUtil.overlay(comp, nodeLayer, NODE_PREFIX + "." + "Text" + "." + elems[i], {"text": elems[i], "pos": textPos});

            path = node["Path"];
            path["layerName"] = NODE_PATH_PREFIX + "." + elems[i];
            path["Position"] = nodeLayer("Transform")("Position").value.slice(0, 2)
            path["Offset"] = offset;
            nodePathLayer = this.addNodePath(comp, path)
            nodePathLayers.push(nodePathLayer);
            queue.push(nodeLayer)

            // treeNode["data"]["edgePathLayer"]["forward_left"] = nodePathLayer
            treeNode["left"] = {"key": elems[i], "data": {"nodeLayer": nodeLayer, "selectedLayer": selectedLayer, "nodePathLayer": nodePathLayer, "edgePathLayer": {"backward": edgePathLayer}}, "left": null, "right": null}
            treeNodeQueue.push(treeNode["left"])
        }
        i += 1;
        if (js_null(elems[i])) {
            edge["pos"] = [parentPos[0]+edgeOffset, parentPos[1]+edgeOffset, parentPos[2]]
            edge["rotation"] = -rotation
            edge["layerName"] = EDGE_PREFIX + "." + "Right" + "." + elems[i]
            shareUtil.addLayer(comp, edge);

            path = edge["Path"]
            path["layerName"] = EDGE_PATH_PREFIX + "." + elems[i];
            path["Position"] = edge["pos"].slice(0, 2);
            path["Rotation"] = -rotation*2
            edgePathLayer = this.addEdgePath(comp, path);
            edgePathLayers.push(edgePathLayer);

            node["pos"] = [parentPos[0]+horizontalDist, parentPos[1]+verticalDist, parentPos[2]]
            node["layerName"] = NODE_PREFIX + "." + "Shape" + "." + elems[i]
            nodeLayer = shareUtil.addLayer(comp, node);

            selected["pos"] = node["pos"]
            selected["layerName"] = NODE_PREFIX + "." + "Selected" + "." + elems[i]
            var selectedLayer = shareUtil.addLayer(comp, selected);
            selectedLayers[selected["layerName"]] = selectedLayer

            textUtil.overlay(comp, nodeLayer, NODE_PREFIX + "." + "Text" + "." + elems[i], {"text": elems[i], "pos": textPos});

            path = node["Path"];
            path["layerName"] = NODE_PATH_PREFIX + "." + elems[i];
            path["Position"] = nodeLayer("Transform")("Position").value.slice(0, 2);
            path["Offset"] = -offset;
            nodePathLayer = this.addNodePath(comp, path)
            nodePathLayers.push(nodePathLayer);
            queue.push(nodeLayer);
            
            // treeNode["data"]["edgePathLayer"]["forward_right"] = nodePathLayer
            treeNode["right"] = {"key": elems[i], "data": {"nodeLayer": nodeLayer, "selectedLayer": selectedLayer, "nodePathLayer": nodePathLayer, "edgePathLayer": {"backward": edgePathLayer}}, "left": null, "right": null}
            treeNodeQueue.push(treeNode["right"])
        }
        i += 1;
        // $.writeln("==================================")
    }

    var forwardPath = []
    var backwardPath = []

    function inorderProcess(data) {
        // $.writeln("==================================")
        // var nodeLayer = data["nodeLayer"]
        // $.writeln(nodeLayer.name)
        // var nodePathLayer = data["nodePathLayer"]
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
    var times = [1, 1.5]
    var nodeKeyframes;
    var edgeKeyframes;
    function inorder(root, func) {
        forwardPath.push(root["data"]["nodePathLayer"])
        if (root["left"]) {
            forwardPath.push(root["left"]["data"]["edgePathLayer"]["backward"])
            backwardPath.unshift(root["data"]["nodePathLayer"])
            backwardPath.unshift(root["left"]["data"]["edgePathLayer"]["backward"])
            backwardPath.unshift(root["left"]["data"]["nodePathLayer"])
            inorder(root["left"], func)
        }
        // $.writeln(root["key"])
        func(root["data"])
        if (root["right"]) {
            forwardPath.push(root["right"]["data"]["edgePathLayer"]["backward"])
            backwardPath.unshift(root["data"]["nodePathLayer"])
            backwardPath.unshift(root["right"]["data"]["edgePathLayer"]["backward"])
            backwardPath.unshift(root["right"]["data"]["nodePathLayer"])
            inorder(root["right"], func)
        }
        if (!root["left"] && !root["right"]) {
            $.writeln("配置路径动画==================================")
            keys = {}
            // 配置路径动画
            nodeKeyframes = {
                'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [50, 0]],
                'Contents.Group 1.Contents.Trim Paths 1.End': [times, [50, 100]],
            }
            edgeKeyframes = {
                'Contents.Group 1.Contents.Trim Paths 1.End': [times, [0, 100]],
            }
            for (var i = 0; i < forwardPath.length; i++) {
                $.writeln(forwardPath[i].name)
                if (forwardPath[i].name.indexOf("Node") == 0) {
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
                keys[forwardPath[i].name] = true
                times[0] += 1
                times[1] = times[0] + 0.5
            }
            var selectedLayerName = forwardPath[i-1].name.replace("Path", "Selected")
            var props = shareUtil.configKeyframes(selectedLayers[selectedLayerName], {"Transform.Opacity": [times, [0, 100]]});
            shareUtil.setKeyframeInterpolationType(props, KeyframeInterpolationType.HOLD)
            forwardPath = [];

            $.writeln("==================================")
            nodeKeyframes = {
                'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [0, 50]],
                'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 50]],
            }
            edgeKeyframes = {
                'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 0]],
            }

            if (backwardPath.length > 0) {
                for (var i = 0; i < 2; i++) {
                    $.writeln(backwardPath[0].name)
                    if (backwardPath[0].name.indexOf("Node") == 0) {
                        shareUtil.configKeyframes(backwardPath[0], nodeKeyframes);
                    } else {
                        shareUtil.configKeyframes(backwardPath[0], edgeKeyframes);
                    }
                    times[0] += 1
                    times[1] = times[0] + 0.5
                    backwardPath.shift()
                }
            }
            selectedLayerName = backwardPath.shift().name.replace("Path", "Selected")
            if (selectedLayers[selectedLayerName]("Transform")("Opacity").numKeys === 0) {
                var props = shareUtil.configKeyframes(selectedLayers[selectedLayerName], {"Transform.Opacity": [times, [0, 100]]});
                shareUtil.setKeyframeInterpolationType(props, KeyframeInterpolationType.HOLD)
            }
            // backwardPath = [];
        }
    }

    $.writeln("二叉树中序==================================")
    inorder(rootNode, inorderProcess)
    for (var i = 0; i < 2; i++) {
        $.writeln(backwardPath[0].name)
        if (backwardPath[0].name.indexOf("Node") == 0) {
            shareUtil.configKeyframes(backwardPath[0], nodeKeyframes);
        } else {
            shareUtil.configKeyframes(backwardPath[0], edgeKeyframes);
        }
        times[0] += 1
        times[1] = times[0] + 0.5
        backwardPath.shift()
    }
    shareUtil.configKeyframes(rootNode["data"]["nodePathLayer"], nodeKeyframes);

    // 动画
    // for (var i = 0; i < nodePathLayers.length; i++) {
    //     shareUtil.configKeyframes(nodePathLayers[i], node["Path"]["keyframes"][i]);
    // }

    // for (var i = 0; i < edgePathLayers.length; i++) {
    //     shareUtil.configKeyframes(edgePathLayers[i], edge["Path"]["keyframes"][i]);
    // }

    // 音效
    if (node["Path"]["sound"]) {
        var soundItem = shareUtil.findItemByName(node["Path"]["sound"]["name"])
        var startTimes = node["Path"]["sound"]["startTimes"]
        for (var i = 0; i < startTimes.length; i++) {
            var soundLayer = comp.layers.add(soundItem);
            soundLayer.startTime = startTimes[i];
        }
    }

    if (edge["Path"]["sound"]) {
        var soundItem = shareUtil.findItemByName(edge["Path"]["sound"]["name"])
        var startTimes = edge["Path"]["sound"]["startTimes"]
        for (var i = 0; i < startTimes.length; i++) {
            var soundLayer = comp.layers.add(soundItem);
            soundLayer.startTime = startTimes[i];
        }
    }

    var compLayer = parentComp.layers.add(comp);
    compLayer("Transform")("Position").setValue(conf["pos"])
    compLayer.startTime = conf["startTime"]
    if (conf['3D']) {
		compLayer.threeDLayer = true;
	}
    return {'comp': comp, 'compLayer': compLayer};
}

PrecompUtil.prototype.graph = function (nodeLayer, edgeLayer, elems) {

}

var precompUtil = new PrecompUtil();