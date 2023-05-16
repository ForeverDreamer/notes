//share_util.head
#includepath "utils/jsx";
#include "json.jsx";
var BASE_DIR = "D:/data_files/notes/ui/ae/"
var conf = jsonUtil.read(BASE_DIR + "基础/树/b-tree/conf.json");
#include "constants.jsx";
#include "color.jsx";
#include "text.jsx";
#include "shape.jsx";
#include "share.jsx";
#include "effects.jsx";
#include "precomp.jsx";
#include "presets.jsx";
#include "camera.jsx";

// app.purge(PurgeTarget.ALL_CACHES);
var project = app.project;
shareUtil.delItems(project.items);
var mainComp = project.items.addComp(NAME, WIDTH, HEIGHT, PIXEL_ASPECT, DURATION, FRAME_RATE);
mainComp.openInViewer();
var bL = textUtil.addOne(mainComp, "字幕", {"text": "你好世界", "Position": [960, 540], "font": FONTS["subtitle"], "fontSize": 100, "fillColor": COLORS["subtitle"]});

presetsUtil.add(bL, [
    {
        "path": "D:/Program Files/Adobe/Adobe After Effects 2021/Support Files/Presets/User/Untitled.ffx",
    }
])

bL("Transform")("Scale").expression = 'result = getAnimationComposerPresetValue();function getAnimationComposerPresetValue(){var bL=thisLayer;var tTrI=null;var tTrO=null;if(bL.marker.numKeys>0){var acmp="zzzzzzzzzzzzzzz_AC";for(var i=1;i<=bL.marker.numKeys;i++){var m=bL.marker.key(i);var p=m.parameters;if(p.hasOwnProperty(acmp+"MarkerEnabled")&&p.hasOwnProperty(acmp+"MarkerType")&&p.hasOwnProperty(acmp+"MarkerAppPresetType")){if(p[acmp+"MarkerEnabled"]!="1"){continue;}switch(p[acmp+"MarkerAppPresetType"]){case "1":{tTrI=m.time;break;}case "2":{tTrO=m.time;break;}}}}};function acPD(fxN){try{if(bL.effect(fxN).active===false){ac.en=false;}}catch(e){}}function acSliderValP(fxN,stN,dV){try{return bL.effect(fxN)(stN);}catch(e){return dV;}}function acValMul(val){acAccM*=val;}function elasticBounce(t,firstBounce,elasticity,maxBounces){if(t>1){t=1;}if(t<0){t=0;}if(typeof(firstBounce)=="undefined"){firstBounce=0.15;}if(typeof(elasticity)=="undefined"){elasticity=0.75;}if(typeof(maxBounces)=="undefined"){maxBounces=9;}e=elasticity;fd=firstBounce*2;t-=firstBounce;t=1-t;fdi=1/fd;g=8*fdi*fdi;vy=fd*g*0.5;nMax=maxBounces;tCur=0;segDur=2*vy/g;tNext=segDur;nb=0;while((tNext<t)&&(nb<=nMax)){vy*=e;segDur*=e;tCur=tNext;tNext+=segDur;nb++}if(nb<=nMax){delta=t-tCur;y=delta*(vy-g*delta/2);if(y>1){y=1;}if(y<0){y=0;}}else{y=0;}return y;}function upACo(tIn,dIn,tOut,dOut,eFi,eFo){if(dIn<0){dIn=0;}if(dOut<0){dOut=0;}ac.fade=1.0;if(t<tOut){if(t<(tIn+dIn)){if(dIn==0){ac.fade=0;}else{ac.fade=(t-tIn)/dIn;if(ac.fade<0){ac.fade=0;}if(ac.fade>1){ac.fade=1;}if(eFi){ac.fade=eFi(ac.fade);}}}}else{if(dOut==0){ac.fade=0;}else{ac.fade=(t-tOut)/dOut;if(ac.fade<0){ac.fade=0;}if(ac.fade>1){ac.fade=1;}if(eFo){ac.fade=eFo(ac.fade);}ac.fade=1-ac.fade;}}ac.intensity=1.0;ac.en=true;ac.t=t-tIn;}var ac={};ac.en=false;var v=thisProperty.value;var t=time;var acAccM=1;ac.en=false;if((tTrI!==null)&&(t<tTrI)){upACo(bL.inPoint,tTrI-bL.inPoint,bL.outPoint,0);ac.fade=1-ac.fade;}acPD("AC IN [BCO] Controls");if(ac.en){acValMul((1 - elasticBounce(ac.fade, 0.45, 0.4, 3) * ((acSliderValP("AC IN [BCO] Controls", "Scale", 0) / (-100)) + 1)));}ac.en=false;if((tTrO!==null)&&(t>=tTrO)){upACo(0,0,tTrO,bL.outPoint-tTrO-thisComp.frameDuration);ac.fade=1-ac.fade;}acPD("AC OUT [BCO] 2 Controls");if(ac.en){acValMul((1 - elasticBounce(ac.fade, 0.45, 0.4, 3) * ((acSliderValP("AC OUT [BCO] 2 Controls", "Scale", 0) / (-100)) + 1)));}v=thisProperty.value;v*=acAccM;return v;}result'

var markers = [
    {"Name": "TR In", "Type": "1", "PresetType": "1", "Code": "BCO#1#1", "Time": 1},
    {"Name": "TR Out", "Type": "2", "PresetType": "2", "Code": "BCO#2#2", "Time": 119}
]
var acmp = "zzzzzzzzzzzzzzz_AC";

for (var i = 0; i < markers.length; i++) {
    var marker = markers[i]
    var mv = new MarkerValue(marker["Name"]);
    var parms = {};

    parms[acmp + "MarkerEnabled"] = "1"
    parms[acmp + "MarkerType"] = marker["Type"]
    parms[acmp + "MarkerAppPresetType"] = marker["PresetType"]
    parms[acmp + "MarkerPresetCode"] = marker["Code"]
    mv.setParameters(parms);
    bL.property("Marker").setValueAtTime(marker["Time"], mv);
}



// var mv = new MarkerValue("TR Out");
// var parms = {};
// var acmp = "zzzzzzzzzzzzzzz_AC";
// parms[acmp + "MarkerEnabled"] = "1"
// parms[acmp + "MarkerType"] = "2"
// parms[acmp + "MarkerAppPresetType"] = "2"
// parms[acmp + "MarkerPresetCode"] = "BCO#2#2"
// mv.setParameters(parms);
// bL2.property("Marker").setValueAtTime(10, mv);

$.writeln(bL.marker.numKeys)

// var m = bL1.marker.keyValue(1);
// var p = m.getParameters();
// $.writeln(p)
// var m = bL1.marker.keyValue(2);
// var p = m.getParameters();
// $.writeln(p)

// var m = bL2.marker.keyValue(1);
// var p = m.getParameters();
// $.writeln(p)
// var m = bL2.marker.keyValue(2);
// var p = m.getParameters();
// $.writeln(p)