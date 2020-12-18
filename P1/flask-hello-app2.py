#app for P1, L3.9, Exercise 1

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

# run the app from command line with python3 flask-hello-app2.py
if __name__ == '__main__':
  app.run()