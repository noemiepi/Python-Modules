# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 13:09:34 by npillet         #+#    #+#               #
#  Updated: 2026/03/06 15:41:22 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def list_comprehension(scores: dict, active_players: dict) -> None:
    high_scorers = [name for name, score in scores.items() if score > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores = [score * 2 for score in scores.values()]
    print(f"Scores doubled: {doubled_scores}")

    active = [name for name, score in scores.items() if
              active_players.get(name) is True]
    print(f"Active players: {active}")


def dict_comprehension(scores: dict, active_players: dict,
                       achievements: dict) -> None:
    players_score = {name: score for name, score in scores.items() if
                     active_players.get(name) is True}
    print(f"Players scores: {players_score}")

    score_cat = {
        "high": sum(1 for score in scores.values() if score > 2100),
        "medium": sum(1 for score in scores.values() if score <= 2100 and
                      score > 2000),
        "low": sum(1 for score in scores.values() if score <= 2000)
    }
    print(f"Score categories: {score_cat}")

    nb_achieve = {name: len(ach) for name, ach in achievements.items() if
                  active_players.get(name) is True}
    print(f"Achievement counts: {nb_achieve}")


def set_comprehension(achievements: dict, players_region: dict,
                      active_players: dict) -> None:
    unique_players = {name for name, region in players_region.items()}
    print(f"Unique players: {unique_players}")

    unique_achievements = {x for x in achievements['Bob']}
    print(f"Unique achievements: {unique_achievements}")

    acti_regions = {region for name, region in players_region.items() if
                    active_players.get(name) is True}
    print(f"Active regions: {acti_regions}")


def combined_analysis(scores: dict, achievements: dict) -> None:
    nb_players = len(scores)
    print(f"Total player: {nb_players}")

    total_achievements = [ach for x in achievements.values() for ach in x]
    unique_achievements = {ach for ach in total_achievements}
    print(f"Total unique achievements: {len(unique_achievements)}")

    average = sum(scores.values()) / nb_players
    print(f"Average score: {average:.1f}")

    sorted_players = sorted(scores)
    sorted_scores = sorted(scores.values())
    top_player = min(player for player in sorted_players)
    best_score = max(score for score in sorted_scores)
    nb_achievement = len(achievements[top_player])
    print(f"Top performer: {top_player} ({best_score} points, {nb_achievement}"
          " achievements)")


def ft_analytics_dashboard() -> None:
    scores = {
        "Alice": 2300,
        "Bob": 1800,
        "Charlie": 2150,
        "Diana": 2050
    }

    achievements = {
        "Alice": {"first_kill", "level_10", "collector", "explorer", "slayer"},
        "Bob": {"first_kill", "level_10", "boss_slayer"},
        "Charlie": {"first_kill", "level_10", "master_crafter", "miner",
                    "slayer", "night_owl", "boss_slayer"},
        "Diana": {"flowerist", "builder", "chatter", "level_10"}
    }

    players_region = {
        "Alice": "North",
        "Bob": "East",
        "Charlie": "Central",
        "Diana": "South"
    }

    active_players = {
        "Alice": True,
        "Bob": True,
        "Charlie": True,
        "Diana": False
    }

    print("=== Game Analytics Dashboard ===")
    print("\n=== List Comprehension Examples ===")
    list_comprehension(scores, active_players)
    print("\n=== Dict Comprehension Examples ===")
    dict_comprehension(scores, active_players, achievements)
    print("\n=== Set Comprehension Examples ===")
    set_comprehension(achievements, players_region, active_players)
    print("\n=== Combined Analysis ===")
    combined_analysis(scores, achievements)


if __name__ == "__main__":
    ft_analytics_dashboard()
