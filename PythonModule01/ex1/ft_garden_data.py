# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 12:00:30 by npillet         #+#    #+#               #
#  Updated: 2026/02/19 09:47:23 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_plant_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sun = Plant("Sunflower", 80, 45)
    cact = Plant("Cactus", 15, 120)
    print(rose.get_plant_info())
    print(sun.get_plant_info())
    print(cact.get_plant_info())


if __name__ == "__main__":
    ft_garden_data()
