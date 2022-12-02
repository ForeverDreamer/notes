#include "precomp.jsx"

function AnimationUtil() {}

AnimationUtil.prototype.traverseBinaryTree = function(nodeLayer, edgeLayer, elems, order) {
	switch (order) {
		case 'PRE':
			importOptions.importAs = ImportAsType.COMP_CROPPED_LAYERS;
			break;
		case 'IN':
			importOptions.importAs = ImportAsType.PROJECT;
			break;
		case 'POST':
			importOptions.importAs = ImportAsType.COMP;
			break;
		default:
            // LEVEL
			importOptions.importAs = ImportAsType.FOOTAGE;
	}
	return project.importFile(importOptions);
}

AnimationUtil.prototype.buildBinaryTree = function(items, parentComp, conf) {
	res = precompUtil.binaryTree(items, parentComp, conf);
	var comp = res['comp'];
	var compLayer = res['compLayer'];
	var node = conf["node"];
    var edge = conf["edge"];
	
	function removeNull(elem) {
		return elem !== null;
	}
	var elems = conf["elems"].filter(removeNull)
	var numLayers = comp.numLayers
	// var startTime = conf["startTime"];
	var interval = 3/(elems.length*2-1);
	var layers = []
	for (var i = numLayers; i >= 1; i--) {
		// $.writeln(comp.layers[i].name)
		layers.push(comp.layers[i])
	}
	for (var i = 0; i < numLayers; i++) {
		$.writeln(layers[i].name)
	}
	var rootShapeLayer = layers[0];
	var start = 0;
	var end = interval;
	rootShapeLayer("Transform")("Scale").setValuesAtTimes([start, end], [[0, 0, 0], node["scale"]])
	var i = 2;
	var shapeLayer;
	while (i < numLayers) {
		edgeLayer = layers[i];
		shapeLayer = layers[i+1];
		start += interval;
		end += interval;
		edgeLayer("Transform")("Scale").setValuesAtTimes([start, end], [[0, 0, 0], edge["scale"]])
		start += interval;
		end += interval;
		shapeLayer("Transform")("Scale").setValuesAtTimes([start, end], [[0, 0, 0], node["scale"]])
		i += 3;
	}
	return compLayer;
}

var animationUtil = new AnimationUtil();