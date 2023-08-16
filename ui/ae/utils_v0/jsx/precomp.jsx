function PrecompUtil() {
    this.queueLayers = {}
}

PrecompUtil.prototype.misc = function (items, parentComp, misc) {
    for (var i = 0; i < misc.length; i++) {
        var conf = misc[i]
        var miscFolder = items.addFolder(conf["layerName"])
        var miscComp = miscFolder.items.addComp(conf["layerName"], conf['width'], conf['height'], PIXEL_ASPECT, conf['duration'], FRAME_RATE);
        miscComp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])

        if (conf["texts"]) {
            textUtil.addMany(miscComp, conf["texts"])
        }
        if (conf["vectors"]) {
            shapeUtil.create_vectors(miscComp, conf['vectors'])
        }
        if (conf["shapes"]) {
            shapeUtil.create_many(miscComp, conf["shapes"])
        }
        if (conf["precomps"]) {
            this.createMany(miscFolder.items, miscComp, conf['precomps'])
        }
        if (conf['codes']) {
            this.create_codes(miscFolder.items, miscComp, conf['codes'])
        }
        if (conf["misc"]) {
            this.misc(miscFolder.items, miscComp, conf['misc'])
        }
        shareUtil.addLayer(parentComp, conf, miscComp);
    }
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

PrecompUtil.prototype._bTreeElems = function (items, parentComp, conf) {
    var unit = conf["unit"]
    var elems = conf["elems"];
    var nodePos = [conf["width"]/2, unit["pathGroup"]["size"][1]/2]
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

PrecompUtil.prototype._bTreeInsert = function (elem, conf) {
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

PrecompUtil.prototype._bTreeNode = function (leaf) {
    return {"leaf": leaf, "keys": [], "children": []}
}

PrecompUtil.prototype._bTreeCreate = function () {
    // 层序遍历
}

PrecompUtil.prototype._bTreeUpdate = function () {
    
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
    var nodePos = [conf["width"]/2, unit["pathGroup"]["Size"][1]/2]

    // if (conf["levels"]) {
    //     this._bTreeLevels(items, parentComp, conf)
    // }
    for (var i = 0; i < elems.length; i++) {
        this._bTreeInsert(elems[i], conf)
    }
    if (!conf["animation"]) {
        this._bTreeCreate()
    }

    shareUtil.addLayer(parentComp, conf, comp)
}

PrecompUtil.prototype.graph = function (nodeLayer, edgeLayer, elems) {

}

var precompUtil = new PrecompUtil();