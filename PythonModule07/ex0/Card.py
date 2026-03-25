# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Card.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/16 10:56:16 by npillet         #+#    #+#               #
#  Updated: 2026/03/18 09:43:21 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    ELITE = "Elite"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: Rarity) -> None:
        if not isinstance(rarity, Rarity):
            raise ValueError("Rarity is not valid")

        if not isinstance(cost, int):
            raise ValueError("Cost must be an int")

        if cost < 0:
            raise ValueError("Cost can't be negative")

        if not isinstance(name, str):
            raise ValueError("Name must be a string")

        self.name = name
        self.cost = cost
        self.rarity = rarity.value

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        info = {"name": self.name, "cost": self.cost,
                "rarity": self.rarity}
        return info

    def is_playable(self, available_mana: int) -> bool:
        pass
