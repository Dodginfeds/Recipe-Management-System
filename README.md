# 🍽 Recipe Management System

## 📌 Overview
The **Recipe Management System** is a Python-based application that allows users to create, manage, and categorize recipes based on cooking time and difficulty. This system helps users efficiently organize their recipes while ensuring ingredient validation.

---

## 🏆 Features
- 🆕 **Create Recipes**: Define a recipe with a name, ingredients, and cooking time.
- 🔍 **Determine Difficulty**: Automatically classifies recipes as **Easy**, **Medium**, or **Hard** based on cooking time.
- 🐂 **Store Recipes as Objects**: Uses object-oriented programming (OOP) principles for better structure.
- 💜 **Ingredient Validation**: Ensures that all ingredients are correctly entered as strings.
- 📖 **Create Recipes from Dictionaries**: Allows importing recipe data in dictionary format.

---

## 🛠 Technologies & Concepts Used
This project demonstrates fundamental Python programming concepts:
- **Object-Oriented Programming (OOP)**: Uses classes, objects, and methods.
- **Encapsulation**: Protects attributes and ensures input validation.
- **Property Decorators**: Implements `@property` for dynamic calculations.
- **Class & Static Methods**: Enables recipe creation from dictionaries and input validation.
- **Error Handling**: Ensures correct input values and manages invalid inputs gracefully.

---

## 📦 Installation & Usage
### 🔹 Prerequisites
- Install **Python 3.x** on your system.

### 🔹 Clone the Repository
```bash
git clone https://github.com/yourusername/recipe-manager.git
cd recipe-manager
```

### 🔹 Run the Application
```bash
python recipe_manager.py
```

---

## 📌 Example Usage
```python
# Creating a new recipe
recipe1 = Recipe("Boiled Eggs", ["Eggs", "Water", "Pot"], 12)

# Displaying the recipe details
print(recipe1)
print(f"Cooking Time: {recipe1.cooking_time} minutes")
print(f"Difficulty Level: {recipe1.difficulty}")
```
**💡 Output**
```
--------------------------------------
🍽 Recipe: Boiled Eggs
🧁 Ingredients: Eggs, Water, Pot
⏳ Cooking Time: 12 mins
🔥 Difficulty: Easy
--------------------------------------
```

### 🔹 Creating a Recipe from a Dictionary
```python
recipe_data = {
    "name": "Cake",
    "Ingredients": ["Flour", "Sugar", "Eggs", "Butter"],
    "Cooking Time": 75
}
cake = Recipe.from_dict(recipe_data)

print(cake)
```
**💡 Output**
```
--------------------------------------
🍽 Recipe: Cake
🧁 Ingredients: Flour, Sugar, Eggs, Butter
⏳ Cooking Time: 75 mins
🔥 Difficulty: Hard
--------------------------------------
```

---

## 🌱 Future Enhancements
- 📚 **Recipe Storage**: Implement file-based or database storage to save recipes.
- 🔍 **Search & Filter**: Allow filtering recipes by difficulty, ingredients, or cooking time.
- 📊 **Nutritional Analysis**: Integrate with an API for calorie and nutrition details.
- 📅 **Meal Planning**: Enable weekly meal planning with saved recipes.

---

## 📝 License
This project is open-source and available under the **MIT License**.

---

### 👨‍🍳 Author
Developed by **Your Name**  
For any inquiries, feel free to reach out via [GitHub](https://github.com/yourusername).

---

## 🤝 Contributions
Contributions, issues, and feature requests are welcome!  
Feel free to fork this project and submit a pull request.

```bash
# Fork the repository
git clone https://github.com/yourusername/recipe-manager.git

# Create a new branch
git checkout -b feature-new-recipe

# Commit your changes
git commit -m "Added a new feature"

# Push to GitHub
git push origin feature-new-recipe
```
---

Happy Cooking! 🍳🔥
