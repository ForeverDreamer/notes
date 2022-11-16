var project = app.project;
var comp = project.activeItem;

/*
// layer collection
var allComps = new Array();
var allText = new Array();
var allLayers = new Array();
*/

// predefined information setup
var fontSize = 100;
var fillColour = new Array(0, 0, 0);
var strokeColour = new Array(0, 0, 0);
var font = "TimesNewRomanPSMT";
var effectMatchName = "ADBE Black&White";
var scalePercent = 1.1;

// UI creation
var mainWindow = new Window("palette", "Batch Processor", undefined);
mainWindow.orientation = "column";

var groupOne = mainWindow.add("group", undefined, "groupOne");
groupOne.orientation = "row";
var timeButton = groupOne.add("button", undefined, "T:0");
timeButton.helpTip = "Changes all compositions' beginning timecodes to 0 seconds";
var textButton = groupOne.add("button", undefined, "Texter");
textButton.helpTip = "Changes every text layer in a selected comp to predefined values";

var groupTwo = mainWindow.add("group", undefined, "groupTwo");
groupTwo.orientation = "row";
var effectsButton = groupTwo.add("button", undefined, "Fx");
effectsButton.helpTip = "Applies " + effectMatchName + " to every layer in the selected comp";
var scaleButton = groupTwo.add("button", undefined, "Scaler");
scaleButton.helpTip = "Multiplies the scale of every layer in the selected comp by " + scalePercent + "%";

mainWindow.center();
mainWindow.show();

// functionality 
timeButton.onClick = function () {
    app.beginUndoGroup("Comp Timecodes to 0");
    for (var i = 1; i <= project.numItems; i++) {
        if (project.item(i) instanceof CompItem) {
            project.item(i).displayStartTime = 0;
        }
    }
    app.endUndoGroup();
    alert("Completed Successfully!", "Timecodes Finished");
}

textButton.onClick = function () {
    app.beginUndoGroup("Change all text layers");
    for (var i = 1; i <= comp.numLayers; i++) {
        if (comp.layer(i) instanceof TextLayer) {
            var textProp = comp.layer(i).property("Source Text");
            var textDocument = textProp.value;
            textDocument.fontSize = fontSize;
            textDocument.fillColor = fillColour;
            textDocument.strokeColor = strokeColour;
            textDocument.font = font;
            textProp.setValue(textDocument);
        }
    }
    app.endUndoGroup();
    alert("Completed Successfully!", "Text Finished");
}

effectsButton.onClick = function () {
    app.beginUndoGroup("Apply Effects");
    for (var i = 1; i <= comp.numLayers; i++) {
        comp.layer(i).Effects.addProperty(effectMatchName);
    }
    app.endUndoGroup();
    alert("Completed Successfully!", "Effects Finished");
}

scaleButton.onClick = function () {
    app.beginUndoGroup("Scale all layers");
    for (var i = 1; i <= comp.numLayers; i++) {
        var curScale = comp.layer(i).property("Scale").value;
        var newScale = curScale * scalePercent;

        comp.layer(i).property("Scale").setValue(newScale);
    }
    app.endUndoGroup();
    alert("Completed Successfully!", "Scaling Finished");
}