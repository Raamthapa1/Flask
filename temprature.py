from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, World! :)</h1>'

@app.route('/greet')
def greet():
    return "Hello"

@app.route('/greet/<name>')
def greet_name(name):
    return f"Hello {name}"

@app.route('/f/<celsius>')
def f(celsius):
    celsius = float(celsius)
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    return f" Input value: {celsius} {chr(176)} C <br/>" \
           f" Converted value: {fahrenheit} {chr(176)} F"
    return str(fahrenheit)

def convert_celsius_to_fahrenheit(celsius):
    """Function to convert celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()