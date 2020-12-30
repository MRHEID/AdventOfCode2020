data = []
table =[]
with open("C:\\Users\\Josh\\OneDrive\\GIT\\AdventOfCode\\AdventOfCode2020\\Day6\\input.txt", "r") as dasInput:
    for line in dasInput.readlines():
        if line == "\n":
            print('## BREAK ##')
            table.append(data)
            data = []
        else:
            print(line)
            data.append(line.strip('\n'))

table.append(data)            

total = 0
listGroupUnique = []
duplicates = {}
groupTotal = 0
for group in table:
    if len(group) > 1:
        for person in group:
            for letter in set(person):
                if letter in duplicates:
                    duplicates[letter] += 1
                else:
                    duplicates[letter] = 1
        
        for item in duplicates:
            if duplicates[item] == len(group):
                groupTotal = groupTotal + 1
        total = total + groupTotal
        listGroupUnique.append(groupTotal)
        print(duplicates)
        duplicates = {}
        groupTotal = 0
        
    else:
        for person in group:
            total = total + len(person)
            listGroupUnique.append(len(person))

print(total)