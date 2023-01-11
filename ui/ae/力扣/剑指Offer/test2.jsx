#includepath "../../utils/jsx;";
#include "constants.jsx";
#include "json.jsx";
#include "animation.jsx";
#include "share.jsx";
#include "color.jsx";
#include "effects.jsx";
#include "presets.jsx";
#include "text.jsx";
#include "shape.jsx";
#include "precomp.jsx"


var project = app.project;
var mainComp = project.activeItem;

var layer = mainComp.layer(1)
var startPointProp = layer("Contents")("Rectangle 1")("Contents")("Gradient Fill 1")("Start Point")
var endPointProp = layer("Contents")("Rectangle 1")("Contents")("Gradient Fill 1")("End Point")
var opacityProp = layer("Contents")("Rectangle 1")("Contents")("Gradient Fill 1")("Opacity")
// var colors = layer("Contents")("Rectangle 1")("Contents")("Gradient Fill 1")("Colors").value

$.writeln(startPointProp.value)
$.writeln(endPointProp.value)
$.writeln(opacityProp.value)
// $.writeln(colors)
$.writeln("=========================================")
startPointProp.setValue([10, 10])
endPointProp.setValue([20, 20])
opacityProp.setValue(55)
$.writeln(startPointProp.value)
$.writeln(endPointProp.value)
$.writeln(opacityProp.value)