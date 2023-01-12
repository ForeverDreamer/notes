function PresetsUtil() {}

PresetsUtil.prototype.add = function(layer, presets) {
    if (!presets) {
		return
	}
    for (var i = 0; i < presets.length; i++) {
        var conf =  presets[i]
        var path = conf["path"];
        var props = conf["props"];

        // var preset = File(path);
        layer.applyPreset(File(path));

        if (props) {
            for (var k in props) {
                // "ADBE Drop Shadow"的Opacity属性内部有个自己的换算比例，100=39%，255约等于100%
                layer.Effects(k).setValue(props[k]);
            }
        }

        shareUtil.configKeyframes(layer.Effects, conf["keyframes"])
    }
}

var presetsUtil = new PresetsUtil();