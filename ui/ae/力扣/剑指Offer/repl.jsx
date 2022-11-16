var project = app.project;
var comp = project.activeItem;
var layer = comp.layer(1)

$.writeln(layer.property("Contents").property("Hexagon").property("Contents").property(2).matchName);