# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/16 11:06:30 by npillet         #+#    #+#               #
#  Updated: 2026/03/19 08:34:49 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def fondation_layer() -> None:
    try:
        print("\nTesting Abstract Base Class Design:")
        dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
        goblin = CreatureCard("Goblin Warrior", 2, Rarity.COMMON, 3, 3)

        print("\nCreatureCard Info:")
        print(dragon.get_card_info())

        available_mana = 6
        print(f"\nPlaying {dragon.name} with {available_mana} mana available:")
        dragon.is_playable(available_mana)

        print(dragon.attack_target(goblin))

        available_mana = 3
        print(f"\nTesting with insufficient mana ({available_mana} "
              "available):")
        print(f"Playable: {dragon.is_playable(available_mana)}")

        print("\nAbstract pattern successfully demonstrated!")
    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    print("\n=== DataDeck Card Fondation ===")
    fondation_layer()
