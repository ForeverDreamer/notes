function PrecompUtil() { }

PrecompUtil.prototype.stack = function (nodeLayer, edgeLayer, elems) {

}

PrecompUtil.prototype.queue = function (comp, conf) {
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
        var textLayer = textUtil.overlay(
            queueComp, shapeLayer, "Text" + "." + elems[i],
            {"text": elems[i], "font": "Arial-BoldItalicMT", "fontSize": 40, "pos": [elemWidth/2, height/2]}
        );
    }
    var queueLayer = mainComp.layers.add(queueComp);
    queueLayer.startTime = startTime;
    shareUtil.setAnchorPoint(queueLayer, 'LEFT')
    queueLayer("Transform")("Position").setValue(conf["pos"]);
    effectsUtil.add(queueLayer, "ADBE Drop Shadow", {"Distance": 10, "Softness": 30, "Opacity": 255});
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
    if (conf["effects"]) {
        for (var i = 0; i < conf["effects"].length; i++) {
            effectsUtil.add(shapeLayer, conf["effects"][i]);
        }
    }
    // shareUtil.configKeyframes(shapeLayer, conf["keyframes"]);
    return shapeLayer
}

PrecompUtil.prototype.binaryTree = function (items, parentComp, conf) {
    var comp = items.addComp("二叉树." + conf["name"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE); 
    var layers = comp.layers;
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

    var selected = conf["selected"];
    if (selected) {
        selected["pos"] = rootNodePos
        selected["layerName"] = "Selected"
        var selectedLayer = shareUtil.addLayer(comp, selected);
        shareUtil.configKeyframes(selectedLayer, selected["keyframes"])
        // selectedLayer.moveToEnd()
    }
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
    textUtil.overlay(comp, nodeLayer, NODE_PREFIX + "." + "Text" + "." + elems[0], {"text": elems[0], "pos": textPos});
    var path = node["Path"]
    path["layerName"] = NODE_PATH_PREFIX + "." + elems[0];
    path["Position"] = nodeLayer("Transform")("Position").value.slice(0, 2)
    var nodePathLayer = this.addNodePath(comp, path)
    nodePathLayers.push(nodePathLayer)
    var rootNode = {"key": elems[0], "data": {"nodeLayer": nodeLayer, "nodePathLayer": nodePathLayer}, "left": null, "right": null}

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
            edgePathLayers.push(this.addEdgePath(comp, path));

            node["pos"] = [parentPos[0]-horizontalDist, parentPos[1]+verticalDist, parentPos[2]];
            node["layerName"] = NODE_PREFIX + "." + "Shape" + "." + elems[i]
            nodeLayer = shareUtil.addLayer(comp, node);
            textUtil.overlay(comp, nodeLayer, NODE_PREFIX + "." + "Text" + "." + elems[i], {"text": elems[i], "pos": textPos});

            path = node["Path"];
            path["layerName"] = NODE_PATH_PREFIX + "." + elems[i];
            path["Position"] = nodeLayer("Transform")("Position").value.slice(0, 2)
            path["Offset"] = offset;
            nodePathLayer = this.addNodePath(comp, path)
            nodePathLayers.push(nodePathLayer);
            queue.push(nodeLayer)

            treeNode["left"] = {"key": elems[i], "data": {"nodeLayer": nodeLayer, "nodePathLayer": nodePathLayer}, "left": null, "right": null}
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
            edgePathLayers.push(this.addEdgePath(comp, path));

            node["pos"] = [parentPos[0]+horizontalDist, parentPos[1]+verticalDist, parentPos[2]]
            node["layerName"] = NODE_PREFIX + "." + "Shape" + "." + elems[i]
            nodeLayer = shareUtil.addLayer(comp, node);
            textUtil.overlay(comp, nodeLayer, NODE_PREFIX + "." + "Text" + "." + elems[i], {"text": elems[i], "pos": textPos});

            path = node["Path"];
            path["layerName"] = NODE_PATH_PREFIX + "." + elems[i];
            path["Position"] = nodeLayer("Transform")("Position").value.slice(0, 2);
            path["Offset"] = -offset;
            nodePathLayer = this.addNodePath(comp, path)
            nodePathLayers.push(nodePathLayer);
            queue.push(nodeLayer);

            treeNode["right"] = {"key": elems[i], "data": {"nodeLayer": nodeLayer, "nodePathLayer": nodePathLayer}, "left": null, "right": null}
            treeNodeQueue.push(treeNode["right"])
        }
        i += 1;
        // $.writeln("==================================")
    }

    var inorderKeyframe = {
        'Transform.Opacity': [[1, 1.5], [0, 100]]
    }

    function inorderProcess(data) {
        $.writeln("==================================")
        var nodeLayer = data["nodeLayer"]
        $.writeln(nodeLayer.name)
        var nodePathLayer = data["nodePathLayer"]
        $.writeln(nodePathLayer.name)
        shareUtil.configKeyframes(nodePathLayer, inorderKeyframe);
        for (var k in inorderKeyframe) {
            inorderKeyframe[k][0][0] += 1
            inorderKeyframe[k][0][1] = inorderKeyframe[k][0][0] + 0.5
        }
    }


    function preorder(root, func) {
        // $.writeln(root["key"])
        func(root["data"])
        if (root["left"]) {
            preorder(root["left"], func)
        }
        if (root["right"]) {
            preorder(root["right"], func)
        }
    }

    // $.writeln("二叉树前序==================================")
    // preorder(rootNode, processNode)

    function inorder(root, func) {
        if (root["left"]) {
            inorder(root["left"], func)
        }
        // $.writeln(root["key"])
        func(root["data"])
        if (root["right"]) {
            inorder(root["right"], func)
        }
    }

    $.writeln("二叉树中序==================================")
    inorder(rootNode, inorderProcess)

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