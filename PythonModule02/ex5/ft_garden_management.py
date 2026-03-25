# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 10:04:24 by npillet         #+#    #+#               #
#  Updated: 2026/02/23 13:21:03 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant():
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager():
    def __init__(self) -> None:
        self.garden = []
        self.tank_water = 5

    def add_plant(self, name: str, water: int, sun: int) -> None:
        try:
            if name is None:
                raise PlantError("Plant name cannot be empty!")
        except PlantError as error:
            print(f"Error adding plant: {error}")
        else:
            self.garden.append(Plant(name, water, sun))
            print(f"Added {name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.garden:
                try:
                    if plant is None:
                        raise ValueError(f"Cannot water '{plant.name}' - "
                                         "invalid plant!")
                except ValueError as error:
                    print(f"Error: {error}")
                else:
                    print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        try:
            for plant in self.garden:
                try:
                    if plant.water < 1:
                        raise ValueError(f"Water level {plant.water} is too "
                                         "low (min 1)")
                    elif plant.water > 10:
                        raise ValueError(f"Water level {plant.water} is too "
                                         "high (max 10)")
                    elif plant.sun < 2:
                        raise ValueError(f"Sunlight hours {plant.sun} is too "
                                         "low (min 2)")
                    elif plant.sun > 12:
                        raise ValueError(f"Sunlight hours {plant.sun} is too "
                                         "high (max 12)")
                except ValueError as error:
                    print(f"Error checking {plant.name}: {error}")
                else:
                    print(f"{plant.name}: healthy (water: {plant.water}, sun: "
                          f"{plant.sun})")
        finally:
            print("")

    def tank_water_error(self) -> None:
        try:
            if self.tank_water < 10:
                raise WaterError("Not enough water in tank")
            print("No errors detected")
        except GardenError as error:
            print(f"Caught GardenError: {error}")
            print("System recovered and continuing...")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    garden = GardenManager()

    print("\nAdding plants to garden...")
    garden.add_plant("tomato", 5, 8)
    garden.add_plant("lettuce", 15, 8)
    garden.add_plant(None, 7, 6)

    print("\nWatering plants...")
    garden.water_plants()

    print("\nChecking plant health...")
    garden.check_plant_health()

    print("Testing error recovery...")
    garden.tank_water_error()
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
