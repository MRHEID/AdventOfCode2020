rows = 127
columns = 7

seatIDList = []
with open("C:\\Users\\Josh\\OneDrive\\GIT\\AdventOfCode\\AdventOfCode2020\\Day5\\input.txt", "r") as boardingPassList:
    for boardingPass in boardingPassList:
        f = 0
        b = 127
        l = 0
        r = 7
        i = 0
        for letter in boardingPass:
            i = i + 1
            if letter == 'F':
                b = range(int(f), int(b+1))[len(range(int(f), int(b)))//2]
                if i == 7:
                    row = f
            elif letter == 'B':
                f = range(int(f), int(b+1))[(len(range(int(f), int(b)))+1)//2]
                if i == 7:
                    row = b
            elif letter == 'R':
                l = range(int(l), int(r+1))[(len(range(int(l), int(r)))+1)//2]
                if i == 10:
                    column = r
            elif letter == 'L':
                r = range(int(l), int(r+1))[len(range(int(l), int(r)))//2]
                if i == 10:
                    column = l
            #i
            #range(int(f), int(b))
            #range(int(l), int(r))
        seatID = row * 8 + column
        seatIDList.append(int(seatID))
        print(boardingPass, 'row', row, 'column', column, 'seat id', seatID)

max(seatIDList)          