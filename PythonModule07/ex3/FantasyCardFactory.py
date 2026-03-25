# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  FantasyCardFactory.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 11:46:21 by npillet         #+#    #+#               #
#  Updated: 2026/03/20 09:23:01 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory

import random


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creatures = {
            "dragon": CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 9, 7),
            "goblin": CreatureCard("Goblin Warrior", 2, Rarity.RARE, 5, 3)
        }
        self.spells = {
            "fire": SpellCard("Fireball", 4, Rarity.RARE, "Deal 4 damage to "
                              "target"),
            "ice": SpellCard("Ice Spike", 3, Rarity.COMMON, "Deal 3 damage to "
                             "target"),
            "lightning": SpellCard("Lightning Bolt", 3, Rarity.RARE, "Deal 3 "
                                   "damage to target"),
        }
        self.artifacts = {
            "ring": ArtifactCard("HP Ring", 1, Rarity.COMMON, 3, "Permanent: "
                                 "+1 health per turn"),
            "staff": ArtifactCard("Mana Staff", 3, Rarity.ELITE, 3, "Permanent"
                                  ": +2 damage on the spell"),
            "crystal": ArtifactCard("Mana Crystal", 2, Rarity.RARE, 3,
                                    "Permanent: +1 mana per turn")
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None or self:
            card = random.choice(list(self.creatures.keys()))
        else:
            card = name_or_power
        return card

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None or self:
            card = random.choice(list(self.spells.keys()))
        else:
            card = name_or_power
        return card

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None or self:
            card = random.choice(list(self.artifacts.keys()))
        else:
            card = name_or_power
        return card

    def create_themed_deck(self, size: int) -> dict:
        card_type = [
            self.create_creature(),
            self.create_spell(),
            self.create_artifact()
            ]
        hand = {}
        all_dict = {}
        card_list = []

        while len(card_list) < size:
            new_card = random.choice(card_type)

            if new_card not in card_list:
                card_list.append(new_card)

        all_dict.update(self.creatures)
        all_dict.update(self.spells)
        all_dict.update(self.artifacts)

        for card in card_list:
            hand[card] = all_dict[card]

        return hand

    def get_supported_types(self) -> dict:
        creature = list(self.creatures.keys())
        spells = list(self.spells.keys())
        artifacts = list(self.artifacts.keys())
        available = {"creatures": creature, "spells": spells,
                     "artifacts": artifacts}
        return available
