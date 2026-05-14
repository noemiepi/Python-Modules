# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 13:58:03 by npillet         #+#    #+#               #
#  Updated: 2026/03/11 14:29:56 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    water = f"{create_water()}"
    return f"Invisibility potion brewed with {create_air()} and {water}"


def wisdom_potion() -> str:
    ele = f"{create_water()}, {create_earth()} and {create_air()}"
    return f"Wisdom potion brewed with all elements {create_fire()}, {ele}"
