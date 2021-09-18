#

from flask import Flask, render_template, request, flash, redirect, url_for
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '1ED964D2E87CF13129B56A5F4B86A'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        startdate = request.form['startdate']
        enddate = request.form['enddate']
        coords = [latitude, longitude]
        period = [startdate, enddate]

        if not latitude or not longitude:
            flash('Latitude and Longitude are required')
        elif not startdate or not enddate:
            flash('Start and end dates are required')
        else:

            return redirect(url_for('result1'))
    return render_template('index.html')

@app.route('/result1', methods=['GET', 'POST'])
def result1(coords, period):
    if request.method == 'POST':
        nextpage = request.form['nextpage']
        if nextpage is not None:
            return redirect(url_for('index2'))
        return render_template('result1.html')

@app.route('/result2', methods=['GET', 'POST'])
def result2():
    return render_template('result2.html')

if __name__ == '__main__':
    app.run(debug=True)