#includepath "../utils;";
#include "json.jsx";
#include "share.jsx";
#include "color.jsx";
#include "effects.jsx";
#include "presets.jsx"
#include "text.jsx"
#include "shape.jsx"
#include "precomp.jsx"
#include "animation.jsx"

app.purge(PurgeTarget.ALL_CACHES)
var project = app.project;
shareUtil.delItems(project.items)
var mainComp = project.activeItem;


function createQueue(comp, conf, queuesObj) {
    var name = conf['name']
    var pos = conf['pos']
    var elems = conf['elems']
    var effects = conf['effects']
    var keyframes = conf['keyframes']
    queuesObj[name] = []
    for (var i = 0; i < elems.length; i++) {
        var shapeLayer = shapeUtil.add(comp, "Shape"+elems[i], {"pos": [25 + 50 * i, 25, 0]})
        // shapeLayer.threeDLayer = true
        // var dropShadowEffect = shapeLayer.Effects.addProperty("ADBE Drop Shadow");
        // dropShadowEffect("Softness").setValue(4);
        // shapeLayer.Effects.addProperty("PESS2");
        conf["text"] = elems[i];
        conf["font"] = "Arial-BoldItalicMT";
        conf["fontSize"] = 40;
        var textLayer = textUtil.overlay(comp, shapeLayer, "Text"+elems[i], conf)
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


function main() {
    if (mainComp == null || !(mainComp instanceof CompItem)) {
        mainComp = project.items.addComp("Main", 1920, 1080, 1, 300, 30);
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
    cameraLayer("Transform")("Point of Interest").setValuesAtTimes([1, 2, 3, 7], [[960, 540, 0], [960, 300, 0], [960, 300, 0], [960, 700, 0]])
    cameraLayer("Transform")("Position").setValuesAtTimes([1, 2, 3, 7], [[960, 540, -800], [960, 300, -800], [960, 300, -800], [960, 700, -800]])
    cameraLayer("Camera Options")("Zoom").setValuesAtTimes([1, 2, 7], [800, 1500, 1500])
    cameraLayer.moveBefore(bgLayer)
    // var path = "D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/conf.json";

    // // var data = {compName: "My Comp", width: 1920, height: 1080, numlayers: 3};
    // // createJSONFile(data);


    var conf = jsonUtil.read("D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/conf.json");
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
        var left = queueLayer.sourceRectAtTime(0, false).left
        var anchorPointProp = queueLayer("Transform")("Anchor Point")
        var value = anchorPointProp.value
        value[0] = left
        anchorPointProp.setValue(value)
        effectsUtil.add(queueLayer, "ADBE Drop Shadow", {"Distance": 10, "Softness": 30, "Opacity": 255});
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
        var item = shareUtil.importFile(project, files[i]);
        var confLayers = files[i]["layers"]
        var addToLayers = files[i]["addToLayers"]
        if (confLayers) {
            for (var j = 0; j < confLayers.length; j++) {
                shareUtil.addLayer(project.items, mainComp.layers, confLayers[j])
            }
        } else {
            if (addToLayers) {
                shareUtil.addLayer(project.items, mainComp.layers, files[i], item)
            }
        }
    }

    var precomps = conf['precomps'];
    for (var i = 0; i < precomps.length; i++) {
        var compLayer;
        switch (precomps[i]["type"]) {
            case 'BINARY_TREE':
                // compLayer = precompUtil.binaryTree(project.items, mainComp, precomps[i]);
                animationUtil.buildBinaryTree(project.items, mainComp, precomps[i]);
                $.writeln('====================================')
                break;
            // case 'PROJECT':
            //     importOptions.importAs = ImportAsType.PROJECT;
            //     break;
            // case 'COMP':
            //     importOptions.importAs = ImportAsType.COMP;
            //     break;
            // default:
            //     importOptions.importAs = ImportAsType.FOOTAGE;
        }
    }


    var audios = conf['audios']
    for (var i = 0; i < audios.length; i++) {
        var item = shareUtil.importFile(project, audios[i]);
        shareUtil.addLayer(project.items, mainComp.layers, audios[i], item)
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
    var textLayer = textUtil.add(mainComp, "视频字幕", {"text": transcript[0]["text"], "pos": [960, 1050, 0], "font": "KaiTi", "fontSize": 50});
    // textLayer.threeDLayer = true
    effectsUtil.add(textLayer, "ADBE Drop Shadow", {"Distance": 10, "Softness": 20, "Opacity": 180});
    // dropShadowEffect("Distance").setValue(10);
    // dropShadowEffect("Softness").setValue(20);
    // 该属性内部有个自己的换算比例，100=39%，255约等于100%
    // dropShadowEffect("Opacity").setValue(180);
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
        var props = annotations[i]
        var name = props["name"]
        var text = props["text"]
        var pos = props["pos"]
        var span = props["span"]
        var keyframes = props["keyframes"]
        var presets = props["presets"]
        // var textLayer = createTextLayer(mainComp, name, {"text": text, "pos": pos, "fontSize": 50, "fillColor": "#FFA119"});
        var textLayer = textUtil.add(mainComp, name, props);
        textLayer.inPoint = span['inPoint']
        textLayer.outPoint = span['outPoint']
        if (keyframes) {
            for (var j = 0; j < keyframes.length; j++) {
                for (var k in keyframes[j]) {
                    var timeValue = keyframes[j][k]
                    textLayer("Transform")(k).setValuesAtTimes(timeValue[0], timeValue[1])
                }
            }
        }
        if (presets) {
            for (var m = 0; m < presets.length; m++) {
                presetsUtil.add(textLayer, presets[m])
            }
        }
        // textLayer.threeDLayer = true
        // textLayer.Effects.addProperty("PESS2");
    }
}

app.beginUndoGroup("Process");

main();

app.endUndoGroup();