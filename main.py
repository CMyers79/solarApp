#

from flask import Flask, render_template, request, flash, redirect, url_for, session
from nrel import get_GHI
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

        if not latitude or not longitude:
            flash('Latitude and Longitude are required')
        elif not startdate or not enddate:
            flash('Start and end dates are required')
        else:

            startdate = [int(numString) for numString in startdate.split("/")]
            enddate = [int(numString) for numString in enddate.split("/")]
            coords = [float(latitude), float(longitude)]
            session['startdate'] = startdate
            session['enddate'] = enddate
            session['coords'] = coords
            return redirect(url_for('result1', startdate=startdate, enddate=enddate, coords=coords))

    return render_template('index.html')

@app.route('/result1', methods=['GET', 'POST'])
def result1():
    startdate = session['startdate']
    enddate = session['enddate']
    coords = session['coords']

    GHI_list = get_GHI(coords, startdate, enddate)
    print(GHI_list)

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