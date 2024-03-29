/**
 * @author fabiantheblind
 * @description adds text to a comp with UI
 *
 *
 * @todo check if it works
 */

/**
 *  function template by @author fabiantheblind
 */
(function (thisObj) {
  // basic panel
  simple(thisObj);
  /**
   * [simple description]
   * @param  {[type]} thisObj [description]
   * @return {[type]}         [description]
   */
  function simple(thisObj) {

    // this is global
    data = {
      x: 10,
      y: 10,
      text: '',
      counter: 0,
      precompose: false,
      precompname: 'precomp',
      split: false,
      addbg: false
    };


    // THIS WILL CHECK IF PANEL IS DOCKABLE OR FLAOTING WINDOW
    var win = buildUI(thisObj);
    if ((win !== null) && (win instanceof Window)) {
      win.center();
      win.show();
    } // end if win  null and not a instance of window

    function buildUI(thisObj) {
      var H = 25; // the height
      var W = 30; // the width
      var G = 5; // the gutter
      var x = G;
      var y = G;
      var win = (thisObj instanceof Panel) ? thisObj : new Window('palette', 'window', [0, 0, G * 3 + W * 6, G * 6 + H * 4], { resizeable: true });

      if (win !== null) {
        win.txt = win.add('edittext', [x, y, x + W * 3, y + H], '');
        x += W * 3 + G;
        win.do_it_button = win.add('button', [x, y, x + W * 3, y + H], 'do it');
        x = G;
        y += H + G;
        win.precompose_check = win.add('checkbox', [x, y, x + W * 3, y + H], 'precompose');
        x = G;
        y += H + G;
        win.split_check = win.add('checkbox', [x, y, x + W * 3, y + H], 'split csv');
        x = G;
        y += H + G;
        win.addbg_check = win.add('checkbox', [x, y, x + W * 3, y + H], 'add bg');


        win.addbg_check.onClick = function () {
          data.addbg = this.value;
        };
        win.split_check.onClick = function () {
          data.split = this.value;
        };
        win.precompose_check.onClick = function () {
          data.precompose = this.value;
        };

        win.do_it_button.onClick = function () {
          data.counter++;
          run();
        };

        win.txt.onChange = function () {
          data.text = this.text;
        };
      }
      return win;
    }
    function run() {
      // "in function run. From here on it is a straight run"

      var curComp = app.project.activeItem;
      if (!curComp || !(curComp instanceof CompItem)) {
        alert('please select a comp');
        return;
      }
      // if(curComp.selectedLayers.length < 1){
      //     alert('Please select at least one layer');
      // return;
      //  }
      app.beginUndoGroup('run function');

      var parentLayer = null;
      var layerslist = [];
      if (data.addbg) {
        var solid = curComp.layers.addSolid([1, 1, 1], 'bg', curComp.width, curComp.height, 1, curComp.duration);
        layerslist.push(solid);
      }
      var txt = null;

      if (!data.split) {

        txt = curComp.layers.addText(data.text);

        layerslist.push(txt);
      } else {
        var words = split_csv(',', data.text);
        data.precompname = words[0];
        for (var i = 0; i < words.length; i++) {
          var w = words[i];
          txt = curComp.layers.addText(w);
          var textProp = txt.property('Source Text');
          var textDocument = textProp.value;

          txt.threeDLayer = true;
          if (i === 0) {
            parentLayer = txt;
            textDocument.fontSize = 100;
          } else {
            textDocument.fontSize = 50;
            var x = (Math.random() * 1000) - 500;
            var y = (Math.random() * 1000) - 500;
            var z = (Math.random() * 1000) - 500;
            txt.transform.position.setValue([x, y, z]);
            txt.setParentWithJump(parentLayer);

          }
          txt.transform.position.expression = 'wiggle(0.5,40)';
          layerslist.push(txt);
          textProp.setValue(textDocument);
        }
      }

      if (data.precompose === true) {

        precomper(layerslist, curComp, data.precompname);


      }
      app.endUndoGroup();
    }

    // my personal precomposer

    /**
     * This is a string prototype function
     * found here http://www.greywyvern.com/?post=258
     * @param  {String} sep is the separator we use only ,
     * @return {Array}     returns an Array of strings
     */
    // String.prototype.splitCSV = function(sep) {
    //   for (var foo = this.split(sep = sep || ","), x = foo.length - 1, tl; x >= 0; x--) {
    //     if (foo[x].replace(/"\s+$/, '"').charAt(foo[x].length - 1) === '"') {
    //       if ((tl = foo[x].replace(/^\s+"/, '"')).length > 1 && tl.charAt(0) === '"') {
    //         foo[x] = foo[x].replace(/^\s*"|"\s*$/g, '').replace(/""/g, '"');
    //       } else if (x) {
    //         foo.splice(x - 1, 2, [foo[x - 1], foo[x]].join(sep));
    //       } else foo = foo.shift().split(sep).concat(foo);
    //     } else foo[x].replace(/""/g, '"');
    //   } return foo;
    // };


    // Dont use prototypes?
    // for the time beeing YES
    // Makes problems with other scripts
    // or we need to use a unique prefix! like ftb_splitCSV

    function split_csv(sep, the_string) {

      for (var foo = the_string.split(sep = sep || ','), x = foo.length - 1, tl; x >= 0; x--) {
        if (foo[x].replace(/"\s+$/, '"').charAt(foo[x].length - 1) === '"') {
          if ((tl = foo[x].replace(/^\s+"/, '"')).length > 1 && tl.charAt(0) === '"') {
            foo[x] = foo[x].replace(/^\s*"|"\s*$/g, '').replace(/""/g, '"');
          } else if (x) {
            foo.splice(x - 1, 2, [foo[x - 1], foo[x]].join(sep));
          } else {
            foo = foo.shift().split(sep).concat(foo);
          }
        } else {
          foo[x].replace(/""/g, '"');
        }
      }
      return foo;
    }

    function precomper(arrOLayers, curComp, name) {

      var layerIndices = []; // precompose takes layer inidcies
      // loop thru a list of layer
      for (var l = 0; l < arrOLayers.length; l++) {
        // and push their index into an array
        layerIndices[layerIndices.length] = arrOLayers[l].index;
      }

      // now precompose the result
      var newComp = curComp.layers.precompose(layerIndices, name, true);
      // newComp.parentFolder = folder;
      // it is the selected layer
      var preCompedLayer = curComp.selectedLayers[0];
    }
  }// close run
}(this));
