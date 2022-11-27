#includepath "./utils;";
#include "json.jsx";
#include "share.jsx";
#include "color.jsx";


// [colorUtil.hexToRgb("#FF0000", true), colorUtil.hexToRgb("#00FF18", true), colorUtil.hexToRgb("#005FB8", true)]
// $.writeln(colorUtil.hexToRgb("#005FB8", true))
var effects = app.effects
for (var i = 0; i < effects.length; i++) {
    $.writeln(effects[i].category + ',' + effects[i].displayName + ',' + effects[i].matchName)
}

// var taskId = app.scheduleTask('$.writeln(app.findMenuCommandId("AtomX"))', 1000, true)
// $.writeln(taskId)
// $.writeln(app.findMenuCommandId("AtomX"))
// $.writeln(app.findMenuCommandId("Animation Composer 3"))
// app.executeCommand(5020);
