import re
goodPass = 0
with open("C:\\Users\\Josh\\OneDrive\\GIT\\AdventOfCode2020\\Day2\\input.txt", "r") as f:
    for line in f.readlines():
        blam = re.split(r'(\d+)\-(\d+)\s(\w)\:\s([a-z]+)', line)
        charPos1 = int(blam[1])-1
        charPos2 = int(blam[2])-1
        char = blam[3]
        pword = blam[4]
        if charPos1 + 1 <= len(pword):
            if pword[charPos1] == char:
                pos1Pass = 1
            else:
                pos1Pass = 0
        if charPos2 + 1 <= len(pword):
            if pword[charPos2] == char:
                pos2Pass = 1
            else:
                pos2Pass = 0
        if pos2Pass + pos1Pass == 1:
            goodPass = goodPass + 1
print(goodPass)