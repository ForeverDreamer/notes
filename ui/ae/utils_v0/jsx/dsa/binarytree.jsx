function BinaryTree() {
    this.nodeLayers = {}
    this.edgeLayers = {}
    this.times = [0, 0.5]
    this.step = [0.5, 0.5]
    this.rootNodePos = [392.5, 75]
    this.horizontalDist = 160
    this.edgeOffset = 45
    this.verticalDist = 240
    this.NODE_PREFIX = "Node"
    this.EDGE_PREFIX = "Edge"
}

BinaryTree.prototype.add = function (items, parentComp, conf) {
    var comp = items.addComp(conf["layerName"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE);
    comp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])

    var elems = conf["elems"];

    var selected = conf["node"]["selected"];
    var drop = conf["node"]["drop"];
    var nodeShape = conf["node"]["shape"];
    var nodePath = conf["node"]["path"];

    var edgeShape = conf["edge"]["shape"];
    var edgePath = conf["edge"]["path"];

    var nodeScale = nodeShape["Scale"][0] / 100
    this.rootNodePos *= nodeScale
    this.edgeOffset *= nodeScale
    this.horizontalDist *= nodeScale
    this.verticalDist *= nodeScale

    if (nodePath) {
        var offset = nodePath["Trim Paths"]["Offset"]
    }
    this.rotation = edgeShape["Rotation"]

    function addNode(elem, parentNode, direction, selected, drop, upEdge) {
        var key = elem["key"]

        if (parentNode) {
            var parentPos = parentNode["Position"]
        }

        switch (direction) {
            case 'left':
                nodeShape["Position"] = [parentPos[0] - binaryTree.horizontalDist, parentPos[1] + binaryTree.verticalDist]
                if (nodePath) {
                    nodePath["Trim Paths"]["Offset"] = offset
                }
                break;
            case 'right':
                nodeShape["Position"] = [parentPos[0] + binaryTree.horizontalDist, parentPos[1] + binaryTree.verticalDist]
                if (nodePath) {
                    nodePath["Trim Paths"]["Offset"] = -offset
                }
                break;
            case null:
                nodeShape["Position"] = binaryTree.rootNodePos
                break;
            default:
                throw new TypeError("参数[direction]类型错误")
        }

        var shapeKeyframes = {
            "Transform.Opacity": [binaryTree.times, [0, 100], { "temporal": [[[0, 0.1], [200, 100]], [[0, 75], [0, 0.1]]] }]
        }
        nodeShape["layerName"] = binaryTree.NODE_PREFIX + "." + "Shape" + "." + key
        var shapeTextProps = { "text": key }
        if (js_bool(conf["animation"])) {
            nodeShape["keyframes"] = shapeKeyframes
            shapeTextProps["keyframes"] = shapeKeyframes
            binaryTree.times += binaryTree.step
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
            selected["layerName"] = binaryTree.NODE_PREFIX + "." + "Selected" + "." + key
            selected["keyframes"] = elem["selectedKeyframes"]
            if (elem["Color"]) {
                selected["Fill"]["Color"] = colorUtil.hexToRgb1(elem["Color"])
            }
            var selectedLayer = shapeUtil.create_one(comp, selected)
            // selectedLayers[selected["layerName"]] = selectedLayer
        }
        var shapeTextLayer = textUtil.overlay(comp, shapeLayer, binaryTree.NODE_PREFIX + "." + "Text" + "." + key, shapeTextProps);

        if (drop) {
            // drop["Fill"]["Color"] = drop["Fill"]["Color"]
            drop["layerName"] = binaryTree.NODE_PREFIX + "." + "Drop" + "." + key
            drop["Position"] = nodeShape["Position"]
            var dropLayer = shapeUtil.create_one(comp, drop)
            // dropLayers[drop["layerName"]] = dropLayer
            var dropTextLayer = textUtil.overlay(comp, dropLayer, binaryTree.NODE_PREFIX + "." + "Drop" + '.' + "Text" + "." + key, { "text": key, "Opacity": 0 });
        }

        if (nodePath) {
            nodePath["pathGroup"]["type"] = "Group"
            nodePath["layerName"] = binaryTree.NODE_PREFIX + "." + "Path" + "." + key;
            // path["Position"] = shapeLayer("Transform")("Position").value.slice(0, 2)
            nodePath["Position"] = nodeShape["Position"]
            var pathLayer = shapeUtil.create_one(comp, nodePath)
            // nodePathLayers.push(pathLayer)
        }

        binaryTree.nodeLayers[key] = {
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
            parentNode[direction] = binaryTree.nodeLayers[key]
        }

        return binaryTree.nodeLayers[key]
    }

    function addEdge(elem, upNode, direction) {
        var key = elem[0]
        var upKey = upNode["key"];
        var upPos = upNode["Position"];

        if (direction === "left") {
            edgeShape["Position"] = [upPos[0] - binaryTree.edgeOffset, upPos[1] + binaryTree.edgeOffset]
            edgeShape["Rotation"] = binaryTree.rotation
            if (edgePath) {
                edgePath["Rotation"] = 0
            }
        } else if (direction === "right") {
            edgeShape["Position"] = [upPos[0] + binaryTree.edgeOffset, upPos[1] + binaryTree.edgeOffset]
            edgeShape["Rotation"] = -binaryTree.rotation
            if (edgePath) {
                edgePath["Rotation"] = -binaryTree.rotation * 2
            }
        } else {
            throw new TypeError("参数[direction]类型错误")
        }

        var edgeKeyframes = {
            // "Transform.Scale": [times, [[0, 0, 0], edgeShape["Scale"]], {"temporal": [[[0, 0.1], [200, 100]], [[0, 75], [0, 0.1]]]}]
            "Transform.Scale": [binaryTree.times, [[0, 0, 0], edgeShape["Scale"]], { "temporal": [[[0, 0.1], [300, 100]], [[0, 75], [0, 0.1]]] }]
        }
        edgeShape["layerName"] = binaryTree.EDGE_PREFIX + "." + direction + "." + "Shape" + "." + upKey + '.' + key
        if (js_bool(conf["animation"])) {
            edgeShape["keyframes"] = edgeKeyframes
            binaryTree.times += binaryTree.step
        }
        var shapeLayer = shareUtil.addLayer(comp, edgeShape)

        if (edgePath) {
            edgePath["pathGroup"]["type"] = "Group"
            edgePath["layerName"] = binaryTree.EDGE_PREFIX + "." + direction + "." + "Path" + "." + upKey + '.' + key
            edgePath["Position"] = edgeShape["Position"]
            var pathLayer = shapeUtil.create_one(comp, edgePath)
        }

        binaryTree.edgeLayers[key] = {
            "key": key,
            "shapeLayer": shapeLayer, "pathLayer": pathLayer,
            "nodeLayers": {
                "up": upNode ? upNode : null,
                "down": null,
            }
        }
        upNode["edgeLayers"]["down"][direction] = binaryTree.edgeLayers[key]

        return binaryTree.edgeLayers[key]
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

var binaryTree = new BinaryTree();