#includepath "../../../../utils_v0/jsx";
#include "json.jsx";
var BASE_DIR = "D:/data_files/notes/ui/Ae/"
var conf = jsonUtil.read(BASE_DIR + "力扣/剑指Offer/07_重建二叉树/conf.json");
#include "constants.jsx";
#include "color.jsx";
#include "text.jsx";
#include "shape.jsx";
#include "share.jsx";
#include "effects.jsx";
#include "presets.jsx";
#include "camera.jsx";
#include "comp.jsx";
#include "dsa/binarytree.jsx"
#include "dsa/codes.jsx"
#include "dsa/queue.jsx"
#include "dsa/stack.jsx"
#include "dsa/dsa.jsx"
#include "utils.jsx"


// 字幕
var mainComp = shareUtil.findItemByName("Main")
var opacityKeyframes = {
    'Opacity': [[260, 260.1, 278], [100, 0, 100]]
}
var subtitlesCnLayer = mainComp.layer("字幕cn")
shareUtil.configKeyframes(subtitlesLayer, opacityKeyframes)
var subtitlesEnLayer = mainComp.layer("字幕en")
shareUtil.configKeyframes(subtitlesLayer, opacityKeyframes)
var subtitlesBgLayer = mainComp.layer("字幕背景")
shareUtil.configKeyframes(subtitlesBgLayer, opacityKeyframes)