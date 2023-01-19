function PrecompUtil() {
    this.queueLayers = {}
}

PrecompUtil.prototype.line = function (items, parentComp, line, conf) {
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
        var textLayer = textUtil.add(lineComp, snippet["text"], snippet)
        var width = textLayer.sourceRectAtTime(0, false).width
        pos_x += width + 2
    }
    var conf = { "layerName": "line." + sn, "Anchor Point": "LEFT", "Position": [indent * 48, sn * conf['heightLine'] + 30] }
    return shareUtil.addLayer(parentComp, conf, lineComp);
}

PrecompUtil.prototype.codes = function (items, parentComp, conf) {
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
        var layer = this.line(codesFolder.items, codesComp, line, conf)
        if (i > 4) {
            lineLayers.push(layer)
        }
    }

    var currentLine = conf["currentLine"]
    var times = []
    var values = []
    var extra = currentLine["keyframes"]["Transform.Position"][2]
    for (var i = 0; i < 72; i++) {
        times.push(conf["startTime"] + 1 + i * 1)
        var sn = currentLine["keyframes"]["Transform.Position"][1][i]
        values.push(lineLayers[sn]("Transform")("Position").value)
    }
    currentLine["keyframes"]["Transform.Position"] = [times, values, extra]
    currentLine["Position"] = [indent * 48, sn * conf['heightLine'] + 30]
    currentLineLayer = shapeUtil.addOne(codesComp, currentLine)
    currentLineLayer.moveToEnd()
    shareUtil.addLayer(parentComp, conf, codesComp);
}

PrecompUtil.prototype.misc = function (items, parentComp, conf) {
    var miscFolder = items.addFolder(conf["layerName"])
    var miscComp = miscFolder.items.addComp(conf["layerName"], conf['width'], conf['height'], PIXEL_ASPECT, conf['duration'], FRAME_RATE);
    miscComp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])
    if (conf['audios']) {

    }
    if (conf['images']) {
        shareUtil.addLayers(miscComp, conf['images'])
    }
    if (conf['videos']) {

    }
    if (conf["texts"]) {
        textUtil.addMany(miscComp, conf["texts"])
    }
    if (conf["vectors"]) {
        shapeUtil.addVectors(miscComp, conf['vectors'])
    }
    if (conf["shapes"]) {
        shapeUtil.addMany(miscComp, conf["shapes"])
    }
    if (conf["precomps"]) {
        this.addMany(miscFolder.items, miscComp, conf['precomps'])
    }
    if (conf['codes']) {
        this.codes(miscFolder.items, miscComp, conf['codes'])
    }
    if (conf["miscs"]) {
        this.miscs(miscFolder.items, miscComp, conf['miscs'])
    }
    if (conf['subtitles']) {
        shareUtil.addSubtitles(conf['subtitles'])
    }
    if (conf['camera']) {
        shareUtil.configKeyframes(cameraLayer, conf['camera'])
    }
    shareUtil.addLayer(parentComp, conf, miscComp);
}

PrecompUtil.prototype.miscs = function (items, parentComp, miscs) {
    for (var i = 0; i < miscs.length; i++) {
        this.misc(items, parentComp, miscs[i])
    }
}

PrecompUtil.prototype.linkedList = function (items, parentComp, conf) {

}

PrecompUtil.prototype.stack = function (parentComp, conf) {
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
        var shapeLayer = shapeUtil.create_one(stackComp, unit)
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
}

PrecompUtil.prototype.queue = function (items, parentComp, conf) {
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
}

