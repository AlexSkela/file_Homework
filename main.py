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


def get_shop_list_by_dishes(dishes, person_count, cook_dict):
    one_dict = {}
    new_dict = {}
    for dish in dishes:
        if dish in cook_dict:
            for ing in cook_dict[dish]:
                new_key = ing['ingredient_name']
                items = ['measure', 'quantity']
                for item in items:
                    one_dict[item] = ing[item]

                one_dict["quantity"] = [x * person_count for x in one_dict['quantity']]

                new_dict.update({new_key: one_dict})
    print(new_dict)


        # print(cook_book[dishes])

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3, cook_book)













