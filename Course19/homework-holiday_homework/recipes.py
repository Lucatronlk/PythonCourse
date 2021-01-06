# Create a recipe class with ingredients and a put them in a recipe manager program 
# that organizes them into categories like deserts, main courses 
# or by ingredients like chicken, beef, soups, pies etc.


import sys


# Recipe is a representation of a cooking recipe
class Recipe:
    def __init__(self):
        self.ingredients = []
        self.instructions = []
        self.name = ""


# Save/Store it into dictionary, Test it
def create():
    recipe = Recipe()
    recipe_dict = {}

    print("Create a recipe!")
    recipe.name = input("Recipe Name: ")

    while True:
        ingredients = input("Ingredients: ")
        if ingredients == 'exit':
            break
        recipe.ingredients.append(ingredients)

    while True:
        instructions = input("Instructions: ")
        if instructions == 'exit':
            break
        recipe.instructions.append(instructions)

    recipe_dict[recipe.name] = recipe


def listrecipe():
    print("listrecipe")


def update():
    print("update")


def delete():
    print("delete")


def main():
    # check if user has entered enough arguments
    if len(sys.argv) != 2:
        print("Usage: recipe <Action> [args]")
        sys.exit(1)

    # argv stores arguments to your program
    action = sys.argv[1]

    if "create" == action:
        create()
    elif "list" == action:
        listrecipe()
    elif "update" == action:
        update()
    elif "delete" == action:
        delete()
    else:
        print("command not found")
        sys.exit(1)


main()