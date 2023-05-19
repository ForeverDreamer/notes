#includepath "./utils/jsx";
#include "misc.jsx";

var BASE_DIR = "~/Desktop"
var fileName = 'myDocument'

app.bringToFront();
// var doc = app.documents.add(800, 500, 72, fileName, NewDocumentMode.RGB)
// doc.saveAs(File(BASE_DIR + fileName + ".psd"))

miscUtil.closeAllDocuments()
var ironmanDoc = miscUtil.openDocument(BASE_DIR + "/iron man.jpg")
var mjDoc = miscUtil.openDocument(BASE_DIR + "/MJ.jpg")
// $.writeln(doc.fullName)
var mergeWidth;
var mergeHeight;
var mergeResolution;
if (ironmanDoc.width.value * ironmanDoc.height.value > mjDoc.width.value * mjDoc.height.value ) {
    app.activeDocument = mjDoc
    mergeWidth = ironmanDoc.width
    mergeHeight = ironmanDoc.height
    mergeResolution = ironmanDoc.resolution
    mjDoc.resizeImage(ironmanDoc.width, ironmanDoc.height)
} else {
    app.activeDocument = ironmanDoc
    mergeWidth = mjDoc.width
    mergeHeight = mjDoc.height
    mergeResolution = mjDoc.resolution
    ironmanDoc.resizeImage(mjDoc.width, mjDoc.height)
}

var mergeDoc = app.documents.add(mergeWidth, mergeHeight*2, mergeResolution, 'mergeDoc')

app.activeDocument = mjDoc
mjDoc.activeLayer.copy()
app.activeDocument = mergeDoc
var selRegion = Array(
    Array(0, 0), 
    Array(mergeDoc.width.value, 0), 
    Array(mergeDoc.width.value, mergeDoc.height.value/2),
    Array(0, mergeDoc.height.value/2),
    Array(0, 0)
)
mergeDoc.selection.select(selRegion)
mergeDoc.paste(true)

app.activeDocument = ironmanDoc
ironmanDoc.activeLayer.copy()
app.activeDocument = mergeDoc
mergeDoc.selection.select(selRegion)
mergeDoc.selection.invert()
mergeDoc.paste(true)

mjDoc.close(SaveOptions.DONOTSAVECHANGES)
ironmanDoc.close(SaveOptions.DONOTSAVECHANGES)
// var artLayer = doc.artLayers.add()
// var artLayer = doc.artLayers.getByName("Layer 1")
// artLayer.name = "My layer"
// $.writeln(artLayer.name)
// app.activeDocument
// app.activeDocument.close()

// while (app.documents.length) {
//     app.activeDocument.close()
// }
// ElementPlacement.INSIDE