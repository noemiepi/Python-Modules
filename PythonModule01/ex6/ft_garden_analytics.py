# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 09:16:28 by npillet         #+#    #+#               #
#  Updated: 2026/02/26 16:17:02 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant():
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def set_height(self, amount: int) -> int:
        self.height += amount
        print(f"{self.name} grew {amount}cm")
        return amount

    def get_height(self) -> int:
        return {self.height}

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name=name, height=height)
        self.color = color

    def get_info(self) -> str:
        return (f"- {self.name}: {self.height}cm, {self.color} flowers "
                "(blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 points: int) -> None:
        super().__init__(name=name, height=height, color=color)
        self.points = points

    def get_info(self) -> str:
        return (f"- {self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming), Prize points: {self.points}")


class GardenManager():
    nb_garden = 0

    def __init__(self) -> None:
        self.garden = {}
        self.stats = GardenManager.GardenStats()

    class GardenStats():
        def __init__(self) -> None:
            self.nb_plant = 0
            self.nb_flower = 0
            self.nb_prized = 0
            self.total_plants = 0

    def add_plant(self, owner: str, plant: list) -> None:
        self.garden[owner] = plant
        for i in range(0, len(plant)):
            print(f"Added {plant[i].name} to {owner}'s garden")

    def add_plant_invis(self, owner: str, plant: list) -> None:
        self.garden[owner] = plant

    def plant_growth(self, owner: str, amount: int) -> None:
        if amount > 0:
            print(f"\n{owner} is helping all plants grow...")
            for garden in self.garden.values():
                for plant in garden:
                    plant.set_height(amount)
                return
        else:
            print(f"Invalid operation attempted: height {amount}cm "
                  "[REJECTED]")
            print("Program stopped")
            return

    def garden_plants(self, owner: str) -> None:
        print(f"\n=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for garden in self.garden.values():
            for plant in garden:
                print(plant.get_info())
                self.stats.total_plants += 1
                if isinstance(plant, PrizeFlower):
                    self.stats.nb_prized += 1
                elif isinstance(plant, FloweringPlant):
                    self.stats.nb_flower += 1
                elif isinstance(plant, Plant):
                    self.stats.nb_plant += 1
            return

    @staticmethod
    def valid_height(amount: int) -> bool:
        if amount > 0:
            return True
        else:
            return False

    def score(self, owner: str) -> int:
        score = 0
        garden = self.garden[owner]
        for plant in garden:
            score += 10
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.points
        return score

    def garden_report(self, owner1: str, owner2: str, amount: int) -> None:
        print(f"\nPlants added: {self.stats.total_plants}, Total growth: "
              f"{self.stats.total_plants * amount}cm")
        print(f"Plant types: {self.stats.nb_plant} regular, "
              f"{self.stats.nb_flower} flowering, {self.stats.nb_prized} "
              "prized flowers")
        print(f"\nHeight validation test: {self.valid_height(amount)}")
        print(f"Garden scores - {owner1}: {self.score(owner1)}, {owner2}: "
              f"{self.score(owner2)}")
        print(f"Total gardens managed: {GardenManager.nb_garden}")

    @classmethod
    def create_garden_network(cls) -> type:
        manager = cls()
        manager.garden["Alice"] = []
        manager.garden["Bob"] = []
        GardenManager.nb_garden += 2
        return manager


def ft_garden_analytics() -> None:
    plant_lst1 = [Plant("Oak Tree", 100),
                  FloweringPlant("Rose", 25, "red"),
                  PrizeFlower("Sunflower", 50, "yellow", 10)]
    plant_lst2 = [Plant("Fern", 15),
                  FloweringPlant("Azalea", 25, "pink"),
                  PrizeFlower("Begonia", 15, "orange", 7)]
    print("=== Garden Management System Demo ===\n")
    network = GardenManager.create_garden_network()
    network.add_plant("Alice", plant_lst1)
    network.add_plant_invis("Bob", plant_lst2)
    network.plant_growth("Alice", 1)
    network.garden_plants("Alice")
    network.garden_report("Alice", "Bob", 1)


if __name__ == "__main__":
    ft_garden_analytics()
