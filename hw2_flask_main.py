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
        requirements = '; '.join([i.strip() for i in requirements])
    return render_template('requirements.html',
                           the_title='Requirements',
                           content=requirements,
                           the_style_url='../static/style.css'
                           )


# Task 2. Display generated users and their emails.
@app.route('/genarate-users/<int:users_number>')
def generate_users(users_number):
    pass


if __name__ == '__main__':
    app.run(debug=True)
