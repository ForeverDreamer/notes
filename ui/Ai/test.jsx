#includepath "./utils/jsx";
#include "constants.jsx";
#include "misc.jsx";
#include "shape.jsx";

miscUtil.closeAllDocuments()
var doc = miscUtil.addDocument({'size': {'width': 1920, 'height': 1080}})
var shapes = [
	{'type': SHAPE_TYPES[0], 'top': 540, 'left': 100, 'width': 200, 'height': 100, 'reversed': false},
	{'type': SHAPE_TYPES[1], 'centerX': 400, 'centerY': 540, 'radius': 100, 'sides': 3, 'reversed': false},
	{'type': SHAPE_TYPES[2], 'top': 540, 'left': 600, 'width': 200, 'height': 100, 'reversed': false},
	{'type': SHAPE_TYPES[3], 'top': 540, 'left': 900, 'width': 200, 'height': 100, 'horizontalRadius': 15, 'verticalRadius': 20, 'reversed': false},
	{'type': SHAPE_TYPES[4], 'centerX': 1200, 'centerY': 540, 'radius': 100, 'innerRadius': 40, 'points': 5, 'reversed': false},
]

paths = []
for (var i=0; i<shapes.length; i++) {
	paths.push(shapeUtil.add(doc, shapes[i]))
}
for (var i=0; i<paths.length; i++) {
	$.writeln("i=" + i)
	for (var j=0; j<paths[i].pathPoints.length; j++) {
		$.writeln(paths[i].pathPoints[j].anchor)
		$.writeln(paths[i].pathPoints[j].leftDirection)
		$.writeln(paths[i].pathPoints[j].rightDirection)
		$.writeln(paths[i].pathPoints[j].pointType)
	}
}

if (app.documents.length > 0) {
	var doc = app.activeDocument;
  
	var line = doc.pathItems.add();
	line.stroked = true;
	line.setEntirePath([
		[220, 475],
		[375, 300]
	]);
  
	// 通过ui界面创建好之后，导出pathPoints保存，方便用代码快速重建和修改局部属性
	// Append another point to the line
	var newPoint = doc.pathItems[0].pathPoints.add();
	newPoint.anchor = Array(220, 300);
	newPoint.leftDirection = newPoint.anchor;
	newPoint.rightDirection = newPoint.anchor;
	newPoint.pointType = PointType.CORNER;
	for (var i=0; i<line.pathPoints.length; i++) {
		$.writeln(line.pathPoints[i].anchor)
		$.writeln(line.pathPoints[i].leftDirection)
		$.writeln(line.pathPoints[i].rightDirection)
		$.writeln(line.pathPoints[i].pointType)
	}
}

if (app.documents.length > 0) {
	// Create a color for both ends of the gradient
	var startColor = new RGBColor();
	startColor.red = 0;
	startColor.green = 100;
	startColor.blue = 255;
  
	var endColor = new RGBColor();
	endColor.red = 220;
	endColor.green = 0;
	endColor.blue = 100;
  
	// Create a new gradient
	// A new gradient always has 2 stops
	var newGradient = app.activeDocument.gradients.add();
	newGradient.name = "NewGradient";
	newGradient.type = GradientType.LINEAR;
  
	// Modify the first gradient stop
	newGradient.gradientStops[0].rampPoint = 30;
	newGradient.gradientStops[0].midPoint = 60;
	newGradient.gradientStops[0].color = startColor;
  
	// Modify the last gradient stop
	newGradient.gradientStops[1].rampPoint = 80;
	newGradient.gradientStops[1].color = endColor;
  
	// construct an Illustrator.GradientColor object referring to the newly created gradient
	var colorOfGradient = new GradientColor();
	colorOfGradient.gradient = newGradient;
  
	// get first path item, apply new gradient as its fill
	var topPath = app.activeDocument.pathItems[0];
	topPath.filled = true;
	topPath.fillColor = colorOfGradient;
  }

app.activeDocument.pathItems[0].selected = true
//   app.executeMenuCommand("Live Zig Zag");
xmlstring = '<LiveEffect name="Adobe Offset Path"><Dict data="R mlim 4 R ofst 20 I jntp 2"/></LiveEffect>';
 
app.activeDocument.pathItems[0].applyEffect(xmlstring);