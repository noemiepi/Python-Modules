# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_pathway_debate.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 14:30:19 by npillet         #+#    #+#               #
#  Updated: 2026/03/11 14:50:09 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy
from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import elixir_of_life, philosophers_stone

if __name__ == "__main__":
    print("\n=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")

    print("\nTesting Package Access:")
    print(f"alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print(f"alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")
