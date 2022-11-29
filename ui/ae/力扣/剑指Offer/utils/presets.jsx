function PresetsUtil() {}

PresetsUtil.prototype.add = function(layer, payload) {
    var preset = File(payload["path"]);
    layer.applyPreset(preset);
    var props = payload["props"]
    if (props) {
        for (var k in props) {
            // "ADBE Drop Shadow"的Opacity属性内部有个自己的换算比例，100=39%，255约等于100%
            effect(k).setValue(props[k]);
        }
    }
    var keyframes = payload["keyframes"]
    if (keyframes) {
        for (var k in keyframes) {
            var propChain = k.split(".")
            var prop = layer.Effects(propChain[0]);
            for (var i = 1; i < propChain.length; i++) {
                prop = prop(propChain[i])
            }
            var numKeys = prop.numKeys 
            for (var i = numKeys; i >= 1; i--) {
                prop.removeKey(i)
            }
            $.writeln(prop.valueAtTime(0, false))
            $.writeln(prop.valueAtTime(2, false))
            prop.setValuesAtTimes(keyframes[k]["times"], keyframes[k]["values"]);
            $.writeln(prop.valueAtTime(10, false))
            $.writeln(prop.valueAtTime(20, false))
        }
    }
    return preset
}

var presetsUtil = new PresetsUtil();