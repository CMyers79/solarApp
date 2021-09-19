#

from flask import Flask, render_template, request, flash, redirect, url_for, session, send_from_directory
from nrel import get_GHI
from calcs import track_battery_changes


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
    start_hour = startdate[2]
    session['start_hour'] = start_hour
    session['GHI_list'] = GHI_list

    if request.method == 'POST':
        if "continue" in request.form:
            return redirect(url_for('index2', start_hour=start_hour, GHI_list=GHI_list))
        return render_template('result1.html', list1=GHI_list)


@app.route('/index2', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        water = request.form.get('water', False)
        fan = request.form.get('fan', False)
        lighting = request.form.get('lighting', False)
        plug_load = request.form.get('plug_load', False)
        refrig = request.form.get('refrig', False)
        batt_type = request.form.get('batt_type', False)
        batt_cap = request.form.get('batt_cap', False)
        panel_size = request.form.get('panel_size', False)
        num_panels = request.form.get('num_panels', False)

        start_hour = session['start_hour']
        GHI_list = session['GHI_list']

        if not water or not fan or not lighting or not plug_load or not refrig or not batt_type or not batt_cap or not panel_size or not num_panels:
            flash('All inputs are required, enter 0 for no consumption')
        else:
            water = int(water) / 2
            fan = int(fan)
            lighting = int(lighting)
            plug_load = int(plug_load)
            batt_cap = int(batt_cap)
            panel_size = int(panel_size)
            num_panels = int(num_panels)

            session['water'] = water
            session['fan'] = fan
            session['lighting'] = lighting
            session['plug_load'] = plug_load
            session['refrig'] = refrig
            session['batt_type'] = batt_type
            session['batt_cap'] = batt_cap
            session['start_hour'] = start_hour
            session['GHI_list'] = GHI_list
            session['panel_size'] = panel_size
            session['num_panels'] = num_panels

            return redirect(url_for('result2', water=water, fan=fan, lighting=lighting, plug_load=plug_load,
                                    refrig=refrig, batt_type=batt_type, batt_cap=batt_cap, start_hour=start_hour,
                                    GHI_list=GHI_list), code=307)

    return render_template('index2.html')


@app.route('/result2', methods=['GET', 'POST'])
def result2():
    water = session['water']
    fan = session['fan']
    lighting=session['lighting']
    plug_load = session['plug_load']
    refrig = session['refrig']
    batt_type = session['batt_type']
    batt_cap = session['batt_cap']
    start_hour = session['start_hour']
    GHI_list = session['GHI_list']
    panel_size = session['panel_size']
    num_panels = session['num_panels']
    GHI_list = [int(numString) for numString in GHI_list]

    if batt_type == "LI":
        batt_charge = batt_cap * 0.8
    elif batt_type == "PB":
        batt_charge = batt_cap * 0.5
    else:
        batt_charge = 0

    if refrig == "LP":
        refrig = 15
    elif refrig == "DC":
        refrig = 220
    elif refrig == "AC":
        refrig = 275
    else:
        refrig = 0

    load_dict = {'water': water, 'fan': fan, 'lighting': lighting, 'plug load': plug_load, 'refrigerator': refrig}

    batt_result = track_battery_changes(batt_charge, load_dict, GHI_list, start_hour, panel_size, num_panels)

    charge_list = batt_result[0]
    percent_remaining = batt_result[1]

    print(charge_list)
    print(percent_remaining)

    if request.method == 'POST':
        if "continue" in request.form:
            return redirect(url_for('/'))

    return render_template('result2.html')


if __name__ == '__main__':
    app.run(debug=True)
