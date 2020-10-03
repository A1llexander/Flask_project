# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:36:40 2020

@author: Aleksandr
"""

from flask import Flask, render_template
import itertools
import data as info

app = Flask(__name__)



@app.route('/')
def render_main():
    output = render_template('index.html', tours=dict(itertools.islice(info.tours.items(), 6)))
    return output

@app.route('/departures/<string:departure>/')
def render_departure(departure):
    output = render_template('departure.html', departure=departure, tours=info.tours)
    return output


@app.route('/tours/<int:id>/')
def render_tours(id):
    output = render_template('tour.html', id=id)
    return output

app.run()