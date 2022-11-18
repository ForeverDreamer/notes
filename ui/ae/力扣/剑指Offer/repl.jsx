var project = app.project;
var comp = project.activeItem;

if (comp === null) {
    comp = project.items.addComp("Main", 1920, 1080, 1, 10, 30);
}

var textLayer = comp.layer(1)
var shapeLayer = comp.layer(2)
var bgLayer = comp.layers.addSolid([1,1,1], "BG", 1920, 1080, 1);
bgLayer.moveToEnd()
var importOptions = new ImportOptions();
importOptions.file = new File("D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/代码.jpg");
importOptions.importAs = ImportAsType.FOOTAGE
var codePhotoItem = project.importFile(new ImportOptions(new File("D:/沉浸式学习/数据结构与算法/力扣/剑指 Offer（第 2 版）/07. 重建二叉树/代码.jpg")));
codePhotoLayer = comp.layers.add(codePhotoItem)
codePhotoLayer.moveBefore(bgLayer)
codePhotoLayer.property("Transform")("Position").setValue([1398, 540, 0])
// $.writeln(textLayer("Transform")("Position").value);
// $.writeln(shapeLayer("Transform")("Position").value);
var positionProp = shapeLayer.property("Transform")("Position");
// positionProp.addKey(0);
// positionProp.addKey(1);
// positionProp.setValueAtKey(2, [300, 100])
for (var i = 1; i <= positionProp.numKeys; i++) {
    positionProp.removeKey(i)
}
positionProp.setValuesAtTimes([0, 0.5, 1, 1.5], [[100, 100], [200, 200], [300, 300], [400, 400]])
var easeIn1 = new KeyframeEase(0, 0.1);
var easeOut1 = new KeyframeEase(2000, 85);
positionProp.setTemporalEaseAtKey(1, [easeIn1], [easeOut1]);
var easeIn2 = new KeyframeEase(0, 0.1);
var easeOut2 = new KeyframeEase(2000, 85);
positionProp.setTemporalEaseAtKey(2, [easeIn2], [easeOut2]);
var easeIn3 = new KeyframeEase(0, 0.1);
var easeOut3 = new KeyframeEase(2000, 85);
positionProp.setTemporalEaseAtKey(3, [easeIn3], [easeOut3]);
var easeIn4 = new KeyframeEase(0, 0.1);
var easeOut4 = new KeyframeEase(2000, 85);
positionProp.setTemporalEaseAtKey(4, [easeIn4], [easeOut4]);
