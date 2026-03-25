# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 11:48:04 by npillet         #+#    #+#               #
#  Updated: 2026/03/24 15:45:38 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def engine_layer() -> None:
    try:
        print("\nConfiguring Fantasy Card Game...")
        try:
            game = GameEngine()
            card_type = FantasyCardFactory()
            game.configure_engine(FantasyCardFactory, AggressiveStrategy)
            print(f"Available types: {card_type.get_supported_types()}")
        except ValueError:
            print("Error while configuring the game")

        deck_size = 3
        hand_stats = []
        print("\nSimulating aggressive turn...")
        try:
            if deck_size <= 0:
                print("Enter a positive value above zero")
                return

            hand = card_type.create_themed_deck(deck_size)
            for card in hand.values():
                game.hand.append(card)
                name = card.name
                cost = card.cost
                card_stats = name + " (" + str(cost) + ")"
                hand_stats.append(card_stats)

            print(f"Hand: {hand_stats}")
        except ValueError:
            print("Error while generating the hand")

        strategy = AggressiveStrategy()
        enemies = [
            CreatureCard("Enemy Player", 3, Rarity.RARE, 2, 20),
            SpellCard("Enemy Spell", 3, Rarity.COMMON, "Deal 3 damage to "
                      "target"),
            ArtifactCard("Enemy Artifact", 2, Rarity.RARE, 3, "Permanent: "
                         "+1 mana per turn")
        ]
        print("\nTurn execution:")
        try:
            enemy_card = strategy.prioritize_targets(enemies)
            for card in enemy_card:
                game.battlefield.append(card)
            print(f"Strategy: {strategy.get_strategy_name()}")
            print(f"Actions: {game.simulate_turn()}")
        except ValueError:
            print("Error while executing the turn")

        print("\nGame Report:")
        try:
            print(game.get_engine_status())
        except ValueError:
            print("Error while printing Game Report")
        print("\nAbstract Factory + Strategy Pattern: Maximum flexibility "
              "achieved!")
    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===")
    engine_layer()
