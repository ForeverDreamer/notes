
def currentline_times(intervals, l_times, steps):
    times = []
    intervals = intervals
    i = 0
    while i < len(intervals):
        if intervals[i] == 0:
            i += 1
            continue
        elif intervals[i] == 1:
            times.append(l_times[i])
        else:
            times.append(l_times[i])
            interval = (l_times[i+1] - l_times[i])/intervals[i]
            times += [times[-1]+interval*j for j in range(1, intervals[i])]
        i += 1

    i = len(times) - 1
    while len(times) < steps:
        times.append(times[i]+1)
        i += 1

    return times
