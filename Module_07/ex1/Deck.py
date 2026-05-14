# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Deck.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/16 12:00:03 by npillet         #+#    #+#               #
#  Updated: 2026/03/16 15:47:06 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck():
    def __init__(self) -> None:
        self.deck = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        self.deck.remove(card_name)
        if card_name not in self.deck:
            return True
        else:
            return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        if len(self.deck) == 0:
            print("The deck is empty")
            return
        card = self.deck.pop(0)
        return card

    def get_deck_stats(self) -> dict:
        tot_card = len(self.deck)
        add = 0
        creature = 0
        spell = 0
        artifact = 0
        for card in self.deck:
            if isinstance(card, CreatureCard):
                creature += 1
            elif isinstance(card, SpellCard):
                spell += 1
            elif isinstance(card, ArtifactCard):
                artifact += 1
            add += card.cost
        avg = add / tot_card
        result = {"total_cards": tot_card, "creatures": creature,
                  "spells": spell, "artifacts": artifact,
                  "avg_cost": round(avg, 1)}
        return result
