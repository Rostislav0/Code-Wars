def cakes(recipe, available):
    return min([available.get(i, 0) // recipe[i] for i in recipe.keys()])


print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))