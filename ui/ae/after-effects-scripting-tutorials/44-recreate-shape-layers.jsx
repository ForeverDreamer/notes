var project = app.project;
var comp = project.activeItem;

app.beginUndoGroup("Process");

if (comp === null) {
    comp = project.items.addComp("Test Comp", 1920, 1080, 1, 10, 30);
}

comp.openInViewer();
var shapeLayer = comp.layers.addShape();
shapeLayer.name = "Hexagon";
var hexagonGroup = shapeLayer.property("Contents").addProperty("ADBE Vector Group");
hexagonGroup.name = "Hexagon";
var pathGroup = shapeLayer.property("Contents").property("Hexagon").property("Contents").addProperty("ADBE Vector Shape - Star")
pathGroup.property("Type").setValue(2);
pathGroup.property("Points").setValue(6);
var strokeGroup = shapeLayer.property("Contents").property("Hexagon").property("Contents").addProperty("ADBE Vector Graphic - Stroke")
var fillGroup = shapeLayer.property("Contents").property("Hexagon").property("Contents").addProperty("ADBE Vector Graphic - Fill")

app.endUndoGroup();
