from collections.abc import Callable
from typing import Any
import random


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> str:
        result_spell1 = spell1(*args, **kwargs)
        result_spell2 = spell2(*args, **kwargs)
        return f"{result_spell1}, {result_spell2}"
    return wrapper


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def wrapper(target: str, power: int) -> int:
        amplified_power = power * multiplier
        return base_spell(target, amplified_power)
    return wrapper


def condition(power: int) -> bool:
    if power > 10:
        return True
    else:
        return False


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if condition is True:
            return spell(*args, **kwargs)
        else:
            return "Spell Fizzled"
    return wrapper


def spell_sequence(spells: list[Callable]) -> Callable:
    def wrapper(target: str, power: int) -> str:
        result = ""
        for spell in spells:
            result += f"{spell(target, power)}\n"
        return result
    return wrapper


# --------------- #
# SPELL FUNCTIONS #
# --------------- #

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def main() -> None:
    try:
        power_list = [5, 10, 16, 21]
        target_list = ['Dragon', 'Romain', 'Gerard', 'yourself']
        spell_list = [heal, fireball]

        print("\nTesting spell combiner...")
        combined = spell_combiner(heal, fireball)
        print(combined(
             target_list[random.randint(0, len(target_list) - 1)],
             power_list[random.randint(0, len(power_list) - 1)])
        )

        print("\nTesting power amplifier...")
        mega_fireball = power_amplifier(fireball, 3)
        original = power_list[random.randint(0, len(power_list) - 1)]
        target = target_list[random.randint(0, len(target_list) - 1)]
        print(f"Original: {original}, Amplified: "
              f"{mega_fireball(target, original)}")

        print("\nTesting conditional casting...")
        cond_cast = conditional_caster(condition(original), fireball)
        print(cond_cast(target, original))

        print("\nTesting spell sequence...")
        sequence = spell_sequence(spell_list)
        print(sequence(target, original))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
