import csv_temperature
import temperature_plot
from matplotlib import pyplot as plt

filename1 = 'sitka_weather_2014.csv'
filename2 = 'death_valley_2014.csv'
print('----------------------------------------------------------------------')
option = input('Do you want to see the chart in Celcius (c) ot Farenheit (f): ')
if option.title() == 'C':
    dates1, highs_temp1, lows_temp1 = csv_temperature.convert_temperature(filename1)
    dates2, highs_temp2, lows_temp2 = csv_temperature.convert_temperature(filename2)
    temperature_plot.subplot_temp(filename1, filename2, option)
if option.title() == 'F':
    dates1, highs_temp1, lows_temp1 = csv_temperature.get_highs_lows(filename1)
    dates2, highs_temp2, lows_temp2 = csv_temperature.get_highs_lows(filename2)
    temperature_plot.subplot_temp(filename1, filename2, option)
else:
    print('Comando inválido o programa será encerrado!')
    print('----------------------------------------------------------------------')
