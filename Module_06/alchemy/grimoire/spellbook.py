# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  spellbook.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 15:04:06 by npillet         #+#    #+#               #
#  Updated: 2026/03/11 15:19:02 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    res = validate_ingredients(ingredients)
    if res is f"{ingredients} - VALID":
        return f"Spell recorded: {spell_name} ({res})"
    else:
        return f"Spell rejected: {spell_name} ({res})"
