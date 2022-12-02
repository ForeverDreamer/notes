#include "color.jsx";

function TextUtil() {}

TextUtil.prototype.configTextDocument = function(textProp, props) {
    textProp.setValue(new TextDocument(props["text"]));
    var textDocument = textProp.value;

    textDocument.resetCharStyle();
    textDocument.resetParagraphStyle();
    textDocument.font = props["font"] ? props["font"] : "Arial-BoldMT";
    textDocument.fontSize = props["fontSize"] ? props["fontSize"] : 50;
    textDocument.fillColor = props["fillColor"] ? colorUtil.hexToRgb1(props["fillColor"]) : [0, 0, 0];
    textDocument.strokeColor = props["strokeColor"] ? props["strokeColor"] : [1, 1, 1];
    textDocument.strokeWidth = props["strokeWidth"] ? props["strokeWidth"] : 0;
    textDocument.strokeOverFill = props["strokeOverFill"] ? props["strokeOverFill"] : true;
    textDocument.applyStroke = props["applyStroke"] ? props["applyStroke"] : true;
    textDocument.applyFill = props["applyFill"] ? props["applyFill"] : true;
    textDocument.justification = props["justification"] ? props["justification"] : ParagraphJustification.CENTER_JUSTIFY;
    textDocument.tracking = props["tracking"] ? props["tracking"] : 0;
    // textDocument.text = props["text"];

    textProp.setValue(textDocument);
}

TextUtil.prototype.add = function(comp, name, props) {
    var textLayer;
    if (props["box"]) {
        textLayer = comp.layers.addBoxText(props["rect"]);
        props["justification"] = ParagraphJustification.LEFT_JUSTIFY
    } else {
        textLayer = comp.layers.addText(props["text"]);
    }
    textLayer.name = name;
    var textProp = textLayer("Source Text");
    this.configTextDocument(textProp, props)
    var left = textLayer.sourceRectAtTime(0, true).left
    var width = textLayer.sourceRectAtTime(0, true).width
    var anchorPointProp = textLayer("Transform")("Anchor Point")
    var value = anchorPointProp.value
    value[0] = left + width/2
    anchorPointProp.setValue(value)
    textLayer("Transform")("Position").setValue(props["pos"])
    // textLayer.threeDLayer = true
    return textLayer
}

TextUtil.prototype.overlay = function(comp, parent, name, props) {
    var textLayer = comp.layers.addText(props["text"]);
    textLayer.setParentWithJump(parent)
    textLayer.name = name;
    textLayer("Transform")("Position").setValue(props["pos"] ? props["pos"] : [0, 15, 0])
    var textProp = textLayer("Source Text");
    this.configTextDocument(textProp, props)
    // var value = textLayer("Transform")("Position").value
    // value[1] = 15
    // textLayer("Transform")("Position").setValue(value)
    return textLayer
}

var textUtil = new TextUtil();