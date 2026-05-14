# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 13:18:12 by npillet         #+#    #+#               #
#  Updated: 2026/02/23 13:31:39 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_temperature(temp_str: str) -> int:
    if not isinstance(temp_str, str):
        print("Error: entered value is not a string")
        return
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return
    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        return
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        return
    else:
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    check_temperature("25")
    print("\nTesting temperature: abc")
    check_temperature("abc")
    print("\nTesting temperature: 100")
    check_temperature("100")
    print("\nTesting temperature: -50")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash")


if __name__ == "__main__":
    test_temperature_input()
