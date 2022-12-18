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
var layer = comp.layer(1)

shapeUtil.add(comp, "Node.Drop.15", {"Fill": {"Color": colorUtil.hexToRgb1("#7EE787")}})