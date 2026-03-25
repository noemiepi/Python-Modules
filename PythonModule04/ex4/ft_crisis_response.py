# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_crisis_response.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 17:21:57 by npillet         #+#    #+#               #
#  Updated: 2026/03/06 17:52:36 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_crisis_response(file_name: str) -> None:

    try:
        with open(file_name, 'r') as file:
            print(f"\nROUTINE ACCESS: Attempting access to '{file_name}'...")
            print(f"SUCCESS: Archive recovered - ''{file.read()}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    ft_crisis_response('lost_archive.txt')

    ft_crisis_response('classified_vault.txt')

    ft_crisis_response('standard_archive.txt')

    print("\nAll crisis scenarios handled successfully. Archives secure.")
