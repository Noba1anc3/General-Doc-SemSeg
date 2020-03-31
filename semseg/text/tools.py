
def overlap(lineA, lineB):
    lengthA = lineA[1] - lineA[0]
    lengthB = lineB[1] - lineB[0]

    if lineA[1] <= lineB[0]:
        return 0
    if lineA[0] >= lineB[1]:
        return 0
    if lineA[0] <= lineB[0] and lineB[1] <= lineA[1]:
        return 1
    if lineB[0] <= lineA[0] and lineA[1] <= lineB[1]:
        return 1

    lap = lineA[1] - lineB[0]
    if lap < min(lengthA, lengthB):
        return lap/min(lengthA, lengthB)
    else:
        lap = lineB[1] - lineA[0]
        return lap/min(lengthA, lengthB)



