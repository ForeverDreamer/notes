var clips = app.project.sequences[0].videoTracks[0].clips
// app.enableQE()
var targetSequence = app.project.sequences[0]
var seqsToDelete = []
for (var i = 0; i < clips.numItems; i++) {
    var name = clips[i].name
    var inPoint = clips[i].inPoint.ticks
    var outPoint = clips[i].outPoint.ticks
    targetSequence.setInPoint(inPoint)
    targetSequence.setOutPoint(outPoint)
    var sequence = targetSequence.createSubsequence(true)
    app.encoder.encodeSequence(
        sequence, 
        "G:\\沉浸式学习\\ExtendScript\\程序员是怎样创作短视频的\\"+name, 
        "C:\\Users\\doer\\Documents\\Adobe\\Adobe Media Encoder\\15.0\\Presets\\Copy of Match Source - High bitrate.epr",
        0,
        1
    )
    seqsToDelete.push(sequence)
}

app.encoder.startBatch()

for (var i = 0; i < seqsToDelete.length; i++) {
    app.project.deleteSequence(seqsToDelete[i])
}
// app.project.rootItem.children[0].createSubClip("test_subclip_lsl", "0", "5486745600000", 0, 1, 1)
// $.writeln(app.project.rootItem.children[1].name)