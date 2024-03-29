// Copyright (c)  2013
// Fabian "fabiantheblind" Morón Zirfas
// for all comps in panel
//
// do something
//
// Permission is hereby granted, free of charge, to any
// person obtaining a copy of this software and associated
// documentation files (the "Software"), to deal in the Software
// without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense,
// and/or sell copies of the Software, and to  permit persons to
// whom the Software is furnished to do so, subject to
// the following conditions:
// The above copyright notice and this permission notice
// shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
// OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
// IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
// DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF  CONTRACT,
// TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTIO
// WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

// see also http://www.opensource.org/licenses/mit-license.php

(function (thisObj) {

  run(thisObj);

  function run(thisObj) {

    var script_data = {
      scale_factor: 4.0,
      scirptname: File($.fileName),
      presets: {

        path: '/Applications/Adobe After Effects CS6/Presets/User Presets/volkswagen/',
        names: [
          '[VolksWagen Besucherdienste] placeholder quick and dirty key.ffx'
        ]
      }
    };

    doApplyPreset(script_data);
    // doScale(script_data);

  }

  // var curComp = app.project.activeItem;
  //    if (!curComp || !(curComp instanceof CompItem)){
  //         alert("noComp");
  //         return;
  //     };


  //                   | |
  //   __ _ _ __  _ __ | |_   _
  //  / _` | '_ \| '_ \| | | | |
  // | (_| | |_) | |_) | | |_| |
  //  \__,_| .__/| .__/|_|\__, |
  //       | |   | |       __/ |
  //       |_|   |_|      |___/
  //  _____                    _
  // |  __ \                  | |
  // | |__) | __ ___  ___  ___| |_
  // |  ___/ '__/ _ \/ __|/ _ \ __|
  // | |   | | |  __/\__ \  __/ |_
  // |_|   |_|  \___||___/\___|\__|


  function doApplyPreset(data) {

    var preset = null;
    var presetFile = File(data.presets.path + data.presets.names[0]);

    if (presetFile.exists === false) {
      alert('preset file does not exist');
      return;
    }
    app.beginUndoGroup('do presetFile');
    var errlog = '';
    for (var i = 0; i < app.project.selection.length; i++) {
      var activeItem = app.project.selection[i];// = app.project.activeItem;
      if ((activeItem === null) || !(activeItem instanceof CompItem)) {
        errlog += ('Please select or open a composition first.' + data.scriptName);
      } else {
        // var activeComp = activeItem;
        for (var j = 1; j <= activeItem.numLayers; j++) {
          var curLayer = activeItem.layer(j);
          curLayer.selected = true;
          curLayer.applyPreset(presetFile);
        } // end j loop
      } // end else active item not a comp
    } // end i loop
    app.endUndoGroup();
    alert('error log' + errlog);

    presetFile.close();// always close files
  }

  // ------------ end of apply preset ------------
  //   _____  _____          _      ______
  //  / ____|/ ____|   /\   | |    |  ____|
  // | (___ | |       /  \  | |    | |__
  //  \___ \| |      / /\ \ | |    |  __|
  //  ____) | |____ / ____ \| |____| |____
  // |_____/ \_____/_/    \_\______|______|

  /**
   * the following functions are taken from the Scale Composition.jsx delivered with AE by Adobe
   * @param  {[type]} data [description]
   * @return {[type]}      [description]
   */
  function doScale(data) {
    // By bracketing the operations with begin/end undo group, we can
    // undo the whole script with one undo operation.
    app.beginUndoGroup('do sale');

    for (var i = 0; i < app.project.selection.length; i++) {

      var activeItem = app.project.selection[i];// = app.project.activeItem;
      if ((activeItem === null) || !(activeItem instanceof CompItem)) {
        alert('Please select or open a composition first.', data.scriptName);
      } else {
        // Validate the input field, in case the user didn't defocus it first (which often can be the case).
        // this.parent.parent.optsRow.text_input.notify("onChange");

        var activeComp = activeItem;

        // app.beginUndoGroup(data.scriptName);

        // Create a null 3D layer.
        var null3DLayer = activeItem.layers.addNull();
        null3DLayer.threeDLayer = true;

        // Set its position to (0,0,0).
        null3DLayer.position.setValue([0, 0, 0]);

        // Set null3DLayer as parent of all layers that don't have parents.
        makeParentLayerOfAllUnparented(activeComp, null3DLayer);

        // Set new comp width and height.

        activeComp.width = Math.floor(activeComp.width * data.scale_factor);
        activeComp.height = Math.floor(activeComp.height * data.scale_factor);

        // Then for all cameras, scale the Zoom parameter proportionately.
        scaleAllCameraZooms(activeComp, data.scale_factor);

        // Set the scale of the super parent null3DLayer proportionately.
        var superParentScale = null3DLayer.scale.value;
        superParentScale[0] *= data.scale_factor;
        superParentScale[1] *= data.scale_factor;
        superParentScale[2] *= data.scale_factor;
        null3DLayer.scale.setValue(superParentScale);

        // Delete the super parent null3DLayer with dejumping enabled.
        null3DLayer.remove();

        // app.endUndoGroup();

        // Reset data.scale_factor to 1.0 for next use.
        // ~         data.scale_factor = 1.0;
        // ~         if (this.parent.parent.optsRow.scaleButton.value) {
        // ~           this.parent.parent.optsRow.text_input.text = "1.0";
        // ~         }
      }
    }
    app.endUndoGroup();

  } // close onScaleClick

  //
  // Scales the zoom factor of every camera by the given scale_factor.
  // Handles both single values and multiple keyframe values.
  function scaleAllCameraZooms(theComp, scaleBy) {
    for (var i = 1; i <= theComp.numLayers; i++) {
      var curLayer = theComp.layer(i);
      if (curLayer.matchName === 'ADBE Camera Layer') {
        var curZoom = curLayer.zoom;
        if (curZoom.numKeys === 0) {
          curZoom.setValue(curZoom.value * scaleBy);
        } else {
          for (var j = 1; j <= curZoom.numKeys; j++) {
            curZoom.setValueAtKey(j, curZoom.keyValue(j) * scaleBy);
          }
        }
      }
    }
  }
  // Sets newParent as the parent of all layers in theComp that don't have parents.
  // This includes 2D/3D lights, camera, av, text, etc.
  //
  function makeParentLayerOfAllUnparented(theComp, newParent) {
    for (var i = 1; i <= theComp.numLayers; i++) {
      var curLayer = theComp.layer(i);
      if (curLayer !== newParfent && curLayer.parent === null) {
        curLayer.parent = newParent;
      }
    }
  }
  // ------------ end of scale functions ------------


}(this));
