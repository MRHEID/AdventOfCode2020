data1 = []
with open("C:\\Users\\Josh\\OneDrive\\GIT\\AdventOfCode2020\\1.1\\1.1_input.txt", "r") as f:
    for line in f.readlines():
        data1.append(int(line))
for x in data1:
    findInt = 2020 - x
    if findInt in data1:
        print(findInt*x)    