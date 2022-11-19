#includepath "../utils;";
#include "json.jsx";
#include "share.jsx";
#include "color.jsx";

// #include "extendscript-es5-shim.js";

// for (var k1 in conf) {
//     $.writeln(k1);
//     for (var i = 0; i < conf[k1].length; i++) {
//         for (var k2 in conf[k1]) {
//             $.writeln(k2);
//         }
//     }
//     $.writeln("=================================");
// }

var project = app.project;
var comp = project.activeItem;

function createShapeLayer(name, elem, pos) {
    var shapeLayer = comp.layers.addShape();
    shapeLayer("Transform")("Position").setValue(pos)
    shapeLayer.name = name + "." + elem;
    var shapeGroup = shapeLayer("Contents").addProperty("ADBE Vector Group");
    // shapeGroup.name = elem;
    pathProp = shapeGroup("Contents").addProperty("ADBE Vector Shape - Rect")
    pathProp("Size").setValue([50, 50])
    strokeProp = shapeGroup("Contents").addProperty("ADBE Vector Graphic - Stroke")
    strokeProp("Color").setValue([0, 0, 0])
    fillProp = shapeGroup("Contents").addProperty("ADBE Vector Graphic - Fill")
    fillProp("Color").setValue([1, 1, 1])
    return shapeLayer
}

function createTextLayer(name, elem, parent) {
    var textLayer = comp.layers.addText(elem);
    textLayer("Transform")("Position").setValue([0, 0])
    textLayer.setParentWithJump(parent)
    textLayer.name = name + "." + elem;
    var textProp = textLayer("Source Text");
    textDocument = textProp.value;
    textDocument.resetCharStyle();
    textDocument.resetParagraphStyle();
    // textDocument.font = "MicrosoftYaHeiUI-Bold";
    textDocument.font = "Arial-BoldItalicMT";
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
    textDocument.tracking = -110;
    // textDocument.leading = 500;

    textProp.setValue(textDocument);
    var value = textLayer("Transform")("Position").value
    value[1] = 15
    textLayer("Transform")("Position").setValue(value)
    return textLayer
}


function createQueue(name, pos, elems, queuesDic) {
    queuesDic[name] = []
    for (var i = 0; i < elems.length; i++) {
        shapeLayer = createShapeLayer(name, elems[i].toString(), [pos[0] + 50 * i, pos[1], pos[2]])
        textLayer = createTextLayer(name, elems[i].toString(), shapeLayer)
        queuesDic[name].push([shapeLayer, textLayer])
    }
}

function main() {
    if (comp == null || !(comp instanceof CompItem)) {
        comp = project.items.addComp("Main", 1920, 1080, 1, 10, 30);
    }
    comp.openInViewer();
    var bgLayer = comp.layers.addSolid([1, 1, 1], "BG", 1920, 1080, 1);
    bgLayer.moveToEnd()
    // var path = "D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/conf.json";

    // // var data = {compName: "My Comp", width: 1920, height: 1080, numlayers: 3};
    // // createJSONFile(data);

    conf = jsonUtil.read("D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/conf.json");
    var queuesDic = {};
    // $.writeln(JSON.stringify(data));
    var queues = conf['queues']
    for (var i = 0; i < queues.length; i++) {
        var name = queues[i]['name']
        var pos = queues[i]['pos']
        var elems = queues[i]['elems']
        // $.writeln(name, pos, elems);
        // $.writeln("=================================");
        createQueue(name, pos, elems, queuesDic)
    }
    (queuesDic["preorder"][0][0]("Contents")("Group 1")("Contents")("Fill 1")("Color")
        .setValuesAtTimes([0, 0.5, 1], [colorUtil.hexToRgb("#FF0000", true), colorUtil.hexToRgb("#00FF18", true), colorUtil.hexToRgb("#005FB8", true)])
    )
    var files = conf['files']
    for (var i = 0; i < files.length; i++) {
        var path = files[i]['path']
        var import_as_type = files[i]['import_as_type']
        var pos = files[i]['pos']
        var importOptions = new ImportOptions();
        importOptions.file = new File(path);
        importOptions.importAs = shareUtil.importAsType(import_as_type)
        var codePhotoItem = project.importFile(importOptions);
        codePhotoLayer = comp.layers.add(codePhotoItem)
        codePhotoLayer.moveBefore(bgLayer)
        codePhotoLayer("Transform")("Position").setValue(pos)
    }

}

app.beginUndoGroup("Process");

main();

app.endUndoGroup();