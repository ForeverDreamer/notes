function procSpatial(times, type) {
    if (!type) {
        type = 'HOLD'
    }
    var spatial = []
    for (var i = 0; i < times.length; i++) {
        spatial.push({"type": type})
    }
    return spatial
}

function propertyKeyframes(times, values, spatial, temporal, clear) {
    var keyframes = []
    keyframes[0] = times
    keyframes[1] = values

    keyframes[2] = {}
    if (spatial) {
       keyframes[2]["spatial"] = spatial
    }
    if (temporal) {
       keyframes[2]["temporal"] = temporal
    }

    if (clear === false) {
        keyframes[3] = false
    } else {
        keyframes[3] = true
    }

    return keyframes
}