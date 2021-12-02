# --- Day 21: Allergen Assessment ---

data = open("input/day_21.in", "r").read().strip("\n").split("\n")

foods = []

for line in data:
    i = line.find("(")

    ingredients = line[:i].strip().split(" ")
    allergens = line[i + 1 + len("contains") : -1].strip().split(", ")

    foods.append([ingredients, allergens])

# --- part 1 ---

# allergens[allergen] is a *set* of ingredients that is
# possible to contain this allergen
allergens = {}

for i, j in foods:

    for allergen in j:
        if allergen not in allergens:
            allergens[allergen] = set(i)
        else:
            allergens[allergen] = allergens[allergen].intersection(set(i))

possible = set()

for allergen in allergens:
    possible = possible.union(allergens[allergen])

count = 0

for i, j in foods:
    for ingredient in i:
        if ingredient not in possible:
            count += 1

print(count)

# --- part 2 ---

# key ==> ingredient
# value ==> allergen this ingredient contains
dangerous = {}

while len(allergens) > 0:

    for allergen in allergens:
        if len(allergens[allergen]) == 1:
            break

    ingredient = allergens[allergen].pop()
    allergens.pop(allergen)

    dangerous[ingredient] = allergen

    for allergen2 in allergens:
        if ingredient in allergens[allergen2]:
            allergens[allergen2].remove(ingredient)

word = ",".join(
    [key for key, value in sorted(dangerous.items(), key=lambda item: item[1])]
)
print(word)
