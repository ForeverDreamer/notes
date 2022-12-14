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
var comp = project.activeItem;
var shapeLayer = comp.layer(1)
// $.writeln(colorProp.name);
// $.writeln(shapeLayer("Effects")("Drop Shadow")("Softness").value)
// colorProp.setValue([0.01, 0.37254901960784, 0.72156862745098])

// for (var i = 1; i <= positionProp.numKeys; i++) {
//     positionProp.removeKey(i)
// }

// app.cancelTask(4)

// $.writeln(app.project.file.fsName)


// Eval Error (#4): "Unterminated string constant" in 'D:\data_files\notes\ui\ae\utils\jsx\precomp.jsx' [58:30] in host 'aftereffects-18.0 (main)'.
// 注意字符串拼接时的引号问题，否则会导致莫名其妙的错误
// "var comp = items.addComp("二叉树." + conf["name"], conf["width"], conf["height"], PIXEL_ASPECT, conf["duration"], FRAME_RATE);" 