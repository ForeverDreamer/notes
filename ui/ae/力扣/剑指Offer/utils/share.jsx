function ShareUtil() { }

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
	return project.importFile(importOptions);
}

ShareUtil.prototype.addLayer = function (items, layers, conf, item) {
	var layer;
	if (item) {
		layer = layers.add(item);
	} else {
		layer = layers.add(this.findItemByName(items, conf["name"]));
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

ShareUtil.prototype.findItemByName = function (items, name) {
	for (var i = 1; i <= items.length; i++) {
		var item = items[i];
		if (item.name == name) {
			return item;
		}
	}
	return null;
}

ShareUtil.prototype.configProps = function (props) {
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

ShareUtil.prototype.configKeyframes = function (keyframes) {
	if (!keyframes) {
		return
	}
	for (var k in keyframes) {
		var propChain = k.split(".")
		var prop = layer(propChain[0]);
		for (var i = 1; i < propChain.length; i++) {
			prop = prop(propChain[i])
		}
		var numKeys = prop.numKeys
		for (var i = numKeys; i >= 1; i--) {
			prop.removeKey(i)
		}
		prop.setValuesAtTimes(keyframes[k]["times"], keyframes[k]["values"]);
	}
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
