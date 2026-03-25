# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 13:49:14 by npillet         #+#    #+#               #
#  Updated: 2026/02/18 15:07:10 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant():
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.days} days old"

    def grow(self) -> int:
        growth = 6
        self.height += growth
        return growth

    def age(self) -> None:
        older = 6
        self.days += older


def ft_plant_growth() -> None:
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(plant.get_info())
    print("=== Day 7 ===")
    growth = plant.grow()
    plant.age()
    print(plant.get_info())
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
