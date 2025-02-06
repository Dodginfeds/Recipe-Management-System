# ---------------------------------------------
# Recipe Management System
# ---------------------------------------------
# This program allows users to:
# 1. Create and manage recipes with ingredients and cooking times.
# 2. Automatically determine the difficulty level based on cooking time.
# 3. Create recipe objects from dictionaries.
# 4. Validate ingredients to ensure they are entered correctly.
# ---------------------------------------------

class Recipe:
    """
    A class representing a recipe, including its name, ingredients, cooking time, 
    and difficulty level based on the cooking duration.
    """

    def __init__(self, name, ingredients, cooking_time):
        """
        Initializes a new Recipe object.
        
        :param name: The name of the recipe.
        :param ingredients: A list of ingredients required.
        :param cooking_time: Time required to cook (in minutes).
        """
        self.name = name
        self.ingredients = ingredients
        self._cooking_time = self._validate_cooking_time(cooking_time)

    # -------------------------------
    # Property: Cooking Time Validation
    # -------------------------------

    @property
    def cooking_time(self):
        """
        Retrieves the cooking time, ensuring it's non-negative.
        """
        return self._cooking_time

    @staticmethod
    def _validate_cooking_time(time):
        """
        Ensures the cooking time is a valid, non-negative number.
        """
        if time < 0:
            raise ValueError("Cooking time cannot be negative.")
        return time

    # -------------------------------
    # Property: Difficulty Level
    # -------------------------------

    @property
    def difficulty(self):
        """
        Determines the difficulty level based on the cooking time.
        """
        if self._cooking_time <= 30:
            return "Easy"
        elif self._cooking_time <= 60:
            return "Medium"
        else:
            return "Hard"

    # -------------------------------
    # String Representation of Recipe
    # -------------------------------

    def __str__(self):
        """
        Returns a formatted string representation of the recipe.
        """
        return (
            f"--------------------------------------\n"
            f"🍽 Recipe: {self.name}\n"
            f"🥄 Ingredients: {', '.join(self.ingredients)}\n"
            f"⏳ Cooking Time: {self._cooking_time} mins\n"
            f"🔥 Difficulty: {self.difficulty}\n"
            f"--------------------------------------"
        )

    # -------------------------------
    # Class Method: Create from Dictionary
    # -------------------------------

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Recipe object from a dictionary.
        
        :param data: Dictionary containing 'name', 'Ingredients', and 'Cooking Time'.
        :return: A Recipe object.
        """
        name = data.get("name")
        ingredients = data.get("Ingredients", [])
        cooking_time = data.get("Cooking Time", 0)

        return cls(name, ingredients, cooking_time)

    # -------------------------------
    # Static Method: Validate Ingredients
    # -------------------------------

    @staticmethod
    def validate_ingredients(ingredients):
        """
        Validates that all ingredients are strings.
        
        :param ingredients: List of ingredient names.
        :raises TypeError: If any ingredient is not a string.
        """
        if not all(isinstance(ingredient, str) for ingredient in ingredients):
            raise TypeError("All ingredients must be strings.")

# ---------------------------------------------
# Example Usage
# ---------------------------------------------

# Creating a recipe manually
recipe1 = Recipe("Boiled Eggs", ["Eggs", "Water", "Pot"], 12)

# Displaying the recipe details
print(recipe1)
print(f"Cooking Time: {recipe1.cooking_time} minutes")
print(f"Difficulty Level: {recipe1.difficulty}")

# Creating a recipe from a dictionary
recipe_data = {
    "name": "Cake",
    "Ingredients": ["Flour", "Sugar", "Eggs", "Butter"],
    "Cooking Time": 75
}
cake = Recipe.from_dict(recipe_data)

# Displaying the new recipe details
print(cake)
