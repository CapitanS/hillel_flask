import csv
import requests
from flask import Flask
from faker import Faker
from flask import render_template
from numpy import mean
from database_hw3 import exec_query


app = Flask(__name__)


# Just main page!
@app.route('/')
@app.route('/index.html')
def hello_world() -> str:
    return render_template('entry.html',
                           the_title='Flask welcomes',
                           the_style_url='static/style.css'
                           )


# Homework 2. Flask.
# Task 1. Return information from requirements.txt
@app.route('/requirements/')
def get_requirements() -> str:
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
def generate_users(users_number: int = 100) -> str:
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
def get_mean_height_weight() -> str:
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
def cosmonauts_in_the_space() -> str:
    r = requests.get('http://api.open-notify.org/astros.json')
    number_of_cosmonauts = r.json()['number']
    return render_template('space.html',
                           the_title='Number of cosmonauts in the space at the moment.',
                           number_of_cosmonauts=number_of_cosmonauts,
                           the_style_url='../static/style.css'
                           )


# Homework 3. SQLite.
# Task 1. Display the number unique customers from table 'customers' of db_hw3.sqlite3.
@app.route('/names/')
def get_unigue_names() -> str:
    number_of_unique_customers = exec_query('SELECT COUNT(DISTINCT FirstName) FROM customers')
    return render_template('names.html',
                           the_title='Number of the unique customers',
                           number_of_unique_customers=number_of_unique_customers[0][0],
                           the_style_url='../static/style.css'
                           )


# Task 2. Display the number of compositions from table 'tracks' of db_hw3.sqlite3.
@app.route('/tracks/')
def get_number_of_tracks() -> str:
    number_of_tracks = exec_query('SELECT COUNT(TracksName) FROM tracks')
    return render_template('tracks_number.html',
                           the_title='Number of the compositions',
                           number_of_tracks=number_of_tracks[0][0],
                           the_style_url='../static/style.css'
                           )


# Task 3. Display compositions with specified genre from table 'tracks' of db_hw3.sqlite3.
@app.route('/tracks/<genre>')
def get_genre_tracks(genre) -> str:
    genre_list = ['Disco', 'Club', 'NewRock', 'RnB', 'Bass']
    if genre in genre_list:
        genre_tracks = exec_query(f'SELECT TracksName, genre FROM tracks WHERE genre=(?)', (genre))
    else:
        genre_tracks = [(f'No {genre} tracks.', 'At all!')]
    return render_template('tracks_genre.html',
                           the_title=f'{genre} compositions',
                           genre_tracks=genre_tracks,
                           the_style_url='../static/style.css'
                           )


# Task 4. Display compositions and their length from table 'tracks' of db_hw3.sqlite3.
@app.route('/tracks-sec/')
def get_tracks_and_length() -> str:
    tracks_and_length = exec_query('SELECT TracksName, TrackLength FROM tracks')
    return render_template('tracks_sec.html',
                           the_title='Compositions and their length',
                           tracks_and_length=tracks_and_length,
                           the_style_url='../static/style.css'
                           )


# Task 5. Display average value of length of all compositions and
# overall length of all compositions from table 'tracks' of db_hw3.sqlite3.
@app.route('/tracks-sec/statistics/')
def get_length_statistics() -> str:
    average_length = exec_query('SELECT AVG(TrackLength) FROM tracks')
    overall_length = exec_query('SELECT SUM(TrackLength) FROM tracks')
    return render_template('tracks_stat.html',
                           the_title='A little bit of statistics',
                           average_length='{:.2f}'.format(average_length[0][0]),
                           overall_length=overall_length[0][0],
                           the_style_url='../../static/style.css'
                           )


if __name__ == '__main__':
    app.run()
