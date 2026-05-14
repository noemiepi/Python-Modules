# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  validator.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 15:01:11 by npillet         #+#    #+#               #
#  Updated: 2026/03/11 15:33:42 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ["fire", "water", "earth", "air"]
    ingredients_list = ingredients.split(" ")
    for ingredient in ingredients_list:
        if ingredient in valid_ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
