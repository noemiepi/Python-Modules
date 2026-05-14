from collections.abc import Callable
from typing import Any
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if spells is None or operation is None:
        return 0

    if operation == "add":
        result = functools.reduce(lambda x, y: operator.add(x, y), spells)
        return result
    elif operation == "multiply":
        result = functools.reduce(lambda x, y: operator.mul(x, y), spells)
        return result
    elif operation == "max":
        result = max(spells)
        return result
    elif operation == "min":
        result = min(spells)
        return result

    else:
        return f"Operation '{operation}' is unknown"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {"fire_enchant": functools.partial(base_enchantment, 10, "fire"),
            "ice_enchant": functools.partial(base_enchantment, 10, "ice")}


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def spell(arg: Any) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @spell.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @spell.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return spell

# --------------- #
# Spell functions #
# --------------- #


def enchantement(power: int, element: str, target: str) -> str:
    return f"{target} is enchanted with {element} (power: {power})"


def functools_artifacts() -> None:
    try:
        spell_list = [10, 20, 30, 40]
        spell_tuple = (10, 20, 30, 40)

        print("\nTesting spell reducer...")

        add = spell_reducer(spell_list, "add")
        mul = spell_reducer(spell_list, "multiply")
        best = spell_reducer(spell_list, "max")
        worst = spell_reducer(spell_list, "min")

        print(f"Sum: {add}")
        print(f"Product: {mul}")
        print(f"Max: {best}")
        print(f"Min: {worst}")

        print("\nTesting partial enchanter...")
        enchant = partial_enchanter(enchantement)
        print(enchant["fire_enchant"]("Sword"))
        print(enchant["ice_enchant"]("Staff"))

        print("\nTesting memoized fibonacci...")

        n = 0
        result = memoized_fibonacci(n)
        print(f"Fib({n}): {result}")

        n = 1
        result = memoized_fibonacci(n)
        print(f"Fib({n}): {result}")

        n = 10
        result = memoized_fibonacci(n)
        print(f"Fib({n}): {result}")

        n = 15
        result = memoized_fibonacci(n)
        print(f"Fib({n}): {result}")

        # print(memoized_fibonacci.cache_info())

        print("\nTesting spell dispatcher...")
        dispatch = spell_dispatcher()
        print(dispatch(42))
        print(dispatch("fireball"))
        print(dispatch(spell_list))
        print(dispatch(spell_tuple))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    functools_artifacts()
