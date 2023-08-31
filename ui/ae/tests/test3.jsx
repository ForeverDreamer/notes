// for (var i = 1; i <= project.items.length; i++) {
//     var item = project.items[i];
//     $.writeln(item.name)
//     $.writeln(item.typeName)
//     $.writeln(item.parentFolder.name)
//     $.writeln("================")
// }

var item = app.project.activeItem
// $.writeln(item.name)
// $.writeln(item.typeName)
// $.writeln(item.parentFolder.name)
// var layer = item.layer("idx_pl")
// $.writeln(layer("Source Text").value)
// $.writeln(layer("Text")("Source Text").value)
// $.writeln(layer("Opacity").value)
// $.writeln(layer("Transform")("Opacity").value)
var layer = item.layer("主函数选中框")
$.writeln(layer("Anchor Point").value)
$.writeln(layer("Position").value)
$.writeln(layer("Scale").value)
$.writeln(layer("Rotation").value)
$.writeln(layer("Opacity").value)