#includepath "../utils;"
#include "json.jsx"

var path = "D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/test.json";

// // var data = {compName: "My Comp", width: 1920, height: 1080, numlayers: 3};
// // createJSONFile(data);

// data = jsonIO.read(path);
// $.writeln(JSON.stringify(data));
// $.writeln(data.position.x);

// if (app.project.activeItem == null || !(app.project.activeItem instanceof CompItem)) {
//     alert("Please select a composition first");
// } else {
//     app.beginUndoGroup("Process");

//     var mainComp = app.project.activeItem;
//     $.writeln(mainComp.numLayers);
//     app.endUndoGroup();
// }
var project = app.project;
var comp = project.activeItem;

function createShapeLayer(name, pos) {
    var shapeLayer = comp.layers.addShape();
    shapeLayer("Transform")("Position").setValue(pos)
    shapeLayer.name = name;
    var shapeGroup = shapeLayer("Contents").addProperty("ADBE Vector Group");
    shapeGroup.name = name;
    pathProp = shapeGroup("Contents").addProperty("ADBE Vector Shape - Rect")
    pathProp("Size").setValue([50, 50])
    strokeProp = shapeGroup("Contents").addProperty("ADBE Vector Graphic - Stroke")
    strokeProp("Color").setValue([0, 0, 0])
    fillProp = shapeGroup("Contents").addProperty("ADBE Vector Graphic - Fill")
    fillProp("Color").setValue([1, 1, 1])
    return shapeLayer
}

function createTextLayer(text, parent) {
    var textLayer = comp.layers.addText(text);
    textLayer("Transform")("Position").setValue([0, 0])
    textLayer.setParentWithJump(parent)
    textLayer.name = text;
    var textProp = textLayer("Source Text");
    textDocument = textProp.value;  
    textDocument.resetCharStyle();
    textDocument.resetParagraphStyle();
    textDocument.font = "MicrosoftYaHeiUI-Bold";
    textDocument.fontSize = 40;
    // textProp.expression = 'text.sourceText.style.setFauxBold(true).setText(' + text + ')'
    textDocument.fillColor = [0, 0, 0];
    textDocument.strokeColor = [1, 1, 1];
    textDocument.strokeWidth = 2;
    textDocument.strokeOverFill = true
    textDocument.applyStroke = true;
    textDocument.applyFill = true;
    // textDocument.text = "Changed String";
    textDocument.justification = ParagraphJustification.CENTER_JUSTIFY;
    textDocument.tracking = 50;
    textDocument.leading = 500;

    textProp.setValue(textDocument);
    var value = textLayer("Transform")("Position").value
    value[1] = 15
    textLayer("Transform")("Position").setValue(value)
    return textLayer
}


function createQueue(pos, length){
    for (var i = 0; i < length; i++) {
        shapeLayer = createShapeLayer(i.toString(), [pos[0]+50*i, pos[1], pos[2]])
        createTextLayer(i.toString(), shapeLayer)
    }
}

function main(){
    if (app.project.activeItem == null || !(app.project.activeItem instanceof CompItem)) {
        alert("Please select a composition first");
        return;
    }
    comp.openInViewer();
    createQueue([100, 100, 0], 10)
}

app.beginUndoGroup("Process");

main();

app.endUndoGroup();