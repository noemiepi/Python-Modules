# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 16:17:26 by npillet         #+#    #+#               #
#  Updated: 2026/02/20 09:15:28 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name=name, height=height, age=age)
        self.color = color

    def get_flower_info(self) -> None:
        print(f"\n{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name=name, height=height, age=age)
        self.trunk_diameter = trunk_diameter

    def get_tree_info(self) -> None:
        print(f"\n{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter} diameter")

    def produce_shade(self) -> None:
        radius = self.height / 100
        area = 3.14 * (radius ** 2)
        print(f"{self.name} provides {int(area)} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name=name, height=height, age=age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_veg_info(self) -> None:
        print(f"\n{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")

    def get_nutri_info(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


def ft_plant_types() -> None:
    plant_list = [
        Flower("Rose", 25, 30, "red"),
        Tree("Oak", 500, 1825, 50),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Flower("Sunflower", 80, 45, "yellow"),
        Tree("Spruce", 800, 2450, 60),
        Vegetable("Carrot", 30, 70, "autumn", "vitamin A")
    ]
    print("=== Garden Plant Types ===")
    for plant in plant_list:
        if isinstance(plant, Flower):
            plant.get_flower_info()
            plant.bloom()
        elif isinstance(plant, Tree):
            plant.get_tree_info()
            plant.produce_shade()
        elif isinstance(plant, Vegetable):
            plant.get_veg_info()
            plant.get_nutri_info()


if __name__ == "__main__":
    ft_plant_types()
