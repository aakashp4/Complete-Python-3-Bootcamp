"""

        11_merging_dataframes.py

        sat_temps and sun_temps are two DataFrames that are combined (different ways) into 'merged'
        using the pd.concat() method.

        At the end, column names are renamed.

        Finally, "inner" joins and join_axes are demonstrated.
"""
import pandas as pd

sat_temps = pd.DataFrame(data=[(78, 50), (82, 52), (83, 53)],
                         index=['Colorado Springs', 'Canon City', 'Pueblo'],
                         columns=['High', 'Low'])
print('Saturday Temperatures:', sat_temps, sep='\n')

sun_temps = pd.DataFrame(data={'High': (77, 81, 84), 'Low': (48, 49, 50)},
                         index=['Colorado Springs', 'Canon City', 'Pueblo'])
print('Sunday Temperatures:', sun_temps, sep='\n')


# -----------------------------------------------------------
# A standard concatenation, no additional args provided
merged = pd.concat([sat_temps, sun_temps])
print('Basic concatenation:', merged, sep='\n')


# ------------------------
# Using hierarchical keys
merged = pd.concat([sat_temps, sun_temps], keys=['Saturday', 'Sunday'])
print('Concatenating specifying keys:', merged, sep='\n')
print('Selecting specific elements: ', merged.ix['Saturday', 'Colorado Springs']['High'])


# --------------------
# Ignoring index
merged = pd.concat([sat_temps, sun_temps], ignore_index=True)
print('Concatenating without an index (ignore_index):', merged, sep='\n')


# --------------------------------
# Concatenating along axis=1
sat_humidity = pd.DataFrame([22, 18, 19, 25],
                            index=['Colorado Springs', 'Canon City', 'Pueblo', 'Denver'],
                            columns=['Humidity'])
print('Merging this humidity DataFrame: ', sat_humidity, sep='\n')

merged = pd.concat([sat_temps, sat_humidity], axis=1)
print('Concatenating along axis=1:', merged, sep='\n')


# -----------------------------
# Changing column names
temps_df = merged
cols = temps_df.columns.values
cols[2] = 'Pct Hum'
temps_df.columns = cols
print('Using df.column.values to change the humidity column name:', temps_df, sep='\n')

# or use rename()...
temps_df.rename(columns={'Pct Hum': '% Hum'}, inplace=True)
print('Using rename():', temps_df, sep='\n')


# ---------------------------------------------------
#  Using 'inner' joins... (default is 'outer' join)
merged = pd.concat([sat_temps, sat_humidity], axis=1, join='inner')
print('Using join="inner":', merged, sep='\n')


# ---------------------------------------------------
#   Using a join_axis argument...
merged = pd.concat([sat_temps, sat_humidity], axis=1, join_axes=[sat_humidity.index[2:]])
print('Using join_axes:', merged, sep='\n')


# ---------------------------------------------------
#   Using merge()
merged = pd.merge(sat_temps, sat_humidity, left_index=True, right_index=True, how='outer')
print('Using merge() left_index & right_index:', merged, sep='\n')



# ------------------------
# Using MultiIndex
merged = pd.concat([sat_temps, sun_temps], keys=['Saturday', 'Sunday'])
print(merged.index)
print(merged.index.levels)

print(merged.iloc[merged.index.get_level_values(1) == 'Colorado Springs'])
