function ShareUtil() { }

function js_bool(v) {
	if (v === 'true') {
		return true
	} else {
		return false
	}
}

function js_null(v) {
	if (v === 'null') {
		return null
	} else {
		return v
	}
}

ShareUtil.prototype.importFile = function (project, conf) {
	var importOptions = new ImportOptions();
	importOptions.file = new File(conf["path"]);
	switch (conf["import_as_type"]) {
		case 'COMP_CROPPED_LAYERS':
			importOptions.importAs = ImportAsType.COMP_CROPPED_LAYERS;
			break;
		case 'PROJECT':
			importOptions.importAs = ImportAsType.PROJECT;
			break;
		case 'COMP':
			importOptions.importAs = ImportAsType.COMP;
			break;
		default:
			importOptions.importAs = ImportAsType.FOOTAGE;
	}
	var item = project.importFile(importOptions);
	var confLayers = conf["layers"]
	if (confLayers) {
		for (var i = 0; i < confLayers.length; i++) {
			var parent = shareUtil.addLayer(mainComp, confLayers[i])
			children = confLayers[i]["children"]
			if (children) {
				for (var j = 0; j < children.length; j++) {
					shareUtil.addLayer(mainComp, children[j], null, parent)
				}
			}
		}
	}
}

ShareUtil.prototype.addLayer = function (comp, conf, item, parent) {
	var layer;
	if (item) {
		layer = comp.layers.add(item);
	} else {
		layer = comp.layers.add(this.findItemByName(conf["name"]));
	}
	if (conf['layerName']) {
		layer.name = conf['layerName'];
	}
	if (conf['anchor']) {
		this.setAnchorPoint(layer, conf["anchor"]);
	}
	if (conf['pos']) {
		layer("Transform")("Position").setValue(conf["pos"]);
	}
	if (conf['scale']) {
		layer("Transform")("Scale").setValue(conf["scale"]);
	}
	if (conf['rotation']) {
		layer("Transform")("Rotation").setValue(conf["rotation"]);
	}
	if (typeof conf["Opacity"] !== "undefined") {
		layer("Transform")("Opacity").setValue(conf["Opacity"]);
	}
	var masks = conf['Masks']
	if (masks) {
		for (var i = 0; i < masks.length; i++) {
			var conf_mask = masks[i]
			var mask = layer.Masks.addProperty("Mask");
			maskShape = mask("maskShape");
			var shape = maskShape.value;
			if (conf_mask["vertices"]) {
				shape.vertices = conf_mask["vertices"];
			}
			if (conf_mask["inTangents"]) {
				shape.inTangents = conf_mask["inTangents"];
			}
			if (conf_mask["outTangents"]) {
				shape.outTangents = conf_mask["outTangents"];
			}
			var closed = js_bool(conf_mask["closed"]);
			shape.closed =  closed ? closed : true;
			maskShape.setValue(shape);
			if (conf_mask["Mask Feather"]) {
				layer.Masks("Mask 1")("Mask Feather").setValue(conf_mask["Mask Feather"])
			}
		}
	}
	if (conf['startTime']) {
		layer.startTime = conf['startTime'];
	}
	if (conf["span"]) {
		layer.inPoint = conf["span"]['inPoint'];
		layer.outPoint = conf["span"]['outPoint'];
	}
	if (conf['3D']) {
		layer.threeDLayer = true;
	}
	if (parent) {
		layer.setParentWithJump(parent)
	}
	return layer;
}

ShareUtil.prototype.delItems = function (items) {
	var numItems = items.length;
	for (var i = numItems; i >= 1; i--) {
		var item = items[i];
		// if (item instanceof FolderItem) {
		//     delItems(item.items);
		// } else {
		//     item.remove()
		// }
		item.remove();
	}
}

ShareUtil.prototype.findItemByName = function (name) {
	for (var i = 1; i <= project.items.length; i++) {
		var item = project.items[i];
		if (item.name == name) {
			return item;
		}
	}
	return null;
}

ShareUtil.prototype.configProps = function (layer, props) {
	if (!props) {
		return
	}
	for (var k in props) {
		var propChain = k.split(".")
		var prop = layer(propChain[0]);
		for (var i = 1; i < propChain.length; i++) {
			prop = prop(propChain[i])
		}
		prop.setValue(props[k]);
	}
}

