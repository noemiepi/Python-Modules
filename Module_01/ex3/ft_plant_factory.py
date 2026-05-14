# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 09:44:32 by npillet         #+#    #+#               #
#  Updated: 2026/02/19 12:32:50 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


def ft_plant_factory():
    plant_list = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    i = 0
    print("=== Plant Factory Output ===")
    for data in plant_list:
        print(data.get_info())
        i += 1
    print(f"\nTotal plants created: {i}")


if __name__ == "__main__":
    ft_plant_factory()
