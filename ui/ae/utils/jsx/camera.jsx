function CameraUtil() {}

CameraUtil.prototype.add = function(name, centerPoint, props, keyframes) {
    var cameraLayer = mainComp.layers.addCamera(name, centerPoint)
    // cameraLayer("Transform")("Position").setValue([960, 540, -800])
    // cameraLayer("Camera Options")("Zoom").setValue(800)
    // cameraLayer("Camera Options")("Focus Distance").setValue(800)
    // cameraLayer("Camera Options")("Aperture").setValue(7.6)
    // cameraLayer("Transform")("Point of Interest").setValuesAtTimes([1, 2, 3, 7], [[960, 540, 0], [960, 300, 0], [960, 300, 0], [960, 700, 0]])
    // cameraLayer("Transform")("Position").setValuesAtTimes([1, 2, 3, 7], [[960, 540, -800], [960, 300, -800], [960, 300, -800], [960, 700, -800]])
    // cameraLayer("Camera Options")("Zoom").setValuesAtTimes([1, 2, 7], [800, 1500, 1500])

    shareUtil.configProps(props)
    if (keyframes) {
        shareUtil.configKeyframes(keyframes)
    }
    // if (props) {
    //     for (var k in props) {
    //         var propChain = k.split(".")
    //         var prop = layer(propChain[0]);
    //         for (var i = 1; i < propChain.length; i++) {
    //             prop = prop(propChain[i])
    //         }
    //         prop.setValue(props[k]);
    //     }
    // }
    // if (keyframes) {
    //     for (var k in keyframes) {
    //         var propChain = k.split(".")
    //         var prop = layer(propChain[0]);
    //         for (var i = 1; i < propChain.length; i++) {
    //             prop = prop(propChain[i])
    //         }
    //         var numKeys = prop.numKeys 
    //         for (var i = numKeys; i >= 1; i--) {
    //             prop.removeKey(i)
    //         }
    //         prop.setValuesAtTimes(keyframes[k]["times"], keyframes[k]["values"]);
    //     }
    // }
    return cameraLayer
}

CameraUtil.prototype.remove = function(layer, effectName) {
}

var cameraUtil = new CameraUtil();