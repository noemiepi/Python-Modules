# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  advanced.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 14:40:17 by npillet         #+#    #+#               #
#  Updated: 2026/03/11 15:47:55 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    heal = healing_potion()
    return f" Philosopher's stone created using {lead_to_gold()} and {heal}"


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
