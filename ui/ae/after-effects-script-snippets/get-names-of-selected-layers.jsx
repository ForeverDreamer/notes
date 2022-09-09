(function (thisObj) {

  var main = function () {
    var proj = app.project;
    var curComp = proj.activeItem;
    if (!curComp || !(curComp instanceof CompItem)) {
      alert('noComp');
      return;
    }
    var arr = [];
    for (var i = 0; i < curComp.selectedLayers.length; i++) {
      arr.push(curComp.selectedLayers[i].name);

    }
    $.writeln('layername\n' + arr.join('\n'));
  };

  var run = function (f) {
    f();
  };
  run(main);
}(this));
