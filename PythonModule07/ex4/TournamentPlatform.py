# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentPlatform.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 11:43:54 by npillet         #+#    #+#               #
#  Updated: 2026/03/24 15:46:16 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self) -> None:
        self.card_dict = {}
        self.nb_card = 0
        self.nb_match = 0
        self.tot_rating = 0

    def register_card(self, card: TournamentCard) -> str:
        self.card_dict.update({card.card_id: card})
        self.nb_card += 1
        return (f"\n{card.name} (ID: {card.card_id}):"
                f"\n- Interfaces: {card.__class__.__name__}"
                f"\n- Rating: {card.rating}"
                f"\n- Record: 0-0")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.card_dict.get(card1_id)
        card2 = self.card_dict.get(card2_id)
        self.nb_match += 1
        while card1.health > 0 or card2.health > 0:
            card1.attack(card2)
            card2.attack(card1)

        if card1.health >= card2.health:
            result = {"winner": card1_id, "loser": card2_id,
                      "winner_rating": card1.rating,
                      "loser_rating": card2.rating}
            card1.update_wins(1)
            card2.update_losses(1)
            card1.calculate_rating()
            card2.calculate_rating()
        elif card1.health < card2.health:
            result = {"winner": card2_id, "loser": card1_id,
                      "winner_rating": card1.rating,
                      "loser_rating": card2.rating}
            card2.update_wins(1)
            card1.update_losses(1)

        self.tot_rating = card1.rating + card2.rating
        return result

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(self.card_dict.values(),
                              key=lambda card: card.rating, reverse=True)
        card_list = []
        for card in sorted_cards:
            card_info = (f"{card.name} - Rating: {card.rating} ({card.win}-"
                         f"{card.loose})")
            card_list.append(card_info)
        return card_list

    def generate_tournament_report(self) -> dict:
        try:
            average = self.tot_rating / self.nb_card
        except ZeroDivisionError as e:
            print(e)
            return
        report = {"total_cards": self.nb_card, "matches_played":
                  self.nb_match, "avg_rating": average,
                  "platform_status": "active"}
        return report
