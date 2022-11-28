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
app.purge(PurgeTarget.ALL_CACHES)
var project = app.project;

// function delItems(items) {
//     numItems = items.length
//     for (var i = numItems; i >= 1; i--) {
//         item = items[i]
//         // if (item instanceof FolderItem) {
//         //     delItems(item.items);
//         // } else {
//         //     item.remove()
//         // }
//         item.remove()
//     }
// }

shareUtil.delItems(project.items)
// for (var i = 1; i <= project.numItems; i++) {
//     if (item instanceof FolderItem) {
//         delFolder(item);
//     } 
//     project.item(i).remove()
// }

var mainComp = project.activeItem;

function createQueueShapeLayer(comp, name, elem, pos) {
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

function overlayTextLayer(comp, name, elem, parent) {
    var textLayer = comp.layers.addText(elem);
    textLayer("Transform")("Position").setValue([0, 0, 0])
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


function createQueue(comp, conf, queuesObj) {
    var name = conf['name']
    var pos = conf['pos']
    var elems = conf['elems']
    var effects = conf['effects']
    var keyframes = conf['keyframes']
    queuesObj[name] = []
    for (var i = 0; i < elems.length; i++) {
        // var shapeLayer = createQueueShapeLayer(comp, name, elems[i].toString(), [pos[0] + 50 * i, pos[1], pos[2]])
        var shapeLayer = createQueueShapeLayer(comp, name, elems[i].toString(), [25 + 50 * i, 25, 0])
        // shapeLayer.threeDLayer = true
        // var dropShadowEffect = shapeLayer.Effects.addProperty("ADBE Drop Shadow");
        // dropShadowEffect("Softness").setValue(4);
        // shapeLayer.Effects.addProperty("PESS2");
        var textLayer = overlayTextLayer(comp, name, elems[i].toString(), shapeLayer)
        // textLayer.threeDLayer = true
        // 嵌套循环计数变量i,j等不要同名，会有意想不到的bug
        for (var j = 0; j < keyframes.length; j++) {
            for (var k in keyframes[j]) {
                var timeValue = keyframes[j][k]
                if (k === "Opacity") {
                    timeValue[0][1] += i*0.25
                    timeValue[0][2] += i*0.25
                }
                shapeLayer("Transform")(k).setValuesAtTimes(timeValue[0], timeValue[1])
                textLayer("Transform")(k).setValuesAtTimes(timeValue[0], timeValue[1])
            }
        }
        // var opacityProp = shapeLayer("Transform")("Opacity")
        // var timeArr = [0, 1+i*0.25, 2+i*0.25]
        // opacityProp.setValuesAtTimes(timeArr, [0, 0, 100])
        // textLayer = overlayTextLayer(name, elems[i].toString(), shapeLayer)
        // opacityProp = textLayer("Transform")("Opacity")
        // opacityProp.setValuesAtTimes(timeArr, [0, 0, 100])
        queuesObj[name].push([shapeLayer, textLayer])
    }
    return comp
}


function createTextLayer(comp, name, payload) {
    var textLayer = comp.layers.addText(payload["text"]);
    textLayer.name = name;
    var textProp = textLayer("Source Text");
    textDocument = textProp.value;
    textDocument.resetCharStyle();
    textDocument.resetParagraphStyle();
    textDocument.font = payload["font"] ? payload["font"] : "Arial-BoldItalicMT";
    textDocument.fontSize = payload["fontSize"] ? payload["fontSize"] : 40;
    textDocument.fillColor = payload["fillColor"] ? colorUtil.hexToRgb1(payload["fillColor"]) : [0, 0, 0];
    textDocument.strokeColor = payload["strokeColor"] ? payload["strokeColor"] : [1, 1, 1];
    textDocument.strokeWidth = payload["strokeWidth"] ? payload["strokeWidth"] : 0;
    textDocument.strokeOverFill = payload["strokeOverFill"] ? payload["strokeOverFill"] : true;
    textDocument.applyStroke = payload["applyStroke"] ? payload["applyStroke"] : true;
    textDocument.applyFill = payload["applyFill"] ? payload["applyFill"] : true;
    textDocument.justification = payload["justification"] ? payload["justification"] : ParagraphJustification.CENTER_JUSTIFY;
    textDocument.tracking = payload["tracking"] ? payload["tracking"] : 0;
    // textDocument.leading = 500;
    textProp.setValue(textDocument);
    var left = textLayer.sourceRectAtTime(0, true).left
    var anchorPointProp = textLayer("Transform")("Anchor Point")
    var value = anchorPointProp.value
    value[0] = left
    anchorPointProp.setValue(value)
    textLayer("Transform")("Position").setValue(payload["pos"])
    // textLayer.threeDLayer = true
    return textLayer
}


function main() {
    if (mainComp == null || !(mainComp instanceof CompItem)) {
        mainComp = project.items.addComp("Main", 1920, 1080, 1, 10, 30);
    }
    mainComp.openInViewer();

    var bgLayer = mainComp.layers.addSolid([1, 1, 1], "BG", 1920, 1080, 1);
    // bgLayer.threeDLayer = true
    bgLayer.moveToEnd()

    var cameraLayer = mainComp.layers.addCamera("Camera", [960, 540])
    cameraLayer("Transform")("Position").setValue([960, 540, -800])
    cameraLayer("Camera Options")("Zoom").setValue(800)
    cameraLayer("Camera Options")("Focus Distance").setValue(800)
    cameraLayer("Camera Options")("Aperture").setValue(7.6)
    cameraLayer("Transform")("Point of Interest").setValuesAtTimes([1, 2, 6, 7], [[960, 540, 0], [960, 300, 0], [960, 300, 0], [960, 540, 0]])
    cameraLayer("Transform")("Position").setValuesAtTimes([1, 2, 6, 7], [[960, 540, -800], [960, 300, -800], [960, 300, -800], [960, 540, -800]])
    cameraLayer("Camera Options")("Zoom").setValuesAtTimes([1, 2, 6, 7], [800, 1500, 1500, 800])
    cameraLayer.moveBefore(bgLayer)
    // var path = "D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/conf.json";

    // // var data = {compName: "My Comp", width: 1920, height: 1080, numlayers: 3};
    // // createJSONFile(data);


    conf = jsonUtil.read("D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/conf.json");
    var queuesObj = {};
    var queueLayers = {};
    // $.writeln(JSON.stringify(data));
    var queues = conf['queues'];
    for (var i = 0; i < queues.length; i++) {
        // $.writeln(name, pos, elems);
        // $.writeln("=================================");
        var name = queues[i]['name']
        var pos = queues[i]['pos']
        var queueComp = project.items.addComp(queues[i]['name'], 250, 50, 1, 10, 30);
        createQueue(queueComp, queues[i], queuesObj);
        var queueLayer = mainComp.layers.add(queueComp);
        // var dropShadowEffect = queueLayer.Effects.addProperty("ADBE Drop Shadow");
        // dropShadowEffect("Softness").setValue(4);
        var left = queueLayer.sourceRectAtTime(0, true).left
        var anchorPointProp = queueLayer("Transform")("Anchor Point")
        var value = anchorPointProp.value
        value[0] = left
        anchorPointProp.setValue(value)
        var dropShadowEffect = queueLayer.Effects.addProperty("ADBE Drop Shadow");
        dropShadowEffect("Distance").setValue(10);
        dropShadowEffect("Softness").setValue(30);
        // 该属性内部有个自己的换算比例，100=39%，255约等于100%
        dropShadowEffect("Opacity").setValue(255);
        // queueLayer.Effects.addProperty("PESS2");
        queueLayer("Transform")("Position").setValue(pos)
        // queueLayer.threeDLayer = true
        queueLayers[name] = queueLayer;
    }
    // (queuesObj["preorder"][0][0]("Contents")("Group 1")("Contents")("Fill 1")("Color")
    //     .setValuesAtTimes([0, 1.5, 3], [colorUtil.hexToRgb1("#FF0000"), colorUtil.hexToRgb1("#00FF18"), colorUtil.hexToRgb1("#005FB8")])
    // )
    colorProp = queuesObj["preorder"][0][0]("Contents")("Group 1")("Contents")("Fill 1")("Color")
    colorProp.setValuesAtTimes([0, 1.5, 3], [colorUtil.hexToRgb1("#FADED8"), colorUtil.hexToRgb1("#CEF2ED"), colorUtil.hexToRgb1("#0573E1")])
    for (var i = 1; i <= colorProp.numKeys; i++) {
        colorProp.setInterpolationTypeAtKey(i, KeyframeInterpolationType.HOLD)
    }
    var files = conf['files']
    for (var i = 0; i < files.length; i++) {
        var path = files[i]['path']
        var import_as_type = files[i]['import_as_type']
        var pos = files[i]['pos']
        var importOptions = new ImportOptions();
        importOptions.file = new File(path);
        importOptions.importAs = shareUtil.importAsType(import_as_type)
        var fileItem = project.importFile(importOptions);
        fileLayer = mainComp.layers.add(fileItem)
        fileLayer.moveBefore(bgLayer)
        fileLayer("Transform")("Position").setValue(pos)
        fileLayer.threeDLayer = true
    }
    var audios = conf['audios']
    for (var i = 0; i < audios.length; i++) {
        var path = audios[i]['path']
        var import_as_type = audios[i]['import_as_type']
        var importOptions = new ImportOptions();
        importOptions.file = new File(path);
        importOptions.importAs = shareUtil.importAsType(import_as_type)
        var audioItem = project.importFile(importOptions);
        audioLayer = mainComp.layers.add(audioItem)
        audioLayer.startTime = audios[i]['startTime']
        // audioLayer.inPoint = span['inPoint']
        // audioLayer.outPoint = span['outPoint']
        // codePhotoLayer.moveBefore(bgLayer)
        // codePhotoLayer("Transform")("Position").setValue(pos)
    }
    // var codes = conf["codes"]
    // var codesArr = []
    // var start_x = 400
    // var start_y = 50
    // var pos_x = start_x;
    // var pos_y = start_y;
    // for (var i = 0; i < codes.length; i++) {
    //     var pair = codes[i]
    //     for (var j = 0; j < pair.length; j++) {
    //         if (pair[j][0]==="") {
    //             continue
    //         }
    //         var pos_x = start_x + pair[j][1]*80
    //         var textLayer = createTextLayer("Code"+"."+i+"."+j, {"text": pair[j][0], "pos": [pos_x, pos_y, 0], "fontSize": 30});
    //         pos_y += 43
    //         codesArr.push(textLayer)
    //     }
    // }
    var transcript = conf["transcript"]
    // var lines = transcript.concat(annotations)
    var textLayer = createTextLayer(mainComp, "视频字幕", {"text": transcript[i]["text"], "pos": [80, 1000, 0], "font": "KaiTi", "fontSize": 50});
    // textLayer.threeDLayer = true
    var dropShadowEffect = textLayer.Effects.addProperty("ADBE Drop Shadow");
    dropShadowEffect("Distance").setValue(10);
    dropShadowEffect("Softness").setValue(20);
    // 该属性内部有个自己的换算比例，100=39%，255约等于100%
    dropShadowEffect("Opacity").setValue(180);
    // textLayer.Effects.addProperty("PESS2");
    for (var i = 0; i < transcript.length; i++) {
        var text = transcript[i]["text"]
        var start = transcript[i]["start"]
        // var keyframes = transcript[i]["keyframes"]
        // var textLayer = createTextLayer(mainComp, "transcript"+"."+i, {"text": text, "pos": [80, 1000, 0], "fontSize": 50});
        // for (var j = 0; j < keyframes.length; j++) {
        //     for (var k in keyframes[j]) {
        //         var timeValue = keyframes[j][k]
        //         textLayer("Transform")(k).setValuesAtTimes(timeValue[0], timeValue[1])
        //     }
        // }
        textLayer("Source Text").setValuesAtTimes([start], [text])
    }
    var annotations = conf["annotations"]
    for (var i = 0; i < annotations.length; i++) {
        var name = annotations[i]["name"]
        var text = annotations[i]["text"]
        var pos = annotations[i]["pos"]
        var span = annotations[i]["span"]
        var keyframes = annotations[i]["keyframes"]
        var textLayer = createTextLayer(mainComp, name, {"text": text, "pos": pos, "fontSize": 50, "fillColor": "#FFA119"});
        textLayer.inPoint = span['inPoint']
        textLayer.outPoint = span['outPoint']
        for (var j = 0; j < keyframes.length; j++) {
            for (var k in keyframes[j]) {
                var timeValue = keyframes[j][k]
                textLayer("Transform")(k).setValuesAtTimes(timeValue[0], timeValue[1])
            }
        }
        // textLayer.threeDLayer = true
        // textLayer.Effects.addProperty("PESS2");
    }
}

app.beginUndoGroup("Process");

main();

app.endUndoGroup();