PrecompUtil.prototype._btTraverseSelectedDropQueue = function (key, traverse) {
    var times = this.times

    var selectedKeyframes = {
        "Transform.Opacity": [null, [0, 100], { "spatial": [{ "type": 'HOLD' }] }]
    }

    var dropTmp = precompUtil.dropTmp;
    var dropKeyframes = {
        "Transform.Opacity": [null, [0, 100, 0]],
        "Transform.Position": [null, null, { "temporal": [[[0, 0.1], [1000, 100]], [[0, 75], [0, 0.1]]] }],
        "Transform.Rotation": [null, [0, 45]],
        "Contents.Group 1.Contents.Path 1.Path": [
            null,
            [
                {
                    "vertices": [[0, -50], [50, 0], [0, 50], [-50, 0]],
                    "inTangents": [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0],
                    [0, 27.6142425537109]],
                    "outTangents": [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0],
                    [0, -27.6142425537109]],
                    "closed": 'true'
                },
                {
                    "vertices": [[0, -57.5], [57.5, 0], [0, 57.5], [-57.5, 0]],
                    // "inTangents": [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0], [0, 27.6142425537109]],
                    // "outTangents": [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0], [0, -27.6142425537109]],
                    "closed": true
                }
            ]
        ]
    }
    // 选中
    var selectedLayer = this.nodeLayers[key]["selectedLayer"]
    if (selectedLayer("Transform")("Opacity").numKeys === 0) {
        selectedKeyframes["Transform.Opacity"][0] = times - [0.5, 0.5];
        shareUtil.configKeyframes(selectedLayer, selectedKeyframes);
        // 掉落
        var dropLayer = this.nodeLayers[key]["dropLayer"]
        dropKeyframes["Transform.Opacity"][0] = [times[0], times[1], times[1] + 0.5]
        dropTmp["Position"] = dropLayer("Transform")("Position").value
        dropKeyframes["Transform.Position"][0] = times
        dropKeyframes["Transform.Position"][1] = [dropTmp["Position"], [50 + dropTmp["sn"] * 80, 810]]
        dropKeyframes["Transform.Rotation"][0] = times
        dropKeyframes["Contents.Group 1.Contents.Path 1.Path"][0] = times
        shareUtil.configKeyframes(dropLayer, dropKeyframes);
        shareUtil.configKeyframes(
            this.nodeLayers[key]["dropTextLayer"],
            { "Transform.Rotation": [times, [0, -45]], "Transform.Opacity": [[times[0], times[1], times[1] + 0.5], [0, 100, 0]] }
        )
        dropTmp["sn"] += 1

        // 队列
        var queueKeyframes = { "Transform.Opacity": [times + [0.5, 0.5], [0, 100]] }
        // var elemLayers = precompUtil.queueLayers[traverse][key]
        var elemLayers = this.queueLayers[traverse][key]
        shareUtil.configKeyframes(elemLayers["shapeLayer"], queueKeyframes)
        shareUtil.configKeyframes(elemLayers["textLayer"], queueKeyframes)
        // if (traverse === "preorder" && key === '3') {
        //     shareUtil.configKeyframes(selectedLayer, {
        //         "Contents.Group 1.Contents.Fill 1.Color": [
        //             [times[0], times[1]+0.5],
        //             [
        //                 colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["default"]),
        //                 colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["root"])
        //             ],
        //             {"spatial": [{"type": 'HOLD'}, {"type": 'HOLD'}]}
        //         ]
        //     });
        //     shareUtil.configKeyframes(elemLayers["shapeLayer"], {
        //         "Contents.Group 1.Contents.Fill 1.Color": [
        //             [times[0], times[1]+0.5],
        //             [
        //                 colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["default"]),
        //                 colorUtil.hexToRgb1(COLORS["tree"]["fillColor"]["root"])
        //             ],
        //             {"spatial": [{"type": 'HOLD'}, {"type": 'HOLD'}]}]
        //     });
        // }
        // for (var kQueue in precompUtil.queueLayers) {
        //     $.writeln(kQueue)
        //     var queue = precompUtil.queueLayers[kQueue]
        //     for (var kElem in queue) {
        //         $.writeln(kElem)
        //     }
        //     $.writeln('===============================')
        // }
    }
}

