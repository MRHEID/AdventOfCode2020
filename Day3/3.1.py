slopeLen = 31
point = 1
eatPine = 0
with open("C:\\Users\\Josh\\OneDrive\\GIT\\AdventOfCode2020\\Day3\\input.txt", "r") as daMap:
    for line in daMap.readlines():
        if line[point-1] == '#':
            eatPine = eatPine + 1
            #print("tree")
        point = point + 3
        print(point)
        if point > slopeLen:
            print("reset slope")
            point = point - slopeLen
            print(point)
print(eatPine)