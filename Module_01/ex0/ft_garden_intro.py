# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_intro.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 11:58:25 by npillet         #+#    #+#               #
#  Updated: 2026/02/19 09:47:39 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_garden_intro() -> None:
    print("=== Welcome to My Garden ===")
    name = "Rose"
    height = 25
    age = 30
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
