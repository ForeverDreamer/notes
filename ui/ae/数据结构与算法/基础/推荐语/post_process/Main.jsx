//share_util.head
#includepath "../../../../utils/jsx";
#include "json.jsx";
var conf = jsonUtil.read("D:/data_files/notes/ui/Ae/数据结构与算法/基础/推荐语/conf.json");
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


//share_util.body
app.purge(PurgeTarget.ALL_CACHES);
var project = app.project;
var mainComp = shareUtil.findItemByName("Main");
if (!mainComp) {
    mainComp = project.items.addComp("Main", WIDTH, HEIGHT, PIXEL_ASPECT, DURATION, FRAME_RATE)
}
mainComp.openInViewer()
mainComp.resolutionFactor = RESOLUTION_FACTOR;
var subtitlesCnLayer = mainComp.layer("字幕cn")
var textSourceTextCn = subtitlesCnLayer("Source Text");
textUtil.configTextDocument(textSourceTextCn, {"text": "Write the code, change the world!", "Position": [960, 1017], "font": FONTS["cn"], "fontSize": 40, "fillColor": COLORS["subtitle"]})
var subtitlesEnLayer = mainComp.layer("字幕en")
var textSourceTextEn = subtitlesEnLayer("Source Text");
textUtil.configTextDocument(textSourceTextEn, {"text": "Write the code, change the world!", "Position": [960, 1017], "font": FONTS["en"], "fontSize": 40, "fillColor": COLORS["subtitle"]})

