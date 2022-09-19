"""Heja Gais"""

# pylint: disable=invalid-name

import emission_data as ed

filename = 'emission_data.csv'

idx_year = {0: 1990, 1: 2005, 2: 2017}

s = '"Country","Area","Year","Population","Emission"\n'
for country, v in ed.country_data.items():
    s1 = f'"{country}",{v["area"]},'
    country_id = v["id"]
    p3 = v["population"]
    for idx in range(3): # Obs! not range(len(p3))
        p_or_NA = p3[idx] if len(p3) > idx else 'NA'  # Was: float('NaN')
        year = idx_year[idx]
        sp = f'{year},{p_or_NA},'

        if year == 1990:
            emission = ed.emission_1990[country_id]
        elif year == 2005:
            emission = ed.emission_2005[country_id]
        elif year == 2017:
            emission = ed.emission_2017[country_id]
        se = str(emission)

        s += s1 + sp + se + '\n'

with open(filename, 'w', encoding='utf-8', newline="\n") as file:
    file.write(s)
# The End
