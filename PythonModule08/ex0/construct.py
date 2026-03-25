# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  construct.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 15:55:49 by npillet         #+#    #+#               #
#  Updated: 2026/03/24 15:55:52 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import os
import sys
import site


def construct() -> None:
    if sys.prefix != sys.base_prefix:
        print("\nMATRIX STATUS: Welcome to the construct")

        print(f"\nCurrent Python: {sys.executable}")
        print(f"Vitual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system")

        print("\nPackage installation path:")
        print(site.getsitepackages()[0])
    else:
        print("\nMATRIX STATUS: You're still plugged in")

        print(f"\nCurrent Python: {sys.executable}.{sys.version_info.minor}")
        print("Vitual Environment: None Detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate     # On Windows")

        print("Then run this program again.")


if __name__ == "__main__":
    construct()
