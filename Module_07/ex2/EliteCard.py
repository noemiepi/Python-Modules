# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  EliteCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 09:22:35 by npillet         #+#    #+#               #
#  Updated: 2026/03/27 11:46:39 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: Rarity, attack_value: int,
                 defense: int, mana: int) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.attack_value = attack_value
        self.defense = defense
        self.mana = mana

        try:
            attack_value = int(attack_value)
            if not isinstance(attack_value, int):
                raise ValueError("Attack must be an int")
            if attack_value < 0:
                raise ValueError("Attack can't be negative")
        except ValueError:
            print("Attack must be an int")
            exit()

        try:
            defense = int(defense)
            if not isinstance(defense, int):
                raise ValueError("Defense must be an int")
            if defense < 0:
                raise ValueError("Defense can't be negative")
        except ValueError:
            print("Defense must be an int")
            exit()

        try:
            mana = int(mana)
            if not isinstance(mana, int):
                raise ValueError("Mana must be an int")
            if mana < 0:
                raise ValueError("Mana can't be negative")
        except ValueError:
            print("Mana must be an int")
            exit()

    def get_card_info(self) -> dict:
        info = {"name": self.name, "cost": self.cost, "attack": self.attack,
                "defense": self.defense, "mana": self.mana}
        return info

    def play(self, game_state: dict) -> dict:
        try:
            can_play = {}
            if game_state.get("play") is True:
                can_play = {"play": True}
            else:
                can_play = {"play": False}
            return can_play
        except Exception as e:
            print(e)

    def attack(self, target) -> dict:
        result = {"attacker": self.name, "target": target.name,
                  "damage": self.attack_value, "combat_type": "melee"}
        return result

    def defend(self, incomming_damage: int) -> dict:
        damage_taken = incomming_damage - self.defense
        if damage_taken <= 0:
            still_alive = False
        else:
            still_alive = True
        result = {"defender": self.name, "damage_taken": damage_taken,
                  "damage_blocked": self.defense, "still_alive": still_alive}
        return result

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        cost_spell = 2
        used_mana = cost_spell * len(targets)
        result = {"caster": self.name, "spell": spell_name, "targets": targets,
                  "mana_used": used_mana}
        return result

    def channel_mana(self, amount: int) -> dict:
        channeled = 3
        new_total = amount - channeled
        result = {"channeled": channeled, "total_mana": new_total}
        return result

    def get_combat_stats(self) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        pass
