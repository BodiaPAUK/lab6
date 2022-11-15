from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '7777')
    app.run(debug=True, port=server_port, host='0.0.0.0')