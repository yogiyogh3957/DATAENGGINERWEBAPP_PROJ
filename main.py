# import pandas as pd
# import numpy as np
# import psycopg2
# from sqlalchemy import create_engine
# from sqlalchemy.types import String, Integer
#
# engine = create_engine('postgresql+psycopg2://postgres@localhost:5432/fpldb')
#
# df = pd.read_csv('playersfpl.csv')
# df.to_sql('players_table_withcode', engine, if_exists='append', index=False, dtype={"name": String(), "team": String(), "position": String(), "goals_score": Integer(), "goals_conceded": Integer(), "total_points": Integer(), "price": Integer(), "code": String()})


from fplapp import app

if __name__ == '__main__':
    app.run(debug=True)