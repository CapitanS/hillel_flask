import csv
import requests
from flask import Flask
from faker import Faker
from flask import render_template
from numpy import mean


app = Flask(__name__)


# Just main page!
@app.route('/')
@app.route('/index.html')
def hello_world() -> 'html':
    return render_template('entry.html',
                           the_title='Flask welcomes',
                           the_style_url='static/style.css'
                           )


# Task 1. Return information from requirements.txt
@app.route('/requirements/')
def get_requirements() -> 'html':
    with open('requirements.txt') as r:
        requirements = r.readlines()
    return render_template('requirements.html',
                           the_title='Requirements for this project',
                           content=requirements,
                           the_style_url='../static/style.css'
                           )


# Task 2. Display generated users and their emails.
@app.route('/generate-users/')
@app.route('/generate-users/<int:users_number>')
def generate_users(users_number: int = 100) -> 'html':
    users_with_emails = {}
    fake = Faker(['en_US'])
    for _ in range(users_number):
        user = fake.name()
        email = user.lower().replace(' ', '') + '@gmail.com'
        users_with_emails[user] = email
    return render_template('generate_users.html',
                           the_title=f'{users_number} users and their emails',
                           users_dict=users_with_emails,
                           the_style_url='../static/style.css'
                           )


# Task 3. Return mean height and weight from hw.csv.
@app.route('/mean/')
def get_mean_height_weight() -> 'html':
    with open('files/hw.csv', newline='') as hw_csvfile:
        hw_reader = csv.DictReader(hw_csvfile)
        height_str = []
        weight_str = []
        index_col, height_col, weight_col = hw_reader.fieldnames
        for i in hw_reader:
            height_str.append(float(i[height_col]))
            weight_str.append(float(i[weight_col]))
        mean_height_m = '{:.2f}'.format(mean(height_str) * 0.0254)
        mean_weight_kg = '{:.2f}'.format(mean(weight_str) * 0.453592)
    return render_template('mean.html',
                           the_title='Mean height and weight from hw.csv.',
                           mean_height=mean_height_m,
                           mean_weight=mean_weight_kg,
                           the_style_url='../static/style.css'
                           )


# Task 4. Display number of cosmonauts in the space at the moment.
@app.route('/space/')
def cosmonauts_in_the_space() -> 'html':
    r = requests.get('http://api.open-notify.org/astros.json')
    number_of_cosmonauts = r.json()['number']
    return render_template('space.html',
                           the_title='Number of cosmonauts in the space at the moment.',
                           number_of_cosmonauts=number_of_cosmonauts,
                           the_style_url='../static/style.css'
                           )


if __name__ == '__main__':
    app.run()
