#includepath "../utils;"
#include "json.jsx"

var path = "D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/test.json";

// // var data = {compName: "My Comp", width: 1920, height: 1080, numlayers: 3};
// // createJSONFile(data);

// data = jsonIO.read(path);
// $.writeln(JSON.stringify(data));
// $.writeln(data.position.x);

if (app.project.activeItem == null || !(app.project.activeItem instanceof CompItem)) {
    alert("Please select a composition first");
} else {
    app.beginUndoGroup("Process");

    var mainComp = app.project.activeItem;
    $.writeln(mainComp.numLayers);
    app.endUndoGroup();
}