import datetime
import random
from webbrowser import open_new_tab

from flask import Flask, render_template, request, redirect
from client.client import Client
import pymysql
import requests


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/proxy-settings')
def proxy_settings():
    return render_template('proxy-settings.html')


@app.route('/home.html', methods=['POST'])
def get_user_input():
    url = request.form.get('url')
    is_private_mode = 0
    if request.form.get('private'):
        is_private_mode = 1
    if "proxy-settings" in url:
        return proxy_settings()
    data = {'url': url, 'is_private_mode': is_private_mode}
    client = Client()
    client.run(data)
    response = client.response_from_proxy()
    body = response[0]
    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
    # name_of_file = random.randint(1000, 10000)
    filename = '/Users/thomasyyu/Documents/GitHub/CSC645/csc645-01-fall2019-projects-thomasyyyu/applications/web-server-proxy/templates/'
    filename = filename + 'index' + '.html'
    f = open(filename, 'w')
    wrapper = """<!DOCTYPE html>
        <html>
            <head>
                <title>%s output - %s</title>
            </head>
            <body>
                <form>
                    <input type="button" value="Go back!" onclick="history.back()">
                </form>
                <p>URL: <a href=\"%s\">%s</a></p><p>%s</p></body>
        </html>"""
    whole = wrapper % (url, now, url, url, body)
    f.write(whole)
    f.close()
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
