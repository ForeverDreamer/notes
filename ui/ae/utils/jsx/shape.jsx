function ShapeUtil() {}

ShapeUtil.prototype.add = function(comp, name, props) {
    var shapeLayer = comp.layers.addShape();
    shapeLayer("Transform")("Position").setValue(props["pos"])
    shapeLayer.name = name;
    var shapeGroup = shapeLayer("Contents").addProperty("ADBE Vector Group");
    // shapeGroup.name = elem;
    pathProp = shapeGroup("Contents").addProperty("ADBE Vector Shape - Rect")
    pathProp("Size").setValue([50, 50])
    strokeProp = shapeGroup("Contents").addProperty("ADBE Vector Graphic - Stroke")
    strokeProp("Color").setValue([0, 0, 0])
    fillProp = shapeGroup("Contents").addProperty("ADBE Vector Graphic - Fill")
    fillProp("Color").setValue([1, 1, 1])
    return shapeLayer
}

ShapeUtil.prototype.remove = function(comp, conf) {
}

var shapeUtil = new ShapeUtil();