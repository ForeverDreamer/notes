function ShareUtil() {}

ShareUtil.prototype.importAsType = function(type) {
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

ShareUtil.prototype.delItems = function(items) {
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

if (typeof shareUtil === "undefined") {
    const shareUtil = new ShareUtil();
}
