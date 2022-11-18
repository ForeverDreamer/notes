function importAsType(type){
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
