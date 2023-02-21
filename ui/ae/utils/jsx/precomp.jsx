function PrecompUtil() {
    this.temporal = [[[0, 0.1], [500,  65]], [[0.1, 75], [0, 0.1]]]
    this.spatial = [{"type": 'HOLD'}, {"type": 'HOLD'}]
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

PrecompUtil.prototype.misc = function (items, parentComp, conf, layersCollecter) {
    var miscFolder = items.addFolder(conf["layerName"])
    var miscComp = miscFolder.items.addComp(conf["layerName"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE);
    miscComp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])
    if (conf["misc"]) {
        layersCollecter["misc"] = {}
        this.misc(miscFolder.items, miscComp, conf["misc"], layersCollecter["misc"])
    }
    if (conf["miscs"]) {
        this.miscs(miscFolder.items, miscComp, conf["miscs"])
    }
    if (conf["subtitles"]) {
        shareUtil.addSubtitles(conf["subtitles"])
    }
    if (conf["camera"]) {
        shareUtil.configKeyframes(cameraLayer, conf["camera"])
    }
    if (conf["audios"]) {
        shareUtil.addLayers(miscComp, conf["audios"])
    }
    if (conf["images"]) {
        shareUtil.addLayers(miscComp, conf["images"])
    }
    if (conf["videos"]) {
        shareUtil.addLayers(miscComp, conf["videos"])
    }
    if (conf["codes"]) {
        this.codes(miscFolder.items, miscComp, conf["codes"])
    }
    if (conf["vectors"]) {
        layersCollecter["vectors"] = {}
        shapeUtil.addVectors(miscComp, conf["vectors"], layersCollecter["vectors"])
    }
    if (conf["shapes"]) {
        layersCollecter["shapes"] = {}
        shapeUtil.addMany(miscComp, conf["shapes"], layersCollecter["shapes"])
    }
    if (conf["precomps"]) {
        layersCollecter["precomps"] = {}
        this.addMany(miscFolder.items, miscComp, conf['precomps'], layersCollecter["precomps"])
    }
    if (conf["texts"]) {
        textUtil.addMany(miscComp, conf["texts"])
    }
    layersCollecter["layer"] = shareUtil.addLayer(parentComp, conf, miscComp);
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

PrecompUtil.prototype.queue = function (items, parentComp, conf, layersCollecter) {
    var layerName = conf["layerName"]
    var elems = conf['elems']
    var unit = conf["unit"];
    layersCollecter["keys"] = {}

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
        var textProps = { "text": key, "font": "Arial-BoldItalicMT", "fontSize": unit["fontSize"], "Position": [elemWidth / 2, elemHeight / 2] }
        if (elems[i]["keyframes"]) {
            unit["keyframes"] = elems[i]["keyframes"]
            textProps["keyframes"] = elems[i]["keyframes"]
            // shareUtil.configKeyframes(shapeLayer, elems[i]["keyframes"])
        }
        var shapeLayer = shapeUtil.addOne(queueComp, unit)
        var textLayer = textUtil.overlay(
            queueComp, shapeLayer, "Text" + "." + key,
            textProps
        );
        layersCollecter["keys"][key] = {'shapeLayer': shapeLayer, "textLayer": textLayer, "keyframes": {}}
    }

    layersCollecter["layer"] = shareUtil.addLayer(parentComp, conf, queueComp)
    layersCollecter["keyframes"] = {}
    // return layersCollecter
    // layersCollecter[layerName]["time"] = 0
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

PrecompUtil.prototype._bTreeNode = function (leaf, level, idx, parent) {
    return {
        "leaf": leaf, "level": level, "idx": idx, "keys": [], "parent": parent, "children": [], "ui": null,
        "parentEdge": null, "childrenEdges": []
    }
}

PrecompUtil.prototype._bTreeSplitChildren = function (items, parentComp, parent, idx, conf, layersCollecter) {
    var order = this._btree.order
    var mid = order / 2
    var child = parent.children[idx]
    var new_child = this._bTreeNode(child.leaf, child.level, idx+1, parent)

    // 移动左右的node和受到推挤的其它node, keys有变动就重建node(queue合成)
    parent.children.splice(idx+1, 0, new_child)
    parent.keys.splice(idx, 0, child.keys[mid-1])
    new_child.keys = child.keys.slice(mid, order-1)
    child.keys = child.keys.slice(0, mid-1)
    // 如果不是叶节点，还要把子节点分裂成左右两部分
    // 移动左右的node和收到推挤的其它node, keys有变动就重建node(queue合成)
    if (!child.leaf) {
        new_child.children = child.children.slice(mid, order)
        child.children = child.children.slice(0, mid)
    }

    function animationSplit() {
        var shotTime = shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"]
        // 中间节点
        // 移动父节点两侧的keys
        for (var i = 0; i < idx; i++) {
            var key = parent.keys[i]
            var layer = layersCollecter[key.key].layer
            var oldPos = layer("Transform")("Position").valueAtTime(shotTime, false)
            shareUtil.configKeyframes(
                layer,
                {
                    "Transform.Position": [
                        [shotTime, shotTime + 1],
                        [oldPos, [oldPos[0]-QUE_ELEM_WIDTH/2, oldPos[1]]],
                        { "temporal": precompUtil.temporal }
                    ]
                }
            )
        }
        for (var i = idx+1; i < parent.keys.length; i++) {
            var key = parent.keys[i]
            var layer = layersCollecter[key.key].layer
            var oldPos = layer("Transform")("Position").valueAtTime(shotTime, false)
            shareUtil.configKeyframes(
                layer,
                {
                    "Transform.Position": [
                        [shotTime+1, shotTime + 2],
                        [oldPos, [oldPos[0]+QUE_ELEM_WIDTH/2, oldPos[1]]],
                        { "temporal": precompUtil.temporal }
                    ]
                }
            )
        }
        shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
        precompUtil._bTreeShowIndicator(false, conf)
        shotTime = shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"]
        // 同步移动indicator
        // if (node.keys[idx+1]) {
        //     precompUtil._bTreeMoveIndicator(conf, 0.5, 0, true)
        // } else {
        //     precompUtil._bTreeMoveIndicator(conf, -0.5, 0, true)
        // }

        // 上升到父节点指定位置
        var key = parent.keys[idx]
        var layer = layersCollecter[key.key].layer
        var oldPos = layer("Transform")("Position").valueAtTime(shotTime, false)

        var referKey = parent.keys[idx-1]
        var referPos
        var newPos
        if (referKey) {
            referPos = layersCollecter[referKey.key].layer("Transform")("Position").valueAtTime(shotTime, false)
            newPos = [referPos[0]+QUE_ELEM_WIDTH/2, referPos[1]]
        } else {
            referKey = parent.keys[idx+1]
            if (referKey) {
                referPos = layersCollecter[referKey.key].layer("Transform")("Position").valueAtTime(shotTime, false)
                newPos = [referPos[0]-QUE_ELEM_WIDTH/2, referPos[1]]
            } else {
                newPos = [oldPos[0], oldPos[1] - QUE_ELEM_HEIGHT * 2]
            }
        }

        shareUtil.configKeyframes(
            layer,
            {
                "Transform.Position": [
                    [shotTime, shotTime + 1],
                    [oldPos, newPos],
                    { "temporal": precompUtil.temporal }
                ]
            }
        )

        // 重定位受影响的两侧子节点keys
        if (!child.leaf) {
            for (var i = 0; i < idx; i++) {
                var childNode = parent.children[i]
                for (var j = 0; j < childNode.keys.length; j++) {
                    var key = childNode.keys[j]
                    var layer = layersCollecter[key.key].layer
                    var oldPos = layer("Transform")("Position").valueAtTime(shotTime, false)
                    shareUtil.configKeyframes(
                        layer,
                        {
                            "Transform.Position": [
                                [shotTime, shotTime + 1],
                                [oldPos, [oldPos[0] - QUE_ELEM_WIDTH / 2, oldPos[1]]],
                                { "temporal": precompUtil.temporal }
                            ]
                        }
                    )
                }
            }
            for (var i = idx+2; i < parent.children.length; i++) {
                var childNode = parent.children[i]
                for (var j = 0; j < childNode.keys.length; j++) {
                    var key = childNode.keys[j]
                    var layer = layersCollecter[key.key].layer
                    var oldPos = layer("Transform")("Position").valueAtTime(shotTime, false)
                    shareUtil.configKeyframes(
                        layer,
                        {
                            "Transform.Position": [
                                [shotTime, shotTime + 1],
                                [oldPos, [oldPos[0] + QUE_ELEM_WIDTH / 2, oldPos[1]]],
                                { "temporal": precompUtil.temporal }
                            ]
                        }
                    )
                }
            }
        }
        
        shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1

        shotTime = shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"]
        var parentPosArr = []
        var parentLayerNames = []
        for (var i = 0; i < parent.keys.length; i++) {
            
            var key = parent.keys[i]
            parentLayerNames.push(parent.level+'.'+parent.idx+'.'+i)
            // parentLayerName += key.key
            var layer = layersCollecter[key.key].layer
            var pos = layer("Transform")("Position").valueAtTime(shotTime, false)
            parentPosArr.push([pos[0]-QUE_ELEM_WIDTH/2, pos[1]+QUE_ELEM_HEIGHT/2])
            if (!parent.keys[i+1]) {
                parentLayerNames.push(parent.level+'.'+parent.idx+'.'+(i+1))
                parentPosArr.push([pos[0]+QUE_ELEM_WIDTH/2, pos[1]+QUE_ELEM_HEIGHT/2])
            }
        }

        var childrenPosArr = []
        var childrenLayerNames = []
        for (var i = 0; i < parent.children.length; i++) {
            var childNode = parent.children[i]
            var firstKeyPos = layersCollecter[childNode.keys[0].key].layer("Transform")("Position").valueAtTime(shotTime, false)
            childrenPosArr.push([firstKeyPos[0]-QUE_ELEM_WIDTH/2+childNode.keys.length*QUE_ELEM_WIDTH/2, firstKeyPos[1]-QUE_ELEM_HEIGHT/2])
            // var childLayerName = ''
            // for (var j = 0; j < childNode.keys.length; j++) {
            //     childLayerName += childNode.keys[j].key
            // }
            childrenLayerNames.push(childNode.level+'.'+childNode.idx)
        }

        for (var i = 0; i < parentPosArr.length; i++) {
            var anchorPoint
            if (parentPosArr[i][0] > childrenPosArr[i][0]) {
                anchorPoint = "RIGHT_TOP"
            } else {
                anchorPoint = "LEFT_TOP"
            }
            var layerName = parentLayerNames[i]+'_'+childrenLayerNames[i]
            var unit = {
                "layerName": layerName,
                "Anchor Point": anchorPoint, 'Position': parentPosArr[i],
                "pathGroup": {
                    "type": "Group",
                    "vertices": [parentPosArr[i], childrenPosArr[i]],
                    "closed": false,
                },
                "Stroke": {
                    "Stroke Width": 1,
                    "Color": colorUtil.hexToRgb1("#000000")
                },
                "Trim Paths": {
                    'Start': 0,
                },
                "keyframes": {
                    "Contents.Group 1.Contents.Trim Paths 1.End": [
                            [shotTime, shotTime+1],
                            [0, 100],
                            {"temporal": precompUtil.temporal}
                        ]
                },
            }
            // 隐藏旧的edges
            if (layersCollecter[layerName]) {
                // layersCollecter[layerName].layer("Transform")("Opacity").setValueAtTime(shotTime, 0)
                // var prop = layersCollecter[layerName].layer("Transform")("Opacity")
                // prop.setValueAtTime(shotTime-2, 0)
                // prop.setInterpolationTypeAtKey(prop.nearestKeyIndex(shotTime-2), TYPE_DIC["HOLD"])
                shareUtil.configKeyframes(
                    layersCollecter[layerName].layer,
                    {
                        "Transform.Opacity": [
                            [conf["startTime"], shotTime-1],
                            [100, 0],
                            {"spatial": precompUtil.spatial}
                        ]
                    }
                )
            }
            layersCollecter[layerName] = {}
            shapeUtil.addOne(parentComp, unit, layersCollecter[layerName])
            parent.childrenEdges.splice(i, 0, layersCollecter[layerName])
            parent.children[i].parentEdge = layersCollecter[layerName]
        }
        shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
    }

    animationSplit()
    this._bTreeIndicatorResetPos(conf, parent, layersCollecter)
}

PrecompUtil.prototype._bTreeIndicatorResetPos = function (conf, node, layersCollecter) {
    var i = this._btree.root.keys.length - 1
    if (i < 0) {
        return
    }
    var keyLayer = layersCollecter[node.keys[i].key].layer
    var indicator = this._bTreeIndicator(conf)
    var shotTime = shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"]
    // var frameTime = conf["startTime"] + shotTime
    // var top = nodeLayer.sourceRectAtTime(frameTime, false).top
    // var left = nodeLayer.sourceRectAtTime(frameTime, false).left
    // var width = nodeLayer.sourceRectAtTime(frameTime, false).width
    var pos = keyLayer("Transform")("Position").valueAtTime(shotTime, false)
    var indicatorPosProp = indicator["layer"]("Transform")("Position")
    indicatorPosProp.setValueAtTime(
        shotTime, [pos[0]+QUE_ELEM_WIDTH/2, pos[1]]
    )
    indicatorPosProp.setInterpolationTypeAtKey(indicatorPosProp.nearestKeyIndex(shotTime), TYPE_DIC["HOLD"])
}

PrecompUtil.prototype._bTreeIndicator = function (conf) {
    var paths = conf["layersRoot"].split(".")
    var indicator = shareUtil.scenes[shareUtil.sName][shareUtil.shot]
    for (var j = 0; j < paths.length; j++) {
        indicator = indicator[paths[j]]
    }
    return indicator["vectors"]["Indicator"]
}

PrecompUtil.prototype._bTreeIndicatorPos = function (conf) {
    var paths = conf["layersRoot"].split(".")
    var indicator = shareUtil.scenes[shareUtil.sName][shareUtil.shot]
    for (var j = 0; j < paths.length; j++) {
        indicator = indicator[paths[j]]
    }
    indicator = indicator["vectors"]["Indicator"]
    var layer = indicator["layer"]
    var shotTime = shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"]
    return layer("Transform")("Position").valueAtTime(shotTime, false)
}

PrecompUtil.prototype._bTreeSetIndicatorPos = function (pos, conf) {
    var indicator = this._bTreeIndicator(conf["layersRoot"])
    var layer = indicator["layer"]
    // layer("Transform")("Position").setValue(pos)
}

PrecompUtil.prototype._bTreeMoveIndicator = function (conf, offset_x, offset_y, notHold) {
    this._bTreeShowIndicator(true, conf)
    if (offset_x === 0 && offset_y === 0) {
        return
    }
    var shotTime = shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"]
    var indicator = this._bTreeIndicator(conf)
    var layer = indicator["layer"]
    var oldPos = layer("Transform")("Position").valueAtTime(shotTime, false)
    var keyframes = {
        "Transform.Position": [
            [shotTime, shotTime+1],
            [oldPos, [oldPos[0]+QUE_ELEM_WIDTH*offset_x, oldPos[1]+QUE_ELEM_HEIGHT*2*offset_y]],
        ]
    }
    if (!notHold) {
        keyframes["Transform.Position"].push({"spatial": this.spatial})
    } else {
        keyframes["Transform.Position"].push({"temporal": precompUtil.temporal, "spatial": [{"type": 'BEZIER'}, {"type": 'BEZIER'}]})
    }
    shareUtil.configKeyframes(
        layer,
        keyframes
    )
    shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
    // var keyframes = indicator["keyframes"]["Transform.Position"]
    // var time = indicator["time"]
    // var prop = layer("Transform")("Position")
    // var pos = keyframes[1].slice(-1)[0]
    // if (keyframes[1].length === 0) {
    //     pos = prop.value
    // } else {
    //     pos = keyframes[1].slice(-1)[0]
    // }
    // indicator["keyframes"]["Transform.Position"] = [keyframes[0].concat([time]), keyframes[1].concat([[pos[0]+30, pos[1]]])]
    // indicator["time"] += 1
}

PrecompUtil.prototype._bTreeAnimationAddKey = function (items, parentComp, node, idx, conf, layersCollecter, moved) {
    // shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
    var shotTime = shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"]

    function _moveKey(i, distance) {
        shotTime = shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"]
        if (!node.keys[i]) {
            return
        }
        var layer = layersCollecter[node.keys[i].key].layer
        var oldPos = layer("Transform")("Position").valueAtTime(shotTime, false)
        shareUtil.configKeyframes(
            layer,
            {
                "Transform.Position": [
                    [shotTime, shotTime+1],
                    [oldPos, [oldPos[0]+distance, oldPos[1]]],
                    {"temporal": precompUtil.temporal}
                ]
            }
        )
        // shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
    }

    // if (moved) {
    //     for (var i = 0; i < idx; i++) {
    //         // shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
    //         _moveKey(i, -QUE_ELEM_WIDTH)
    //         // shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
    //     }
    // } else {
    //     for (var i = node.keys.length-1; i > idx; i--) {
    //         _moveKey(i, QUE_ELEM_WIDTH)
    //     }
    // }

    // if (idx > 0) {
    //     shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
    // }
    shotTime = shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"]
    var indicatorPos = this._bTreeIndicatorPos(conf)
    var layerName = node.keys[idx].key

    QUE_UNIT['layerName'] = layerName
    var pos = [QUE_ELEM_WIDTH/2, QUE_ELEM_HEIGHT/2]
    QUE_UNIT['Position'] = pos
    var misc = {
        'layerName': layerName, 'width': QUE_ELEM_WIDTH, 'height': QUE_ELEM_HEIGHT, 'duration': conf["duration"],
        'Position': [indicatorPos[0]-QUE_ELEM_WIDTH/2, indicatorPos[1]],
        'texts': [
            {
                'text': layerName, 'Position': pos,
                'font': FONTS['subtitle'], 'fillColor': COLORS['text'], 'fontSize': 40,
            }
        ],
        'shapes': [
            QUE_UNIT
        ],
        'keyframes': {
            "Transform.Opacity": [
                [shotTime, shotTime+1],
                [0, 100],
                {"spatial": [{"type": 'HOLD'}, {"type": 'HOLD'}]}
            ]
        }
    }
    // shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
    layersCollecter[layerName] = {}
    this.misc(items, parentComp, misc, layersCollecter[layerName])

    for (var i = 0; i < idx; i++) {
        // shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
        _moveKey(i, -QUE_ELEM_WIDTH)
        // shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
    }

    for (var i = idx+1; i < node.keys.length-1; i++) {
        this._bTreeMoveIndicator(conf, 0.5, 0)
        _moveKey(i, QUE_ELEM_WIDTH/2)
    }

    // shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
    // this._bTreeShowIndicator(false, conf)
    shotTime = shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"]
    if (node.parentEdge) {
        var edgeLayer = node.parentEdge.layer
        var path = edgeLayer("Contents")("Group 1")("Contents")("Path 1")("Path").valueAtTime(shotTime, false)
        // 计算边界key所处的位置
        var parentPos = path.vertices[0]
        var childPos = path.vertices[1]

        var distance
        if (parentPos[0] > childPos[0]) {
            distance = -QUE_ELEM_WIDTH/2
        } else {
            distance = QUE_ELEM_WIDTH/2
        }
        // 重新定位edges
        shareUtil.configKeyframes(
            edgeLayer,
            {
                "Contents.Group 1.Contents.Path 1.Path": [
                    [shotTime + 1, shotTime + 2],
                    [
                        {
                            "vertices": path.vertices,
                            "closed": false
                        },
                        {
                            "vertices": [path.vertices[0],[path.vertices[1][0]+distance, path.vertices[1][1]]],
                            "closed": false
                        }
                    ],
                    { "temporal": precompUtil.temporal }
                ]
            }
        )

        var startKeyLayer
        var startPos
        if (parentPos[0] <= childPos[0]) {
            shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
            this._bTreeShowIndicator(false, conf)
            shotTime = shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"]
            startKeyLayer = layersCollecter[node.keys[0].key].layer
            startPos = startKeyLayer("Transform")("Position").valueAtTime(shotTime, false)
            distance = parentPos[0]-startPos[0]+QUE_ELEM_WIDTH/2
            // 同时移动所有key和父连接线的终点到节点整体的中间位置
            for (var j = 0; j < node.keys.length; j++) {
                var keyLayer = layersCollecter[node.keys[j].key].layer
                var oldPos = keyLayer("Transform")("Position").valueAtTime(shotTime, false)
                shareUtil.configKeyframes(
                    keyLayer,
                    {
                        "Transform.Position": [
                            [shotTime, shotTime+1],
                            // [oldPos, [oldPos[0]-(parentPos[0]-childPos[0]), oldPos[1]]],
                            [oldPos, [oldPos[0]+distance, oldPos[1]]],
                            // {"spatial": [{"type": 'HOLD'}, {"type": 'HOLD'}]}
                            {"temporal": this.temporal}
                        ]
                    }
                )
            }
        }
    }

    shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
    return layersCollecter[layerName]
}

PrecompUtil.prototype._bTreeInsertNonFull = function (items, parentComp, node, key, conf, layersCollecter) {
    var i = node.keys.length - 1
    // if (i >= 0) {
    //     this._bTreeSetIndicatorPos(layersCollecter[node.keys[i].key].layer("Transform")("Position").value, conf)
    // }
    var moved = false
    if (node.leaf) {
        node.keys.push(null)
        while (i >= 0 && key["key"] < node.keys[i]["key"]) {
            node.keys[i + 1] = node.keys[i]
            i -= 1
            // 移动标杆
            this._bTreeMoveIndicator(conf, -1, 0)
            moved = true
        }
        // 移动node, keys有变动就重建node(queue合成)，配置edge的vertices顶点变动keyframes
        node.keys[i + 1] = key
        node["ui"] = this._bTreeAnimationAddKey(items, parentComp, node, i + 1, conf, layersCollecter, moved)
    } else {
        while (i >= 0 && key["key"] < node.keys[i]["key"]) {
            i -= 1
            // 移动标杆
            this._bTreeMoveIndicator(conf, -1, 0)
            // indicatorMoveTimes += 1
            moved = true
        }
        i += 1
        var splited = false
        if (node.children[i].keys.length === this._btree.order - 1) {
            this._bTreeSplitChildren(items, parentComp, node, i, conf, layersCollecter)
            // this._bTreeMoveIndicator(conf, node.children[i+1].keys.length, 1)
            if (key["key"] > node.keys[i]["key"]) {
                i += 1
            }
            splited = true
            // this._bTreeMoveIndicator(conf, node.children[i].keys.length, 1)
        }
        if (moved) {
            this._bTreeMoveIndicator(conf, 0, 1)
        } else {
            this._bTreeMoveIndicator(conf, node.children[i].keys.length, 1)
        }
        
        // if (splited) {
        //     this._bTreeMoveIndicator(conf, node.children[i].keys.length, 1)
        // } else {
        //     this._bTreeMoveIndicator(conf, 0, 1)
        // }
        // this._bTreeMoveIndicator(conf, node.children[i].keys.length, 1)

        this._bTreeInsertNonFull(items, parentComp, node.children[i], key, conf, layersCollecter)
    }
}

PrecompUtil.prototype._bTreeSearch = function (k, node) {
    if (node) {
        i = 0
        while ((i < node.keys.length) && (k > node.keys[i]["key"])) {
            i += 1
        }
        if ((i < node.keys.length) && (k === node.keys[i]["key"])) {
            return node, i
        } else if (node.leaf) {
            return null
        } else {
            return this._bTreeSearch(k, node.children[i])
        }       
    } else {
        return this._bTreeSearch(k, this._btree.root)
    }
}

PrecompUtil.prototype._bTreeShowIndicator = function (show, conf) {
    var shotTime = shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"]
    var prop = this._bTreeIndicator(conf)["layer"]("Transform")("Opacity")
    prop.setValueAtTime(shotTime, show ? 100 : 0)
    prop.setInterpolationTypeAtKey(prop.nearestKeyIndex(shotTime), TYPE_DIC["HOLD"])
    // shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
}

PrecompUtil.prototype._bTreeInsert = function (items, parentComp, elem, conf, layersCollecter) {
    var key = {"key": elem["key"]}
    var root = this._btree.root
    // 根节点满了，分裂节点，树的高度加1
    if (root.keys.length === this._btree.order - 1) {
        var new_root = this._bTreeNode(false, 0, 0, null)
        root.parent = new_root
        root.level += 1
        new_root.children.unshift(root)
        this._btree.root = new_root
        this._bTreeSplitChildren(items, parentComp, new_root, 0, conf, layersCollecter)
        this._bTreeInsertNonFull(items, parentComp, new_root, key, conf, layersCollecter)
    }else {
        this._bTreeInsertNonFull(items, parentComp, root, key, conf, layersCollecter)
    }
    this._bTreeShowIndicator(false, conf)
}

PrecompUtil.prototype._bTreeAdd = function (items, parentComp, elems, unit) {
    for (var i = 0; i < elems.length; i++) {
        var elem = elems[i]
        if (elem.oper === "I") {
            this._bTreeInsert(parentComp, elems[i])
        }
    }

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
        var queue = [[{"parent": null, "level": level, "nodes": [precompUtil._btree.root]}]]
        var queueInv = [[{"parent": null, "level": level, "nodes": [precompUtil._btree.root]}]]
        while (queue.length > 0) {
            var levelNodes = queue.shift()
            var tmpLevelNodes = []
            for (var i = 0; i < levelNodes.length; i++) {
                var children = levelNodes[i]["nodes"]
                for (var j = 0; j < children.length; j++) {
                    var node = children[j]
                    if (node.children.length > 0) {
                        tmpLevelNodes.push({"parent": node, "level": level+1, "nodes": node.children})
                    }
                }
            }
            if (tmpLevelNodes.length > 0) {
                queue.push(tmpLevelNodes)
                queueInv.unshift(tmpLevelNodes)
                level += 1
            }
        }
        var maxLevel = level
        var pos = null
        var posArr = []
        var start_x = 0
        var step_x = start_x
        while (queueInv.length > 0) {
            var levelNodes = queueInv.shift()
            for (var i = 0; i < levelNodes.length; i++) {
                var level = levelNodes[i]["level"]
                var nodes = levelNodes[i]["nodes"]
                var childrenPos = []
                for (var j = 0; j < nodes.length; j++) {
                    var node = nodes[j]
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
                    pos = addNode(nodes[j], width, level, j, pos)
                    childrenPos.push([pos[0] - width/2, pos[1]-elem_height])
                }
                pos_x = step_x + (pos[0]-step_x)/2
                posArr.push(pos_x)
                if (level > 0) {
                    var parent = levelNodes[i]["parent"]
                    addEdges([pos_x - (elem_width * parent.keys.length + strokeAdd)/2, pos[1]-elem_height*2], childrenPos, level, unit["RC"]["Radius"])
                }
                step_x = pos[0] + elem_width
            }
            pos[1] -= elem_height*2
        }
    }

    add()
}

