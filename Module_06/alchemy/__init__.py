# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  __init__.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 13:31:08 by npillet         #+#    #+#               #
#  Updated: 2026/03/11 13:55:08 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .elements import create_fire, create_water

__version__ = "1.0.0"
__author__ = "Master Pythonicus"
__all__ = ["create_fire", "create_water"]
