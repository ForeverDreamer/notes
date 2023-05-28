#includepath "./utils/jsx";
#include "constants.jsx";
#include "misc.jsx";
#include "shape.jsx";

miscUtil.closeAllDocuments()
var doc = miscUtil.addDocument({'size': {'width': 1920, 'height': 1080}})
var shapes = [
	{'type': SHAPE_TYPES[0], 'top': 540, 'left': 100, 'width': 200, 'height': 100, 'reversed': false},
	{'type': SHAPE_TYPES[1], 'centerX': 400, 'centerY': 540, 'radius': 100, 'sides': 8, 'reversed': false},
	{'type': SHAPE_TYPES[2], 'top': 540, 'left': 600, 'width': 200, 'height': 100, 'reversed': false},
	{'type': SHAPE_TYPES[3], 'top': 540, 'left': 900, 'width': 200, 'height': 100, 'horizontalRadius': 15, 'verticalRadius': 20, 'reversed': false},
	{'type': SHAPE_TYPES[4], 'centerX': 1200, 'centerY': 540, 'radius': 100, 'innerRadius': 40, 'points': 5, 'reversed': false},
]
for (var i=0; i<shapes.length; i++) {
	shapeUtil.add(doc, shapes[i])
}

