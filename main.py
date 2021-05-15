from typing import List

cook_book = {}
key_ = ['ingredient_name', 'quantity', 'measure']

with open('recipes.txt', 'r', encoding='utf-8') as f:
    for line in f:
        dish = line.strip()
        counter = int(f.readline().strip())
        keys_ = []
        for _ in range(int(counter)):
            q = f.readline().strip().split('|')
            dish_dict = dict(zip(key_, q))
            keys_ += [dish_dict]
        cook_book[dish] = keys_
        f.readline().strip()
    print(cook_book)



        # print(dish)











