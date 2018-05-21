import csv
from matplotlib import pyplot as plt
from datetime import datetime


def get_highs_lows(filename):
    # Getting the max temperature of the file
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        dates, highs, lows = [], [], []
        for row in reader:
            try:
                date = datetime.strptime(row[0], '%Y-%m-%d')
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print('-----------------------------------------------------------')
                print(date, 'missing data')
                ('-----------------------------------------------------------')
            else:
                dates.append(date)
                highs.append(high)
                lows.append(low)
    return dates, highs, lows


def convert_temperature(filename):
    dates, highs, lows = get_highs_lows(filename)
    # Converting the Fahrenheit degreees into Celsius degrees
    highs_celcius = []
    for high in highs:
        high_celcius = round((high - 32) * (5 / 9), 2)
        highs_celcius.append(high_celcius)
    lows_celcius = []
    for low in lows:
        low_celcius = round((low - 32) * (5 / 9), 2)
        lows_celcius.append(low_celcius)
    return dates, highs_celcius, lows_celcius
