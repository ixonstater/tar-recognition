from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/deployment.js')
def js_app():
    return render_template('deployment.js')

@app.route('/predict', methods=['POST'])
def predict():
    pass


if __name__ == "__main__":
    port = 8080
    app.run(debug=True, host='0.0.0.0', port=port)