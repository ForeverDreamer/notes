function get_obj(obj, type) {
    if (typeof obj === "undefined") {
        return new type();
    } else {
        return obj
    }
}