"""

        15_apply.py

        First, 3 separate spreadsheets are read and merged using concat yielding
        the following DataFrame:

                                   High  Humidity   Low
        Saturday Canon City        82.0      18.0  52.0
                 Colorado Springs  78.0      22.0  50.0
                 Denver             NaN      25.0   NaN
                 Pueblo            83.0      19.0  53.0
        Sunday   Colorado Springs  77.0       NaN  48.0
                 Canon City        81.0       NaN  49.0
                 Pueblo            84.0       NaN  50.0


        Then apply() is used to find the temperature deltas (high - low) for
        each city on Sunday.  Results are plotted in a barh graph.

        The last example uses applymap() to find elements that are NaN values and
        replaces them with zero (0).

"""
import matplotlib.pyplot as plt
import pandas as pd

sat_temps = pd.read_excel('temperatures.xlsx', sheetname='Saturday')
sun_temps = pd.read_excel('temperatures.xlsx', sheetname=1)
sat_humidity = pd.read_excel('temperatures.xlsx', sheetname='Humidity')

sat_merged = pd.concat([sat_temps, sat_humidity], axis=1)
merged = pd.concat([sat_merged, sun_temps], keys=['Saturday', 'Sunday'])
print('Multiple Excel Spreadsheets merged:', merged, sep='\n')


# -----------------------------------------------------------------------
# Demonstrating apply(), which (in this case) works on rows due to axis=1
def get_temp_delta(row):
    return row['High'] - row['Low']


temperature_deltas = merged.apply(get_temp_delta, axis=1)

bar_chart = temperature_deltas['Sunday'].plot(kind='barh')
bar_chart.set_xlim(25, 35)
bar_chart.set_yticklabels(['COS', 'CAN', 'PUE'])
plt.show()


# ---------------------------------------------------------------
# Demonstrating applymap() which works element-wise on DataFrames
def remove_nans(elem):
    if pd.isnull(elem):
        elem = 0
    return elem

results = merged.applymap(remove_nans)
print('After applymap(remove_nans):', results, sep='\n')