PrecompUtil.prototype._btTraverseForwardPath = function (traverse, forwardPath) {
    var times = this.times
    var nodePathKeyframes = {
        'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [50, 0]],
        'Contents.Group 1.Contents.Trim Paths 1.End': [times, [50, 100]],
    }
    var edgePathKeyframes = {
        'Contents.Group 1.Contents.Trim Paths 1.End': [times, [0, 100]],
    }

    for (var i = 0; i < forwardPath.length; i++) {
        if (forwardPath[i].name.indexOf("Node") !== -1) {
            // if (!keys[forwardPath[i].name]) {
            //     shareUtil.configKeyframes(forwardPath[i],  {
            //         'Contents.Group 1.Contents.Trim Paths 1.Start': [[0, times[0]-1/FRAME_RATE], [50, 50]],
            //         'Contents.Group 1.Contents.Trim Paths 1.End': [[0, times[0]-1/FRAME_RATE], [50, 50]],
            //     });
            // }
            shareUtil.configKeyframes(forwardPath[i], nodePathKeyframes);
            if (traverse === 'preorder') {
                var key = forwardPath[i].name.split('.').slice(-1)[0]
                this._btTraverseSelectedDropQueue(key, traverse)
            }
        } else {
            // if (!keys[forwardPath[i].name]) {
            //     shareUtil.configKeyframes(forwardPath[i],  {
            //         'Contents.Group 1.Contents.Trim Paths 1.End': [[0, times[0]-1/FRAME_RATE], [0, 0]],
            //     });
            // }
            shareUtil.configKeyframes(forwardPath[i], edgePathKeyframes);
        }
        // keys[forwardPath[i].name] = true
        times[0] += 1
        times[1] = times[0] + 0.5
    }
    if (traverse === 'inorder') {
        var key = forwardPath[i - 1].name.split('.').slice(-1)[0]
        this._btTraverseSelectedDropQueue(key, traverse)
    }
    forwardPath.length = 0;
}

PrecompUtil.prototype._btTraverseBackwardPath = function (traverse, backwardPath) {
    var times = this.times
    var nodePathKeyframes = {
        'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [0, 50]],
        'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 50]],
    }
    var edgePathKeyframes = {
        'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 0]],
    }
    var length;
    switch (traverse) {
        case 'preorder':
            length = backwardPath.length
            break;
        case 'inorder':
            length = 2
            break;
    }
    for (var i = 0; i < length; i++) {
        if (backwardPath[0].name.indexOf("Edge") !== -1) {
            shareUtil.configKeyframes(backwardPath[0], edgePathKeyframes);
        }
        else {
            shareUtil.configKeyframes(backwardPath[0], nodePathKeyframes);
        }
        times[0] += 1
        times[1] = times[0] + 0.5
        backwardPath.shift()
    }
    if (traverse === 'inorder') {
        var key = backwardPath.shift().name.split('.').slice(-1)[0]
        this._btTraverseSelectedDropQueue(key, traverse)
    }
}

