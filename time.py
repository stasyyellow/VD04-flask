#task1

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h2>Текущая дата и время: {current_time}</h2>"


if __name__ == '__main__':
    app.run()
