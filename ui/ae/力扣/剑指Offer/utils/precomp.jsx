#include "constants.jsx"
#include "share.jsx"
#include "text.jsx"

function PrecompUtil() { }

PrecompUtil.prototype.stack = function (nodeLayer, edgeLayer, elems) {

}

PrecompUtil.prototype.queue = function (nodeLayer, edgeLayer, elems) {

}

PrecompUtil.prototype.binaryTree = function (items, conf) {
    var comp = items.addComp("二叉树" + conf['name'], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE);
    var layers = comp.layers;
    var node = conf["node"];
    var edge = conf["edge"];
    var elems = conf["elems"];
    var root_node_pos = [conf["width"]/2, 50, 0];
    var horizontalDist = 50;
    var verticalDist = 80;


    node["pos"] = root_node_pos;
    var nodeLayer = shareUtil.addLayer(items, layers, node);
    textUtil.overlay(comp, nodeLayer, "Shape" + elems[0], {"text": elems[0]});
    var node_top = nodeLayer.sourceRectAtTime(0, true).top;
    var node_left = nodeLayer.sourceRectAtTime(0, true).left;
    var node_width = nodeLayer.sourceRectAtTime(0, true).width;
	var node_height = nodeLayer.sourceRectAtTime(0, true).height;
    var rootLeftEdgePos = [node_left + node_width/4, node_top + node_height, 0];
    var rootRightEdgePos =  [node_left + node_width/4*3, node_top + node_height, 0];
    // var edgeLayer = shareUtil.addLayer(items, layers, edge);
    // edgeLayer("Transform")("Rotation").setValue(edge["rotation"]);
    // var edge_top = edgeLayer.sourceRectAtTime(0, true).top;
    // var edge_left = edgeLayer.sourceRectAtTime(0, true).left;
    // var edge_width = edgeLayer.sourceRectAtTime(0, true).width;
	// var edge_height = edgeLayer.sourceRectAtTime(0, true).height;

    var level = 0;
    var i = 1;
    var count = 1;
    while (count > 0) {
        count -= 1;
        edge["pos"] = [rootLeftEdgePos[0]-horizontalDist*level, rootLeftEdgePos[1]+verticalDist*level, rootLeftEdgePos[2]];
        node["pos"] = [root_node_pos[0]-horizontalDist*(level+1), root_node_pos[1]+verticalDist*(level+1), root_node_pos[2]];
        if (elems[i]) {
            // edge["pos"] = [rootLeftEdgePos[0]-horizontalDist*level, rootLeftEdgePos[1]+verticalDist*level, rootLeftEdgePos[2]];
            shareUtil.addLayer(items, layers, edge);
            // node["pos"] = [root_node_pos[0]-horizontalDist*(level+1), root_node_pos[1]+verticalDist*(level+1), root_node_pos[2]];
            textUtil.overlay(comp, shareUtil.addLayer(items, layers, node), "Node" + elems[i], {"text": elems[i]});
            count += 1;
        }
        i += 1;
        edge["pos"] = [rootRightEdgePos[0]+horizontalDist*level, rootRightEdgePos[1]+verticalDist*level, rootRightEdgePos[2]];
        node["pos"] = [root_node_pos[0]+horizontalDist*(level+1), root_node_pos[1]+verticalDist*(level+1), root_node_pos[2]];
        if (elems[i]) {
            // edge["pos"] = [rootRightEdgePos[0]+horizontalDist*level, rootRightEdgePos[1]+verticalDist*level, rootRightEdgePos[2]];
            edge["rotation"] = -edge["rotation"]
            shareUtil.addLayer(items, layers, edge);
            // node["pos"] = [root_node_pos[0]+horizontalDist*(level+1), root_node_pos[1]+verticalDist*(level+1), root_node_pos[2]];
            textUtil.overlay(comp, shareUtil.addLayer(items, layers, node), "Node" + elems[i], {"text": elems[i]});
            count += 1;
        }
        i += 1;
        level += 1;
    }

    return comp;
}

PrecompUtil.prototype.graph = function (nodeLayer, edgeLayer, elems) {

}

var precompUtil = new PrecompUtil();