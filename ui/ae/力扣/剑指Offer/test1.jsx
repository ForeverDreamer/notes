#includepath "../../utils/jsx;";
#include "constants.jsx";
#include "json.jsx";
#include "animation.jsx";
#include "share.jsx";
#include "color.jsx";
#include "effects.jsx";
#include "presets.jsx";
#include "text.jsx";
#include "shape.jsx";
#include "precomp.jsx"

var project = app.project;
var comp = project.activeItem;
// var layer = comp.layer(1)
// var path = layer("Contents")("Rectangle 1")("Contents")("Path 1")("Path").value
// $.writeln(path.vertices)
// $.writeln(path.inTangents)
// $.writeln(path.outTangents)

var shapeLayer = shapeUtil.add(
    comp, 
    "Node.Drop.15", 
    {
        "pathGroup": {
            "type": "Group", 
            "vertices": [[0, -50], [50, 0], [0, 50], [-50, 0]],
            "inTangents": [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0], [0, 27.6142425537109]],
            "outTangents": [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0], [0, -27.6142425537109]],
            "closed": true
        },
        "Fill": {"Color": colorUtil.hexToRgb1("#FF0000")},
        "Position": [188, 444],
        "keyframes": {
            "Transform.Position": [[0, 1], [[188, 444], [188, 750]]],
            "Transform.Rotation": [[0, 1], [0, 45]],
            "Contents.Group 1.Contents.Path 1.Path": [
                [0, 1], 
                [
                    {
                        "vertices": [[0, -50], [50, 0], [0, 50], [-50, 0]],
                        "inTangents": [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0], [0, 27.6142425537109]],
                        "outTangents": [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0], [0, -27.6142425537109]],
                        "closed": true
                    }, 
                    {
                        "vertices": [[0, -50], [50, 0], [0, 50], [-50, 0]],
                        // "vertices": [[47,-60.5], [-38,-60.5], [-38,24.5], [47,24.5]],
                        // "inTangents": [[-27.6142425537109, 0], [0, -27.6142425537109], [27.6142425537109, 0], [0, 27.6142425537109]],
                        // "outTangents": [[27.6142425537109, 0], [0, 27.6142425537109], [-27.6142425537109, 0], [0, -27.6142425537109]],
                        "closed": true
                    }
                ]]
        }
    }
)