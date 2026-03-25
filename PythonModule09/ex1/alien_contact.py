# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  alien_contact.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 16:50:58 by npillet         #+#    #+#               #
#  Updated: 2026/03/25 09:00:31 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from enum import Enum
from typing import Optional
from datetime import datetime
from typing_extensions import Self
from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: False

    @model_validator(mode='after')
    def check(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")

        if self.contact_type == ContactType.PHYSICAL and self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC and \
           self.witness_count < 3:
            raise ValueError("Telepathic contact has not enough witnesses")

        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signal should include a message")

        return self


def alien_contact() -> None:
    try:
        print("======================================")
        contact = AlienContact(contact_id="AC_2024_001",
                               timestamp=datetime.now(),
                               location="Area 51, Nevada",
                               contact_type=ContactType.RADIO,
                               signal_strength=8.5,
                               duration_minutes=45,
                               witness_count=5,
                               message_received="Greetings from Zeta Reticuli",
                               is_verified=False)
        contact.check()

        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        if contact.message_received:
            print(f"Message: {contact.message_received}")

    except ValidationError as e:
        print("Expected validation error:")
        print(e)

    try:
        print("\n======================================")
        contact = AlienContact(contact_id="AC_2024_001",
                               timestamp=datetime.now(),
                               location="Area 51, Nevada",
                               contact_type=ContactType.TELEPATHIC,
                               signal_strength=8.5,
                               duration_minutes=45,
                               witness_count=2,
                               message_received="Greetings from Zeta Reticuli",
                               is_verified=False)
        contact.check()

    except ValidationError as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    alien_contact()
