from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    ticker = request.form['ticker']
    data_folder = os.path.join(os.path.dirname(__file__), 'backend/Display')

    if ticker == 'Pepsi':
        filename = 'PEP.txt'
        image_path = 'images/PEP.png'
    elif ticker == 'Coca Cola':
        filename = 'KO.txt'
        image_path = 'images/KO.png'
    elif ticker == 'Nike':
        filename = 'NKE.txt'
        image_path = 'images/NKE.png'
    else:
        return "Ticker not found"

    # Read text data from file
    with open(os.path.join(data_folder, filename), 'r') as file:
        text_data = file.read()

    return render_template('index.html', ticker=ticker, text_data=text_data, image_path=image_path)

@app.route('/images/<path:image_name>')
def serve_image(image_name):
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'static/images'), image_name)

if __name__ == '__main__':
    app.run(debug=True)
