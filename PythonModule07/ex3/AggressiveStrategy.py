# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  AggressiveStrategy.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 11:36:43 by npillet         #+#    #+#               #
#  Updated: 2026/03/20 11:17:14 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        played = []
        mana_used = 0
        damage_dealt = 0
        on_board = 1
        max_board = 2
        for card in hand:
            if isinstance(card, CreatureCard) or isinstance(card, SpellCard):
                if card.cost < 4 and on_board <= max_board:
                    played.append(card.name)
                    mana_used += card.cost
                    if isinstance(card, CreatureCard):
                        damage_dealt += card.attack
                    elif isinstance(card, SpellCard):
                        damage_dealt += card.cost
                    on_board += 1

        for card in hand:
            if isinstance(card, CreatureCard) or isinstance(card, SpellCard):
                if card.cost >= 4 and on_board <= max_board:
                    played.append(card.name)
                    mana_used += card.cost
                    if isinstance(card, CreatureCard):
                        damage_dealt += card.attack
                    elif isinstance(card, SpellCard):
                        damage_dealt += card.cost
                    on_board += 1

        resume = {"card_played": played, "mana_used": mana_used,
                  "targets_attacked": battlefield,
                  "damage_dealt": damage_dealt}
        return resume

    def get_strategy_name(self) -> str:
        return "AggresiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        attacked = []

        for enemy in available_targets:
            if isinstance(enemy, CreatureCard):
                attacked.append(enemy.name)
        return attacked
