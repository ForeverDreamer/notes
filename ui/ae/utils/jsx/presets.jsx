function PresetsUtil() {}

PresetsUtil.prototype.add = function(layer, conf) {
    var path = conf["path"];
    var props = conf["props"];
    var keyframes = conf["keyframes"];

    var preset = File(path);
    layer.applyPreset(preset);

    if (props) {
        for (var k in props) {
            // "ADBE Drop Shadow"的Opacity属性内部有个自己的换算比例，100=39%，255约等于100%
            effect(k).setValue(props[k]);
        }
    }

    if (keyframes) {
        for (var k in keyframes) {
            var propChain = k.split(".")
            var prop = layer.Effects(propChain[0]);
            for (var i = 1; i < propChain.length; i++) {
                prop = prop(propChain[i])
            }
            // var numKeys = prop.numKeys
            // for (var i = numKeys; i >= 1; i--) {
            //     prop.removeKey(i)
            // }
            prop.setValuesAtTimes(keyframes[k]["times"], keyframes[k]["values"]);
        }
    }
    
    return preset
}

var presetsUtil = new PresetsUtil();