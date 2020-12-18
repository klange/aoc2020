with open('day18.in','r') as f:
    lines = [x.strip() for x in f.readlines()]

"""
def apply(total, current, value):
    if current == '+':
        return total + value
    elif current == '*':
        return total * value
    else:
        raise ValueError("Invalid")

def expr(tokens):
    total = 0
    current = '+'
    while tokens:
        token = tokens.pop(0)
        if token == '(':
            inner = []
            d = 1
            while tokens:
                n = tokens.pop(0)
                if n == ')':
                    d -= 1
                elif n == '(':
                    d += 1
                if d == 0:
                    break
                inner.append(n)
            total = apply(total, current, expr(inner))
            current = None
        elif token == ')':
            print("Invalid express")
            break
        elif token == '+':
            current = '+'
        elif token == '*':
            current = '*'
        else:
            total = apply(total, current, int(token))
    return total

total = 0
for line in lines:
    e = expr(line.replace('(','( ').replace(')',' )').split())
    total += e
    print(total, e)
"""

# Part 2
def expr(tokens):
    units = []
    left = None
    while tokens:
        token = tokens.pop(0)
        if token == '(':
            inner = []
            d = 1
            while tokens:
                n = tokens.pop(0)
                if n == ')':
                    d -= 1
                elif n == '(':
                    d += 1
                if d == 0:
                    break
                inner.append(n)
            if left:
                units.append(expr(inner) + left)
                left = None
            else:
                units.append(expr(inner))
        elif token == ')':
            print("Invalid express")
            break
        elif token == '+':
            left = units.pop(-1)
        elif token == '*':
            if left:
                raise ValueError("?")
            # skip
        else:
            if left:
                units.append(int(token) + left)
                left = None
            else:
                units.append(int(token))

    value = 1
    while units:
        # There must have been multiplications
        value = value * units.pop(0)

    return value

total = 0
for line in lines:
    e = expr(line.replace('(','( ').replace(')',' )').split())
    total += e
    print(total, e)
