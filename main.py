from flask import Flask
import os
app = Flask(__name__)
MESSAGE = os.getenv('MESSAGE', 'Couldn\'t load envs')
SOME_API_KEY = os.getenv('SOME_API_KEY', None)

@app.route("/")
def hello():
    return MESSAGE

if __name__ == "__main__":
    app.run(host='0.0.0.0')
