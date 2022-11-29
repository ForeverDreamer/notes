function ShareUtil() { }

ShareUtil.prototype.importAsType = function (type) {
  var t;
  switch (type) {
    case 'COMP_CROPPED_LAYERS':
      t = ImportAsType.COMP_CROPPED_LAYERS;
      break;
    case 'PROJECT':
      t = ImportAsType.PROJECT;
      break;
    case 'COMP':
      t = ImportAsType.COMP;
      break;
    default:
      t = ImportAsType.FOOTAGE;
  }
  return t
}

ShareUtil.prototype.delItems = function (items) {
  numItems = items.length
  for (var i = numItems; i >= 1; i--) {
    item = items[i]
    // if (item instanceof FolderItem) {
    //     delItems(item.items);
    // } else {
    //     item.remove()
    // }
    item.remove()
  }
}

ShareUtil.prototype.configProps = function (props) {
  if (!props) {
    return
  }
  for (var k in props) {
    var propChain = k.split(".")
    var prop = layer(propChain[0]);
    for (var i = 1; i < propChain.length; i++) {
      prop = prop(propChain[i])
    }
    prop.setValue(props[k]);
  }
}

ShareUtil.prototype.configKeyframes = function (keyframes) {
  if (!keyframes) {
    return
  }
  for (var k in keyframes) {
    var propChain = k.split(".")
    var prop = layer(propChain[0]);
    for (var i = 1; i < propChain.length; i++) {
        prop = prop(propChain[i])
    }
    var numKeys = prop.numKeys 
    for (var i = numKeys; i >= 1; i--) {
        prop.removeKey(i)
    }
    prop.setValuesAtTimes(keyframes[k]["times"], keyframes[k]["values"]);
}
}

var shareUtil = new ShareUtil();
// if (typeof shareUtil === "undefined") {
//     var shareUtil = new ShareUtil();
// }
