from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! you made it, there is need of improvemnt'

if __name__ == '__main__':
    app.run()
