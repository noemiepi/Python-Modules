# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 13:47:01 by npillet         #+#    #+#               #
#  Updated: 2026/02/28 15:14:59 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def garden_operations(x: int, div=None, file=None, key=None) -> None:
    dict = {'name': 'Alice'}
    nb = int(x)
    if div is not None:
        _ = nb / div
    if file is not None:
        open(file, 'r')
    if key is not None:
        _ = dict[key]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("\nTesting ValueError...")
    try:
        garden_operations(x="abc")
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations(x=2, div=0)
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    file_name = 'missing.txt'
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations(x=2, file=file_name)
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    word = "_plant"
    print("\nTesting KeyError...")
    try:
        garden_operations(x=2, key=word)
    except KeyError as error:
        print(f"Caught KeyError: {error}")
    print("\nTesting multiple errors together...")
    try:
        garden_operations(x=2, div=0, file=file_name)
    except (ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested succesfully!")


if __name__ == "__main__":
    test_error_types()
