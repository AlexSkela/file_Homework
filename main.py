cook_book = {}

with open('recipes.txt', encoding='utf-8') as f:
    for line in f:
        dish = line.strip()
        counter = int(f.readline().strip())
        list_of_ingred = []
        for i in range(counter):
            temp_dict = {}
            ingred = f.readline()
            ingred = ingred.strip().split('|')
            temp_dict['ingredient_name'] = ingred[0].strip()
            temp_dict['quantity'] = int(ingred[1])
            temp_dict['measure'] = ingred[2].strip()
            list_of_ingred.append(temp_dict)
        cook_book[dish]= list_of_ingred
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
                one_dict["quantity"] = person_count * one_dict['quantity']
                new_dict.update({new_key: one_dict})
    print(new_dict)


        # print(cook_book[dishes])

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 10, cook_book)













