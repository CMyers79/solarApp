import pylab as plt


def track_battery_changes(charge, load_dict, ghi_list, start_time, panel_size, num_panels):
    """
    Track hourly battery changes

    :param charge: battery starting with full charge
    :param load_dict: dict with hourly power usage
    :param ghi_list: list of hourly ghi
    :param start_time: hour to start tracking changes
    :param panel_size: size of each solar panel in m^2
    :param num_panels: number of solar panels installed
    :return track_charge: list of remaining battery charge each hour
    :return battery_percentage: battery percentage at end time
    """

    # Hours to track from given start time
    num_hours = len(ghi_list)

    max_charge = charge
    hours_tracked = 0
    current_time = start_time
    track_times = [str(current_time) + ":00"]
    track_charge = [charge]
    dark_hours = 0

    while hours_tracked < num_hours:
        # Calculate battery used
        if ghi_list[hours_tracked] != 0:  # daylight
            charge -= load_dict["water"]
            dark_hours = 0

            # Calculate battery replenished
            charge += ghi_list[hours_tracked] * panel_size * num_panels * .2

        else:  # nighttime
            charge -= load_dict["fan"]
            if dark_hours < 2:  # first two dark hours
                charge -= load_dict["lighting"]
                dark_hours += 1

        # Subtracted every hour
        charge -= load_dict["plug load"] / 0.8
        charge -= load_dict["refrigerator"]

        # Maximum/minimum charge
        if charge > max_charge:
            charge = max_charge
        elif charge < 0:
            charge = 0

        # Update variables
        hours_tracked += 1
        current_time += 1

        # Next day
        if current_time == 24:
            current_time = 0

        # Add current battery charge and time to lists for graph
        track_times.append(str(current_time) + ":00")
        track_charge.append(charge)

    generate_graph(track_times, track_charge)

    battery_percentage = str(int(charge / max_charge * 100)) + "%"

    return track_charge, battery_percentage


def generate_graph(times, charge):
    """
    Generate graph of battery usage over time

    :param times: list of all hours tracked
    :param charge: list of battery charge at each hour
    """

    # Filter list to every 4 hours
    if len(times) > 20:
        times = times[::4]
        charge = charge[::4]

    # Generate and display graph
    xs = range(len(times))
    plt.plot(xs, charge)
    plt.xticks(xs, times)
    plt.xlabel("Time")
    plt.ylabel("Battery Charge (Wh)")
    plt.savefig("./static/img/charge_plot.png")

    return