PrecompUtil.prototype._btTraverse = function (traverse, nodePath, edgePath) {

    function processNode(node) {
        // $.writeln("==================================")
    }

    function preorder(traverse, root, func, forwardPath, backwardPath) {
        func(root)
        forwardPath.push(root["pathLayer"])
        backwardPath.unshift(root["pathLayer"])
        var direction = "left"
        if (root[direction]) {
            forwardPath.push(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root["edgeLayers"]["down"][direction]["pathLayer"])
            preorder(traverse, root[direction], func, forwardPath, backwardPath)
        }
        direction = "right"
        if (root[direction]) {
            forwardPath.push(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root["edgeLayers"]["down"][direction]["pathLayer"])
            preorder(traverse, root[direction], func, forwardPath, backwardPath)
        }
    }

    // 对动画路径来说其实是前序遍历
    function inorder(traverse, root, func, forwardPath, backwardPath) {
        forwardPath.push(root["pathLayer"])
        var direction = "left"
        if (root[direction]) {
            forwardPath.push(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root["pathLayer"])
            backwardPath.unshift(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root[direction]["pathLayer"])
            inorder(traverse, root[direction], func, forwardPath, backwardPath)
        }
        func(root)
        direction = "right"
        if (root[direction]) {
            forwardPath.push(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root["pathLayer"])
            backwardPath.unshift(root["edgeLayers"]["down"][direction]["pathLayer"])
            backwardPath.unshift(root[direction]["pathLayer"])
            inorder(traverse, root[direction], func, forwardPath, backwardPath)
        }
        if (!root["left"] && !root["right"]) {
            // 配置路径动画
            precompUtil._btTraverseForwardPath(traverse, forwardPath)
            if (backwardPath.length > 0) {
                precompUtil._btTraverseBackwardPath(traverse, backwardPath)
            }
        }
    }

    function doTraverse(traverse, root, func) {
        precompUtil.dropTmp = { "Position": null, "sn": 0 };
        var times = precompUtil.times
        var forwardPath = []
        var backwardPath = []

        if (traverse === 'preorder') {
            preorder(traverse, root, func, forwardPath, backwardPath)
            precompUtil._btTraverseForwardPath(traverse, forwardPath)
            precompUtil._btTraverseBackwardPath(traverse, backwardPath)
        } else if (traverse === 'inorder') {
            inorder(traverse, root, func, forwardPath, backwardPath)
            precompUtil._btTraverseBackwardPath(traverse, backwardPath)
            shareUtil.configKeyframes(root["pathLayer"], {
                'Contents.Group 1.Contents.Trim Paths 1.Start': [times, [0, 50]],
                'Contents.Group 1.Contents.Trim Paths 1.End': [times, [100, 50]],
            });
        }

    }

    doTraverse(traverse, this.rootNode, processNode)

    // 音效
    if (nodePath["sound"]) {
        var soundItem = shareUtil.findItemByName(node["Path"]["sound"]["name"])
        var startTimes = node["Path"]["sound"]["startTimes"]
        for (var i = 0; i < startTimes.length; i++) {
            var soundLayer = comp.layers.add(soundItem);
            soundLayer.startTime = startTimes[i];
        }
    }

    if (edgePath["sound"]) {
        var soundItem = shareUtil.findItemByName(edge["Path"]["sound"]["name"])
        var startTimes = edge["Path"]["sound"]["startTimes"]
        for (var i = 0; i < startTimes.length; i++) {
            var soundLayer = comp.layers.add(soundItem);
            soundLayer.startTime = startTimes[i];
        }
    }
}

