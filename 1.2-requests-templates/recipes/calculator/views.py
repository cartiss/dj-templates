from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, recipe_name):
    DATA = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'butter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },
    }

    ingredients = DATA.get(recipe_name)
    servings = request.GET.get('servings')

    if servings is not None and int(servings) > 0:
        for ing, quantity in ingredients.items():
            ingredients[ing] = quantity * int(servings)

    context = {
        'recipe': ingredients
    }

    return render(request, 'calculator/index.html', context)

