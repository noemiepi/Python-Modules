# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_circular_curse.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/11 14:50:29 by npillet         #+#    #+#               #
#  Updated: 2026/03/11 15:47:29 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===")

    print("\nTesting ingredients validation:")
    from alchemy.grimoire.validator import validate_ingredients
    print(f"validate_ingredients('fire air'): "
          f"{validate_ingredients('fire air')}")
    print(f"validate_ingredients('dragon scales'): "
          f"{validate_ingredients('dragon scales')}")

    print("\nTesting spell recording with validation:")
    from alchemy.grimoire.spellbook import record_spell
    print(f"record_spell('Fireball', 'fire air'): "
          f"{record_spell('Fireball', 'fire air')}")
    print(f"record_spell('Dark Magic', 'shadow'): "
          f"{record_spell('Dark Magic', 'shadow')}")

    print("\nTesting late import technique:")
    print(f"record_spell('Lightning', 'air'): "
          f"{record_spell('Lightning', 'air')}")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