ShareUtil.prototype.setKeyframeInterpolationType = function (props, inType, outType) {
	for (var i = 0; i < props.length; i++) {
		var prop = props[i]
		for (var j = 1; j <= prop.numKeys; j++) {
			prop.setInterpolationTypeAtKey(j, inType, outType ? outType : inType)
		}
	}
}

ShareUtil.prototype.configKeyframes = function (layer, keyframes) {
	if (!keyframes) {
		return
	}
	var props = []
	for (var k in keyframes) {
		var propChain = k.split(".")
		var prop = layer(propChain[0]);
		for (var i = 1; i < propChain.length; i++) {
			prop = prop(propChain[i])
		}
		// var numKeys = prop.numKeys
		// for (var i = numKeys; i >= 1; i--) {
		// 	prop.removeKey(i)
		// }
		var values
		if (propChain[propChain.length-1] === "Path") {
			values = []
			for (var i = 0; i < keyframes[k][1].length; i++) {
				var confPath = keyframes[k][1][i]
				var shape = new Shape();
				shape.vertices = confPath["vertices"];
				if (confPath["inTangents"]) {
					shape.inTangents = confPath["inTangents"]
				}
				if (confPath["outTangents"]) {
					shape.outTangents = confPath["outTangents"]
				}
				shape.closed = confPath["closed"];
				values.push(shape)
			}
		} else {
			values = keyframes[k][1]
		}
		prop.setValuesAtTimes(keyframes[k][0], values)
		var confExtra = keyframes[k][2]
		if (confExtra) {
			if (confExtra["temporal"]) {
				var confTemporal = confExtra["temporal"]
				for (var i = 0; i < confTemporal.length; i++) {
					var easeIn = new KeyframeEase(confTemporal[i][0][0], confTemporal[i][0][1]);
					var easeOut = new KeyframeEase(confTemporal[i][1][0], confTemporal[i][1][1]);
					prop.setTemporalEaseAtKey(i+1, [easeIn], [easeOut])
				}
			}
			if (confExtra["spatial"]) {
				var confSpatial = confExtra["spatial"]
				for (var i = 0; i < confSpatial.length; i++) {
					prop.setInterpolationTypeAtKey(i+1, TYPE_DIC[confSpatial[i]["type"]])
					prop.setSpatialTangentsAtKey(i+1, confSpatial[i]["inTangents"].concat([0]), confSpatial[i]["outTangents"].concat([0]))
				}
			}
		}
		
		props.push(prop)
	}
	return props
}

ShareUtil.prototype.setAnchorPoint = function (layer, direction) {
	var top = layer.sourceRectAtTime(0, false).top
    var left = layer.sourceRectAtTime(0, false).left
    var width = layer.sourceRectAtTime(0, false).width
	var height = layer.sourceRectAtTime(0, false).height
    var prop = layer("Transform")("Anchor Point")
    var value = prop.value

	switch (direction) {
		case 'LEFT':
			value[0] = left;
			value[1] = top + height/2;
			break;
		case 'LEFT_TOP':
			value[0] = left;
			value[1] = top;
			break;
		case 'LEFT_DOWN':
			value[0] = left;
			value[1] = top + height;
			break;
		case 'RIGHT':
			value[0] = left + width;
			value[1] = top + height/2;
			break;
		case 'RIGHT_TOP':
			value[0] = left + width;
			value[1] = top;
			break;
		case 'RIGHT_DOWN':
			value[0] = left + width;
			value[1] = top + height;
			break;
		case 'TOP':
			value[0] = left + width/2;
			value[1] = top;
			break;
		case 'TOP_LEFT':
			value[0] = left;
			value[1] = top;
			break;
		case 'TOP_RIGHT':
			value[0] = left + width;
			value[1] = top;
			break;
		case 'DOWN':
			value[0] = left + width/2;
			value[1] = top + height;
			break;
		case 'DOWN_LEFT':
			value[0] = left;
			value[1] = top + height;
			break;
		case 'DOWN_RIGHT':
			value[0] = left + width;
			value[1] = top + height;
			break;
		default:
			// MIDDLE
			value[0] = left + width/2;
			value[1] = top + height/2;
	}

	prop.setValue(value);
	return value
}

var shareUtil = new ShareUtil();
// if (typeof shareUtil === "undefined") {
//     var shareUtil = new ShareUtil();
// }
