function CompUtil() {}

CompUtil.prototype.addOne = function (parentObj, parentComp, conf) {
    var compFolder = parentObj.items.addFolder(conf["layerName"])
    var newComp = compFolder.items.addComp(conf["layerName"], conf['width'], conf['height'], PIXEL_ASPECT, conf['duration'], FRAME_RATE);
    newComp.bgColor = colorUtil.hexToRgb1(COLORS["bg"])
    if (conf['files']) {
        shareUtil.importFiles(project, conf["files"]);
    }
    // if (conf['images']) {
    //     shareUtil.addLayers(newComp, conf['images'])
    // }
    // if (conf['videos']) {
    //
    // }
    if (conf["texts"]) {
        textUtil.addMany(newComp, conf["texts"])
    }
    if (conf["vectors"]) {
        var vectors = conf['vectors']
        for (var i = 0; i < vectors.length; i++) {
            shareUtil.addLayer(newComp, vectors[i])
        }
    }
    if (conf["shapes"]) {
        shapeUtil.addMany(newComp, conf["shapes"])
    }
    if (conf["dsa"]) {
        dsa.addMany(compFolder.items, newComp, conf['dsa'])
    }
    // if (conf['codes']) {
    //     this.create_codes(compFolder.items, newComp, conf['codes'])
    // }
    if (conf["comps"]) {
        compUtil.addMany(compFolder, newComp, conf['comps'])
    }
    // if (conf["misc"]) {
    //     this.misc(compFolder.items, newComp, conf['misc'])
    // }
    if (conf['codes']) {
        codes.add(compFolder.items, newComp, conf['codes'])
    }
    if (conf['subtitles']) {
        shareUtil.createSubtitles(conf['subtitles'])
    }
    if (conf['camera']) {
        shareUtil.configKeyframes(cameraLayer, conf['camera'])
    }
    shareUtil.addLayer(parentComp, conf, newComp);
}

CompUtil.prototype.addMany = function(parentComp, comps) {
    for (var i = 0; i < comps.length; i++) {
        this.addOne(parentComp, comps[i])
    }
}

var compUtil = new CompUtil();