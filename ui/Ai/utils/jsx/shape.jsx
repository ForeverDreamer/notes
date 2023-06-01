function ShapeUtil() {
}

ShapeUtil.prototype.add = function (doc, conf) {
    var shape
    switch (conf['type']) {
        case SHAPE_TYPES[0]:
            shape = doc.pathItems.ellipse(conf['top'], conf['left'], conf['width'], conf['height'], conf['reversed']);
            break;
        case SHAPE_TYPES[1]:
            shape = doc.pathItems.polygon(conf['centerX'], conf['centerY'], conf['radius'], conf['sides'], conf['reversed']);
            break;
        case SHAPE_TYPES[2]:
            shape = doc.pathItems.rectangle(conf['top'], conf['left'], conf['width'], conf['height'], conf['reversed']);
            break;
        case SHAPE_TYPES[3]:
            shape = doc.pathItems.roundedRectangle(conf['top'], conf['left'], conf['width'], conf['height'], conf['horizontalRadius'], conf['verticalRadius'], conf['reversed']);
            break;
        case SHAPE_TYPES[4]:
            shape = doc.pathItems.star(conf['centerX'], conf['centerY'], conf['radius'], conf['innerRadius'], conf['points'], conf['reversed']);
            break;
        default:
            throw new Error('未知SHAPE类型')
    }
    miscUtil.setColor(shape, 'fillColor', '#FFFF00')
    shape.opacity = Math.random() * 100;
    return shape
}


var shapeUtil = new ShapeUtil();