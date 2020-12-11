def sledge_ride(moveRight,moveDown):
    slopeLen = 31
    point = 1
    eatPine = 0
    with open("C:\\Users\\Josh\\OneDrive\\GIT\\AdventOfCode2020\\Day3\\input.txt", "r") as daMap:
        for count,line in enumerate(daMap, start=0):
            if count % moveDown == 0:
                if line[point-1] == '#':
                    eatPine = eatPine + 1
                point = point + moveRight
                if point > slopeLen:
                    point = point - slopeLen
    return eatPine
(sledge_ride(1,1))*(sledge_ride(3,1))*(sledge_ride(5,1))*(sledge_ride(7,1))*(sledge_ride(1,2))