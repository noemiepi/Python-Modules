# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 16:50:22 by npillet         #+#    #+#               #
#  Updated: 2026/02/23 13:35:31 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class WaterError(Exception):
    pass


def watering_error(plant) -> None:
    if plant is None:
        raise WaterError(f"Cannot water {plant} - invalid plant!")
    else:
        print(f"Watering {plant}")


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            watering_error(plant)
    except WaterError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    plant_list = [
        "tomato",
        "lettuce",
        "carrots"
    ]
    print("\nTesting normal watering system...")
    water_plants(plant_list)
    print("Watering completed succesfully!")
    plant_list = [
        "tomato",
        None,
        "carrots"
    ]
    print("\nTesting with error...")
    water_plants(plant_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
