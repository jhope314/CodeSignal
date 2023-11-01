from collections import defaultdict

def solution(dishes):
    ingredientList = defaultdict(list)
    filteredIngredientList = []
    for dish in dishes: 
        name = dish[0] 
        for i in range(1, len(dish)):
            ingredient = dish[i]
            ingredientList[ingredient] += [name]        
    print(ingredientList)
    n = 0
    for item in ingredientList:
        ingredientDishList = ingredientList[item]
        if len(ingredientDishList) > 1:
            ingredientDishList = sorted(ingredientDishList)
            filteredIngredientList.append([item])
            filteredIngredientList[n].extend(ingredientDishList)
            n += 1
    return sorted(filteredIngredientList)
    