function Queue() {
    this.queueLayers = {}
}

Queue.prototype.add = function (items, parentComp, conf) {
    var traverse = conf["traverse"]
    this.queueLayers[traverse] = {}
    var elems = conf['elems']
    var unit = conf["unit"];

    var queueComp = items.addComp(conf["layerName"], conf['width'], conf['height'], PIXEL_ASPECT, conf['duration'], FRAME_RATE);
    queueComp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])

    var elemWidth = unit["pathGroup"]["Size"][0]
    var elemHeight = unit["pathGroup"]["Size"][1]
    // var height = layer.sourceRectAtTime(startTime, false).height
    var stroke_add = unit['Stroke']['Stroke Width'] * 2
    var pos_x = elemWidth / 2 + stroke_add
    for (var i = 0; i < elems.length; i++) {
        var key = elems[i]["key"]
        unit["layerName"] = "Shape" + "." + key
        if (i > 0) {
            pos_x += elemWidth
            pos_x -= 1
        }
        unit["Position"] = [pos_x, elemHeight / 2 + stroke_add]
        if (elems[i]["Color"]) {
            unit["Fill"]["Color"] = colorUtil.hexToRgb1(elems[i]["Color"])
        }
        // var shapeLayer = shareUtil.addLayer(queueComp, unit);
        var shapeLayer = shapeUtil.addOne(queueComp, unit)
        if (elems[i]["keyframes"]) {
            shareUtil.configKeyframes(shapeLayer, elems[i]["keyframes"])
        }
        var textLayer = textUtil.overlay(
            queueComp, shapeLayer, "Text" + "." + key,
            { "text": key, "font": "Arial-BoldItalicMT", "fontSize": unit["fontSize"], "Position": [elemWidth / 2, elemHeight / 2] }
        );
        this.queueLayers[traverse][key] = { 'shapeLayer': shapeLayer, "textLayer": textLayer }
    }
    shareUtil.addLayer(parentComp, conf, queueComp);
    // effectsUtil.add(queueLayer, "ADBE Drop Shadow", {"Distance": 10, "Softness": 30, "Opacity": 255});
    return queueComp
}

var queue = new Queue();