# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 10:35:35 by npillet         #+#    #+#               #
#  Updated: 2026/03/09 08:55:15 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math


def ft_coordinates_system() -> tuple:
    try:
        coor = tuple(int(x) for x in str.split(","))
        return coor
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: ValueError, Args: ({error})")
        return None


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    try:
        pos = (10, 20, 5)
        start = (0, 0, 0)
        print(f"\nPosition created: {pos}")
        x1, y1, z1 = pos
        x2, y2, z2 = start
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        print(f"Distance between {start} and {pos}: {dist:.2f}")

        str = "3,4,0"
        print(f"\nParsing coordinates: '{str}'")
        coor1 = ft_coordinates_system()
        print(f"Parsed postion: {coor1}")
        if coor1 is not None:
            x1, y1, z1 = coor1
            dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            print(f"Distance between {start} and {coor1}: {dist:.1f}")

        str = "abc,def,ghi"
        print(f"\nParsing coordinates: '{str}'")
        coor2 = ft_coordinates_system()
        if coor2 is not None:
            x1, y1, z1 = coor2
            dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            print(f"Distance between {start} and {coor2}: {dist:.1f}")

        print("\nUnpacking demonstration:")
        x1, y1, z1 = coor1
        print(f"Player at x={x1}, y={y1}, z={z1}")
        print(f"Coordinates: X={x1}, Y={y1}, Z={z1}")

    except TypeError as e:
        print(e)
