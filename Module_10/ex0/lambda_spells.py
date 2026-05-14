def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sort_artifacts = list(
                     sorted(artifacts, key=lambda x: x['power'], reverse=True))
    return sort_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    mage_filter = list(filter(lambda x: x['power'] >= min_power, mages))
    return mage_filter


def spell_transformer(spells: list[str]) -> list[str]:
    transform_spell = list(map(lambda x: f'* {x} *', spells))
    return transform_spell


def mage_stats(mages: list[dict]) -> dict:
    best = max(mages, key=lambda x: x['power'])
    worst = min(mages, key=lambda x: x['power'])
    added_power = sum(map(lambda x: int(x['power']), mages))
    avg = added_power / len(mages)
    avg_rounded = round(avg, 2)
    result = {'max_power': best['power'], 'min_power': worst['power'],
              'avg_power': avg_rounded}
    return result


def lambda_spells() -> None:
    try:
        artifact_list = [
            {'name': 'Fire Staff', 'power': 92, 'type': 'fire'},
            {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'}
        ]
        print("\nTesting artifact sorter...")
        sort_art = artifact_sorter(artifact_list)
        print(f"{sort_art[0]['name']} ({sort_art[0]['power']} power) comes "
              f"before {sort_art[1]['name']} ({sort_art[1]['power']} power)")

        spells = [
            "fireball",
            "heal",
            "shield"
        ]
        print("\nTesting spell transformer...")
        transform_spell = spell_transformer(spells)
        for spell in transform_spell:
            print(spell)

        mage_list = [
            {'name': 'Mage Spellicus', 'power': 50, 'element': str},
            {'name': 'Fire Tyrant', 'power': 60, 'element': str}
        ]
        min_power = 55
        print("\nTesting power filter...")
        mage_filter = power_filter(mage_list, min_power)
        print(f"Mage(s) with power above or equal to {min_power}:")
        for mage in mage_filter:
            print(f"- {mage['name']} ({mage['power']} power)")

        print("\nTesting mages stats...")
        print(mage_stats(mage_list))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    lambda_spells()
