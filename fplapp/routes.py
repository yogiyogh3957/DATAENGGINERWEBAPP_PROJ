from fplapp import app, db
from flask import render_template, redirect, url_for, flash, request, jsonify, session
from fplapp.models import FPLplayers
from fplapp.forms import QueryForm

import matplotlib.pyplot as plt, mpld3
import numpy as np
import pandas as pd

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/blogpost', methods=['POST', 'GET'])
def blogpost():

    return render_template("blogpost.html")

@app.route('/', methods=['POST', 'GET'])
def home_page():

    # form = QueryForm()
    # all_name = FPLplayers.query.filter_by(team='').all()
    # form.players.choices = [n.name for n in all_name]
    # form.players2.choices = [n2.name for n2 in all_name]
    #
    # if request.method == 'POST':
    #
    #     player1 = FPLplayers.query.filter_by(id=form.players.data).first()
    #     player2 = FPLplayers.query.filter_by(id=form.players2.data).first()
    #
    #     if form.higher.data:
    #         flash("HIGHER IS BETTER !!")
    #         df = pd.read_csv('higher.csv')
    #         p1image = f'https://resources.premierleague.com/premierleague/photos/players/110x140/p{player1.code}.png'
    #         p2image = f'https://resources.premierleague.com/premierleague/photos/players/110x140/p{player2.code}.png'
    #         session['p1'] = p1image
    #         session['p2'] = p2image
    #
    #         categories = df.iloc[334, 1:].index.tolist()
    #
    #         values = df.iloc[int(player1.id), 1:].values.tolist()
    #         values2 = df.iloc[int(player2.id), 1:].values.tolist()
    #         angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
    #         fig = plt.figure(figsize=(6, 6))
    #         ax = fig.add_subplot(polar=True)
    #
    #         # values == mosalah
    #         ax.plot(angles, values, 'o--', color='green', label=player1.name)
    #         ax.fill(angles, values, alpha=0.35, color='green')
    #
    #         # values2 == bruno/pogba/etc
    #         ax.plot(angles, values2, 'o--', color='red', label=player2.name)
    #         ax.fill(angles, values2, alpha=0.35, color='red')
    #
    #         # hidding y label
    #         ax.set_yticklabels([])
    #         ax.set_thetagrids(angles * 180 / np.pi, labels=categories, color='black', fontsize=18, weight='bold')
    #
    #         plt.grid(True)
    #         plt.tight_layout()
    #         plt.legend(bbox_to_anchor=(0.80, 1.05), loc='lower center', borderaxespad=0)
    #         plt.show()
    #         filename = "graph1.png"
    #         fig.savefig(f"fplapp/static/image/{filename}")
    #
    #         return redirect(url_for('show_image', filename=filename))
    #
    #     if form.lower.data:
    #         flash("LOWER IS BETTER !!")
    #         df = pd.read_csv('lower.csv')
    #         p1image = f'https://resources.premierleague.com/premierleague/photos/players/110x140/p{player1.code}.png'
    #         p2image = f'https://resources.premierleague.com/premierleague/photos/players/110x140/p{player2.code}.png'
    #         session['p1'] = p1image
    #         session['p2'] = p2image
    #
    #         categories = df.iloc[334, 1:].index.tolist()
    #
    #         values = df.iloc[int(player1.id), 1:].values.tolist()
    #         values2 = df.iloc[int(player2.id), 1:].values.tolist()
    #         angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
    #         fig = plt.figure(figsize=(7, 7))
    #         ax = fig.add_subplot(polar=True)
    #
    #         # values == mosalah
    #         ax.plot(angles, values, 'o--', color='green', label=player1.name)
    #         ax.fill(angles, values, alpha=0.35, color='green')
    #
    #         # values2 == bruno/pogba/etc
    #         ax.plot(angles, values2, 'o--', color='red', label=player2.name)
    #         ax.fill(angles, values2, alpha=0.35, color='red')
    #
    #         # hidding y label
    #         ax.set_yticklabels([])
    #         ax.set_thetagrids(angles * 180 / np.pi, labels=categories, color='black', fontsize=17, weight='bold')
    #
    #         plt.grid(True)
    #         plt.tight_layout()
    #         plt.legend(bbox_to_anchor=(0.80, 1.05), loc='lower center', borderaxespad=0, fontsize=15)
    #         plt.show()
    #         filename = "graph1.png"
    #         fig.savefig(f"fplapp/static/image/{filename}")
    #
    #         return redirect(url_for('show_image', filename=filename))
    return render_template('home.html')
    # return render_template('home.html', form=form)


@app.route('/show_image/<filename>/', methods=['POST', 'GET'])
def show_image(filename):

    p1img_url = session.get("p1", None)
    p2img_url = session.get("p2", None)

    return render_template('compare_page.html', image=f"image/{filename}", p1img_url=p1img_url, p2img_url=p2img_url)


@app.route('/showteam/<team_name>/<player1_id>/<team2_name>/<player2_id>', methods=['POST', 'GET'])
def show_team(team_name, player1_id, team2_name, player2_id):
    player1 = FPLplayers.query.filter_by(id=player1_id).first()
    player2 = FPLplayers.query.filter_by(id=player2_id).first()

    print(type(player1_id))
    print(type(player2_id))


    team_data = FPLplayers.query.filter_by(team=team_name).all()

    return render_template('show.html', team_data=team_data)

@app.route('/city/<state>')
def city(state):
    cities = FPLplayers.query.filter_by(team=state).all()

    cityArray = [" "]

    for city in cities:
        cityObj = {}
        cityObj['id'] = city.id
        cityObj['name'] = city.name
        cityArray.append(cityObj)
        # print(cityObj)

    return jsonify({'cities' : cityArray})

@app.route('/city2/<state2>')
def city2(state2):
    cities = FPLplayers.query.filter_by(team=state2).all()

    cityArray = [" "]

    for city in cities:
        cityObj = {}
        cityObj['id'] = city.id
        cityObj['name'] = city.name
        cityArray.append(cityObj)
        # print(cityObj)

    return jsonify({'cities' : cityArray})




