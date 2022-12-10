import pandas
from flask import flask , redirect , url_for ,render_template , request , flash
import requests
from flask import send_file
app = flask(__name__)


@app.route('/')
def main():
    mypages = [f'https://api.divar.ir/v8/web-search/ardabil/car?has-photo=fals&user_type=peronal&non-negotiable=true&page=1']
    for mp in mypages:
        url = requests.get(mp)
        x = url.json()
    return render_template('index.html' , data = x)


if __name__ == '__main__':
    app.run(debug=True)