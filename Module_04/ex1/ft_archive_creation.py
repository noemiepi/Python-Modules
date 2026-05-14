# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 16:29:20 by npillet         #+#    #+#               #
#  Updated: 2026/03/06 17:53:17 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    try:
        print("\nInitializing new storage unit: new_discovery.txt")
        file = open('new_discovery.txt', 'w')
    except FileExistsError as e:
        print(f"ERROR: {e}")
        return
    print("Storage unit created successfully...")

    print("\nInscribing preservation data...")
    file.write("[ENTRY 001] New quantum algorithm discovered\n"
               "[ENTRY 002] Efficiency increased by 347%\n"
               "[ENTRY 003] Archived by Data Archivist trainee")
    file.close()
    file = open('new_discovery.txt', 'r')
    print(file.read())

    print("\nData inscription complete. Storage unit sealed")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    ft_archive_creation()
