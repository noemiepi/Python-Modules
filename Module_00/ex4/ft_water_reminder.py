# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 12:46:12 by npillet         #+#    #+#               #
#  Updated: 2026/02/17 14:45:30 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_water_reminder():
    x = int(input("Days since last watering: "))
    if (x > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
