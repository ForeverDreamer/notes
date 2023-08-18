function TextUtil() {}

TextUtil.prototype.configTextDocument = function(textProp, props) {
    textProp.setValue(new TextDocument(props["text"]));
    var textDocument = textProp.value;

    textDocument.resetCharStyle();
    textDocument.resetParagraphStyle();
    textDocument.font = props["font"] ? props["font"] : FONTS["en"];
    textDocument.fontSize = props["fontSize"] ? props["fontSize"] : 50;
    textDocument.fillColor = props["fillColor"] ? colorUtil.hexToRgb1(props["fillColor"]) : colorUtil.hexToRgb1(COLORS["text"]);
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

TextUtil.prototype.addOne = function(props, comp) {
    var textLayer;
    if (props["box"]) {
        textLayer = comp.layers.addBoxText(props["rect"]);
        props["justification"] = ParagraphJustification.LEFT_JUSTIFY
    } else {
        switch (props["justification"]) {
            case 'LEFT_JUSTIFY':
                props["justification"] = ParagraphJustification.LEFT_JUSTIFY
                break;
            case 'RIGHT_JUSTIFY':
                props["justification"] = ParagraphJustification.RIGHT_JUSTIFY
                break;
        }
        textLayer = comp.layers.addText(props["text"]);
    }
    textLayer.name = props["layerName"] ? props["layerName"] : props["text"];
    var textProp = textLayer("Source Text");
    this.configTextDocument(textProp, props)
    shareUtil.setAnchorPoint(textLayer, props["Anchor Point"])
    if (props['startTime']) {
		textLayer.startTime = props['startTime'];
	}
    if (props["span"]) {
		textLayer.inPoint = props["span"]["inPoint"];
        textLayer.outPoint = props["span"]["outPoint"];
	}
    textLayer("Transform")("Position").setValue(props["Position"])
    shareUtil.configKeyframes(textLayer, props["keyframes"])
    // textLayer.threeDLayer = true
    presetsUtil.add(textLayer, props["presets"])
    return textLayer
}

TextUtil.prototype.addMany = function(texts, comp) {
    for (var i = 0; i < texts.length; i++) {
        this.addOne(texts[i], comp)
    }
}

TextUtil.prototype.overlay = function(props, comp, parent) {
    var textLayer = comp.layers.addText(props["text"]);
    textLayer.name = props["layerName"];
    var textProp = textLayer("Source Text");
    this.configTextDocument(textProp, props)
    // textLayer("Transform")("Anchor Point").setValue(parent("Transform")("Anchor Point").value)
    shareUtil.setAnchorPoint(textLayer)
    textLayer.setParentWithJump(parent)
    textLayer("Transform")("Position").setValue(parent("Transform")("Anchor Point").value)
    if (props["Rotation"]) {
        textLayer("Transform")("Rotation").setValue(props["Rotation"])
    }
    if (props["Opacity"]) {
        textLayer("Transform")("Opacity").setValue(props["Opacity"])
    }
    if (props["keyframes"]) {
		shareUtil.configKeyframes(textLayer, props["keyframes"])
	}
    return textLayer
}

var textUtil = new TextUtil();