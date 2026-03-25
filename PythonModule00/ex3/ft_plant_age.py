# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 12:05:57 by npillet         #+#    #+#               #
#  Updated: 2026/02/17 14:45:23 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_plant_age():
    x = int(input("Enter plant age in days: "))
    if (x > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
