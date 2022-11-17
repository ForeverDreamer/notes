app.beginUndoGroup("Text Layer Stuff");

var comp = app.project.activeItem;
var layer = comp.layer(1);
var textLayer;

if (layer.property("Source Text") !== null) {
    textLayer = layer;
}

// var textDocument = new TextDocument("Test Text");
// textLayer.property("Source Text").setValue(textDocument);

var textProp = textLayer.property("Source Text");
textDocument = textProp.value;

textDocument.resetCharStyle();
textDocument.resetParagraphStyle();
textDocument.font = "Microsoft YaHei UI";
textDocument.fontSize = 50;
textDocument.fillColor = [0, 1, 0];
textDocument.strokeColor = [1, 1, 1];
textDocument.strokeWidth = 2;
textDocument.strokeOverFill = true
textDocument.applyStroke = true;
textDocument.applyFill = true;
textDocument.text = "Changed String";
textDocument.justification = ParagraphJustification.CENTER_JUSTIFY;
textDocument.tracking = 50;
textDocument.leading = 500;

textProp.setValue(textDocument);

app.endUndoGroup();

var pointText, boxText, boxTextSize;
pointText = textDocument.pointText;
boxText = textDocument.boxText;
$.writeln("pointText = " + pointText);
$.writeln("boxText = " + boxText);
if (boxText) {
    boxTextSize = textDocument.boxTextSize;
    $.writeln("boxTextSize = " + boxTextSize);
}