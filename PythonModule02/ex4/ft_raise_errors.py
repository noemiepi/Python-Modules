# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_errors.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 17:13:53 by npillet         #+#    #+#               #
#  Updated: 2026/02/23 13:26:19 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_plant_health(plant_name: str, water_level: int, sunlight_hours:
                       int) -> str:
    if plant_name is None:
        raise ValueError("Plant name cannot be empty")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high "
                         "(max 12)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low "
                         "(min 2)")
    else:
        return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    try:
        check_plant_health("tomato", 5, 6)
        print(check_plant_health("tomato", 5, 6))
    except ValueError as error:
        print(f"Error: {error}")
    print("\nTesting empty plant name...")
    try:
        check_plant_health(None, 5, 6)
        print(check_plant_health(None, 5, 6))
    except ValueError as error:
        print(f"Error: {error}")
    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 6)
        print(check_plant_health("tomato", 15, 6))
    except ValueError as error:
        print(f"Error: {error}")
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
        print(check_plant_health("tomato", 5, 0))
    except ValueError as error:
        print(f"Error: {error}")
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
