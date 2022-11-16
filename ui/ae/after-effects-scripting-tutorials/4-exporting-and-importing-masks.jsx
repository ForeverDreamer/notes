// basic var initialisation
var project = app.project;
var comp = project.activeItem;
var currentLine;
var maskCounter = 0;
var layerMask;
var allStuff = new Array();
var exportArray = new Array();
var allVertices = new Array();
var allInTangents = new Array();
var allOutTangents = new Array();

var maskShape = new Shape();
var importShape = new Shape();

// UI
var mainWindow = new Window("palette", "Mask Importer/Exporter", undefined);
mainWindow.orientation = "column";

var groupOne = mainWindow.add("group", undefined, "groupOne");
groupOne.orientation = "row";
var importButton = groupOne.add("button", undefined, "Import Mask");
var exportButton = groupOne.add("button", undefined, "Export Mask");

mainWindow.center();
mainWindow.show();

// Importing mask information
importButton.onClick = function () {
    app.beginUndoGroup("Import Mask");
    var importFile = new File;
    importFile = importFile.openDlg("Choose Mask Text File", "Text File:*.txt");

    var fpath = importFile.absoluteURI;
    readDocument(importFile);

    var newComp = project.items.addComp("Import Mask", 1920, 1080, 1, 10, 30);
    newComp.openInViewer();
    var vParse;
    var vArray;
    var allVs = [];
    var allIs = [];
    var allOs = [];
    var iParse;
    var iArray;
    var oParse;
    var oArray;
    var importLayer = newComp.layers.addSolid([1, 1, 1], "Mask Layer", 1920, 1080, 1, 10);
    // generate and apply masks
    for (var e = 0; e < maskCounter; e++) {
        vParse = allVertices[e].toString();
        vArray = vParse.split(",");
        while (vArray.length > 0) {
            allVs.push(vArray.splice(0, 2));
        }
        //alert(allInTangents[e]);
        iParse = allInTangents[e].toString();
        iArray = iParse.split(",");
        while (iArray.length > 0) {
            allIs.push(iArray.splice(0, 2));
        }
        oParse = allOutTangents[e].toString();
        oArray = oParse.split(",");
        while (oArray.length > 0) {
            allOs.push(oArray.splice(0, 2));
        }

        importShape.vertices = allVs;
        importShape.inTangents = allIs;
        importShape.outTangents = allOs;

        layerMask = importLayer.Masks.addProperty("Mask");
        layerMask.property("ADBE Mask Shape").setValue(importShape);
    }
    app.endUndoGroup();
    alert("Import Successful");
}


// exporint mask information
exportButton.onClick = function () {
    app.beginUndoGroup("Export Mask");

    var layer = comp.layer(1);
    var numMasks = layer.property("Masks").numProperties;
    for (var q = 1; q <= numMasks; q++) {


        var myPath = layer.property("Masks").property("Mask " + q).property("Mask Path");

        var myVertices = layer.property("Masks").property("Mask " + q).property("Mask Path").value.vertices;
        var myInTangents = layer.property("Masks").property("Mask " + q).property("Mask Path").value.inTangents;
        var myOutTangents = layer.property("Masks").property("Mask " + q).property("Mask Path").value.outTangents;
        maskShape.vertices = myVertices;
        maskShape.inTangents = myInTangents;
        maskShape.outTangents = myOutTangents;

        var mainString = "mask " + q + "\r\n" + "vertices = " + maskShape.vertices.toString() + "\r\n" + "intangents = " + maskShape.inTangents.toString() + "\r\n" + "outtangents = " + maskShape.outTangents.toString() + "\r\n";
        exportArray.push(mainString);
    }

    exportArray = exportArray.join("\r\n");

    var myFile = new File("~/Desktop/mask.txt");
    myFile.open("w")
    myFile.encoding = "UTF-8";
    myFile.write(exportArray);
    myFile.close();

    app.endUndoGroup();
    alert("Export Successful");
}

// reading, parsing, and storing info in text file
function readDocument(inputDoc) {
    var thisDoc = new File(inputDoc);
    if (thisDoc.exists) {
        thisDoc.open("r");
        while (!thisDoc.eof) {
            currentLine = thisDoc.readln();
            allStuff.push(currentLine);
        }
        thisDoc.close();
    }

    var thisLine;
    var equalsCharIndex;
    var tempLine;
    for (var i = 0; i < allStuff.length; i++) {
        thisLine = allStuff[i];
        //alert(thisLine);
        if (thisLine.match(/mask/g)) {
            maskCounter++;
            // alert("mask");
        }
        if (thisLine.match(/vertices =/g)) {
            equalsCharIndex = thisLine.indexOf("=");
            tempLine = thisLine.slice(equalsCharIndex + 1, thisLine.length);
            allVertices.push(tempLine);
            //alert("vertices")
        }
        if (thisLine.match(/intangents =/g)) {
            equalsCharIndex = thisLine.indexOf("=");
            tempLine = thisLine.slice(equalsCharIndex + 1, thisLine.length);
            allInTangents.push(tempLine);
            //alert("hintangetns");
        }
        if (thisLine.match(/outtangents =/g)) {
            equalsCharIndex = thisLine.indexOf("=");
            tempLine = thisLine.slice(equalsCharIndex + 1, thisLine.length);
            allOutTangents.push(tempLine);
            //alert("outtahere");
        }
    }
}