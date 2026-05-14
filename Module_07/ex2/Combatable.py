# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Combatable.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 09:23:33 by npillet         #+#    #+#               #
#  Updated: 2026/03/18 10:58:08 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> dict:
        pass

    @abstractmethod
    def defend(self, incomming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
