# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 12:01:15 by npillet         #+#    #+#               #
#  Updated: 2026/02/17 14:45:18 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_harvest_total():
    x = int(input("Day 1 harvest: "))
    y = int(input("Day 2 harvest: "))
    z = int(input("Day 3 harvest: "))
    print(f"Total harvest: {x + y + z}")
