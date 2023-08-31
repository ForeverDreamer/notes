function AtomxTypographyUtil() {}

AtomxTypographyUtil.prototype.titleMinimal_94 = function(conf, comp) {
    // Text_1
    var sourceText = comp.layer("Text_1")("Source Text");
    sourceText.setValue(new TextDocument(conf["text"]));
    var textDocument = sourceText.value;
    textDocument.leading = conf["leading"]
    sourceText.setValue(textDocument);

    // _controller
    var _controller = comp.layer("_controller")
    _controller("Effects")("Text Color 1")("Color").setValue(colorUtil.hexToRgb1(conf["textColor"]))
    _controller("Effects")("Element Color")("Color").setValue(colorUtil.hexToRgb1(conf["elementColor"]))
    // Element_1
    var element_1 = comp.layer("Element_1")
    element_1("Scale").setValue(conf["Scale"])
    element_1("Position").setValue(conf["Position"])
}

AtomxTypographyUtil.prototype.titleBig_20 = function(conf, comp) {
    // Text_1
    var sourceText = comp.layer("Text_1")("Source Text");
    sourceText.setValue(new TextDocument(conf["text"]));
    var textDocument = sourceText.value;
    sourceText.setValue(textDocument);

    // _controller
    var _controller = comp.layer("_controller")
    _controller("Effects")("Text Color 1")("Color").setValue(colorUtil.hexToRgb1(conf["textColor"]))
    _controller("Effects")("Element Color")("Color").setValue(colorUtil.hexToRgb1(conf["elementColor"]))
}

AtomxTypographyUtil.prototype.titleCalloutL1 = function(conf, comp) {
    // Text_1
    if (conf["textScale"]) {
        comp.layer("Text_1")("Scale").setValue(conf["textScale"])
    }
    var sourceText = comp.layer("Text_1")("Source Text");
    sourceText.setValue(new TextDocument(conf["text"]));
    var textDocument = sourceText.value;
    sourceText.setValue(textDocument);

    // _controller
    var _controller = comp.layer("_controller")
    _controller("Effects")("Text Color")("Color").setValue(colorUtil.hexToRgb1(conf["textColor"]))
    _controller("Effects")("Line Color")("Color").setValue(colorUtil.hexToRgb1(conf["lineColor"]))
    _controller("Effects")("Dot Color")("Color").setValue(colorUtil.hexToRgb1(conf["dotColor"]))
}

var atomxTypographyUtil = new AtomxTypographyUtil();
