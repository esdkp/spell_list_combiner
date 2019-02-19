from datetime import datetime

from spell_lists import glowing, greater, median, lesser, minor

time_length = len("[Mon Nov 26 19:17:50 2018]")
time_format = '[%a %b %d %H:%M:%S %Y]'


def sort_spells(spells):
    parsed_spells = []
    for spell in spells:
        date = datetime.strptime(spell[:time_length], time_format)
        parsed_spells.append((date, spell))

    return [x[1] for x in sorted(parsed_spells, key=lambda y: y[0])]


def print_spell_tier(tier, spells, wait):
    limit_index = len(spells) - wait

    print(f"{tier}: {len(spells)}")
    for spell in spells[:limit_index]:
        print(spell)

    print(f"----------- Wait List: {wait} -----------")

    for spell in spells[limit_index:]:
        print(spell)


high_tier = sort_spells(glowing + greater)
low_tier = sort_spells(median + lesser + minor)

print_spell_tier('Greater/Glowing', high_tier, 18)
print()
print()
print_spell_tier('Median/Lesser/Minor', low_tier, 24)
