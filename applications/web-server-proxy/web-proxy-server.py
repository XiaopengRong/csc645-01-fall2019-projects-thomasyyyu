from flask import Flask, render_template, request, redirect
from client.client import Client
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
    client.response_from_proxy()
    #render_template(response)
    return str(data)


if __name__ == '__main__':
    app.run()
