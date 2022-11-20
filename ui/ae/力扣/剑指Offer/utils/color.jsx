function ColorUtil() {}

// ColorUtil.prototype.componentToHex = function(c) {
//     var hex = c.toString(16);
//     return hex.length == 1 ? "0" + hex : hex;
// }

ColorUtil.prototype.rgbToHex = function(r, g, b) {
    function componentToHex(c) {
        var hex = c.toString(16);
        return hex.length == 1 ? "0" + hex : hex;
    }
    return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}

ColorUtil.prototype.rgbNormalize = function(r, g, b) {
    return [r / 255, g / 255, b / 255];
}

ColorUtil.prototype.hexToRgb = function(hex, normalize) {
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    var rgb;
    if (normalize) {
        rgb = this.rgbNormalize(parseInt(result[1], 16), parseInt(result[2], 16), parseInt(result[3], 16))
    } else {
        rgb = [parseInt(result[1], 16), parseInt(result[2], 16), parseInt(result[3], 16)]
    }

    return rgb;
}

ColorUtil.prototype.hexToRgb1 = function(hex) {
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return this.rgbNormalize(parseInt(result[1], 16), parseInt(result[2], 16), parseInt(result[3], 16));
}

ColorUtil.prototype.hexToRgb255 = function(hex) {
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return [parseInt(result[1], 16), parseInt(result[2], 16), parseInt(result[3], 16)];
}

// ColorUtil.prototype.hexToRgb255 = function(hex) {
//     var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
//     r = parseInt(result[1], 16)
//     g = parseInt(result[2], 16)
//     b = parseInt(result[3], 16)
//     return result ? [r, g, b] : null;
// }


if (typeof colorUtil === "undefined") {
    const colorUtil = new ColorUtil();
}