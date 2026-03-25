# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ArtifactCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/16 11:56:13 by npillet         #+#    #+#               #
#  Updated: 2026/03/18 09:20:01 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card, Rarity


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity, durability: int,
                 effect: str) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.durability = durability
        self.effect = effect

        if not isinstance(durability, int):
            raise ValueError("Durability must be an int")
        if durability < 0:
            raise ValueError("Durability can't be negative")

        if not isinstance(effect, str):
            raise ValueError("Effect must be a string")

    def play(self, game_state: dict) -> dict:
        pass

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= 5:
            playable = True
            print(f"Playable: {playable}")

            result = {"card_played": self.name, "mana_used": 5,
                      "effect": self.effect}
            print(f"Play result: {result}")
        else:
            playable = False
        return playable

    def activate_ability(self) -> dict:
        pass
