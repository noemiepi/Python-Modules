# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 12:50:38 by npillet         #+#    #+#               #
#  Updated: 2026/02/18 10:03:06 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_iterative():
    x = int(input("Days until harvest: "))
    for i in range(1, x+1):
        print(f"Day {i}")
        i = i + 1
    print("Harvest time!")
