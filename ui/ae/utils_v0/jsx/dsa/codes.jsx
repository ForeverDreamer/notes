function Codes() {
}

Codes.prototype.addLine = function (items, parentComp, line, conf) {
    var indent = line.shift()
    var sn = line.pop()
    var lineComp = items.addComp("line." + sn, conf['widthLine'], conf['heightLine'], PIXEL_ASPECT, conf['duration'], FRAME_RATE);
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
        var textLayer = textUtil.addOne(lineComp, snippet["text"], snippet)
        var width = textLayer.sourceRectAtTime(0, false).width
        pos_x += width + 2
    }
    return shareUtil.addLayer(
        parentComp,
        { "layerName": "line." + sn, "Anchor Point": "LEFT", "Position": [indent * 48, sn * conf['heightLine'] + 30] },
        lineComp
    );
}

Codes.prototype.add = function (items, parentComp, conf) {
    var codesFolder = items.addFolder("Codes")
    var codesComp = codesFolder.items.addComp(conf["layerName"], conf['width'], conf['height'], PIXEL_ASPECT, conf['duration'], FRAME_RATE);
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
        var layer = this.addLine(codesFolder.items, codesComp, line, conf)
        if (i > 4) {
            lineLayers.push(layer)
        }
    }

    var currentLine = conf["currentLine"]
    var times = []
    var values = []
    var extra = currentLine["keyframes"]["Transform.Position"][2]
    for (var i = 0; i < currentLine['steps']; i++) {
        // times.push(conf["startTime"] + 1 + i * 1)
        var sn = currentLine["keyframes"]["Transform.Position"][1][i]
        values.push(lineLayers[sn]("Transform")("Position").value)
    }
    currentLine["keyframes"]["Transform.Position"][1] = values
    currentLine["Position"] = [indent * 48, sn * conf['heightLine'] + 30]
    currentLineLayer = shapeUtil.addOne(codesComp, currentLine)
    currentLineLayer.moveToEnd()
    shareUtil.addLayer(parentComp, conf, codesComp);
}

var codes = new Codes();