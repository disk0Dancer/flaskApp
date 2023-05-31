from flask import send_from_directory
from userApp import userApp
import config
import os

# Интерфейсы загрузки зависимостей из PUG(HTML) файлов, все файлы отправляются с диска из указанной в config.ini директории
@userApp.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory(os.path.join(config.config['TEMPLATES']['template_folder'], 'static/fonts'), path)

@userApp.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(os.path.join(config.config['TEMPLATES']['template_folder'], 'static/css'), path)

@userApp.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(os.path.join(config.config['TEMPLATES']['template_folder'], 'static/js'), path)

@userApp.route('/img/<path:path>')
def send_img(path):
    return send_from_directory(os.path.join(config.config['TEMPLATES']['template_folder'], 'static/imgs'), path)