# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 10:14:39 by npillet         #+#    #+#               #
#  Updated: 2026/03/09 13:11:06 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) > 1:
        score = []
        for arg in sys.argv[1:]:
            try:
                nb = int(arg)
                score.append(nb)
            except ValueError:
                print(f"Error: {arg} is not a valid score")
        try:
            nb_arg = len(sys.argv)
            print(f"Scores processed: {score}")
            print(f"Total players: {len(score)}")
            print(f"Total score: {sum(score)}")
            print(f"Average score: {sum(score) / len(score)}")
            print(f"High score: {max(score)}")
            print(f"Low score: {min(score)}")
            print(f"Score range: {max(score) - min(score)}")
        except ZeroDivisionError as e:
            print(e)
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
