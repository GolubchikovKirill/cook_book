from task1 import Cookbook  # Импортируем Cookbook из task1.py

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cookbook = Cookbook()
    cookbook.load_from_file("/Users/golubcikovkirill/Desktop/Projects/for Netology VSC/Open file Python/files/recipes.txt")

    for dish in dishes:
        if dish in cookbook.recipes:
            for ingredient in cookbook.recipes[dish]:  # cookbook.recipes[dish] — это список ингредиентов
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity']
                measure = ingredient['measure']

                total_quantity = quantity * person_count

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += total_quantity
                else:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': total_quantity}

    return shop_list


# Тестовый вызов функции с выводом результата
if __name__ == "__main__":
    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    result = get_shop_list_by_dishes(dishes, person_count)
    print(result)





