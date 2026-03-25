# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 11:47:45 by npillet         #+#    #+#               #
#  Updated: 2026/03/24 15:46:38 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Rarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def platform_layer() -> None:
    try:
        print("\nRegistering Tournament Cards...")
        try:
            platform = TournamentPlatform()
            dragon = TournamentCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 10,
                                    1200, "dragon_001")
            wizard = TournamentCard("Ice Wizard", 4, Rarity.ELITE, 5, 6, 1150,
                                    "wizard_001")
        except (ValueError, TypeError) as e:
            print(e)
            return

        print(platform.register_card(dragon))
        print(platform.register_card(wizard))

        print("\nCreating tournament match...")
        match = platform.create_match(dragon.card_id, wizard.card_id)
        print(f"Match result: {match}")

        print("\nTournament Leaderboard:")
        leaderboard = platform.get_leaderboard()
        i = 1
        for card in leaderboard:
            print(f"{i}. {card}")
            i += 1

        print("\nPlatform Report:")
        print(platform.generate_tournament_report())

        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===")
    platform_layer()
