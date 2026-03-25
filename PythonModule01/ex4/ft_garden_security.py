# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 12:33:33 by npillet         #+#    #+#               #
#  Updated: 2026/02/26 15:01:06 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class SecurePlant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def get_info(self) -> None:
        if self.__height <= 0 or self.__age <= 0:
            return
        else:
            print(f"\nCurrent plant: {self.name} ({self.__height}cm, "
                  f"{self.__age} days)")

    def set_height(self, amount: int) -> None:
        if not isinstance(amount, int):
            print("\nHeight is not int")
            return
        if amount > 0:
            self.__height = amount
        else:
            print(f"\nInvalid operation attempted: height {amount}cm "
                  f"[REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, amount: int) -> None:
        if not isinstance(amount, int):
            print("\nAge is not int")
            return
        if amount > 0:
            self.__age = amount
        else:
            print(f"\nInvalid operation attempted: age {amount} days "
                  f"[REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> str:
        if self.__height > 0:
            return f"Height updated: {self.__height}cm [OK]"
        else:
            return f"Height cannot be updated: {self.__height}cm [REJECTED]"

    def get_age(self) -> str:
        if self.__age > 0:
            return f"Age updated: {self.__age} days [OK]"
        else:
            return f"Age cannot be updated: {self.__height} days [REJECTED]"

    def get_name(self) -> str:
        return f"Plant created: {self.name}"


def ft_garden_security() -> None:
    rose = SecurePlant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print(rose.get_name())
    print(rose.get_height())
    print(rose.get_age())
    rose.set_height(-5)
    # rose.set_age(-1)
    rose.get_info()


if __name__ == "__main__":
    ft_garden_security()
