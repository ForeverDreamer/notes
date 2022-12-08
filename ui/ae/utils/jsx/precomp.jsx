function PrecompUtil() { }

PrecompUtil.prototype.stack = function (nodeLayer, edgeLayer, elems) {

}

PrecompUtil.prototype.queue = function (nodeLayer, edgeLayer, elems) {

}

PrecompUtil.prototype.binaryTree = function (items, parentComp, conf) {
    var comp = items.addComp("二叉树." + conf['name'], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE);
    var layers = comp.layers;
    var node = conf["node"];
    var edge = conf["edge"];
    var elems = conf["elems"];

    var scale = node["scale"][0]/100
    var edgeOffset = 40*scale;
    var horizontalDist = 160*scale;
    var verticalDist = 240*scale;
    var textPos = [65, 75, 0];

    var NODE_PREFIX = "Node";
    var EDGE_PREFIX = "Edge";

    node["pos"] = [225*scale, 65*scale, 0]
    node["layerName"] = NODE_PREFIX + "." + "Shape" + "." + elems[0]
    var nodeLayer = shareUtil.addLayer(items, layers, node);
    textUtil.overlay(comp, nodeLayer, NODE_PREFIX + "." + "Text" + "." + elems[0], {"text": elems[0], "pos": textPos});

    var i = 1;
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
            shareUtil.addLayer(items, layers, edge);
            node["pos"] = [parentPos[0]-horizontalDist, parentPos[1]+verticalDist, parentPos[2]];
            node["layerName"] = NODE_PREFIX + "." + "Shape" + "." + elems[i]
            layer = shareUtil.addLayer(items, layers, node);
            textUtil.overlay(comp, layer, NODE_PREFIX + "." + "Text" + "." + elems[i], {"text": elems[i], "pos": textPos});
            queue.push(layer)
        }
        i += 1;
        if (js_null(elems[i])) {
            edge["pos"] = [parentPos[0]+edgeOffset, parentPos[1]+edgeOffset, parentPos[2]]
            edge["rotation"] = -rotation
            edge["layerName"] = EDGE_PREFIX + "." + "Right" + "." + elems[i]
            shareUtil.addLayer(items, layers, edge);
            node["pos"] = [parentPos[0]+horizontalDist, parentPos[1]+verticalDist, parentPos[2]]
            node["layerName"] = NODE_PREFIX + "." + "Shape" + "." + elems[i]
            layer = shareUtil.addLayer(items, layers, node);
            textUtil.overlay(comp, layer, NODE_PREFIX + "." + "Text" + "." + elems[i], {"text": elems[i], "pos": textPos});
            // count += 1;
            queue.push(layer)
        }
        i += 1;
        // $.writeln("==================================")
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