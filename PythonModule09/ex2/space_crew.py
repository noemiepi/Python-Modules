# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  space_crew.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 17:29:43 by npillet         #+#    #+#               #
#  Updated: 2026/03/25 09:00:52 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from enum import Enum
from datetime import datetime
from typing_extensions import Self
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    lauch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., ge=1, le=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def valid_mission(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if Rank.COMMANDER not in self.crew or Rank.CAPTAIN not in self.crew:
            raise ValueError("Mission crew must have one Commander or Captain")

        if self.duration_days > 365:
            i = 0
            for crew in self.crew:
                if crew.years_experience <= 5:
                    i += 1
            if i > len(self.crew) / 2:
                raise ValueError("Missions of over a year need half of the "
                                 "crew to be experienced (+5 years)")

        for crew in self.crew:
            if crew.is_active is False:
                raise ValueError("All crew members must be active")

        return self


def space_crew() -> None:
    try:
        print("=========================================")
        crew_list = [
            CrewMember(member_id="COMM_001", name="Sarah Connor",
                       rank=Rank.COMMANDER, age=37,
                       specialization="Mission Command", years_experience=19,
                       is_active=True),
            CrewMember(member_id="NAV_001", name="Jonh Smith",
                       rank=Rank.LIEUTENANT, age=45,
                       specialization="Navigation", years_experience=27,
                       is_active=True),
            CrewMember(member_id="ENG_001", name="Alice Johnson",
                       rank=Rank.OFFICER, age=28, specialization="Engineering",
                       years_experience=10, is_active=True)
        ]

        mission = SpaceMission(mission_id="M2024_MARS",
                               mission_name="Mars Colony Establishment",
                               destination="Mars",
                               lauch_date=datetime.now(),
                               duration_days=900,
                               crew=crew_list,
                               mission_status="planned",
                               budget_millions=2500.0)
        mission.valid_mission()

        print("Validation mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(crew_list)}")
        print("Crew members:")
        for crew in crew_list:
            print(f"- {crew.name} ({crew.rank}) - {crew.specialization}")

    except ValidationError as e:
        print("Expected validation error:")
        print(e)

    try:
        print("\n=========================================")
        crew_list = [
            CrewMember(member_id="COMM_001", name="Sarah Connor",
                       rank=Rank.LIEUTENANT, age=37,
                       specialization="Mission Command", years_experience=19,
                       is_active=True),
            CrewMember(member_id="NAV_001", name="Jonh Smith",
                       rank=Rank.LIEUTENANT, age=45,
                       specialization="Navigation", years_experience=27,
                       is_active=True),
            CrewMember(member_id="ENG_001", name="Alice Johnson",
                       rank=Rank.OFFICER, age=28, specialization="Engineering",
                       years_experience=10, is_active=True)
        ]

        mission = SpaceMission(mission_id="M2024_MARS",
                               mission_name="Mars Colony Establishment",
                               destination="Mars",
                               lauch_date=datetime.now(),
                               duration_days=900,
                               crew=crew_list,
                               mission_status="planned",
                               budget_millions=2500.0)
        mission.valid_mission()

    except ValidationError as e:
        print("Expected validation error:")
        print(e)
