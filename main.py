# Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd

# Reading database using pandas
df = pd.read_csv("Global_Earthquake_Data.csv")

# From GeoPandas, world map data
worldmap = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# Creating axes and plotting world map
fig, ax = plt.subplots(figsize=(12, 6))
worldmap.plot(color="green", ax=ax)

# Plotting earthquake data with color map
# pass

# Creating axis and title
plt.xlim([-180, 180])
plt.ylim([-90, 90])

plt.title("Earthquakes")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()