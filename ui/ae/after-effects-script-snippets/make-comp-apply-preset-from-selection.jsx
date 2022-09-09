var getFolder = function (_name) {
  // function for gettin a specific folder
  var bFolder;
  for (var i = 1; i <= app.project.numItems; i++) {
    if (app.project.item(i).name == _name && app.project.item(i) instanceof FolderItem) {
      bFolder = app.project.item(i);
    }
  }

  // if ther is no such folder, add it
  if (!bFolder) {
    bFolder = app.project.items.addFolder(_name);
  }
  return bFolder;
};


var main = function () {
  var folder = Folder.myDocuments.fsName + '/Adobe/After Effects CC 2014/User Presets/';
  var ffxone = 'jacobs-keylight-bildecke-01.ffx';
  var ffxtwo = 'jacobs-keylight-bohnen-01.ffx';
  var ffxthree = 'jacobs-keylight-bohnen-02.ffx';
  var ffxfour = 'jacobs-keylight-braune-tuete-01.ffx';
  var ffxfive = 'jacobs-keylight-kaffee-filter-01.ffx';
  var ffxsix = 'jacobs-keylight-misc-haende-01.ffx';
  var ffxseven = 'jacobs-keylight-kaffeeTrinken-01.ffx';
  var ffxspill1 = 'jacobs-spill-surpress-01.ffx';
  var ffxeight = '';
  var presetfilepath = folder + ffxspill1; // "path/to/mypreset.ffx";
  var pfile = File(presetfilepath);
  if (pfile.exists !== true) {
    alert('Presert file does not exist');
    return;
  }

  app.beginUndoGroup('apply preset create comp');
  var proj = app.project;

  if (proj.selection <= 0) {
    alert('Please select some images to prcess');

  } else {
    var folder = getFolder('greenscreen-precomps');
    for (var i = 0; i < proj.selection.length; i++) {
      if (proj.selection[i] instanceof FootageItem) {
        var item = proj.selection[i];
        var name = item.name + ' key';
        var w = item.width;
        var h = item.height;
        var aspect = item.pixelAspect;
        var fps = 25;
        var dur = 1 / fps;

        var keycomp = proj.items.addComp(name, w, h, aspect, dur, fps);
        var layer = keycomp.layers.add(item, dur);
        layer.applyPreset(pfile);
        keycomp.parentFolder = folder;
        keycomp.openInViewer();
      }
    }

  }
  app.endUndoGroup();
};


var run = function (func) {
  func();
};


run(main);
