import csv_temperature
from matplotlib import pyplot as plt


def plot_temperature(highs_temp, lows_temp, dates, unit):
    # Plotting the data
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs_temp, c='red', alpha=0.5)
    plt.plot(dates, lows_temp, c='blue', alpha=0.5)
    plt.fill_between(dates, highs_temp, lows_temp, facecolor='green', alpha=0.1)
    # Formatating the chart
    plt.title('Daily high and low temperatures', fontsize=16)
    plt.xlabel('', fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (°{})'.format(unit.title()), fontsize=12)
    plt.tick_params(axis='both', labelsize=10)
    plt.xlim(dates[0], dates[-1])
    plt.grid()
    plt.show()


def subplot_temp(filename1, filename2, unit):
    if unit.title() == 'C':
        dates1, highs1, lows1 = csv_temperature.convert_temperature(filename1)
        dates2, highs2, lows2 = csv_temperature.convert_temperature(filename2)
        limy = (-13, 50)
    if unit.title() == 'F':
        dates1, highs1, lows1 = csv_temperature.get_highs_lows(filename1)
        dates2, highs2, lows2 = csv_temperature.get_highs_lows(filename2)
        limy = (10, 120)
    fig = plt.figure(dpi=128, figsize=(10, 6))

    ax1 = plt.subplot(211)
    plt.plot(dates1, highs1, c='red', alpha=0.5)
    plt.plot(dates1, lows1, c='blue', alpha=0.5)
    plt.fill_between(dates1, highs1, lows1, facecolor='green', alpha=0.1)
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.title('Daily high and low temperatures Sitka - 2014', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (°{})'.format(unit.title()), fontsize=12)
    plt.tick_params(axis='both', labelsize=10)
    plt.xlim(dates1[0], dates1[-1])
    plt.ylim(limy)
    plt.grid()

    ax2 = plt.subplot(212, sharex=ax1)
    plt.plot(dates2, highs2, c='red', alpha=0.5)
    plt.plot(dates2, lows2, c='blue', alpha=0.5)
    plt.fill_between(dates2, highs2, lows2, facecolor='green', alpha=0.1)
    plt.setp(ax1.get_xticklabels(), fontsize=14)
    plt.title('Daily high and low temperatures Death Valley - 2014', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (°{})'.format(unit.title()), fontsize=12)
    plt.tick_params(axis='both', labelsize=10)
    plt.xlim(dates2[0], dates2[-1])
    plt.ylim(limy)
    plt.grid()

    plt.show()
