from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
import csv
import datetime

userApp = Flask(__name__)

userApp.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASE']['URI']
userApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(userApp)
from userApp.database import *
db.create_all()

# Читаем CSV
with open('Pobeda.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # Пропуск заголовка
    next(reader)
    for row in reader:
        # Создаем объъект класса БД
        flight = Flights(flight = row[0],
                         source = row[1],
                         dest = row[2],
                         start_date = datetime.datetime.strptime(row[3], '%d.%m.%Y').date(),
                         days = row[4],depart = datetime.datetime.strptime(row[5], '%H:%M').time(),
                         arrival = datetime.datetime.strptime(row[6], '%H:%M').time())
        # Добавляем объект к сессии
        db.session.add(flight)
        # Записываем изменения в БД
        db.session.commit()
