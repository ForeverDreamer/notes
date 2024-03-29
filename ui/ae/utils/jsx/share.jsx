function ShareUtil() { }

function js_bool(v) {
	if (v === 'true') {
		return true
	} else {
		return false
	}
}

ShareUtil.prototype.configShots = function (shots) {
	for (var sn in shots) {
		$.writeln('Configing s' + sn)
		var shot = shots[sn]
		for (var i = 0; i < shot.length; i++) {
			var conf = shot[i]
			var comp = shareUtil.findItemByName(conf["sourceName"], conf["parentFolderName"], conf["typeName"])
			shareUtil.configLayer(shot[i], comp.layer(conf["layerName"]))
		}
	}
}

ShareUtil.prototype.addShots = function (shots) {
	for (var sn in shots) {
		$.writeln('Creating s' + sn)
		var shot = shots[sn]
		shot['width'] = WIDTH
		shot['height'] = HEIGHT
		compUtil.addOne(shot, mainComp, project)
	}
}

ShareUtil.prototype.createSubtitles = function (subtitles) {
	// var textLayer = textUtil.add(mainComp, "视频字幕", {"text": subtitles[1][0], "Position": [960, 1025, 0], "font": 'KaiTi', "fontSize": 40, "fillColor": COLORS["subtitles"]});
	subtitlesCnLayer("Source Text").setValuesAtTimes(subtitles["cn"][0], subtitles["cn"][1])
	subtitlesEnLayer("Source Text").setValuesAtTimes(subtitles["en"][0], subtitles["en"][1])
}

ShareUtil.prototype.createAnnotations = function (parentComp, annotations) {
	for (var i = 0; i < annotations.length; i++) {
		var conf = annotations[i]
		if (!conf["fillColor"]) {
			conf["fillColor"] = COLORS["annotation"]
		}

		textUtil.add(parentComp, conf["name"], conf)
	}
}

ShareUtil.prototype.importFiles = function (files, parentObj, comp) {
	var _comp = comp ? comp : mainComp
	for (var i = 0; i < files.length; i++) {
		var conf = files[i]
		if (conf["folder"]) {
			var folder = parentObj.items.addFolder(conf["folder"])
			shareUtil.importFiles(conf["files"], folder, _comp);
			continue
		}
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
		var importedObj = project.importFile(importOptions);
		if (parentObj.typeName === "Folder") {
			importedObj.parentFolder = parentObj;
		}
		var layers = conf["layers"]
		if (layers) {
			for (var j = 0; j < layers.length; j++) {
				var parentLayer = shareUtil.addLayer(layers[j], _comp)
				children = layers[j]["children"]
				if (children) {
					for (var k = 0; k < children.length; k++) {
						children[k]['parent'] = parentLayer
						shareUtil.addLayer(children[k], _comp)
					}
				}
			}
		}
	}
}

ShareUtil.prototype.configLayer = function (conf, layer) {
	if (conf['layerName']) {
		layer.name = conf['layerName'];
	}
	if (conf["Audio Levels"]) {
		layer("Audio")("Audio Levels").setValue(conf["Audio Levels"]);
	}
	this.setAnchorPoint(layer, conf["Anchor Point"]);
	if (conf['Position']) {
		layer("Position").setValue(conf["Position"]);
	}
	if (conf['Scale']) {
		layer("Scale").setValue(conf["Scale"]);
	}
	if (conf['Rotation']) {
		layer("Rotation").setValue(conf["Rotation"]);
	}
	if (typeof conf["Opacity"] !== "undefined") {
		layer("Opacity").setValue(conf["Opacity"]);
	}
	if (conf['startTime']) {
		layer.startTime = conf['startTime'];
	}
	if (conf["inPoint"]) {
		layer.inPoint = conf['inPoint'];
	}
	if (conf["outPoint"]) {
		layer.outPoint = conf['outPoint'];
	}
	if (conf['3D']) {
		layer.threeDLayer = true;
	}
	if (conf["parent"]) {
		layer.setParentWithJump(conf["parent"])
	}
	this.configMasks(layer, conf["Masks"])
	this.configKeyframes(layer, conf["keyframes"])
	presetsUtil.add(layer, conf["presets"])
	effectsUtil.add(layer, (conf["effects"]))
	return layer;
}

