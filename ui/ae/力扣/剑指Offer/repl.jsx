var project = app.project;
var comp = project.activeItem;

if (comp === null) {
    comp = project.items.addComp("Main", 1920, 1080, 1, 10, 30);
}

// var textLayer = comp.layer(26)
// var shapeLayer = comp.layer(2)
// $.writeln(textLayer.anchorPoint.value)
// var value = textLayer.anchorPoint.value
// value[1] = 0
// textLayer.anchorPoint.setValue(value)
// $.writeln(textLayer.sourceRectAtTime(0, true).top)
// $.writeln(textLayer.sourceRectAtTime(0, true).left)
// $.writeln(textLayer.sourceRectAtTime(0, true).width)
// $.writeln(textLayer.sourceRectAtTime(0, true).height)
// $.writeln(textLayer("Transform")("Anchor Point").value)
// 也可以再WATCH窗口观察
// for (var key in textLayer) {
//     $.writeln(key)
// }
// $.writeln(textLayer("Transform")("Position").value);
// $.writeln(shapeLayer("Transform")("Position").value);
// colorProp = shapeLayer("Contents")("Group 1")("Contents")("Fill 1")("Color")
// $.writeln(colorProp.name);
// $.writeln(shapeLayer("Effects")("Drop Shadow")("Softness").value)
// var testColor = new RGBColor()//initial default colour
// testColor.red = 180;
// testColor.green = 93;
// testColor.blue = 120;
// colorProp.setValue([0.01, 0.37254901960784, 0.72156862745098])
// var positionProp = shapeLayer("Transform")("Position");
// positionProp.addKey(0);
// positionProp.addKey(1);
// positionProp.setValueAtKey(2, [300, 100])
// for (var i = 1; i <= positionProp.numKeys; i++) {
//     positionProp.removeKey(i)
// }
// positionProp.setValuesAtTimes([0, 0.5, 1, 1.5], [[100, 100], [200, 200], [300, 300], [400, 400]])
// var easeIn1 = new KeyframeEase(0, 0.1);
// var easeOut1 = new KeyframeEase(2000, 85);
// positionProp.setTemporalEaseAtKey(1, [easeIn1], [easeOut1]);
// var easeIn2 = new KeyframeEase(0, 0.1);
// var easeOut2 = new KeyframeEase(2000, 85);
// positionProp.setTemporalEaseAtKey(2, [easeIn2], [easeOut2]);
// var easeIn3 = new KeyframeEase(0, 0.1);
// var easeOut3 = new KeyframeEase(2000, 85);
// positionProp.setTemporalEaseAtKey(3, [easeIn3], [easeOut3]);
// var easeIn4 = new KeyframeEase(0, 0.1);
// var easeOut4 = new KeyframeEase(2000, 85);
// positionProp.setTemporalEaseAtKey(4, [easeIn4], [easeOut4]);
app.cancelTask(4)