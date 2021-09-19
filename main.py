#

from flask import Flask, render_template, request, flash, redirect, url_for, session
from nrel import get_GHI
from calcs import track_battery_changes, generate_graph
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

            return redirect(url_for('result1', startdate=startdate, enddate=enddate, coords=coords), code=307)

    return render_template('index.html')


@app.route('/result1', methods=['GET', 'POST'])
def result1():
    startdate = session['startdate']
    enddate = session['enddate']
    coords = session['coords']

    GHI_list = get_GHI(coords, startdate, enddate)

    if request.method == 'POST':
        if "continue" in request.form:
            return redirect(url_for('index2'))
        return render_template('result1.html', list1=GHI_list)


@app.route('/index2', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        water = request.form.get('water', False)
        fan = request.form.get('fan', False)
        lighting = request.form.get('lighting', False)
        plug_load = request.form.get('plug_load', False)
        refrig = request.form.get('refrig', False)

        if not water or not fan or not lighting or not plug_load or not refrig:
            flash('All inputs are required, enter 0 for no consumption')
        else:
            water = int(water) / 2
            fan = int(fan)
            lighting = int(lighting)
            plug_load = int(plug_load)
            refrig = int(refrig)
            session['water'] = water
            session['fan'] = fan
            session['lighting'] = lighting
            session['plug_load'] = plug_load
            session['refrig'] = refrig

            return redirect(url_for('result2', water=water, fan=fan, lighting=lighting, plug_load=plug_load, refrig=refrig), code=307)

    return render_template('index2.html')


@app.route('/result2', methods=['GET', 'POST'])
def result2():
    return render_template('result2.html')


if __name__ == '__main__':
    app.run(debug=True)
