function PrecompUtil() { }

PrecompUtil.prototype.stack = function (nodeLayer, edgeLayer, elems) {

}

PrecompUtil.prototype.queue = function (nodeLayer, edgeLayer, elems) {

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
    var comp = items.addComp(conf["name"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE); 
    var layers = comp.layers;
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
        var selectedLayer = shareUtil.addLayer(items, layers, selected);
        shareUtil.configKeyframes(selectedLayer, selected["keyframes"])
        // selectedLayer.moveToEnd()
    }
    // var tracker = conf["tracker"];
    // if (tracker) {
    //     tracker["pos"] = rootNodePos
    //     tracker["layerName"] = "Tracker"
    //     var trackerLayer = shareUtil.addLayer(items, layers, tracker);
    //     shareUtil.configKeyframes(trackerLayer, tracker["keyframes"])
    //     // var effectsProp = trackerLayer.Effects.addProperty("PEDG");
    //     // effectsProp("Radius").expression = "random() * 50 + 10"
    //     // trackerLayer.moveToEnd()
    // }

    node["pos"] = rootNodePos
    node["layerName"] = NODE_PREFIX + "." + "Shape" + "." + elems[0]
    var nodeLayer = shareUtil.addLayer(items, layers, node);
    textUtil.overlay(comp, nodeLayer, NODE_PREFIX + "." + "Text" + "." + elems[0], {"text": elems[0], "pos": textPos});
    var path = node["Path"]
    path["layerName"] = NODE_PATH_PREFIX + "." + elems[0];
    path["Position"] = nodeLayer("Transform")("Position").value.slice(0, 2)
    nodePathLayers.push(this.addNodePath(comp, path))

    var i = 1;
    var offset = node["Path"]["Offset"]
    var rotation = edge["rotation"]
    var queue = [nodeLayer];
    // $.writeln(elems)
    while (queue.length > 0) {
        var parentNodeLayer = queue.shift();
        var parentPos = parentNodeLayer("Transform")("Position").value;
        var layer;
        if (js_null(elems[i])) {
            edge["pos"] = [parentPos[0]-edgeOffset, parentPos[1]+edgeOffset, parentPos[2]];
            edge["rotation"] = rotation
            edge["layerName"] = EDGE_PREFIX + "." + "Left" + "." + elems[i]
            layer = shareUtil.addLayer(items, layers, edge);

            var path = edge["Path"];
            path["layerName"] = EDGE_PATH_PREFIX + "." + elems[i];
            path["Position"] = edge["pos"].slice(0, 2);
            path["Rotation"] = 0;
            // $.writeln(path["Position"]);
            edgePathLayers.push(this.addEdgePath(comp, path));

            node["pos"] = [parentPos[0]-horizontalDist, parentPos[1]+verticalDist, parentPos[2]];
            node["layerName"] = NODE_PREFIX + "." + "Shape" + "." + elems[i]
            layer = shareUtil.addLayer(items, layers, node);
            textUtil.overlay(comp, layer, NODE_PREFIX + "." + "Text" + "." + elems[i], {"text": elems[i], "pos": textPos});

            var path = node["Path"];
            path["layerName"] = NODE_PATH_PREFIX + "." + elems[i];
            path["Position"] = layer("Transform")("Position").value.slice(0, 2)
            nodePathLayers.push(this.addNodePath(comp, path));
            queue.push(layer)
        }
        i += 1;
        if (js_null(elems[i])) {
            edge["pos"] = [parentPos[0]+edgeOffset, parentPos[1]+edgeOffset, parentPos[2]]
            edge["rotation"] = -rotation
            edge["layerName"] = EDGE_PREFIX + "." + "Right" + "." + elems[i]
            layer = shareUtil.addLayer(items, layers, edge);

            var path = edge["Path"]
            path["layerName"] = EDGE_PATH_PREFIX + "." + elems[i];
            path["Position"] = edge["pos"].slice(0, 2);
            path["Rotation"] = -rotation*2
            edgePathLayers.push(this.addEdgePath(comp, path));

            node["pos"] = [parentPos[0]+horizontalDist, parentPos[1]+verticalDist, parentPos[2]]
            node["layerName"] = NODE_PREFIX + "." + "Shape" + "." + elems[i]
            layer = shareUtil.addLayer(items, layers, node);
            textUtil.overlay(comp, layer, NODE_PREFIX + "." + "Text" + "." + elems[i], {"text": elems[i], "pos": textPos});

            var path = node["Path"];
            path["layerName"] = NODE_PATH_PREFIX + "." + elems[i];
            path["Position"] = layer("Transform")("Position").value.slice(0, 2);
            path["Offset"] = -offset;
            nodePathLayers.push(this.addNodePath(comp, path));
            queue.push(layer);
        }
        i += 1;
        // $.writeln("==================================")
    }

    // 动画
    for (var i = 0; i < nodePathLayers.length; i++) {
        shareUtil.configKeyframes(nodePathLayers[i], node["Path"]["keyframes"][i]);
    }

    for (var i = 0; i < edgePathLayers.length; i++) {
        shareUtil.configKeyframes(edgePathLayers[i], edge["Path"]["keyframes"][i]);
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