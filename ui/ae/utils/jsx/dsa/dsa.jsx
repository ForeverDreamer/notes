function Dsa() {
}

Dsa.prototype.addOne = function (conf, parentComp, parentObj) {
    var comp;
    if (conf["type"] === "STACK") {
        comp = stack.add(conf, parentComp, parentObj)
    } else if (conf["type"] === "QUEUE") {
        comp = queue.add(conf, parentComp, parentObj)
    } else if (conf["type"] === "LINKED_LIST") {
        comp = linkedList.add(conf, parentComp, parentObj)
    } else if (conf["type"] === "BINARY_TREE") {
        comp = binaryTree.add(conf, parentComp, parentObj)
    } else if (conf["type"] === "B-TREE") {
        comp = bTree.add(conf, parentComp, parentObj)
    } else if (conf["type"] === "GRAPH") {
        comp = graph.add(conf, parentComp, parentObj)
    }
    // if (conf["children"]) {
    //     for (var j = 0; j < conf["children"].length; j++) {
    //         this.addOne(items, comp, conf["children"][j])
    //     }
    // }
    return comp
}

Dsa.prototype.addMany = function (dsa, parentComp, parentObj) {
    for (var i = 0; i < dsa.length; i++) {
        this.addOne(dsa[i], parentComp, parentObj)
    }
}

var dsa = new Dsa();