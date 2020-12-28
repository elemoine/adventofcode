import operator
import re


def parse_foods(inputfile):
    with open(inputfile) as f:
        data = [line.strip() for line in f]
    alergens = {}
    ingredients = set()
    foods = []
    for line in data:
        m = re.match(r"^(.+) \(contains (.+)\)$", line)
        ingredients_list = set(m.group(1).split())
        alergens_list = m.group(2).split(", ")
        ingredients |= ingredients_list
        for alergen in alergens_list:
            alergens[alergen] = (
                alergens[alergen] & ingredients_list
                if alergen in alergens
                else set(ingredients_list)
            )
        foods.append(ingredients_list)
    return ingredients, alergens, foods


def main():
    ingredients, alergens, foods = parse_foods("input")
    ingredients_no_alergens = set()
    for ingredient in ingredients:
        for alergen in alergens:
            if ingredient in alergens[alergen]:
                break
        else:
            ingredients_no_alergens.add(ingredient)
    found = set()
    while not all(len(ingredients) == 1 for ingredients in alergens.values()):
        for alergen, ingredients in alergens.items():
            if len(ingredients) == 1:
                found.add(list(ingredients)[0])
            else:
                alergens[alergen] -= found
    print(
        ",".join(
            map(
                operator.itemgetter(1),
                sorted(
                    (
                        (alergen, list(ingredients)[0])
                        for alergen, ingredients in alergens.items()
                    ),
                    key=operator.itemgetter(0),
                ),
            )
        )
    )


if __name__ == "__main__":
    main()
