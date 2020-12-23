# Initialize a hash as a circular linked list by pointing each cup label as a
# key to the cup label that follows as a value.
p = "538914762"
ordering = {
    int(v): int(p[i+1] if i < len(p)-1 else p[0]) for i,v in enumerate(p)
}

if False: # Part 1
    # For both parts, we'll store the size of the circle and the rounds to run
    l = 9
    r = 100
else: # Part 2
    l = 1_000_000
    r = 10_000_000
    # In part 2 we also need to adjust the end of our circle to hook up the
    # extra values, so since my last number was 2 we'll make that point to 10
    # and we'll make 1,000,000 point back around to my first number, 5.
    ordering[2] = 10
    ordering[l] = 5
    # Then we'll add all the mappings up to a million.
    for i in range(10,1000000):
        ordering[i] = i+1

m0 = 5 # Current cup, starts as first cup from our input
for i in range(r):
    # Pick up the next three cups in sequence
    m1 = ordering[m0]
    m2 = ordering[m1]
    m3 = ordering[m2]

    # Since we took away the "next three", the "current" cup is now
    # followed by the cup that was previously clockwise from the third cup...
    ordering[m0] = ordering[m3]

    # Find the destination cup; make sure we don't pick one of the next cups
    # that we picked up, and count down from the value on the current cup.
    nx = (m0 + (l - 2)) % l + 1
    while nx in (m1,m2,m3):
        nx = (nx + (l - 2)) % l + 1

    # What cup was originally after the destination cup?
    px = ordering[nx]
    # Put the cups after the destination cup
    ordering[nx] = m1
    # And before the cup after the destination cup
    ordering[m3] = px
    # The next 'current cup' is the one that is clockwise from this round's
    m0 = ordering[m0]

if l == 9:
    # For part one, convert the order of the cups after 1 back into a string
    i = 1
    nums = ""
    while True:
        i = ordering[i]
        if i == 1: break
        nums += str(i)
    print(nums)
else:
    # For part 2, do the multiplication...
    print(ordering[1]*ordering[ordering[1]])
