from collections.abc import Callable
import random


def mage_counter() -> Callable:
    count = 0

    def counting() -> str:
        nonlocal count
        i = 0
        count += 1
        i += 1
        return f"counter_a call {i}: {count}"

    return counting


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power
    power_list = [10, 20, 30, 40, 50]

    def accumulator() -> str:
        nonlocal power
        added_power = power_list[random.randint(0, len(power_list) - 1)]
        power += added_power
        return f"Base {initial_power}, add {added_power}: {power}"

    return accumulator


def enchantment_factory(enchantement_type: str) -> Callable:
    def enchant(weapon: str) -> None:
        return f"{enchantement_type} {weapon}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: str) -> str:
        memory.update({key: value})
        return f"Store '{key}' = {value}"

    def recall(key: str) -> None:
        for k, v in memory.items():
            if k == key:
                return f"Recall '{key}': {v}"
        return f"Recall '{key}': Memory not found"

    return {"store": store, "recall": recall}


def scope_mysteries() -> None:
    try:
        power = 100
        enchant_type1 = "Flaming"
        enchant_type2 = "Frozen"

        print("Testing mage counter...")
        counter = mage_counter()
        print(counter())
        print(counter())

        print("\nTesting spell accumulator...")
        accumulator = spell_accumulator(power)
        print(accumulator())
        print(accumulator())

        print("\nTesting enchantment factory...")
        enchanting1 = enchantment_factory(enchant_type1)
        print(enchanting1("Sword"))
        enchanting2 = enchantment_factory(enchant_type2)
        print(enchanting2("Shield"))

        print("\nTesting memory vault...")
        closure = memory_vault()
        create = closure["store"]("secret", 42)
        verify = closure["recall"]("secret")
        fail = closure["recall"]("unknown")
        print(create)
        print(verify)
        print(fail)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    scope_mysteries()
