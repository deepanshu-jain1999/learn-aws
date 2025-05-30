from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! you made it, on deplyment'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
