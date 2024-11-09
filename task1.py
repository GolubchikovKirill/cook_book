class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, name, quantity, unit):
        ingredient = {
            'ingredient_name': name,  # Используем 'ingredient_name'
            'quantity': quantity,
            'measure': unit  # Используем 'measure'
        }
        self.ingredients.append(ingredient)

    def __str__(self):
        ingredients_str = "\n".join(
            f"{ing['ingredient_name']} | {ing['quantity']} | {ing['measure']}" for ing in self.ingredients
        )
        return f"{self.name}:\nКоличество ингредиентов: {len(self.ingredients)}\n{ingredients_str}"


class Cookbook:
    def __init__(self):
        self.recipes = {}

    def load_from_file(self, filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]

        i = 0
        while i < len(lines):
            name = lines[i]  # Название блюда
            i += 1
            num_ingredients = int(lines[i])  # Количество ингредиентов
            i += 1

            recipe = Recipe(name)

            for _ in range(num_ingredients):
                ingredient_name, quantity, unit = lines[i].split(" | ")
                recipe.add_ingredient(ingredient_name, int(quantity), unit)
                i += 1

            self.recipes[name] = recipe.ingredients  # Сохраняем только ингредиенты рецепта

    def get_recipe_by_name(self, name):
        return self.recipes.get(name, None)  # Возвращаем список ингредиентов по названию рецепта

    def get_all_recipes(self):
        return self.recipes  # Получаем все рецепты


# Пример вызова:
if __name__ == "__main__":
    cookbook = Cookbook()
    cookbook.load_from_file("/Users/golubcikovkirill/Desktop/Projects/for Netology VSC/Open file Python/files/recipes.txt")

    # Получаем все рецепты в нужном формате
    cook_book = cookbook.get_all_recipes()

    # Проверяем содержимое cook_book
    print(cook_book)




