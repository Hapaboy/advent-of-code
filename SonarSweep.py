def sweep(report: list[int]):
    previousDepth: int = None
    increaseCount: int = 0

    for depth in report:
        if (previousDepth != None):
            if (depth - previousDepth > 0):
                increaseCount += 1
        previousDepth = depth
    return increaseCount

def windowSweep(report: list[int]):
    start: int = 0
    end: int = start + 3
    length: int = len(report)
    windows: list[int] = []
    for i in range(length - 2):
        windowValue: int = 0
        for j in range(start, end):
            windowValue += report[j]
        windows.append(windowValue)
        start += 1
        if (end + 1 < length):
            end += 1
        else:
            end = length
    
    return sweep(windows)

