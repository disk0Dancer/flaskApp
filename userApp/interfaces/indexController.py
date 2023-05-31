# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request
from userApp import *
from userApp.database import *
import json

# Интерфейс загрузки страницы с статическим контентом
@userApp.route('/')
def index():
    flights = Flights.query.all()
    return render_template('index.pug', flights=flights)

# Интерфейс загрузки страницы с динамическим контентом
@userApp.route('/dynamic')
def dynamic():
    return render_template('dynamic_page.pug')


# Интерфейс поиска на странице с статическим контентом
@userApp.route('/', methods=['POST'])
def index_post():
    source = request.form['source']
    flights = Flights.query.filter_by(source = source).all()
    return render_template('index.pug', flights=flights)


# Интерфейс поиска на странице с динамическим контентом
@userApp.route('/get_flights', methods=['POST'])
def get_flights():
    data = json.loads(request.data)
    source = data['source']
    flights = Flights.query.filter_by(source=source).all()
    result = list()
    for flight in flights:
        result.append(flight.serialize)
    return jsonify(result)