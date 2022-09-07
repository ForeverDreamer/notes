function changeLayerName(){
    app.beginUndoGroup('changeLayerName');
    var curComp = app.project.activeItem;
    if ((curComp != null) && (curComp instanceof CompItem)) {
        var selLayers = curComp.selectedLayers;
        var counter ;
        var searchStr, replaceStr, newStr;
        counter = 0;
        searchStr= prompt("Enter search string" , "search text", "Find Layer Names");
        replaceStr= prompt("Enter Replace string" , "replace text", "Replace Layer Names");
        
        for (var i = 0; i < selLayers.length; i++){
            var curLayer = selLayers[i];
            // for (var j = 0; j < curLayer.name.length; j++){
            newStr = curLayer.name.replace(searchStr, replaceStr);
            if (newStr != curLayer.name) {
                curLayer.name = newStr;
                counter ++;
            }
            // }
        }
        alert(counter + " changes were made");

    } else {
           alert("Please select layers to offset");
    }
    app.endUndoGroup();
 }
 
 changeLayerName();
 