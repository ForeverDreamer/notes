function animationUtil() {}

AnimationUtil.prototype.traverseBinaryTree = function(nodeLayer, edgeLayer, elems, order) {
	switch (order) {
		case 'PRE':
			importOptions.importAs = ImportAsType.COMP_CROPPED_LAYERS;
			break;
		case 'IN':
			importOptions.importAs = ImportAsType.PROJECT;
			break;
		case 'POST':
			importOptions.importAs = ImportAsType.COMP;
			break;
		default:
            // LEVEL
			importOptions.importAs = ImportAsType.FOOTAGE;
	}
	return project.importFile(importOptions);
}

var animationUtil = new AnimationUtil();