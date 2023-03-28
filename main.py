# Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd

# Reading database using pandas
df = pd.read_csv("Global_Earthquake_Data.csv")
dataset = df.iloc[:, 0:5]
dataset = dataset[(0 <= dataset['mag']) & (dataset['mag'] <= 100)].sort_values(by=['mag'])

# From GeoPandas, world map data
worldmap = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# Creating axes and plotting world map
fig, ax = plt.subplots(figsize=(12, 6))
worldmap.plot(color="grey", ax=ax)

# Plotting earthquake places with color map
x = dataset['longitude']
y = dataset['latitude']
dataset_time = dataset['time']
m = dataset['mag']
m_min = int(dataset['mag'].min())
m_max = int(dataset['mag'].max())+1
plt.scatter(x, y, s=0.1*m, c=m, vmin=m_min, vmax=m_max, cmap="autumn")
plt.colorbar(label="Earthquake Magnitude Scale")

# Creating axis and title
plt.xlim([-180, 180])
plt.ylim([-90, 90])
first_year = dataset_time.min()[0:4]
last_year = dataset_time.max()[0:4]
plt.title(f"Earthquakes Reported by Seismic Sensors\n {first_year} - {last_year}")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()


# # Getting every class count
# cl5 = (dataset['mag'] >= 8).sum()
# cl4 = (dataset['mag'] >= 7).sum()-cl5
# cl3 = (dataset['mag'] >= 6.1).sum()-cl4-cl5
# cl2 = (dataset['mag'] >= 5.5).sum()-cl3-cl4-cl5
# cl1 = (dataset['mag'] >= 2.5).sum()-cl2-cl3-cl4-cl5
# cl0 = (dataset['mag'] <= 2.5).sum()
