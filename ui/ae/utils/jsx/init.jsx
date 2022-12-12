// 路径从tmp/script.jsx开始算
#includepath "../utils/jsx";
#include "constants.jsx";
#include "json.jsx";
#include "color.jsx";
#include "shape.jsx";
#include "text.jsx";
#include "share.jsx";
#include "precomp.jsx";
#include "animation.jsx";
#include "effects.jsx";
#include "presets.jsx";


app.purge(PurgeTarget.ALL_CACHES);
var project = app.project;
shareUtil.delItems(project.items)
var mainComp = project.activeItem;

if (mainComp == null || !(mainComp instanceof CompItem)) {
    mainComp = project.items.addComp("Main", 1920, 1080, 1, 300, 30);
}
mainComp.openInViewer();

// var conf = jsonUtil.read(CONF_FILE);
var bgLayer = mainComp.layers.addSolid([1, 1, 1], "BG", 1920, 1080, 1);
// bgLayer.threeDLayer = true
bgLayer.moveToEnd()