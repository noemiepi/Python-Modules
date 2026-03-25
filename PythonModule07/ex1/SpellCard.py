# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  SpellCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/16 11:52:41 by npillet         #+#    #+#               #
#  Updated: 2026/03/18 09:20:10 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card, Rarity


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 effect_type: str) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.effect_type = effect_type

        if not isinstance(effect_type, str):
            raise ValueError("Effect_type must be a string")

    def get_card_info(self) -> dict:
        info = {"name": self.name, "cost": self.cost,
                "effect": self.rarity}
        return info

    def play(self, game_state: dict) -> dict:
        pass

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= 5:
            playable = True
            print(f"Playable: {playable}")

            result = {"card_played": self.name, "mana_used": 5,
                      "effect": self.effect_type}
            print(f"Play result: {result}")
        else:
            playable = False
        return playable

    def resolve_effect(self, targets: list) -> dict:
        pass
