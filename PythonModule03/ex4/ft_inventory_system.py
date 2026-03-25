# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 14:37:16 by npillet         #+#    #+#               #
#  Updated: 2026/03/09 09:01:01 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def total_items(moderate: dict, scarce: dict) -> int:
    tot_item = sum(moderate.values()) + sum(scarce.values())
    return tot_item


def sorted_dict(moderate: dict, scarce: dict) -> None:
    print("\n=== Current Inventory ===")
    for mkey in sorted(moderate, key=moderate.get, reverse=True):
        percent = (int(moderate.get(mkey)) /
                   total_items(moderate, scarce)) * 100
        print(f"{mkey}: {moderate.get(mkey)} units ({percent:.1f}%)")
    for skey in sorted(scarce, key=scarce.get, reverse=True):
        percent = (int(scarce.get(skey)) / total_items(moderate, scarce)) * 100
        if int(scarce.get(skey)) > 1:
            print(f"{skey}: {scarce.get(skey)} units ({percent:.1f}%)")
        else:
            print(f"{skey}: {scarce.get(skey)} unit ({percent:.1f}%)")


def abundance(moderate: dict, scarce: dict) -> None:
    print("\n=== Inventory Statistics ===")
    if len(moderate) > 0:
        sort_mod = sorted(moderate, key=moderate.get, reverse=True)
        first_mod = list(sort_mod)[0]
        print(f"Most abundant: {first_mod} ({moderate.get(first_mod)} units)")
    if len(scarce) > 0:
        sort_sca = sorted(scarce, key=scarce.get, reverse=False)
        first_sca = list(sort_sca)[0]
        if int(scarce.get(first_sca)) > 1:
            print(f"Least abundant: {first_sca} ({scarce.get(first_sca)} "
                  "units)")
        else:
            print(f"Least abundant: {first_sca} ({scarce.get(first_sca)} "
                  "unit)")


def suggestion(scarce: dict) -> None:
    print("\n=== Management Suggestions ===")
    restock = {}
    for key, value in scarce.items():
        if value == 1:
            restock[key] = value
    low_item = ", ".join(f"{key}" for key, value in restock.items())
    print(f"Restock needed: {low_item}")


def properties(combined: dict) -> None:
    print("\n=== Dictionary Properties Demo ===")
    keys = ", ".join(f"{key}" for key, value in combined.items())
    print(f"Dictionary keys: {keys}")
    values = ", ".join(f"{value}" for key, value in combined.items())
    print(f"Dictionary values: {values}")
    item = "sword"
    print(f"Sample lookup - '{item}' in inventory: "
          f"{sample_lookup(inventory, item)}")


def sample_lookup(inventory: dict, item: str) -> bool:
    for key, value in inventory.items():
        for key, value in value.items():
            if key == item:
                return True
    return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        combined = {}
        moderate = {}
        scarce = {}
        for arg in sys.argv[1:]:
            new = arg.split(":")
            try:
                if not new[0].isdigit():
                    new[1] = int(new[1])
                    combined.update({new[0]: new[1]})
                    if new[1] >= 5:
                        moderate.update({new[0]: new[1]})
                    else:
                        scarce.update({new[0]: new[1]})
                else:
                    print(f"\nSkipping {new[0]}: {new[1]}...")
                    print("Please give a non-digit as key.\n")
            except ValueError:
                print(f"\nSkipping {new[0]}: {new[1]}...")
                print("Please give an int as value.\n")

        inventory = {"moderate": moderate, "scarce": scarce}

        print("=== Inventory System Analysis ===")
        print(f"Total items in inventory: {total_items(moderate, scarce)}")
        print(f"Unique item types: {len(moderate) + len(scarce)}")
        sorted_dict(moderate, scarce)
        abundance(moderate, scarce)

        print("\n=== Item Categories ===")
        if len(moderate) > 0:
            print(f"Moderate: {moderate}")
        if len(scarce) > 0:
            print(f"Scarce: {scarce}")
            suggestion(scarce)
        properties(combined)

    else:
        print("No arguments provided. Usage: python3 ft_score_analytics.py "
              "<key1:value1> <key2:value2> ...")
