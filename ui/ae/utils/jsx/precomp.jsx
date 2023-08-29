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