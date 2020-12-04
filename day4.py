# Passport Processing

with open('day4.in','r') as f:
    lines = [l.strip() for l in f.readlines()]

def is_digits(val, cnt):
    if len(val) != cnt:
        return False
    return not any([x not in '0123456789' for x in val])

def check_passport(passport):
    print("checking passport", passport)
    expected = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] #, 'cid'
    if not all([e in passport for e in expected]):
        print('Missing expected value')
        return False

    # Stop here for part 1
    # return True

    if not is_digits(passport['byr'], 4) or  int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        print('Bad birth year')
        return False

    if not is_digits(passport['iyr'], 4) or  int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        print('Bad issue year')
        return False

    if not is_digits(passport['eyr'], 4) or  int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        print('Bad expire year')
        return False

    if passport['hgt'][-2:] == 'cm':
        if not is_digits(passport['hgt'][:-2], 3) or int(passport['hgt'][:-2]) < 150 or int(passport['hgt'][:-2]) > 193:
            print('bad height in cm')
            return False
    elif passport['hgt'][-2:] == 'in':
        if not is_digits(passport['hgt'][:-2], 2) or int(passport['hgt'][:-2]) < 59 or int(passport['hgt'][:-2]) > 76:
            print('bad height in inches:', int(passport['hgt'][:-2]))
            return False
    else:
        print('bad height generally')
        return False

    if len(passport['hcl']) != 7 or passport['hcl'][0] != '#' or any([x not in '0123456789abcdef' for x in passport['hcl'][1:]]):
        print('bad hair color')
        return False

    if passport['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
        print('bad eye color')
        return False

    if not is_digits(passport['pid'], 9):
        print('bad pid')
        return False

    return True

count = 0
passport = {}
for line in lines:
    if not len(line):
        count += check_passport(passport)
        passport = {}
        continue

    # Parse line
    elems = line.split(' ')
    for elem in elems:
        name, value = elem.split(':',1)
        passport[name] = value

count += check_passport(passport)

print("count =", count)
