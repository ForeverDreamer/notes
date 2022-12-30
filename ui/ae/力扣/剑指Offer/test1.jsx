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
var layer = mainComp.layer(16)
// var path = layer("Contents")("Rectangle 1")("Contents")("Path 1")("Path").value

for (var i = 1; i <= 3; i++) {
    $.writeln("=========================================")
    var path = layer("Masks")("Mask "+i)("Mask Path").value
    $.writeln(path.vertices)
    $.writeln(path.inTangents)
    $.writeln(path.outTangents)
}

