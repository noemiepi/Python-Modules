# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 17:11:39 by npillet         #+#    #+#               #
#  Updated: 2026/03/06 17:56:38 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    print("\nInitiating secure vault access...")
    try:
        with open('classified_data.txt', 'r') as file:
            print("Vault connection established with failsafe protocols")

            print("\nSECURE EXTRACTION:")
            print(file.read())

        with open('security_protocols.txt', 'r') as file:
            print("\nSECURE PRESERVATION:")
            print(file.read())
        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")
    except FileNotFoundError as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    ft_vault_security()
