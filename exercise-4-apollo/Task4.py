import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import geodatasets
import geopandas as gpd

# Section done by Kateryna

ascend_dict={   # Build dictionary
    'time':[],
    'dist':[],
    'long':[],
    'lat':[],
    'vel_az':[],
    'vel_el':[],
    'ef_vel':[],
    'head':[],
    'flt_path':[],
    'sf_vel':[],
    'range':[],
    'altitude':[]
}
keys=list(ascend_dict.keys())
print(keys)

with open('as-505-ascent-phase-data.txt', mode='r') as file:
# File must be in the same directory as script
    for line in file:
        line_str=line.strip()
        # To skip blank lines, comments, 
        # lines that start with $, and headers
        if(
            not line_str
            or line_str.startswith('$')
            or line_str.startswith('TIME')
            or line_str.startswith('SEC')
        ):
            continue
        # Replace commas with spaces and then skip empty strings
        row=line_str.replace(',' , ' ').split()
        #if len(row)==len(ascend_dict): has extra 0s that mess the plots
        # Can be avoid extra 0s by using 12 columns exactly
        if len(row)==12:
            # Need to convert values to float first, 
            # to avoid the error "ValueError
            int_values=[int(float(val)) for val in row]
            # Assign each value to appropriate key
            for key, val in zip(ascend_dict.keys(), int_values):
                ascend_dict[key].append(val)

# Convert lists to numpy array
for key in ascend_dict:
    ascend_dict[key]=np.array(ascend_dict[key])

print(ascend_dict)

# Dictionary with units for the labels
units={
    'dist':'km',
    'long': 'deg E',
    'lat':'deg N',
    'vel_az':'deg',
    'vel_el': 'deg',
    'ef_vel': 'm/s',
    'head': 'deg',
    'flt_path':'deg',
    'sf_vel':'m/s',
    'range':'m',
    'altitude':'m'
}

# Parameters excluding time
parameter=[key for key in ascend_dict.keys() if key!='time']

fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(12,10))
axes = axes.ravel()

for i, (col, ax) in enumerate(zip(parameter, axes)):
    # To use a unit correscopnding to each parameter
    unit=units.get(col, '')
    ax.plot( ascend_dict['time'], ascend_dict[col], label=f"{i}, {parameter}", color='m')
    ax.set_xlabel('time (s)')
    ax.set_ylabel(f"{col} ({unit})")
    ax.set_title(f"{col} vs time")
# Hide the empty 12th subplot
fig.delaxes(axes[11])

plt.tight_layout()
plt.show()


# Section done by me

# Install geodatasets and geopandas to plot
# the map of the globe if not previously installed
# pip install geodatasets
# pip install geopandas

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import seaborn as sns
import geodatasets
import geopandas as gpd

# Import the data for the globe plot
path = geodatasets.get_path("naturalearth.land")
world = gpd.read_file(path)

# Plot function
fig, ax = plt.subplots(figsize=(12, 6))
world.plot(color="lightgrey", ax=ax)

# Assign coordinates
x = ascend_dict['long']
y = ascend_dict['lat']
z = ascend_dict['altitude']

plt.scatter(x, y, c=z, cmap='plasma')

plt.colorbar(label='Altitude [meter]') # Add colorbar for altitude
plt.title("NASA: Apollo 10 ground control")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()