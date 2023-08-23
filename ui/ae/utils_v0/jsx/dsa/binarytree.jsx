function BinaryTree() {

}

BinaryTree.prototype.add = function (conf, parentComp, parentObj) {
    var comp = parentObj.items.addComp(conf["layerName"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE);
    comp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])
    comp.resolutionFactor = RESOLUTION_FACTOR

    var elems = conf["elems"];

    var selected = conf["node"]["selected"];
    var drop = conf["node"]["drop"];
    var nodeShape = conf["node"]["shape"];
    var nodePath = conf["node"]["path"];

    var edgeShape = conf["edge"]["shape"];

    var edgePath = conf["edge"]["path"];

    const NODE_SCALE = nodeShape["Scale"][0] / 100
    const ROTATION = edgeShape["Rotation"]

    var times = [0, 0.5]
    const STEP = [0.5, 0.5]
    const NODE_PREFIX = "Node"
    const EDGE_PREFIX = "Edge"

    const ROOT_NODE_POS = conf["rootNodePos"]
    const EDGE_OFFSET = 45 * NODE_SCALE
    const HORIZONTAL_DIST = 160 * NODE_SCALE
    const VERTICAL_DIST = 240 * NODE_SCALE

    // this.verticalDist *= NODE_SCALE
    const nodeLayers = {}
    const edgeLayers = {}

    if (nodePath) {
        var offset = nodePath["Trim Paths"]["Offset"]
    }

    function addNode(elem, parentNode, direction, selected, drop, upEdge) {
        var key = elem["key"]
        var layerName = elem["layerName"] ? elem["layerName"] : key

        if (parentNode) {
            var parentPos = parentNode["Position"]
        }

        switch (direction) {
            case 'left':
                nodeShape["Position"] = [parentPos[0] - HORIZONTAL_DIST, parentPos[1] + VERTICAL_DIST]
                if (nodePath) {
                    nodePath["Trim Paths"]["Offset"] = offset
                }
                break;
            case 'right':
                nodeShape["Position"] = [parentPos[0] + HORIZONTAL_DIST, parentPos[1] + VERTICAL_DIST]
                if (nodePath) {
                    nodePath["Trim Paths"]["Offset"] = -offset
                }
                break;
            case null:
                nodeShape["Position"] = ROOT_NODE_POS
                break;
            default:
                throw new TypeError("参数[direction]类型错误")
        }

        var shapeKeyframes = {
            "Transform.Opacity": [times, [0, 100], { "temporal": [[[0, 0.1], [200, 100]], [[0, 75], [0, 0.1]]] }]
        }
        nodeShape["layerName"] = NODE_PREFIX + "." + "Shape" + "." + layerName
        var shapeTextProps = { "text": key }
        if (js_bool(conf["animation"])) {
            nodeShape["keyframes"] = shapeKeyframes
            shapeTextProps["keyframes"] = shapeKeyframes
            times += STEP
        }
        if (elem["keyframes"]) {
            nodeShape["keyframes"] = elem["keyframes"]
            shapeTextProps["keyframes"] = elem["keyframes"]
            if (upEdge) {
                shareUtil.configKeyframes(upEdge["shapeLayer"], elem["keyframes"])
            }
        }
        var shapeLayer = shareUtil.addLayer(nodeShape, comp);

        if (selected) {
            selected["Position"] = nodeShape["Position"]
            selected["layerName"] = NODE_PREFIX + "." + "Selected" + "." + layerName
            selected["keyframes"] = elem["selectedKeyframes"]
            if (elem["Color"]) {
                selected["Fill"]["Color"] = colorUtil.hexToRgb1(elem["Color"])
            }
            var selectedLayer = shapeUtil.create_one(comp, selected)
            // selectedLayers[selected["layerName"]] = selectedLayer
        }
        shapeTextProps["layerName"] = NODE_PREFIX + "." + "Text" + "." + layerName
        var shapeTextLayer = textUtil.overlay(shapeTextProps, comp, shapeLayer);

        if (drop) {
            // drop["Fill"]["Color"] = drop["Fill"]["Color"]
            drop["layerName"] = NODE_PREFIX + "." + "Drop" + "." + layerName
            drop["Position"] = nodeShape["Position"]
            var dropLayer = shapeUtil.create_one(comp, drop)
            // dropLayers[drop["layerName"]] = dropLayer
            var dropTextLayer = textUtil.overlay(
                { "layerName": NODE_PREFIX + "." + "Drop" + '.' + "Text" + "." + key,  "text": key, "Opacity": 0 },
                comp, dropLayer
            )
        }

        if (nodePath) {
            nodePath["pathGroup"]["type"] = "Group"
            nodePath["layerName"] = NODE_PREFIX + "." + "Path" + "." + layerName;
            // path["Position"] = shapeLayer("Transform")("Position").value.slice(0, 2)
            nodePath["Position"] = nodeShape["Position"]
            var pathLayer = shapeUtil.create_one(comp, nodePath)
            // nodePathLayers.push(pathLayer)
        }

        nodeLayers[layerName] = {
            "layerName": layerName,
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
            parentNode[direction] = nodeLayers[layerName]
        }

        return nodeLayers[layerName]
    }

    function addEdge(elem, upNode, direction) {
        var key = elem["key"]
        var layerName = elems["layerName"] ? elems["layerName"] : key
        var upLayerName = upNode["layerName"];
        var upPos = upNode["Position"];

        if (direction === "left") {
            edgeShape["Position"] = [upPos[0] - EDGE_OFFSET, upPos[1] + EDGE_OFFSET]
            edgeShape["Rotation"] = ROTATION
            if (edgePath) {
                edgePath["Rotation"] = 0
            }
        } else if (direction === "right") {
            edgeShape["Position"] = [upPos[0] + EDGE_OFFSET, upPos[1] + EDGE_OFFSET]
            edgeShape["Rotation"] = -ROTATION
            if (edgePath) {
                edgePath["Rotation"] = -ROTATION * 2
            }
        } else {
            throw new TypeError("参数[direction]类型错误")
        }

        var edgeKeyframes = {
            // "Transform.Scale": [times, [[0, 0, 0], edgeShape["Scale"]], {"temporal": [[[0, 0.1], [200, 100]], [[0, 75], [0, 0.1]]]}]
            "Transform.Scale": [times, [[0, 0, 0], edgeShape["Scale"]], { "temporal": [[[0, 0.1], [300, 100]], [[0, 75], [0, 0.1]]] }]
        }
        edgeShape["layerName"] = EDGE_PREFIX + "." + direction + "." + "Shape" + "." + upLayerName + '.' + layerName
        if (js_bool(conf["animation"])) {
            edgeShape["keyframes"] = edgeKeyframes
            times += STEP
        }
        var shapeLayer = shareUtil.addLayer(edgeShape, comp)

        if (edgePath) {
            edgePath["pathGroup"]["type"] = "Group"
            edgePath["layerName"] = EDGE_PREFIX + "." + direction + "." + "Path" + "." + upLayerName + '.' + layerName
            edgePath["Position"] = edgeShape["Position"]
            var pathLayer = shapeUtil.create_one(comp, edgePath)
        }

        edgeLayers[layerName] = {
            "layerName": layerName,
            "key": key,
            "shapeLayer": shapeLayer, "pathLayer": pathLayer,
            "nodeLayers": {
                "up": upNode ? upNode : null,
                "down": null,
            }
        }
        upNode["edgeLayers"]["down"][direction] = edgeLayers[layerName]

        return edgeLayers[layerName]
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

    conf["item"] = comp
    var compLayer = shareUtil.addLayer(conf, parentComp)
    return { 'comp': comp, 'compLayer': compLayer };
}

var binaryTree = new BinaryTree();