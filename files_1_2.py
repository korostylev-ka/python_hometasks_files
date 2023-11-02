import os


cook_book = {}
with open(os.path.join(os.path.dirname(__file__), 'recipes.txt'), encoding='utf-8') as f:
    list_recipes = []
    list = f.readlines()
    new_element = []
    #разбиваем список из строк на список из списков блюд
    for idx, element in enumerate(list):
        line = element.strip()
        if line != '' and idx != len(list) - 1:
            new_element.append(line)            
        elif idx == len(list) - 1:
            new_element.append(line)
            list_recipes.append(new_element)
            new_element = []
        else:
            list_recipes.append(new_element)
            new_element = []
            continue
    for dish in list_recipes:
        cook_book[dish[0]] = []
        for a in range(2, len(dish)):
            split_components = dish[a].split('|')
            dict = {}
            dict['ingredient_name'] = split_components[0]
            dict['quantity'] = split_components[1]
            dict['measure'] = split_components[2]
            cook_book[dish[0]].append(dict)
    
def get_shop_list_by_dishes(dishes, person_count):
    foods_count = {}
    for dish in dishes:
        if dish in cook_book:
            foods = cook_book[dish]
            for components in foods:
                ingredient_name = components['ingredient_name']
                measure = components['measure']
                quantity = int(components['quantity'])
                if ingredient_name in foods_count:
                    foods_count[ingredient_name]['quantity'] += quantity
                else:
                    foods_count[ingredient_name] = {'measure': measure, 'quantity': quantity}
        else:
            return f'{dish} нет в кулинарной книге'
    for food in foods_count:
        foods_count[food]['quantity'] *= person_count
    return foods_count

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))

