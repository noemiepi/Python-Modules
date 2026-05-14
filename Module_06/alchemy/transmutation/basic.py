# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  basic.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 14:37:39 by npillet         #+#    #+#               #
#  Updated: 2026/03/11 14:42:26 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    return f"Stone transmuted to gem using {create_earth()}"
