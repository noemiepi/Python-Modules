from collections.abc import Callable
from typing import Any
from functools import wraps
import random
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Callable:
        print(f"Casting {func.__name__}...")

        start = time.time()
        time.sleep(0.036)
        spell = func(*args, **kwargs)
        end = time.time()

        print(f"Spell completed in {end - start:.3f} seconds")
        return spell
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Callable:
            power = kwargs.get('power')
            if power is None and len(args) > 2:
                power = args[2]

            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Callable | str:
            i = 1
            while i <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    print(f"Spell failed, retrying... (attempt {i}/"
                          f"{max_attempts})")
                    time.sleep(0.75)
                i += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild():
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
        lenght = len(name)

        if lenght < 3:
            return False

        for letter in name:
            if letter not in alphabet:
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Casting {spell_name} with {power} power"

# --------------- #
# Spell functions #
# --------------- #


@spell_timer
def fireball_spell() -> str:
    # time.sleep(1)
    return "Result: Fireball casted"


@retry_spell(3)
def basic_spell() -> None:
    raise ValueError("Fizzle!")


def decorator_mastery() -> None:
    try:
        mage = MageGuild()
        name_list = ["Spellticus The Great", "23", "slop", "fart_du_69", "Romanus"]
        spell_list = ["Lightning", "Fireball", "Hydrogen Bomb", "Heal"]
        power_list = [5, 9, 10, 15]

        print("\nTesting spell timer...")
        print(fireball_spell())

        print("\nTesting retrying spell...")
        print(basic_spell())

        print("\nTesting MageGuild...")
        name = random.choice(name_list)
        if mage.validate_mage_name(name):
            print(f"{name} is valid!")
        else:
            print(f"{name} is invalid :(")

        spell = random.choice(spell_list)
        power = power_list[random.randint(0, len(power_list) - 1)]
        print(mage.cast_spell(spell, power))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    decorator_mastery()
