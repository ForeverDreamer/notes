function MiscUtil() {
}

MiscUtil.prototype.closeAllDocuments = function () {
    while (app.documents.length) {
        app.activeDocument.close(SaveOptions.DONOTSAVECHANGES)
    }
}

MiscUtil.prototype.addDocument = function (conf) {
    var colorSpace = DocumentColorSpace.RGB
    var width = DOC_WIDTH
    var height = DOC_HEIGHT

    if (conf) {
        if (conf['colorSpace']) {
            colorSpace = conf['colorSpace']
        }
        if (conf['size']) {
            var size = conf['size']
            width = size['width']
            height = size['height']
        }
        if (conf['artboard']) {
            return app.documents.add(
                colorSpace, width, height,
                conf['artboard']['numArtBoards'], conf['artboard']['artboardLayout'],
                conf['artboard']['artboardSpacing'], conf['artboard']['artboardRowsOrCols']
            )
        }
    }
    
    return app.documents.add(colorSpace, width, height);
}

MiscUtil.prototype.setColor = function (obj, prop, hex) {
    var values = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    var rgbColor = new RGBColor();
    rgbColor.red = parseInt(values[1], 16);
    rgbColor.green = parseInt(values[2], 16);
    rgbColor.blue = parseInt(values[3], 16);
    obj[prop] = rgbColor;
}

var miscUtil = new MiscUtil();