PrecompUtil.prototype._bTreeAnimation = function (items, parentComp, conf, layersCollecter) {
    // shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
    var elems = conf["elems"]
    function insert(elem) {
        // 插入数据的同时记录需要更新的节点信息
        precompUtil._bTreeInsert(items, parentComp, elem, conf, layersCollecter)
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

    for (var i = 0; i < elems.length; i++) {
        this._bTreeIndicatorResetPos(conf, precompUtil._btree.root, layersCollecter)
        var elem = elems[i]
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
        shareUtil.scenes[shareUtil.sName][shareUtil.shot]["time"] += 1
        if (i === 6) {
            break
        }
    }
    
    // var indicator = shareUtil.scenes[shareUtil.sName][shareUtil.shot]["misc"]["vectors"]["Indicator"]
    // var posKeyframes = indicator["keyframes"]["Transform.Position"]
    // var spatial = []
    // for (var i = 0; i < posKeyframes[0].length; i++) {
    //     spatial.push({"type": "HOLD"})
    // }
    // posKeyframes.push({"spatial": spatial})
    // shareUtil.configKeyframes(
    //     indicator["layer"],
    //     indicator["keyframes"]
    // )
}

PrecompUtil.prototype.bTree = function (items, parentComp, conf, layersCollecter) {
    this._btree = {
        "root": this._bTreeNode(true, 0, 0, null),
        "order": 4,
    }

    var comp = items.addComp(conf["layerName"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE);
    comp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])

    var unit = conf["unit"]
    var elems = conf["elems"]

    this._bTreeShowIndicator(false, conf)
    if (conf["animation"]) {
        layersCollecter["nodes"] = {}
        this._bTreeAnimation(items, comp, conf, layersCollecter["nodes"])
    } else {
        this._bTreeAdd(items, comp, elems, unit)
    }

    shareUtil.addLayer(parentComp, conf, comp)
    var indicator = this._bTreeIndicator(conf)
    indicator["layer"].moveToBeginning()
}

