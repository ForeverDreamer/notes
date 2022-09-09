/**
 * Set the output file for all outputmodules for all items in the renderque
 * @return {[type]} [description]
 */
var main = function () {
  var p = app.project;
  var rq = p.renderQueue;
  var targetFolder = Folder.selectDialog('Select your outputfolder');
  if (targetFolder === null) {
    return;
  }
  app.beginUndoGroup('Set OM output location');
  for (var i = 1; i < rq.numItems + 1; i++) {
    var n = rq.item(i).comp.name;
    n = n.replace(new RegExp('\.jpg'), '');
    for (var j = 1; j < rq.item(i).numOutputModules + 1; j++) {
      var om = rq.item(i).outputModule(j);
      var path = targetFolder.fsName + '/' + n + '_[#####].tif';
      $.writeln(path);
      om.file = File(path);
    }
  }
  app.endUndoGroup();
  return 0;
};


var run = function (func) {
  if (parseInt(app.version, 10) < 13) {
    alert('This script is written for AE CC 2014\n Could also work in older versions');
    return func();
    // return;
  }
  return func();


};
run(main);
