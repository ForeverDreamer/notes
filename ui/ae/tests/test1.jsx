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

var layer = mainComp.layer(4)
// var path = layer("Contents")("Rectangle 1")("Contents")("Path 1")("Path").value
masks_layer_4 = []
for (var i = 1; i <= 5; i++) {
    $.writeln("=========================================")
    // $.writeln(layer("Masks")("Mask "+i)("Mask Opacity").value)
    var path = layer("Masks")("Mask "+i)("Mask Path").value
    $.writeln(path.vertices)
    $.writeln(path.inTangents)
    $.writeln(path.outTangents)
    var mask = {
        "vertices": path.vertices,
        "inTangents": path.inTangents,
        "outTangents": path.outTangents,
        "inverted": layer("Masks")("Mask "+i).inverted,
    }
    masks_layer_4.push(mask)
}


// var layer = mainComp.layer(3)
// masks_layer_3 = []
// for (var i = 1; i <= 3; i++) {
//     $.writeln("=========================================")
//     // $.writeln(layer("Masks")("Mask "+i)("Mask Opacity").value)
//     var path = layer("Masks")("Mask "+i)("Mask Path").value
//     $.writeln(path.vertices)
//     $.writeln(path.inTangents)
//     $.writeln(path.outTangents)
//     var mask = {
//         "vertices": path.vertices,
//         "inTangents": path.inTangents,
//         "outTangents": path.outTangents,
//         "inverted": layer("Masks")("Mask "+i).inverted,
//     }
//     masks_layer_3.push(mask)
// }

// var layer = mainComp.layer(2)
// masks_layer_2 = []
// for (var i = 1; i <= 3; i++) {
//     $.writeln("=========================================")
//     // $.writeln(layer("Masks")("Mask "+i)("Mask Opacity").value)
//     var path = layer("Masks")("Mask "+i)("Mask Path").value
//     $.writeln(path.vertices)
//     $.writeln(path.inTangents)
//     $.writeln(path.outTangents)
//     var mask = {
//         "vertices": path.vertices,
//         "inTangents": path.inTangents,
//         "outTangents": path.outTangents,
//         "inverted": layer("Masks")("Mask "+i).inverted,
//     }
//     masks_layer_2.push(mask)
// }

jsonUtil.write(
    BASE_DIR + '力扣/剑指Offer/07_重建二叉树/conf_utils/scenes/s5.json', 
    // {"4": masks_layer_4, "3": masks_layer_3, "2": masks_layer_2},
    {"4": masks_layer_4}
)
