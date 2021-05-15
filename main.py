cook_book = {}
key_ = ['ingredient_name', 'quantity', 'measure']

with open('recipes.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i == 0:
            dish = line.strip()
        elif i == 1:
            count_ing = line.strip()
    print(dish)
    print(count_ing)
    ingred_list = []










