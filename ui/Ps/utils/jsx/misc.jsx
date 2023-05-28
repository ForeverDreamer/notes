function MiscUtil() {
}

MiscUtil.prototype.closeAllDocuments = function () {
    while (app.documents.length) {
		app.activeDocument.close(SaveOptions.DONOTSAVECHANGES)
	}
}

MiscUtil.prototype.openDocument = function (path) {
    return app.open(File(path))
}


var miscUtil = new MiscUtil();