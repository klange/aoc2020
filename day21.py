with open('day21.in','r') as f:
    lines = [x.strip() for x in f.readlines()]

foods = []
ingredients = set()
allergens = {}

for line in lines:
    i, a = line.replace(')','').split(' (contains ', 1)
    ingred = i.split(' ')
    allerg = a.split(', ')

    for i in ingred:
        ingredients.add(i)

    # We'll use this later to scan the foods for safe ingredients.
    foods.append((ingred, allergens))

    for a in allerg:
        if a not in allergens:
            # If we've not seen this allergen before, all of these ingredients
            # are suspect.
            allergens[a] = set(ingred)
        else:
            # Otherwise, the allergen must be in one of the ingredients that
            # is in common among all of the things it is known to appear in.
            allergens[a] = allergens[a].intersection(set(ingred))

# If there are any allergens that have only one candidate, they must be that
# ingredient and we can eliminate it from the candidates for other allergens.
# Do that until we can't do it anymore. This happens to be enough to get to a
# final answer for the input sets.
while True:
    madeChanges = False
    remove = []
    for a, l in allergens.items():
        if len(l) == 1:
            remove.append((a, list(l)[0]))
    for a, i in remove:
        for _a, l in allergens.items():
            if _a == a: continue
            if i in l:
                l.remove(i)
                madeChanges = True
    if not madeChanges:
        break

# Determine which ingredients can not possibly contain one of the allergens.
# That is to say, look at each ingredient, and if it doesn't appear in the
# candidates list for any allergen, count all the instances of that ingredient.
# With the inputs we have, we can actually do this _without_ the previous step,
# but might as well do it after...
count = 0
for i in ingredients:
    if not any([i in v for v in allergens.values()]):
        scount = 0
        for _i, v in enumerate(foods):
            if i in foods[_i][0]:
                scount += 1
        count += scount
print(count)

# We have our mappings, sort them by the allergen...
print(",".join(str(list(allergens[a])[0]) for a in sorted(allergens.keys())))
