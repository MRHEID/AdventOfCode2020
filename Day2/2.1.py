import re
goodPass = 0
with open("C:\\Users\\Josh\\OneDrive\\GIT\\AdventOfCode2020\\Day2\\input.txt", "r") as f:
    for line in f.readlines():
        blam = re.split(r'(\d+)\-(\d+)\s(\w)\:\s([a-z]+)', line)
        minChar = int(blam[1])
        maxChar = int(blam[2])
        char = blam[3]
        pword = blam[4]
        count = pword.count(char)
        if minChar <= count <= maxChar:
            goodPass = goodPass + 1
print(goodPass)