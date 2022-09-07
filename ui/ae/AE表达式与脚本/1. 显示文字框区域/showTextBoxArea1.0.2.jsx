function showTextBoxAreaSourceRect(){
    app.beginUndoGroup('textBoxSize');
    var curComp = app.project.activeItem;

    if ((curComp != null) && (curComp instanceof CompItem)) {
        
        var selLayers = curComp.selectedLayers;
        for (var i = 0; i < selLayers.length; i++){           
                var curTextLayer = selLayers[i];
                var isTextLayer = checkLayerType(curTextLayer);
                if (isTextLayer) {
                    var textScaleTemp = curTextLayer.property("ADBE Transform Group")(6).value;
                    curTextLayer.property("ADBE Transform Group")(6).setValue([100,100]);
                    var xBox = curTextLayer.sourceText.value.boxTextSize[0];
                    var yBox = curTextLayer.sourceText.value.boxTextSize[1];
                    var boxTextLayerPos = curTextLayer.sourceText.value.boxTextPos;
                    var boxTextCompPos = curTextLayer.sourcePointToComp(boxTextLayerPos);
                    var textPos = curTextLayer.property("ADBE Transform Group")(2).value; //text position
                    var shapeLayer = addTextBox(curTextLayer, xBox, yBox, boxTextCompPos, textPos);
                    curTextLayer.property("ADBE Transform Group")(6).setValue(textScaleTemp);
                   
                }else{ 
                    alert("Not paragraph text layer")
                    break;
                }
           
            }
        
    } else {
           alert("Please select a composition");
    }
    app.endUndoGroup();

    function checkLayerType(layer) {
        if ((layer != null) & (layer instanceof TextLayer)) {
            if (layer.property("Source Text").value.pointText == false) {
                return true;
            }else {
                return false;
            }
            
        } else {
            return false;
        }
    }


    function addTextBox(layer, x, y, pos, position) {
        var greyColor = [120/255,120/255,120/255];
        var textBoxLayer = curComp.layers.addShape();
        textBoxLayer.moveAfter(layer);
        textBoxLayer.name = "Text Box";
        textBoxLayer.guideLayer = true;
        
        //set anchor point to text box layer
        var p1 = pos + [x, y]/2;
        var difPos = position - p1;
        textBoxLayer.property("ADBE Transform Group")(2).setValue(p1 + difPos); //transform.position
        textBoxLayer.property("ADBE Transform Group")(1).setValue(difPos); //transform.position

        var addShapeGroup = textBoxLayer.property("Contents").addProperty("ADBE Vector Group");
        var addShape = addShapeGroup.property("Contents").addProperty("ADBE Vector Shape - Rect");
        addShape(2).setValue([x,y] + [5,5]);
        var shapeColor = addShapeGroup.property("Contents").addProperty("ADBE Vector Graphic - Fill");
        shapeColor(4).setValue(greyColor);
        textBoxLayer.property("ADBE Transform Group")(11).setValue(50);
        //textBoxLayer.property("ADBE Transform Group")(6).setValue(scale);
        textBoxLayer.parent = layer;
        textBoxLayer.inPoint = layer.inPoint;
        textBoxLayer.outPoint = layer.outPoint;
        textBoxLayer.locked = true;
        return textBoxLayer;
    }   

 }
 
 showTextBoxAreaSourceRect();
 