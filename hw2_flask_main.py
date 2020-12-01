from flask import Flask
from faker import Faker
from flask import render_template

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
def generate_users(users_number=100) -> 'html':
    users_with_emails = {
        'Bob': 'bob@gmail.com',
        'David': 'david@gmail.com'
    }
    return render_template('generate_users.html',
                           the_title=f'Display {users_number} user and their emails',
                           users_dict=users_with_emails,
                           the_style_url='../static/style.css'
                           )


if __name__ == '__main__':
    app.run(debug=True)
