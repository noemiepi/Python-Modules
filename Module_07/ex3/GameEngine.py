# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameEngine.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 11:40:42 by npillet         #+#    #+#               #
#  Updated: 2026/03/20 11:11:28 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine():
    def __init__(self) -> None:
        self.hand = []
        self.battlefield = []
        self.turn = 0
        self.tot_damage = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        print(f"Factory: {factory.__name__}")
        print(f"Strategy: {strategy.__name__}")
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if len(self.battlefield) == 0:
            raise ValueError("Error! Battlefield is empty")
        if len(self.hand) == 0:
            raise ValueError("Error! Hand is empty")
        result_turn = self.strategy.execute_turn(self, self.hand,
                                                 self.battlefield)
        self.tot_damage += result_turn.get("damage_dealt")
        self.turn += 1

        return result_turn

    def get_engine_status(self) -> dict:
        report = {"turns_simulated": self.turn,
                  "strategy_used": self.strategy.__name__,
                  "total_damage": self.tot_damage,
                  "cards_created": len(self.hand)}
        return report
