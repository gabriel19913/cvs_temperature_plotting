import cvs_temperature
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
