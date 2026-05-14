# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 16:00:49 by npillet         #+#    #+#               #
#  Updated: 2026/03/06 17:53:33 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    try:
        file = open('ancient_fragment.txt', 'r')
    except FileNotFoundError:
        print("\nERROR: Storage Vault not found.")
        return

    print("\nAccessing Storage Vault: ancient_fragment.txt")
    print("Connection established...")

    print("\nRECOVERED DATA:")
    content = file.read()
    print(content)
    file.close()

    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    ft_ancient_text()