PrecompUtil.prototype.binaryTree = function (items, parentComp, conf) {
    var comp = items.addComp(conf["layerName"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE);
    comp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])

    var elems = conf["elems"];

    var nodeShape = conf["node"]["shape"];
    var selected = conf["node"]["selected"];
    var drop = conf["node"]["drop"];
    var nodePath = conf["node"]["path"];

    var edgeShape = conf["edge"]["shape"];
    var edgePath = conf["edge"]["path"];

    var nodeScale = nodeShape["Scale"][0] / 100
    var edgeOffset = 45 * nodeScale;
    var horizontalDist = 160 * nodeScale;
    var verticalDist = 240 * nodeScale;

    var NODE_PREFIX = "Node";
    var EDGE_PREFIX = "Edge";

    var rootNodePos = [235 * nodeScale, 75 * nodeScale]
    this.nodeLayers = {}
    this.edgeLayers = {}

    if (nodePath) {
        var offset = nodePath["Trim Paths"]["Offset"]
    }
    var rotation = edgeShape["Rotation"]

    this.times = [0, 0.5]
    var step = [0.5, 0.5]

    function addNode(elem, parentNode, direction, selected, drop, upEdge) {
        var times = precompUtil.times
        var nodeLayers = precompUtil.nodeLayers
        var key = elem["key"]

        if (parentNode) {
            var parentPos = parentNode["Position"]
        }

        switch (direction) {
            case 'left':
                nodeShape["Position"] = [parentPos[0] - horizontalDist, parentPos[1] + verticalDist]
                if (nodePath) {
                    nodePath["Trim Paths"]["Offset"] = offset
                }
                break;
            case 'right':
                nodeShape["Position"] = [parentPos[0] + horizontalDist, parentPos[1] + verticalDist]
                if (nodePath) {
                    nodePath["Trim Paths"]["Offset"] = -offset
                }
                break;
            case null:
                nodeShape["Position"] = rootNodePos
                break;
            default:
                throw new TypeError("参数[direction]类型错误")
        }

        var shapeKeyframes = {
            "Transform.Opacity": [times, [0, 100], { "temporal": [[[0, 0.1], [200, 100]], [[0, 75], [0, 0.1]]] }]
        }
        nodeShape["layerName"] = NODE_PREFIX + "." + "Shape" + "." + key
        var shapeTextProps = { "text": key }
        if (js_bool(conf["animation"])) {
            nodeShape["keyframes"] = shapeKeyframes
            shapeTextProps["keyframes"] = shapeKeyframes
            precompUtil.times += step
        }
        if (elem["keyframes"]) {
            nodeShape["keyframes"] = elem["keyframes"]
            shapeTextProps["keyframes"] = elem["keyframes"]
            if (upEdge) {
                shareUtil.configKeyframes(upEdge["shapeLayer"], elem["keyframes"])
            }
        }
        var shapeLayer = shareUtil.addLayer(comp, nodeShape);

        if (selected) {
            selected["Position"] = nodeShape["Position"]
            selected["layerName"] = NODE_PREFIX + "." + "Selected" + "." + key
            selected["keyframes"] = elem["selectedKeyframes"]
            if (elem["Color"]) {
                selected["Fill"]["Color"] = colorUtil.hexToRgb1(elem["Color"])
            }
            var selectedLayer = shapeUtil.create_one(comp, selected)
            // selectedLayers[selected["layerName"]] = selectedLayer
        }
        var shapeTextLayer = textUtil.overlay(comp, shapeLayer, NODE_PREFIX + "." + "Text" + "." + key, shapeTextProps);

        if (drop) {
            // drop["Fill"]["Color"] = drop["Fill"]["Color"]
            drop["layerName"] = NODE_PREFIX + "." + "Drop" + "." + key
            drop["Position"] = nodeShape["Position"]
            var dropLayer = shapeUtil.create_one(comp, drop)
            // dropLayers[drop["layerName"]] = dropLayer
            var dropTextLayer = textUtil.overlay(comp, dropLayer, NODE_PREFIX + "." + "Drop" + '.' + "Text" + "." + key, { "text": key, "Opacity": 0 });
        }

        if (nodePath) {
            nodePath["pathGroup"]["type"] = "Group"
            nodePath["layerName"] = NODE_PREFIX + "." + "Path" + "." + key;
            // path["Position"] = shapeLayer("Transform")("Position").value.slice(0, 2)
            nodePath["Position"] = nodeShape["Position"]
            var pathLayer = shapeUtil.create_one(comp, nodePath)
            // nodePathLayers.push(pathLayer)
        }

        nodeLayers[key] = {
            "key": key,
            "Position": shapeLayer("Transform")("Position").value,
            "shapeLayer": shapeLayer, "shapeTextLayer": shapeTextLayer, "selectedLayer": selectedLayer, "dropLayer": dropLayer, "dropTextLayer": dropTextLayer, "pathLayer": pathLayer,
            "edgeLayers": {
                "down": { "left": null, "right": null },
                "up": upEdge ? upEdge : null,
            },
            "left": null, "right": null
        }
        if (parentNode) {
            parentNode[direction] = nodeLayers[key]
        }

        return nodeLayers[key]
    }

    function addEdge(elem, upNode, direction) {
        var times = precompUtil.times
        var edgeLayers = precompUtil.edgeLayers

        var key = elem[0]
        var upKey = upNode["key"];
        var upPos = upNode["Position"];

        if (direction === "left") {
            edgeShape["Position"] = [upPos[0] - edgeOffset, upPos[1] + edgeOffset]
            edgeShape["Rotation"] = rotation
            if (edgePath) {
                edgePath["Rotation"] = 0
            }
        } else if (direction === "right") {
            edgeShape["Position"] = [upPos[0] + edgeOffset, upPos[1] + edgeOffset]
            edgeShape["Rotation"] = -rotation
            if (edgePath) {
                edgePath["Rotation"] = -rotation * 2
            }
        } else {
            throw new TypeError("参数[direction]类型错误")
        }

        var edgeKeyframes = {
            // "Transform.Scale": [times, [[0, 0, 0], edgeShape["Scale"]], {"temporal": [[[0, 0.1], [200, 100]], [[0, 75], [0, 0.1]]]}]
            "Transform.Scale": [times, [[0, 0, 0], edgeShape["Scale"]], { "temporal": [[[0, 0.1], [300, 100]], [[0, 75], [0, 0.1]]] }]
        }
        edgeShape["layerName"] = EDGE_PREFIX + "." + direction + "." + "Shape" + "." + upKey + '.' + key
        if (js_bool(conf["animation"])) {
            edgeShape["keyframes"] = edgeKeyframes
            precompUtil.times += step
        }
        var shapeLayer = shareUtil.addLayer(comp, edgeShape)

        if (edgePath) {
            edgePath["pathGroup"]["type"] = "Group"
            edgePath["layerName"] = EDGE_PREFIX + "." + direction + "." + "Path" + "." + upKey + '.' + key
            edgePath["Position"] = edgeShape["Position"]
            var pathLayer = shapeUtil.create_one(comp, edgePath)
        }

        edgeLayers[key] = {
            "key": key,
            "shapeLayer": shapeLayer, "pathLayer": pathLayer,
            "nodeLayers": {
                "up": upNode ? upNode : null,
                "down": null,
            }
        }
        upNode["edgeLayers"]["down"][direction] = edgeLayers[key]

        return edgeLayers[key]
    }

    this.rootNode = addNode(elems[0], null, null, selected, drop)

    var i = 1;
    var nodeQueue = [this.rootNode]

    while (nodeQueue.length > 0) {
        var treeNode = nodeQueue.shift();
        if (elems[i] && elems[i]["key"]) {
            var edgeLayer = addEdge(elems[i], treeNode, "left")
            var nodeLayer = addNode(elems[i], treeNode, "left", selected, drop, edgeLayer)
            nodeQueue.push(nodeLayer)
        }
        i += 1;
        if (elems[i] && elems[i]["key"]) {
            var edgeLayer = addEdge(elems[i], treeNode, "right")
            var nodeLayer = addNode(elems[i], treeNode, "right", selected, drop, edgeLayer)
            nodeQueue.push(nodeLayer)
        }
        i += 1;
    }

    if (conf["traverse"]) {
        this._btTraverse(conf["traverse"], nodePath, edgePath)
    }

    var compLayer = shareUtil.addLayer(parentComp, conf, comp)
    return { 'comp': comp, 'compLayer': compLayer };
}

