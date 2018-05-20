import cvs_temperature
import temperature_plot

filename = 'sitka_weather_2014.csv'
print('----------------------------------------------------------------------')
option = input('Do you want to see the chart in Celcius (c) ot Farenheit (f): ')
if option.title() == 'C':
    dates, highs_temp, lows_temp = cvs_temperature.convert_temperature(filename)
    temperature_plot.plot_temperature(highs_temp, lows_temp, dates, option)
if option.title() == 'F':
    dates, highs_temp, lows_temp = cvs_temperature.get_highs_lows(filename)
    temperature_plot.plot_temperature(highs_temp, lows_temp, dates, option)
