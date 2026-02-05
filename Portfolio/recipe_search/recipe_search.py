"""
The following program allows a user to search for
a recipe based on the recipe names, preparation times,
and ingredients used in the recipe.  

The program uses a helper function to organize the 
recipes in a file submitted by the user.
"""


def get_recipe_data(filename: str):
    """
    The function reads the file and then returns a list
    of recipes, where each recipe is a block of lines
    """
    recipes = []

    # Read the entire file and split the file into recipe blocks
    with open(filename) as new_file:
        content = new_file.read()
        recipe_blocks = content.split('\n\n')
        
        # Check if recipe is an empty string
        for recipe in recipe_blocks:
            if not recipe.strip():
                continue

            # Append each block of recipes to be returned
            lines = recipe.split('\n')
            recipes.append(lines)
        
    return recipes


def search_by_name(filename: str, word: str):
    recipe_names = []

    # Use the helper function to retrieve the recipes
    recipes_list = get_recipe_data(filename)

    # The recipe title is found at the 0-th index of each recipe block
    for recipe in recipes_list:
        recipe_title = recipe[0].strip()

        if word.lower() in recipe_title.lower():
            recipe_names.append(recipe_title)

    return recipe_names   


def search_by_time(filename: str, prep_time: int):
    recipe_times = []

    # Use the helper function to retrieve the recipes
    recipes_list = get_recipe_data(filename)

    # The recipe title is found at the 0th index of each recipe block
    # The recipe prep time is found at the 1st index of each recipe block
    for recipe in recipes_list:
        recipe_title = recipe[0].strip()
        recipe_prep_time = recipe[1].strip()

        if int(recipe_prep_time) <= prep_time:
            recipe_times.append(f"{recipe_title}, preparation time {recipe_prep_time} min")
        
    return recipe_times     


def search_by_ingredient(filename: str, ingredient: str):
    recipe_ingredients = []     

    # Use the helper function to retrieve the recipes
    recipes_list = get_recipe_data(filename)

    # The recipe title is found at the 0th index of each recipe block
    # The recipe prep time is found at the 1st index of each recipe block
    for recipe in recipes_list:
        recipe_title = recipe[0].strip()
        recipe_prep_time = recipe[1].strip()

        # If the ingredient is found in the current block, break;  go to next block
        for line in recipe[2:]:
            if ingredient.lower() in line.lower().strip():
                recipe_ingredients.append(f"{recipe_title}, preparation time {recipe_prep_time} min")
                break
        
    return recipe_ingredients