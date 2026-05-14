# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 15:42:06 by npillet         #+#    #+#               #
#  Updated: 2026/02/28 15:17:56 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def generate_plant_error(plant: str, watering: int) -> None:
    if watering == 0:
        raise PlantError(f"The {plant} plant is wilting!")


def generate_water_error(water_level: int):
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    plant = "tomato"
    watering = 0
    print("\nTesting PlantError...")
    try:
        generate_plant_error(plant, watering)
        print("No error detected")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    water_level = 5
    print("\nTesting WaterError...")
    try:
        generate_water_error(water_level)
        print("No error detected")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        generate_plant_error(plant, watering)
        print("No error detected")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        generate_water_error(water_level)
        print("No error detected")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
