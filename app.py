from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/example')
def example():
    return "Another endpoint available!"

@app.route('/example-3')
def example():
    return "Third endpoint available!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
