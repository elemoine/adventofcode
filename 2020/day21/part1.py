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
    print(
        sum(
            len(ingredients_no_alergens & ingredients_list)
            for ingredients_list in foods
        )
    )


if __name__ == "__main__":
    main()
