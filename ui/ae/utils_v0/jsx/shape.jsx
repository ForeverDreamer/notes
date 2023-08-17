function ShapeUtil() {}

ShapeUtil.prototype.addOne = function(parentComp, conf) {
    var shapeLayer = parentComp.layers.addShape();
    shapeLayer.name = conf["layerName"];
    conf_pg = conf["pathGroup"]
    var shapeGroup = shapeLayer("Contents").addProperty("ADBE Vector Group");
    var pathGroup = shapeGroup("Contents").addProperty("ADBE Vector Shape - " + conf_pg["type"]);

    if (conf_pg["type"] === "Group") {
        var shape = new Shape();
        shape.vertices = conf_pg["vertices"];
        if (conf_pg["inTangents"]) {
            shape.inTangents = conf_pg["inTangents"]
        }
        if (conf_pg["outTangents"]) {
            shape.outTangents = conf_pg["outTangents"]
        }
        shape.closed = js_bool(conf_pg["closed"]);
        pathGroup("Path").setValue(shape);
    } else {
        if (conf_pg["Size"]) {
            pathGroup("Size").setValue(conf_pg["Size"])
        }
        // pathGroup("Position").setValue(conf["Position"] ? conf["Position"] : [0, 0])
        pathGroup("Position").setValue([0, 0])
    }

    if (conf["Stroke"]) {
        var strokeGroup = shapeGroup("Contents").addProperty("ADBE Vector Graphic - Stroke")
        for (var k in conf["Stroke"]) {
            strokeGroup(k).setValue(conf["Stroke"][k])
        }
    }
    if (conf["Fill"]) {
        var fillGroup = shapeGroup("Contents").addProperty("ADBE Vector Graphic - Fill")
        for (var k in conf["Fill"]) {
            fillGroup(k).setValue(conf["Fill"][k])
        }
    }
    // if (conf["Gradient Fill"]) {
    //     var gFillGroup = shapeGroup("Contents").addProperty("ADBE Vector Graphic - G-Fill")
    //     for (var k in conf["Gradient Fill"]) {
    //         gFillGroup(k).setValue(conf["Gradient Fill"][k])
    //     }
    // }
    if (conf["Trim Paths"]) {
        var trimGroup = shapeGroup("Contents").addProperty("ADBE Vector Filter - Trim")
        for (var k in conf["Trim Paths"]) {
            trimGroup(k).setValue(conf["Trim Paths"][k])
        }
    }

    if (conf["Rotation"]) {
        shapeLayer("Transform")("Rotation").setValue(conf["Rotation"])
    }
    shareUtil.setAnchorPoint(shapeLayer, conf["Anchor Point"])
    shapeLayer("Transform")("Position").setValue(conf["Position"])
    shapeGroup("Transform")("Anchor Point").setValue([0, 0]);
    shapeGroup("Transform")("Position").setValue([0, 0]);

    if (conf['startTime']) {
		shapeLayer.startTime = conf['startTime'];
	}
	if (conf["span"]) {
		shapeLayer.inPoint = conf["span"]['inPoint'];
		shapeLayer.outPoint = conf["span"]['outPoint'];
	}

    if (conf["effects"]) {
        effectsUtil.add(shapeLayer, conf["effects"])
    }

    if (conf["keyframes"]) {
        shareUtil.configKeyframes(shapeLayer, conf["keyframes"])
    }

    return shapeLayer
}

ShapeUtil.prototype.addMany = function(parentComp, shapes) {
    for (var i = 0; i < shapes.length; i++) {
        this.addOne(parentComp, shapes[i])
    }
}

var shapeUtil = new ShapeUtil();