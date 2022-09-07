function trimLayerIOPoint(){
    app.beginUndoGroup('trimLayerIOPoint');
    var curComp = app.project.activeItem;
    if ((curComp != null) && (curComp instanceof CompItem)) {
        var selLayers = curComp.selectedLayers;
        var lastSelLayer;
        var tarInPoint, tarOutPoint;
        var tarIndex = selLayers.length-1;
        lastSelLayer = selLayers[tarIndex];
        tarInPoint = lastSelLayer.inPoint;
        tarOutPoint = lastSelLayer.outPoint;
        for (var i = 0; i < (selLayers.length - 1); i++){
            var curLayer = selLayers[i];
            curLayer.inPoint = tarInPoint;
            curLayer.outPoint = tarOutPoint;
        }

    } else {
           alert("Please select layers to offset");
    }
    app.endUndoGroup();
 }
 
 trimLayerIOPoint();
 