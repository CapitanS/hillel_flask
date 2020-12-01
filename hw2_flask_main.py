from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Flask!'


@app.route('/requirements/')
def get_requirements() -> str:
    with open('requirements.txt') as r:
        requirements = r.readlines()
        requirements = '; '.join([i.strip() for i in requirements])
    return requirements


if __name__ == '__main__':
    app.run(debug=True)
