function JsonUtil() {}

JsonUtil.prototype.write = function(path) {
    var file = File(path);
    file.open("w");
    file.write(JSON.stringify(data));
    file.close();
}

JsonUtil.prototype.read = function(path) {
    var file = File(path);
    file.open("r");
    var data = file.read();
    file.close();
    return JSON.parse(data)
}

var jsonUtil = new JsonUtil();
// if (typeof jsonUtil === "undefined") {
//     var jsonUtil = new JsonUtil();
// }
// $.writeln(p);

// function createJSONFile(data) {
//     var file = File(filePath);
//     file.open("w");
//     file.write(JSON.stringify(data));
//     file.close();
// }

// function readJSONFile(path) {
//     var file = File(path);
//     file.open("r");
//     var data = file.read();
//     file.close();
//     return JSON.parse(data)
// }