PrecompUtil.prototype._bTreeElems = function (items, parentComp, conf) {
    var unit = conf["unit"]
    var elems = conf["elems"];
    var nodePos = [conf["width"]/2, unit["pathGroup"]["size"][1]/2]
}

PrecompUtil.prototype._bTreeNode = function (leaf) {
    return {"leaf": leaf, "keys": [], "children": [], "animation": []}
}

PrecompUtil.prototype._bTreeSplitChildren = function (node, i) {
    var order = this._btree.order
    var mid = order / 2
    var child = node.children[i]
    var new_child = this._bTreeNode(child.leaf)
    node.children.splice(i+1, 0, new_child)
    node.keys.splice(i, 0, child.keys[mid-1])
    new_child.keys = child.keys.slice(mid, order-1)
    child.keys = child.keys.slice(0, mid-1)
    // 如果不是叶节点，还要把子节点分裂成左右两部分
    if (!child.leaf) {
        new_child.children = child.children.slice(mid, order)
        child.children = child.children.slice(0, mid)
    }

    // if (conf["animation"]) {
        
    // }

    // return level, node_idx, key_idx
}

PrecompUtil.prototype._bTreeInsertNonFull = function (node, key) {
    var i = node.keys.length - 1
    if (node.leaf) {
        node.keys.push(null)
        while (i >= 0 && key < node.keys[i]) {
            node.keys[i + 1] = node.keys[i]
            i -= 1
        }
        node.keys[i + 1] = key
    } else {
        while (i >= 0 && key < node.keys[i]) {
            i -= 1
        }
        i += 1
        if (node.children[i].keys.length === this._btree.order - 1) {
            this._bTreeSplitChildren(node, i)
            if (key > node.keys[i]) {
                i += 1
            }
        }
        this._bTreeInsertNonFull(node.children[i], key)
    }
}