PrecompUtil.prototype.graph = function (nodeLayer, edgeLayer, elems) {

}

PrecompUtil.prototype.addOne = function (items, parentComp, conf, layersCollecter) {
    var comp;
    var type = conf["type"]
    layersCollecter[type] = {}
    if (type === "CODES") {
        comp = this.codes(parentComp, conf, layersCollecter[type])
    // } else if (conf["type"] === "MISCS") {
    //     comp = this.miscs(parentComp, conf, layersCollecter)
    } else if (type === "STACK") {
        comp = this.stack(parentComp, conf, layersCollecter[type])
    } else if (type === "QUEUE") {
        comp = this.queue(items, parentComp, conf, layersCollecter[type])
    } else if (type === "LINKED_LIST") {
        comp = this.linkedList(items, parentComp, conf, layersCollecter[type])
    } else if (type === "BINARY_TREE") {
        comp = this.binaryTree(items, parentComp, conf, layersCollecter[type])
    } else if (type === "B-TREE") {
        comp = this.bTree(items, parentComp, conf, layersCollecter[type])
    } else if (type === "GRAPH") {
        comp = this.graph(conf, layersCollecter[type])
    }
    return comp
}

PrecompUtil.prototype.addMany = function (items, parentComp, precomps, layersCollecter) {
    for (var i = 0; i < precomps.length; i++) {
        this.addOne(items, parentComp, precomps[i], layersCollecter)
    }
}

var precompUtil = new PrecompUtil();