# -*- coding: utf-8 -*-
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
# Чтение файла конфигурации
from config import config
# Инициализация Flask приложения
userApp = Flask(__name__)

# TODO: Убрать в случае работы без БД
# Указание конфигурации Flask-SQLAlchemy для работы с БД
userApp.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASE']['URI']
userApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# Создание сессии для БД
db = SQLAlchemy(userApp)
# Инициализация классов БД
from userApp.database import *
# Создание таблиц БД в соответствии с описанными классами
db.create_all()

# Инициализация интерфейсов
from userApp.interfaces import *

# Указание использования препроцессора PUG для HTML файлов
userApp.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
# Импорт функций используемых в PUG файлах
from userApp.helper import jinjaHelper
# Указание конфигурации Flask приложения
userApp.config['SECRET_KEY'] = os.environ.get("SECRET_KEY") or os.urandom(24)

