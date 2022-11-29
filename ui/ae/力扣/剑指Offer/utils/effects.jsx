function EffectsUtil() {}

EffectsUtil.prototype.add = function(layer, name, props, keyframes) {
    var effect = layer.Effects.addProperty(name);
    if (props) {
        for (var k in props) {
            // "ADBE Drop Shadow"的Opacity属性内部有个自己的换算比例，100=39%，255约等于100%
            effect(k).setValue(props[k]);
        }
    }
    if (keyframes) {
    }
    return effect
}

EffectsUtil.prototype.remove = function(layer, effectName) {
}

var effectsUtil = new EffectsUtil();