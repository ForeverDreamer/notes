var project = app.project;
var comp = project.activeItem;
var layer = comp.layer(1);
var threshold = 1;

var mainWindow = new Window("palette", "Auto Jump Cutter", undefined);
mainWindow.orientation = "column";

var groupOne = mainWindow.add("group", undefined, "groupOne");
groupOne.add("statictext", undefined, "Select a comp and layer, set padding, and run to auto-edit");

var groupTwo = mainWindow.add("group", undefined, "groupTwo");
groupTwo.orientation = "row";
groupTwo.add("statictext", undefined, "Padding (frames)");
var pad = groupTwo.add("edittext", undefined, "5");
pad.size = [60, 25];

var groupThree = mainWindow.add("group", undefined, "groupThree");
var button = groupThree.add("button", undefined, "Go!");

mainWindow.center();
mainWindow.show();

button.onClick = function () {
    app.beginUndoGroup("Auto Editing");
    convertAudio();

    var keyInfo = calculateKeys();

    editVideo(keyInfo[0], keyInfo[1]);
    alert("Completed!", "Success");
    app.endUndoGroup();
}


function convertAudio() {
    app.executeCommand(app.findMenuCommandId("Convert Audio to Keyframes"));
}

function calculateKeys() {
    var keyTimes = new Array();
    var keyValues = new Array();
    var audioLayer = comp.layer(1);
    var slider = audioLayer("Effects")("Both Channels")("Slider");
    for (var i = 1; i <= slider.numKeys; i++) {
        keyTimes.push(slider.keyTime(i));
        keyValues.push(slider.keyValue(i));
    }
    audioLayer.remove();
    return [keyTimes, keyValues];
}

function editVideo(keyTimes, keyValues) {
    var inAndOutTimes = new Array();
    var isRun = false;
    var counter = 0;
    var padding = parseInt(pad.text);
    for (var i = 0; i < keyTimes.length; i++) {
        if (!isRun) {
            if (keyValues[i] >= threshold) {
                isRun = true;
                if (keyValues[i - padding] >= 0) {
                    inAndOutTimes[inAndOutTimes.length] = keyTimes[i - padding];
                }
                else {
                    inAndOutTimes[inAndOutTimes.length] = keyTimes[0];
                }
            }
        }
        else {
            if (keyValues[i] < threshold) {
                counter++;
                if (counter >= padding) {
                    isRun = false;
                    counter = 0;
                    inAndOutTimes[inAndOutTimes.length] = keyTimes[i - 1];
                }
            }
            if (keyValues[i] >= threshold) {
                counter = 0;
            }
        }
    }

    for (var e = 0; e < inAndOutTimes.length; e += 2) {
        var currentLayer = layer.duplicate();
        currentLayer.inPoint = inAndOutTimes[e];
        currentLayer.outPoint = inAndOutTimes[e + 1];
    }
    layer.remove();
    var startTime = 0;
    for (var z = 1; z <= comp.numLayers; z++) {
        var thisLayer = comp.layer(z);
        thisLayer.name = z;
        thisLayer.startTime = startTime - thisLayer.inPoint;
        startTime = thisLayer.outPoint;
    }
    comp.workAreaDuration = comp.layer(comp.numLayers).outPoint;
    app.executeCommand(app.findMenuCommandId("Trim Comp to Work Area"));
}