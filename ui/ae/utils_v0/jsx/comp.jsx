function CompUtil() {}

CompUtil.prototype.addOne = function (conf, parentComp, parentObj) {
    if (conf["comps"] || conf["dsa"] || parentComp.name == "Main") {
        parentObj = parentObj.items.addFolder(conf["layerName"])
    }
    var comp = parentObj.items.addComp(conf["layerName"], conf['width'], conf['height'], PIXEL_ASPECT, conf['duration'], FRAME_RATE);
    comp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])
    if (conf['files']) {
        shareUtil.importFiles(conf["files"], parentObj, comp);
    }
    if (conf['codes']) {
        codes.add(conf['codes'], comp, parentObj)
    }
    if (conf["dsa"]) {
        dsa.addMany(conf['dsa'], comp, parentObj)
    }
    if (conf["comps"]) {
        compUtil.addMany(conf['comps'], comp, parentObj)
    }
    if (conf["vectors"]) {
        var vectors = conf['vectors']
        for (var i = 0; i < vectors.length; i++) {
            shareUtil.addLayer(vectors[i], comp)
        }
    }
    if (conf["shapes"]) {
        shapeUtil.addMany(conf["shapes"], comp)
    }
    if (conf["texts"]) {
        textUtil.addMany(conf["texts"], comp)
    }
    if (conf['subtitles']) {
        shareUtil.createSubtitles(conf['subtitles'])
    }
    if (conf['camera']) {
        shareUtil.configKeyframes(cameraLayer, conf['camera'])
    }
    conf["item"] = comp
    shareUtil.addLayer(conf, parentComp);
}

CompUtil.prototype.addMany = function(comps, parentComp, parentObj) {
    for (var i = 0; i < comps.length; i++) {
        this.addOne(comps[i], parentComp, parentObj)
    }
}

var compUtil = new CompUtil();