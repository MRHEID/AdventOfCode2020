matches = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
person = []
valid = 0
with open("C:\\Users\\Josh\\OneDrive\\GIT\\AdventOfCode2020\\Day4\\input.txt", "r") as batch:
    for line in batch.readlines():
        print(line.strip())
        if line=="\n":
            if all(x in person for x in matches) == True:
                print('valid found')
                valid = valid + 1
                print(person)
                len(person)
            print('## NewLine ##')
            person=[]
        else:
            if line.find('byr') != -1:
                person.append('byr')            
            if line.find('iyr') != -1:
                person.append('iyr')
            if line.find('eyr') != -1:
                person.append('eyr')
            if line.find('hgt') != -1:
                person.append('hgt')
            if line.find('hcl') != -1:
                person.append('hcl')
            if line.find('ecl') != -1:
                person.append('ecl')
            if line.find('pid') != -1:
                person.append('pid')
            if line.find('cid') != -1:
                person.append('cid')
if all(x in person for x in matches) == True:
    print('valid found')
    valid = valid + 1
    print('## NewLine ##')
    person = []
print(valid)