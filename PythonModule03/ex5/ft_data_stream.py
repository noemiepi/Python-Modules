# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/26 13:13:18 by npillet         #+#    #+#               #
#  Updated: 2026/03/09 09:05:32 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Generator
from time import time


def event_gen(count: int) -> Generator[tuple[int, str, int, str], None, None]:
    event_type = [
        "killed a monster!",
        "found a treasure!",
        "leveled up!"
    ]

    players_list = {
        "Alice": 4,
        "Bob": 12,
        "Charlie": 8
    }

    for id_event in range(1, count+1):
        if id_event % 3 == 1:
            player = "Alice"
        elif id_event % 2 == 1:
            player = "Bob"
        else:
            player = "Charlie"

        level = players_list[player]

        event = event_type[((id_event * 4) % 23 + 1) % 3]

        if event == "leveled up!":
            level += 1

        yield (id_event, player, level, event)


def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    if n < 0:
        return f"{n} is not a valid input."
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_numbers(n: int) -> Generator[int, None, None]:
    a = 2
    if n < 0:
        return f"{n} is not a valid input."
    while n > 0:
        is_prime = True
        for i in range(2, a):
            if a % i == 0:
                is_prime = False
                break
        if is_prime is True:
            yield a
            n -= 1
        a += 1


def gen_demo() -> None:
    nb_fib = 10
    fib_list = []

    for i in fibonacci(nb_fib):
        fib_list.append(str(i))

    fib_seq = ", ".join(fib_list)
    print(f"Fibonacci sequence (first {nb_fib}): {fib_seq}")

    nb_prime = 5
    prime_list = []

    for i in prime_numbers(nb_prime):
        prime_list.append(str(i))

    prime_seq = ", ".join(prime_list)
    print(f"Prime numbers (first {nb_prime}): {prime_seq}")


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    nb_events = 1500
    if nb_events <= 0:
        print(f"{nb_events} is too low")
    print(f"\nProcessing {nb_events} game events...\n")
    generator = event_gen(nb_events)
    treasure_event = 0
    level_event = 0
    high_player = 0

    start_time = time()
    for id_event, player, level, event in generator:
        if id_event <= 3:
            print(f"Event {id_event}, Player {player} (level {level}), "
                  f"{event}")
            if id_event == 3 and nb_events > 3:
                print("...")
        if event == "found a treasure!":
            treasure_event += 1
        if event == "leveled up!":
            level_event += 1
        if level >= 10:
            high_player += 1
    end_time = time()

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {nb_events}")
    print(f"High-level players (+10): {high_player}")
    print(f"Treasure events: {treasure_event}")
    print(f"Level-up events: {level_event}")

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.4f} seconds")

    print("\n=== Generator Demonstration ===")
    gen_demo()


if __name__ == "__main__":
    ft_data_stream()
