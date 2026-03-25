# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_seed_inventory.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 14:28:39 by npillet         #+#    #+#               #
#  Updated: 2026/02/17 15:42:57 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
    elif (unit == "grams"):
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
    elif (unit == "area"):
        print(f"{seed_type.capitalize()} seeds: covers {quantity}"
              " square meters")
    else:
        print("Unknown unit type")
