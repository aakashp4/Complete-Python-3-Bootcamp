"""

        14_multiindex_grouping.py

        Here, weekend_temps is a multiindex dataframe.

        In this example we group the cities together and then extract only the
        Canon City data.

                                       High  Low
            Day      City
            Saturday Colorado Springs    78   50
                     Canon City          82   52
                     Pueblo              83   53
            Sunday   Colorado Springs    77   48
                     Canon City          81   49
                     Pueblo              84   50


            Final result:
                                 High  Low
            Day      City
            Saturday Canon City    82   52
            Sunday   Canon City    81   49

"""
import pandas as pd

sat_temps = pd.DataFrame(data=[(78, 50), (82, 52), (83, 53)],
                         index=['Colorado Springs', 'Canon City', 'Pueblo'],
                         columns=['High', 'Low'])

sun_temps = pd.DataFrame(data={'High': (77, 81, 84), 'Low': (48, 49, 50)},
                         index=['Colorado Springs', 'Canon City', 'Pueblo'])

weekend_temps = pd.concat([sat_temps, sun_temps], keys=['Saturday', 'Sunday'])
weekend_temps.index.names = ['Day', 'City']
print('MultiIndex Keys:', weekend_temps, sep='\n')

print(weekend_temps.groupby(level='City').get_group('Canon City'))
