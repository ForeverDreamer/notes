function Dsa() {
}

Dsa.prototype.addOne = function (items, parentComp, conf) {
    var comp;
    if (conf["type"] === "STACK") {
        comp = stack.add(parentComp, conf)
    } else if (conf["type"] === "QUEUE") {
        comp = queue.add(items, parentComp, conf)
    } else if (conf["type"] === "LINKED_LIST") {
        comp = linkedList.add(items, parentComp, conf)
    } else if (conf["type"] === "BINARY_TREE") {
        comp = binaryTree.add(items, parentComp, conf)
    } else if (conf["type"] === "B-TREE") {
        comp = bTree.add(items, parentComp, conf)
    } else if (conf["type"] === "GRAPH") {
        comp = graph.add(conf)
    }
    if (conf["children"]) {
        for (var j = 0; j < conf["children"].length; j++) {
            this.addOne(items, comp, conf["children"][j])
        }
    }
    return comp
}

Dsa.prototype.addMany = function (items, parentComp, dsa) {
    for (var i = 0; i < dsa.length; i++) {
        this.addOne(items, parentComp, dsa[i])
    }
}

var dsa = new Dsa();