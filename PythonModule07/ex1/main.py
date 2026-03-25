# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/16 12:04:50 by npillet         #+#    #+#               #
#  Updated: 2026/03/19 08:35:18 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex1.Deck import Deck
from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


def implementation_layer():
    try:
        print("\nBuilding deck with different card types...")
        card_list = [
            CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5),
            SpellCard("Lightning Bolt", 3, Rarity.RARE, "Deal 3 damage "
                      "to target"),
            ArtifactCard("Mana Crystal", 2, Rarity.RARE, 3, "Permanent: +1 "
                         "mana per turn")
        ]

        deck = Deck()
        try:
            for card in card_list:
                deck.add_card(card)
        except ValueError:
            print("Could not put every card in the deck")

        print(f"Deck stats: {deck.get_deck_stats()}")

        deck.shuffle()
        print("\nDrawing and playing cards:")
        available_mana = 6
        i = 0
        try:
            for card in deck.deck:
                while i <= len(deck.deck) + 1:
                    card = deck.draw_card()
                    if type(card).__name__ == "CreatureCard":
                        print(f"\nDrew: {card.name} (Creature)")
                    if type(card).__name__ == "SpellCard":
                        print(f"\nDrew: {card.name} (Spell)")
                    if type(card).__name__ == "ArtifactCard":
                        print(f"\nDrew: {card.name} (Artifact)")
                    card.is_playable(available_mana)
                    i += 1
        except ValueError:
            print("An error occured while drawing and playing the cards")
        print("\nPolymorphism in action: Same interface, different card "
              "behaviors!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===")
    implementation_layer()
