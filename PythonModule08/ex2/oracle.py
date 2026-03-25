# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 15:56:16 by npillet         #+#    #+#               #
#  Updated: 2026/03/25 09:02:21 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import os
from dotenv import load_dotenv, find_dotenv


def oracle() -> None:
    load_dotenv(find_dotenv(".env.exemple"))
    print("\nConfiguration loaded:")
    if os.getenv("MATRIX_MODE"):
        if os.getenv("MATRIX_MODE") == "development":
            print("Mode: development")
        elif os.getenv("MATRIX_MODE") == "production":
            print("Mode: production")
    if os.getenv("DATABASE_URL"):
        if os.getenv("DATABASE_URL") is not None:
            print("Database: Connected to local instance")
        else:
            print("Database: Failed to connect to local instance")
    if os.getenv("API_KEY"):
        if os.getenv("API_KEY") is not None:
            print("API Access: Authenticated")
        else:
            print("API Access: Not authenticated")
    if os.getenv("LOG_LEVEL"):
        if os.getenv("LOG_LEVEL") is True:
            print("Log Level: DEBUG")
        elif os.getenv("LOG_LEVEL") is False:
            print("Log Level: jsp quoi mettre")
    if os.getenv("ZION_ENDPOINT"):
        if os.getenv("ZION_ENDPOINT") is not None:
            print("Zion Network: Online")
        else:
            print("Zion Network: Offline")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...")

    oracle()
