import re

recordMatches = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
eclMatches = ['amb','blu','brn','gry','grn','hzl','oth']
data = []
valid = 0
table =[]
with open("C:\\Users\\Josh\\OneDrive\\GIT\\AdventOfCode\\AdventOfCode2020\\Day4\\input.txt", "r") as batch:
    for line in batch.readlines():
        if line == "\n":
            print('## BREAK ##')
            table.append(data)
            data = []
        else:
            for field in line.split(" "):
                print(field)
                data.append((field.strip('\n')).split(':'))

data = []

passedPerson = []
validRecords = 0
for person in table:
    
    recordList = []
    failed = ''
    for record in person:
        value = record[1]
        if record[0] == 'pid':
            if re.match(r'[0-9]{9}',value):
                record.append(True)
                recordList.append('pid')
            else:
                failed = True
        elif record[0] == 'hcl':
            if re.match(r'\#[0-9a-f]{6}',value):
                record.append(True)
                recordList.append('hcl')
            else:
                failed = True
        elif record[0] == 'byr':
            if 1920 <= int(value) <= 2002:
                record.append(True)
                recordList.append('byr')
            else:
                failed = True
        elif record[0] == 'iyr':
            if 2010 <= int(value) <= 2020:
                record.append(True)
                recordList.append('iyr')
            else:
                failed = True
        elif record[0] == 'eyr':
            if 2020 <= int(value) <= 2030:
                record.append(True)
                recordList.append('eyr')
            else:
                failed = True
        elif record[0] == 'hgt':
            hgtMatches = re.match(r'(\d{2,3})(cm|in)',value)
            if hgtMatches:
                if hgtMatches[2] == 'cm':
                    if 150 <= int(hgtMatches[1]) <= 193:
                        record.append(True)
                        recordList.append('hgt')
                elif hgtMatches[2] == 'in':
                    if 59 <= int(hgtMatches[1]) <= 76:
                        record.append(True)
                        recordList.append('hgt')
                else:
                    failed = True
            else:
                failed = True
        elif record[0] == 'ecl':
            if any(x in value for x in eclMatches):
                record.append(True)
                recordList.append('ecl')
            else:
                failed = True
        elif record[0] == 'cid':
            record.append(True)
            recordList.append('cid')
    
    if all(x in recordList for x in recordMatches) == True and failed != True:
        validRecords = validRecords + 1
        print(person)
        print("pass")
        passedPerson.append(person)
    else:
        print(person)
        print("fail")

validRecords