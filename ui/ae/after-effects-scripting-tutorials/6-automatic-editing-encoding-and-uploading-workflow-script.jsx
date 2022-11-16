app.beginUndoGroup("Import and rendering test");

var myFolder = new Folder("~\\Desktop\\test");
var myImportOptions = new ImportOptions();
var importedLayers = new Array();

var myFiles = myFolder.getFiles("*.mp4");
var myAudioFiles = myFolder.getFiles("*.mp3");
var allMyFiles = myFiles.concat(myAudioFiles);

var numFiles = allMyFiles.length;
var numAudio = 0;
var numVisual = 0;
var audioArray = new Array();
var visualArray = new Array();
for (var i = 0; i < allMyFiles.length; i++) {
    myImportOptions.file = allMyFiles[i];
    importedLayers.push(app.project.importFile(myImportOptions));
}

var duration = 0;
for (var e = 1; e <= app.project.numItems; e++) {
    if (app.project.item(e).hasVideo == true) {
        numVisual++;
        visualArray.push(app.project.item(e));
        duration += app.project.item(e).duration;
    }
    if (app.project.item(e).hasVideo == false && app.project.item(e).hasAudio == true) {
        numAudio++;
        audioArray.push(app.project.item(e));
    }
}

var tempComp = app.project.items.addComp("This is a test comp", 1920, 1080, 1, duration, 30);
tempComp.openInViewer();
var startTime = 0;
for (var q = 0; q < visualArray.length; q++) {

    var thisLayer = tempComp.layers.add(visualArray[q]);
    thisLayer.audioEnabled = false;
    thisLayer.startTime = startTime;
    startTime = thisLayer.outPoint;
}
var audioLayer = tempComp.layers.add(audioArray[0]);
audioLayer.outPoint = duration;
alert("pause")
var myFile = new File("~\\Desktop\\test\\ae renders\\" + tempComp.name + ".mov");
var theRender = app.project.renderQueue.items.add(tempComp);
theRender.outputModules[1].applyTemplate("MOV H.264 10Mbps Q:85");
theRender.outputModules[1].file = myFile;
app.endUndoGroup();
app.project.renderQueue.render();

app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.newProject();