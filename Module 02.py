# %% [markdown]
# ***Module 02: Visualizing Geospatial Data in Python***

# %%
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import leafmap as lm

# %%
# ********** Creating Dictionary Data & Printing ***********
data = {
    "Name": ["Tokyo", "Saitama", "Dhaka", "Sylhet", "New Delhi"],
    "Population": [36000000, 2000000, 25000000, 1000000, 35000000],
    "Latitude": [35.6895, 35.86139, 23.76444, 24.894802, 28.61389],
    "Longitude": [139.69171, 139.64556, 90.38889, 91.869034, 77.20889]
}

cities_df = pd.DataFrame(data)

gdf = gpd.GeoDataFrame(
    cities_df,
    geometry=gpd.points_from_xy(
        cities_df['Longitude'],
        cities_df['Latitude']
    )
)

gdf.set_crs("EPSG:4326", inplace=True)  # coordinate system

# %%
ax = gdf.plot(figsize=(8, 12),
                  marker='^',
                  markersize=20,
                  color='red',
                  edgecolor='black',
                  linewidth=1)

ax.set_xlim([75, 145])
ax.set_ylim([0, 50])
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.grid(True, linestyle='--', alpha=0.7)
ax.margins(0)
dpi = 600

ctx.add_basemap(ax, source=ctx.providers.CartoDB.PositronNoLabels, crs=gdf.crs)

plt.savefig("Map001.png", dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.show()

# %%
m = lm.Map(center=[0,0], zoom=2)

m

# %%
m.add_gdf(gdf, layer_name="Points")
m.add_basemap("Esri.WorldImagery")

m.save("my_interactive_map.html")



# %%
