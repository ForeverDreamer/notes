function ShapeUtil() {}

ShapeUtil.prototype.add = function(comp, name, conf) {
    var shapeLayer = comp.layers.addShape();
    shapeLayer.name = name;
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
        shape.closed = conf_pg["closed"];
        pathGroup("Path").setValue(shape);
    } else {
        if (conf_pg["Size"]) {
            pathGroup("Size").setValue(conf_pg["Size"])
        }
        pathGroup("Position").setValue(conf_pg["Position"] ? conf_pg["Position"] : [0, 0])
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

    shareUtil.setAnchorPoint(shapeLayer, conf["Anchor Point"])
    shapeLayer("Transform")("Position").setValue(conf["Position"])
    shapeGroup("Transform")("Anchor Point").setValue(conf["Position"]);
    shapeGroup("Transform")("Position").setValue(conf["Position"]);

    if (conf["effects"]) {
        for (var i = 0; i < conf["effects"].length; i++) {
            effectsUtil.add(shapeLayer, conf["effects"][i])
        }
    }

    if (conf["keyframes"]) {
        shareUtil.configKeyframes(shapeLayer, conf["keyframes"])
    }

    return shapeLayer
}

ShapeUtil.prototype.remove = function(comp, conf) {
}

var shapeUtil = new ShapeUtil();