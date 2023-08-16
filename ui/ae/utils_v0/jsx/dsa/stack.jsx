function Stack() {
}

Stack.prototype.add = function (parentComp, conf) {
    var elems = conf['elems']
    var unit = conf["unit"];

    var stackComp = project.items.addComp(conf["layerName"], conf['width'], conf['height'], PIXEL_ASPECT, conf['duration'], FRAME_RATE);
    stackComp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])

    var elemWidth = unit["pathGroup"]["Size"][0]
    var elemHeight = unit["pathGroup"]["Size"][1]
    // var height = layer.sourceRectAtTime(startTime, false).height
    var stroke_add = unit['Stroke']['Stroke Width'] * 2
    var pos_y = elemHeight * elems.length - elemHeight / 2
    for (var i = 0; i < elems.length; i++) {
        var key = elems[i]["key"]
        unit["layerName"] = "Shape" + "." + key
        if (i > 0) {
            pos_y -= elemHeight
            pos_y += 1
        }
        unit["Position"] = [elemWidth / 2 + stroke_add, pos_y]
        if (elems[i]["Color"]) {
            unit["Fill"]["Color"] = colorUtil.hexToRgb1(elems[i]["Color"])
        }
        // var shapeLayer = shareUtil.addLayer(queueComp, unit);
        var shapeLayer = shapeUtil.addOne(stackComp, unit)
        var textProps = { "text": key, "font": "Arial-BoldItalicMT", "fontSize": unit["fontSize"], "Position": [elemWidth / 2, elemHeight / 2] }
        if (elems[i]["keyframes"]) {
            shareUtil.configKeyframes(shapeLayer, elems[i]["keyframes"])
            textProps["keyframes"] = elems[i]["keyframes"]
        }
        textUtil.overlay(
            stackComp, shapeLayer, "Text" + "." + key, textProps
        );
    }
    shareUtil.addLayer(parentComp, conf, stackComp);
    // effectsUtil.add(queueLayer, "ADBE Drop Shadow", {"Distance": 10, "Softness": 30, "Opacity": 255});
    return stackComp
}

var stack = new Stack();