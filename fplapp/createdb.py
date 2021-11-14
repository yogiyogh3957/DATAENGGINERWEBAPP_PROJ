import numpy as np
import requests, json
from pprint import pprint
import pandas as pd
pd.set_option('display.max_columns', None)

base_url = 'https://fantasy.premierleague.com/api/'
r = requests.get(base_url+'bootstrap-static/').json()
pprint(r, indent=2, depth=1, compact=True)

df = pd.DataFrame(columns=['id', 'name', 'team', 'position', 'assist', 'chance_created', 'goals_score', 'goals_conceded', 'total_points', 'price', 'code'])
for id in range(len(r['elements'])):
    first_name = r['elements'][id]['first_name']
    second_name = r['elements'][id]['second_name']
    player_code = r['elements'][id]['code']
    team_id = r['elements'][id]['team']
    team = r['teams'][team_id-1]['name']
    goals_conceded = r['elements'][id]['goals_conceded']
    goals_scored = r['elements'][id]['goals_scored']
    creativity = round(float(r['elements'][id]['creativity']))
    assist = r['elements'][id]['assists']
    clean_sheet = r['elements'][id]['clean_sheets']
    price = r['elements'][id]['now_cost']
    total_points = r['elements'][id]['total_points']
    perform = r['elements'][id]['form']
    chance_created = r['elements'][id]['creativity']
    position_id = r['elements'][id]['element_type']
    position = r['element_types'][position_id-1]['plural_name']
    df.loc[id] = [id, first_name+" "+second_name, team, position, assist, creativity, goals_scored, goals_conceded, total_points, price, player_code]

df.to_csv('playersfpl.csv', index=False)