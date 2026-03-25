# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  CreatureCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/16 11:00:39 by npillet         #+#    #+#               #
#  Updated: 2026/03/18 09:57:23 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card, Rarity


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity, attack: int,
                 health: int) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.attack = attack
        self.health = health

        if not isinstance(attack, int):
            raise ValueError("Attack must be an int")
        if not isinstance(health, int):
            raise ValueError("Health must be an int")

        if attack < 0:
            raise ValueError("Attack can't be negative")
        if health < 0:
            raise ValueError("Health can't be negative")

    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        info = {"name": self.name, "cost": self.cost,
                "rarity": self.rarity, "type": "Creature",
                "attack": self.attack, "health": self.health}
        return info

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= 5:
            playable = True
            print(f"Playable: {playable}")

            result = {"card_played": self.name, "mana_used": 5,
                      "effect": "Creature summoned to the battlefield"}
            print(f"Play result: {result}")
        else:
            playable = False
        return playable

    def attack_target(self, target) -> dict:
        print(f"\n{self.name} attacks {target.name}:")
        if self.attack >= target.health:
            combat = True
        else:
            combat = False
        result = {"attacker": self.name, "target": target.name,
                  "damage_dealt": self.attack, "combat_resolved": combat}
        return f"Attack result: {result}"
