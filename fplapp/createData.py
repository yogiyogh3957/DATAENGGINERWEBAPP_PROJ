import numpy as np
import requests, json
from pprint import pprint
import pandas as pd
from matplotlib import pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.types import String, Integer
pd.set_option('display.max_columns', None)
base_url = 'https://fantasy.premierleague.com/api/'
r = requests.get(base_url+'bootstrap-static/').json()

class Create :
    def __init__(self):
        self.error = 0

    def dataforDB(self):
        df = pd.DataFrame(
            columns=['id', 'name', 'team', 'position', 'assist', 'chance_created', 'goals_score', 'goals_conceded',
                     'total_points', 'price', 'code'])
        for id in range(len(r['elements'])):
            first_name = r['elements'][id]['first_name']
            second_name = r['elements'][id]['second_name']
            player_code = r['elements'][id]['code']
            team_id = r['elements'][id]['team']
            team = r['teams'][team_id - 1]['name']
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
            position = r['element_types'][position_id - 1]['plural_name']
            df.loc[id] = [id, first_name + " " + second_name, team, position, assist, creativity, goals_scored,
                          goals_conceded, total_points, price, player_code]

        df.to_csv('playersfpl.csv', index=False)

    def higher(self):
        # DATA HIGER IS BETTER
        df = pd.DataFrame(
            columns=['id', 'assist', 'chance_created', 'goals_score', 'total_points', 'saves', 'clean_sheet'])
        for id in range(len(r['elements'])):
            first_name = r['elements'][id]['first_name']
            second_name = r['elements'][id]['second_name']
            player_code = r['elements'][id]['code']
            team_id = r['elements'][id]['team']
            team = r['teams'][team_id - 1]['name']
            goals_conceded = r['elements'][id]['goals_conceded'] * 10
            goals_scored = r['elements'][id]['goals_scored'] * 10
            creativity = round(float(r['elements'][id]['creativity']) / 5)
            assist = r['elements'][id]['assists'] * 10
            clean_sheet = r['elements'][id]['clean_sheets'] * 10
            saves = (r['elements'][id]['saves'] + 1) * 10
            price = r['elements'][id]['now_cost']
            total_points = r['elements'][id]['total_points']
            perform = r['elements'][id]['form']
            chance_created = r['elements'][id]['creativity']
            position_id = r['elements'][id]['element_type']
            position = r['element_types'][position_id - 1]['plural_name']

            df.loc[id] = [id, assist, creativity, goals_scored, total_points, saves, clean_sheet]

        df.to_csv('higher.csv', index=False)

    def lower(self):
        df = pd.DataFrame(
            columns=['id', 'price', 'goals_conceded', 'price_fall', "yellow_card", 'min_per_goal', 'min_per_assist'])
        for id in range(len(r['elements'])):
            first_name = r['elements'][id]['first_name']
            second_name = r['elements'][id]['second_name']
            player_code = r['elements'][id]['code']
            team_id = r['elements'][id]['team']
            team = r['teams'][team_id - 1]['name']
            goals_conceded = r['elements'][id]['goals_conceded'] * 10
            goals_scored = r['elements'][id]['goals_scored'] * 10
            creativity = round(float(r['elements'][id]['creativity']) / 10)
            assist = r['elements'][id]['assists'] * 10
            clean_sheet = r['elements'][id]['clean_sheets']
            saves = r['elements'][id]['saves']
            price = r['elements'][id]['now_cost']
            total_points = r['elements'][id]['total_points']
            perform = r['elements'][id]['form']
            chance_created = r['elements'][id]['creativity']
            price_fall = (r['elements'][id]['cost_change_start_fall'] + 5) * 10
            yellow_card = (r['elements'][id]['yellow_cards'] + 1) * 20
            min_per_goal = r['elements'][id]['minutes'] / (
                        r['elements'][id]['goals_scored'] + 1) / 5  # supaya tidak dibagi nol
            min_per_assist = r['elements'][id]['minutes'] / (r['elements'][id]['assists'] + 1) / 5

            position_id = r['elements'][id]['element_type']
            position = r['element_types'][position_id - 1]['plural_name']

            df.loc[id] = [id, price, goals_conceded, price_fall, yellow_card, min_per_goal, min_per_assist]
        df.to_csv('lower.csv', index=False)

    def createdatabase(self):
        #createengine on lokal
        engine = create_engine('postgresql+psycopg2://postgres@localhost:5432/fpldb')

        df = pd.read_csv('playersfpl.csv')
        df.to_sql('tesfromjupyter', engine, if_exists='append', index=False, dtype={"name": String(), "team": String(), "position": String(), "goals_score": Integer(), "goals_conceded": Integer(), "total_points": Integer(), "price": Integer(), "code": String()})