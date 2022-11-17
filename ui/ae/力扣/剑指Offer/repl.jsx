var project = app.project;
var comp = project.activeItem;

var textLayer = comp.layer(1)
var shapeLayer = comp.layer(2)

// $.writeln(textLayer("Transform")("Position").value);
$.writeln(shapeLayer("Transform")("Position").value);