with open('day2.in','r') as f:
    lines = f.readlines()

def check_first(policy_low, policy_high, letter, password):
    count = 0
    for l in password:
        if l == letter:
            count += 1
    return count >= policy_low and count <= policy_high

def check_second(policy_low, policy_high, letter, password):
    count = 0
    if password[policy_low-1] == letter:
        count += 1
    if password[policy_high-1] == letter:
        count += 1
    return count == 1

valid = 0
for line in lines:
    policy, password = line.strip().split(':',1)
    password = password.strip()
    policy_low, _ = policy.split('-',1)
    policy_high, letter = _.split(' ',1)
    policy_low = int(policy_low)
    policy_high = int(policy_high)
    is_valid = check_second(policy_low, policy_high, letter, password)
    print(policy_low, policy_high, letter, password, is_valid)
    if is_valid:
        valid += 1
print(valid)
