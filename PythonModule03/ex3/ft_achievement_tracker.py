# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 11:54:09 by npillet         #+#    #+#               #
#  Updated: 2026/02/24 14:36:12 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    print(f"\nPlayer alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {alice.union(bob, charlie)}")
    print(f"Total unique achievement: {len(alice.union(bob, charlie))}")

    print(f"\nCommon to all players: {alice.intersection(bob, charlie)}")
    rare_alice = alice.difference(bob, charlie)
    rare_bob = bob.difference(alice, charlie)
    rare_charlie = charlie.difference(alice, bob)
    rare = rare_alice.union(rare_bob, rare_charlie)
    print(f"Rare achivement (1 player): {rare}")

    print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    ft_achievement_tracker()