ShareUtil.prototype.addLayer = function (conf, comp) {
	var layer;

	if (conf["item"]) {
		layer = comp.layers.add(conf["item"]);
	} else if (conf["sourceName"]) {
		layer = comp.layers.add(this.findItemByName(conf["sourceName"], conf["parentFolderName"], conf["typeName"]));
	} else if (conf["solid"]) {
		layer = comp.layers.addSolid(conf["color"], conf["name"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"]);
		if (conf["adjustmentLayer"]) {
			layer.adjustmentLayer = true;
		}
	}

	if (conf['layerName']) {
		layer.name = conf['layerName'];
	}
	if (conf["Audio Levels"]) {
		layer("Audio")("Audio Levels").setValue(conf["Audio Levels"]);
	}
	this.setAnchorPoint(layer, conf["Anchor Point"]);
	if (conf['Position']) {
		layer("Transform")("Position").setValue(conf["Position"]);
	}
	if (conf['Scale']) {
		layer("Transform")("Scale").setValue(conf["Scale"]);
	}
	if (conf['Rotation']) {
		layer("Transform")("Rotation").setValue(conf["Rotation"]);
	}
	if (typeof conf["Opacity"] !== "undefined") {
		layer("Transform")("Opacity").setValue(conf["Opacity"]);
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
	if (conf["parent"]) {
		layer.setParentWithJump(conf["parent"])
	}
	this.configMasks(layer, conf["Masks"])
	this.configKeyframes(layer, conf["keyframes"])
	presetsUtil.add(layer, conf["presets"])
	effectsUtil.add(layer, (conf["effects"]))
	return layer;
}

ShareUtil.prototype.addLayers = function (layers, comp) {
	for (var i = 0; i < layers.length; i++) {
		this.addLayer(layers[i], comp)
	}
}

ShareUtil.prototype.delItems = function () {
	var numItems = project.items.length;
	for (var i = numItems; i >= 1; i--) {
		var item = items[i];
		item.remove();
	}
}

ShareUtil.prototype.findItemByName = function (sourceName, parentFolderName, typeName) {
	for (var i = 1; i <= project.items.length; i++) {
		var item = project.items[i];
		if (
			(item.name !== sourceName) ||
			(parentFolderName && item.parentFolder.name !== parentFolderName) ||
			(typeName && item.typeName !== typeName)
		) {
			continue
		}
		return item
	}
}

ShareUtil.prototype.configMasks = function (layer, masks) {
	if (!masks) {
		return
	}
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
		if (conf_mask["inverted"]) {
			mask.inverted = conf_mask["inverted"];
		}
		// var closed = js_bool(conf_mask["closed"]);
		shape.closed =  conf_mask["closed"] ? conf_mask["closed"] : true;
		maskShape.setValue(shape);
		if (conf_mask["Mask Feather"]) {
			layer.Masks("Mask 1")("Mask Feather").setValue(conf_mask["Mask Feather"])
		}
	}
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

// ShareUtil.prototype.setKeyframeInterpolationType = function (props, inType, outType) {
// 	for (var i = 0; i < props.length; i++) {
// 		var prop = props[i]
// 		for (var j = 1; j <= prop.numKeys; j++) {
// 			prop.setInterpolationTypeAtKey(j, inType, outType ? outType : inType)
// 		}
// 	}
// }

ShareUtil.prototype.configKeyframes = function (propGroup, keyframes) {
	if (!keyframes) {
		return
	}
	var props = []
	for (var k in keyframes) {
		var propChain = k.split(".")
		var prop = propGroup(propChain[0]);
		for (var i = 1; i < propChain.length; i++) {
			prop = prop(propChain[i])
		}

		var clear = keyframes[k][3]
		if (clear) {
			var numKeys = prop.numKeys
			for (var i = numKeys; i >= 1; i--) {
				prop.removeKey(i)
			}
		}

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
					if (prop.propertyValueType === PropertyValueType.ThreeD) {
						prop.setTemporalEaseAtKey(i+1, [easeIn, easeIn, easeIn], [easeOut, easeOut, easeOut])
			
					} else if (prop.propertyValueType === PropertyValueType.TwoD) {
						prop.setTemporalEaseAtKey(i+1, [easeIn, easeIn], [easeOut, easeOut])
					} else {
						prop.setTemporalEaseAtKey(i+1, [easeIn], [easeOut])
					}
					
				}
			}
			if (confExtra["spatial"]) {
				var confSpatial = confExtra["spatial"]
				for (var i = 0; i < confSpatial.length; i++) {
					prop.setInterpolationTypeAtKey(i+1, TYPE_DIC[confSpatial[i]["type"]])
					var inTangents = confSpatial[i]["inTangents"]
					if (!inTangents) {
						continue
					}
					var outTangents = confSpatial[i]["outTangents"]
					if (outTangents) {
						prop.setSpatialTangentsAtKey(i+1, inTangents.concat([0]), outTangents.concat([0]))
					} else {
						prop.setSpatialTangentsAtKey(i+1, inTangents.concat([0]))
					}
				}
			}
		}
		
		props.push(prop)
	}
	return props
}

ShareUtil.prototype.setAnchorPoint = function (layer, direction) {
	if (direction === null) {
		return
	}
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

// s11_s11.队列.前序_数据_Shape.3
ShareUtil.prototype.getPosition = function (params) {
	var layerName = params["layerName"]
	var itemName = params["itemName"]
	var parentFolderName = params["parentFolderName"]
	var typeName = params["typeName"]
	var item = this.findItemByName(itemName, parentFolderName, typeName)
	return item.layer(layerName)("Transform")("Position").value
}

var shareUtil = new ShareUtil();
// if (typeof shareUtil === "undefined") {
//     var shareUtil = new ShareUtil();
// }
