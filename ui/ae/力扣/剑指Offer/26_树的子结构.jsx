newComp = app.project.items.addComp('test', 1920, 1080, 1, 5, 30)
parentShapeLayer = newComp.layers.addShape()
// var methods = parentShapeLayer.reflect.methods;
// for (var i = 0; i < methods.length; i++) {
//   $.writeln('method: ' + methods[i].name + ', arguments: ' + methods[i].arguments.toString());
// }
for (var i = 0; i < 5; i++) {
    parentShapeLayer.property('Contents').addProperty('ADBE Vector Shape - Ellipse')
}
