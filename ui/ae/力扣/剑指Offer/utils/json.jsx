function JsonIO() {}

JsonIO.prototype.write = function(path) {
    var file = File(path);
    file.open("w");
    file.write(JSON.stringify(data));
    file.close();
}

JsonIO.prototype.read = function(path) {
    var file = File(path);
    file.open("r");
    var data = file.read();
    file.close();
    return JSON.parse(data)
}


if (typeof jsonIO === "undefined") {
    const jsonIO = new JsonIO();
}
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