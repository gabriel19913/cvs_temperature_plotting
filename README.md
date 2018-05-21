# Plotting temperature from CSV file
This project is based on the content and exercises from chapter 16 of Python Crash Course book. This repository contain 3 important .py files:
1. `__init__.py`: This file ask the user if he/she wants to see the temperature chart in Celcius (°C) ot Farenheit (°F). After that, it calls the functions to plot the temperature of to region (Sitka and Death Valley) together in the same window using the same scale for x and y axes. Obs.: you can plot just one chart using the function `plot_temperature` as will be explained bellow.
2. `csv_temperature.py`: This file contains two functions:
    - `get_highs_lows(filename)`: This function receive as a parameter the name of the CSV file and read it returning the dates, the highs temperatures and the lows temperatures.
    - `convert_temperature(filename)`: This function receive as a parameter the name of the CSV file and return the temperatures converted to Celcius.
3. `temperature_plot.py`: This file contains two functions:
    - `plot_temperature(highs_temp, lows_temp, dates, unit)`: Receiving the highs and lows temperatures, the dates and the unit of temperature, it will plot a chart temperature in a new window using only one file.
    - `subplot_temp(filename1, filename2, unit)`: This function receive two CSV files and the temperature unit, it will plot the data from the files in the same windows in this way is easier to compare them.

> Any doubts or improvement suggestions, you can contact me. 