function Codes() {
}

Codes.prototype.addLine = function (line, conf, parentComp, parentObj) {
    var indent = line.shift()
    var sn = line.pop()
    var lineComp = parentObj.items.addComp("line." + sn, conf['widthLine'], conf['heightLine'], PIXEL_ASPECT, conf['duration'], FRAME_RATE);
    lineComp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])
    var pos_x = 0
    for (var i = 0; i < line.length; i++) {
        var snippet = line[i]
        snippet["Anchor Point"] = "LEFT"
        var pos_y = conf['heightLine'] / 2
        // if (snippet["fillColor"]) {
        //     pos_y -= 2
        // }
        if (snippet["text"] === ',') {
            pos_y += 7.5
        } else if (snippet["text"] === ' ') {
            pos_x += 7
        }
        snippet["Position"] = [pos_x, pos_y]
        snippet["font"] = conf["font"]
        snippet["fontSize"] = conf["fontSize"]
        var textLayer = textUtil.addOne(snippet, lineComp)
        var width = textLayer.sourceRectAtTime(0, false).width
        pos_x += width + 2
    }
    return shareUtil.addLayer(
        { "item": lineComp, "layerName": "line." + sn, "Anchor Point": "LEFT", "Position": [indent * 48, sn * conf['heightLine'] + 30]},
        parentComp
    );
}

Codes.prototype.add = function (conf, parentComp, parentObj) {
    var parentObj = parentObj.items.addFolder(conf["layerName"])
    var codesComp = parentObj.items.addComp(conf["layerName"], conf['width'], conf['height'], PIXEL_ASPECT, conf['duration'], FRAME_RATE);
    codesComp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])
    var lines = conf["lines"]
    var indent
    var sn

    var lineLayers = []
    for (var i = 0; i < lines.length; i++) {
        var line = lines[i]
        if (line.length === 0) {
            continue
        }
        line.push(i)
        indent = line[0]
        sn = i
        var layer = this.addLine(line, conf, codesComp, parentObj)
        if (i > 4) {
            lineLayers.push(layer)
        }
    }

    var currentLine = conf["currentLine"]
    var values = []
    for (var i = 0; i < currentLine['steps']; i++) {
        var sn = currentLine["keyframes"]["Transform.Position"][1][i]
        values.push(lineLayers[sn]("Transform")("Position").value)
    }
    currentLine["keyframes"]["Transform.Position"][1] = values
    currentLine["Position"] = [indent * 48, sn * conf['heightLine'] + 30]
    currentLineLayer = shapeUtil.addOne(currentLine, codesComp)
    currentLineLayer.moveToEnd()
    conf['item'] = codesComp
    var codesLayer = shareUtil.addLayer(conf, parentComp);
    codesLayer.moveToEnd()
}

var codes = new Codes();