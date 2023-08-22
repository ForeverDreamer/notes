
def currentline_times(subtitles, steps):
    times = []
    intervals = subtitles[2]
    i = 0
    while i < len(subtitles[2]):
        if intervals[i] == 0:
            i += 1
            continue
        elif intervals[i] == 1:
            times.append(subtitles[0][i])
        else:
            times.append(subtitles[0][i])
            interval = (subtitles[0][i+1] - subtitles[0][i])/intervals[i]
            times += [times[-1]+interval*j for j in range(1, intervals[i])]
        i += 1

    i = len(times) - 1
    while len(times) < steps:
        times.append(times[i]+1)
        i += 1

    return times