PrecompUtil.prototype._bTreeInsert = function (elem) {
    var root = this._btree.root
    // 根节点满了，分裂节点，树的高度加1
    if (root.keys.length === this._btree.order - 1) {
        var new_root = this._bTreeNode(false)
        this._btree.root = new_root
        new_root.children.unshift(root)
        this._bTreeSplitChildren(new_root, 0)
        this._bTreeInsertNonFull(new_root, elem["key"])
    }else {
        this._bTreeInsertNonFull(root, elem["key"])
    }
        
}

PrecompUtil.prototype._bTreeAdd = function (items, parentComp, unit) {
    var strokeAdd = unit['Stroke']['Stroke Width'] * 4
    var elem_width = unit["pathGroup"]["Size"][0]
    var elem_height = unit["pathGroup"]["Size"][1]
    var height = elem_height + strokeAdd

    function addEdges(parentPos, childrenPos, level, rc) {
        parentPos[1] -= rc/2
        for (var i = 0; i < childrenPos.length; i++) {
            if (i > 0) {
                parentPos[0] += elem_width
            }
            
            var anchorPoint
            if (parentPos[0] > childrenPos[i][0]) {
                anchorPoint = "RIGHT_TOP"
            } else {
                anchorPoint = "LEFT_TOP"
            }
            var unit = {
                "layerName": level+"."+i,
                "Anchor Point": anchorPoint, 'Position': parentPos,
                "pathGroup": {
                    "type": "Group",
                    "vertices": [parentPos, childrenPos[i]],
                    "closed": false,
                },
                "Stroke": {
                    "Stroke Width": 1,
                    "Color": colorUtil.hexToRgb1("#000000")
                },
            }
            shapeUtil.addOne(parentComp, unit)
        }
    }

    function addNode(node, width, level, idx, pos) {
        var conf = {
            "layerName": level+"."+idx, "type": "QUEUE", "traverse": "inorder",
            "width": width, "height": height, "Anchor Point": "LEFT_DOWN", "Position": pos,
            "duration": parentComp.duration,
            "unit": unit,
        }
        var elems = []
        for (var k = 0; k < node.keys.length; k++) {
            elems.push({"key": node.keys[k]})
        }
        conf["elems"] = elems
        precompUtil.queue(items, parentComp, conf)
        pos[0] += width
        return pos
    }

    // 层序遍历
    function add() {
        var level = 0
        var queue = [[{"parent": null, "level": level, "children": [precompUtil._btree.root]}]]
        var queue_inv = [[{"parent": null, "level": level, "children": [precompUtil._btree.root]}]]
        while (queue.length > 0) {
            var ChildrenArr = queue.shift()
            var tmpChildrenArr = []
            for (var i = 0; i < ChildrenArr.length; i++) {
                var children = ChildrenArr[i]["children"]
                for (var j = 0; j < children.length; j++) {
                    var node = children[j]
                    if (node.children.length > 0) {
                        tmpChildrenArr.push({"parent": node, "level": level+1, "children": node.children})
                    }
                }
            }
            if (tmpChildrenArr.length > 0) {
                queue.push(tmpChildrenArr)
                queue_inv.unshift(tmpChildrenArr)
                level += 1
            }
        }
        var maxLevel = level
        var pos = null
        var posArr = []
        var start_x = 0
        var step_x = start_x
        while (queue_inv.length > 0) {
            var ChildrenArr = queue_inv.shift()
            for (var i = 0; i < ChildrenArr.length; i++) {
                var level = ChildrenArr[i]["level"]
                var children = ChildrenArr[i]["children"]
                var childrenPos = []
                for (var j = 0; j < children.length; j++) {
                    var node = children[j]
                    var width =  elem_width * node.keys.length + strokeAdd
                    if (level < maxLevel) {
                        pos[0] = posArr.shift() - width/2
                        if (i === 0 && j === 0) {
                            start_x = pos[0]
                            step_x = start_x
                        }
                    } else {
                        if (!pos) {
                            pos = [0, parentComp.height]
                        } else {
                            pos[0] += elem_width
                        }
                    }
                    pos = addNode(children[j], width, level, j, pos)
                    childrenPos.push([pos[0] - width/2, pos[1]-elem_height])
                }
                pos_x = step_x + (pos[0]-step_x)/2
                posArr.push(pos_x)
                if (level > 0) {
                    var parent = ChildrenArr[i]["parent"]
                    addEdges([pos_x - (elem_width * parent.keys.length + strokeAdd)/2, pos[1]-elem_height*2], childrenPos, level, unit["RC"]["Radius"])
                }
                step_x = pos[0] + elem_width
            }
            pos[1] -= elem_height*2
        }
    }

    add()
}

