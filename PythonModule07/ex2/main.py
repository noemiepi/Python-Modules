# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/18 09:35:08 by npillet         #+#    #+#               #
#  Updated: 2026/03/20 09:22:09 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard


def ability_layer() -> None:
    try:
        print("\nEliteCard capabilities:")
        card_func = ["play", "get_card_info", "is_playable"]
        comb_func = ["attack", "defend", "get_combat_stats"]
        magic_func = ["cast_spell", "channel_mana", "get_magic_stats"]
        print(f"- Card: {card_func}")
        print(f"- Combatable: {comb_func}")
        print(f"- Magical: {magic_func}")

        warrior = EliteCard("Arcane Warrior", 4, Rarity.ELITE, 5, 3, 10)
        print(f"\nPlaying {warrior.name} (Elite Card):")

        enemy = CreatureCard("Enemy", 2, Rarity.RARE, 5, 7)
        try:
            print("\nCombat phase:")
            print(f"Attack result: {warrior.attack(enemy)}")
            print(f"Defense result: {warrior.defend(5)}")
        except (ValueError, TypeError) as e:
            print(e)

        enemies = ["Enemy1", "Enemy2"]
        try:
            print("\nMagic phase:")
            spell = "Fireball"
            print(f"Spell cast: {warrior.cast_spell(spell, enemies)}")
            print(f"Mana channel: {warrior.channel_mana(warrior.mana)}")
        except (ValueError, TypeError) as e:
            print(e)
        print("\nMultiple interface implementation successful!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("\n=== DataDeck Ability System ===")
    ability_layer()
