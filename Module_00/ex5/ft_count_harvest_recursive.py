# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 12:53:11 by npillet         #+#    #+#               #
#  Updated: 2026/02/18 09:53:27 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_recursive(days=None, x=1):
    if (days is None):
        days = int(input("Days until harvest: "))
    if (x < days+1):
        print(f"Day {x}")
        ft_count_harvest_recursive(days, x+1)
    if (x > days):
        print("Harvest time!")
