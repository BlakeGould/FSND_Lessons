#app for P1, L3.9, Exercise 1

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
  app.run()