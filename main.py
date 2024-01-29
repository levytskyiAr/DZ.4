from flask import Flask, render_template, request, url_for
import json
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/message/<username>', methods=['GET', 'POST'])
@app.route('/message/', methods=['GET', 'POST'])
def contact(username = None):
    if request.method == 'POST':
        data_dict = {}

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        data_dict['timestamp'] = timestamp

        username = request.form['username']
        message = request.form['message']

        data_dict['name'] = username
        data_dict['message'] = message

        with open('storage/data.json', 'w') as f:
            json.dump(data_dict, f)
            f.write('\n')
    return render_template('message.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