PrecompUtil.prototype._bTreeAnimation = function (items, parentComp, unit, animationElems) {
    function insert(elem) {
        // 插入数据的同时记录需要更新的节点信息
        this._bTreeInsert(elem)
        // 配置插入动画
    }

    function del(elem) {
        // 删除数据的同时记录需要更新的节点信息
        // 配置删除动画
    }

    function search(elem) {
        // 搜索数据的同时记录需要更新的节点信息
        // 配置搜索动画
    }

    for (var i = 0; i < animationElems.length; i++) {
        var elem = animationElems[i]
        switch (elem.oper) {
            case 'S':
                search(elem)
                break;
            case 'D':
                del(elem)
                break;
            default:
                insert(elem)
        }
    }
}

PrecompUtil.prototype.bTree = function (items, parentComp, conf) {
    this._btree = {
        "root": this._bTreeNode(true),
        "order": 4,
    }
    var comp = items.addComp(conf["layerName"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE);
    comp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])

    var unit = conf["unit"]
    var elems = conf["elems"];

    if (conf["animationElems"]) {
        this._bTreeAnimation(items, comp, unit, conf["animationElems"])
    } else {
        for (var i = 0; i < elems.length; i++) {
            this._bTreeInsert(elems[i])
        }
        this._bTreeAdd(items, comp, unit)
    }

    shareUtil.addLayer(parentComp, conf, comp)
}

PrecompUtil.prototype.graph = function (nodeLayer, edgeLayer, elems) {

}

PrecompUtil.prototype.addOne = function (items, parentComp, conf) {
    var comp;
    if (conf["type"] === "CODES") {
        comp = this.codes(parentComp, conf)
    } else if (conf["type"] === "MISCS") {
        comp = this.miscs(parentComp, conf)
    } else if (conf["type"] === "STACK") {
        comp = this.stack(parentComp, conf)
    } else if (conf["type"] === "QUEUE") {
        comp = this.queue(items, parentComp, conf)
    } else if (conf["type"] === "LINKED_LIST") {
        comp = this.linkedList(items, parentComp, conf)
    } else if (conf["type"] === "BINARY_TREE") {
        comp = this.binaryTree(items, parentComp, conf)
    } else if (conf["type"] === "B-TREE") {
        comp = this.bTree(items, parentComp, conf)
    } else if (conf["type"] === "GRAPH") {
        comp = this.graph(conf)
    }
    return comp
}

PrecompUtil.prototype.addMany = function (items, parentComp, precomps) {
    for (var i = 0; i < precomps.length; i++) {
        this.addOne(items, parentComp, precomps[i])
    }
}

var precompUtil = new PrecompUtil();