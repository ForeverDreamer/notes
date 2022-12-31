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
precomps_2_masks = []
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
    precomps_2_masks.push(mask)
}

// var layer = mainComp.layer(17)
// precomps_1_masks = []
// for (var i = 1; i <= 1; i++) {
//     var path = layer("Masks")("Mask "+i)("Mask Path").value
//     var mask = {
//         "vertices": path.vertices,
//         "inTangents": path.inTangents,
//         "outTangents": path.outTangents,
//         "inverted": layer("Masks")("Mask "+i).inverted,
//     }
//     precomps_1_masks.push(mask)
// }

// var layer = mainComp.layer(18)
// precomps_0_masks = []
// for (var i = 1; i <= 1; i++) {
//     var path = layer("Masks")("Mask "+i)("Mask Path").value
//     var mask = {
//         "vertices": path.vertices,
//         "inTangents": path.inTangents,
//         "outTangents": path.outTangents,
//         "inverted": layer("Masks")("Mask "+i).inverted,
//     }
//     precomps_0_masks.push(mask)
// }

jsonUtil.write(
    BASE_DIR + '力扣/剑指Offer/07_重建二叉树/conf_utils/scenes/s5.json', 
    [
        {
            "precomps": {
                // 0:{"Masks": precomps_0_masks}, 
                // 1:{"Masks": precomps_1_masks}, 
                2:{"Masks": precomps_2_masks}
            }
        },
    ]
)
