# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentCard.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 11:38:32 by npillet         #+#    #+#               #
#  Updated: 2026/03/24 15:27:12 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: Rarity, attack_point: int,
                 health: int, rating: int, card_id: str) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.health = health
        self.attack_point = attack_point
        self.rating = rating
        self.card_id = card_id
        self.win = 0
        self.loose = 0

        if not isinstance(attack_point, int):
            raise ValueError("Attack must be an int")
        if attack_point < 0:
            raise ValueError("Attack can't be negative")

        if not isinstance(health, int):
            raise ValueError("Health must be an int")
        if health < 0:
            raise ValueError("Health can't be negative")

        if not isinstance(rating, int):
            raise ValueError("Rating must be an int")
        if rating < 0:
            raise ValueError("Rating can't be negative")

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        target.health -= self.attack_point
        return {"health": target.health}

    def defend(self, incomming_damage: int) -> dict:
        damage = incomming_damage - self.health
        if damage <= 0:
            still_alive = False
        else:
            still_alive = True
        if incomming_damage >= 0:
            return ({"damage received": incomming_damage,
                     "still_alive": still_alive})

    def update_wins(self, wins: int) -> None:
        self.win += wins

    def update_losses(self, losses: int) -> None:
        self.loose += losses

    def calculate_rating(self) -> int:
        if self.win > 0:
            self.rating += 16
        elif self.loose > 0:
            self.rating -= 16
        return self.rating

    def get_rank_info(self) -> dict:
        return {"Rating": {self.rating}}

    def get_tournament_stats(self) -> dict:
        return {"Record": f"{self.win}-{self.loose}"}

    def get_combat_stats(self) -> dict:
        pass
