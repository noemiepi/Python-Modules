# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 09:31:56 by npillet         #+#    #+#               #
#  Updated: 2026/03/06 10:45:34 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    nb_arg = len(sys.argv)
    if nb_arg > 1:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {nb_arg - 1}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    else:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {nb_arg}")
