import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

print(gpd.__version__)

print("Module 01: Geospatial Data in Python")

# ********** Creating Dictionary Data & Printing ***********
data = {
    "Name": ["Tokyo", "Saitama", "Dhaka", "Sylhet", "New Delhi"],
    "Population": [36000000, 2000000, 25000000, 1000000, 35000000],
    "Latitude": [35.6895, 35.86139, 23.76444, 24.894802, 28.61389],
    "Longitude": [139.69171, 139.64556, 90.38889, 91.869034, 77.20889]
}

print(type(data))

print(data["Name"])
print(data["Population"])
print(data["Latitude"])
print(data["Longitude"])

print(type(data["Population"][0]))

print(data["Name"][0])

# ********* Dict > DataFrame & Printing **********
cities_df = pd.DataFrame(data)

print(cities_df)
print(cities_df[['Name', 'Population']])
print(type(cities_df))
print(type(cities_df["Population"]))

# ********** DataFrame > GeoDataFrame & Printing **********
gdf = gpd.GeoDataFrame(
    cities_df,
    geometry=gpd.points_from_xy(
        cities_df['Longitude'],
        cities_df['Latitude']
    )
)

print(gdf)
print(type(gdf))
print(gdf.info())
print(gdf.geometry)

print(type(gdf.geometry))  # A single column of DataFrame is called Series & GeoDataFrame is GeoSeries

print(gdf['geometry'][0])
print(type(gdf['geometry'][0]))

# *********** Creating Polygon & Mapping **************
saitama = ('POLYGON((139.47307 36.17808, 139.5142 36.19283, 139.56309 36.19097, 139.61001 36.17945, 139.67404 '
           '36.15221, 139.679 36.14069, 139.68551 36.1255, 139.71094 36.09829, 139.72401 36.08924, 139.73347 36.0849, '
           '139.75284 36.07956, 139.78592 36.03679, 139.79646 36.01891, 139.83057 35.93791, 139.83863 35.9229, '
           '139.85785 35.90075, 139.86653 35.88882, 139.87186 35.86936, 139.8748 35.85037, 139.86395 35.77813, '
           '139.80452 35.79035, 139.75781 35.79528, 139.74013 35.79141, 139.73068 35.78717, 139.72132 35.77813, '
           '139.71471 35.77642, 139.70613 35.77565, 139.64128 35.77712, 139.62577 35.77301, 139.61508 35.76748, '
           '139.6036 35.75903, 139.5356 35.75156, 139.52878 35.75926, 139.5263 35.76733, 139.52288 35.77479, '
           '139.51668 35.77756, 139.50738 35.77766, 139.49281 35.77384, 139.46718 35.76138, 139.4526 35.75637, '
           '139.43431 35.75224, 139.41147 35.75198, 139.3845 35.75492, 139.28951 35.8021, 139.27153 35.80898, '
           '139.06017 35.85306, 139.0456 35.85882, 139.01361 35.87729, 139.00395 35.87887, 138.99372 35.87654, '
           '138.95289 35.85789, 138.92282 35.83538, 138.86897 35.83776, 138.83063 35.84546, 138.79761 35.856, '
           '138.7157 35.89647, 138.69952 35.94982, 138.70092 35.96954, 138.71642 35.98106, 138.73182 35.99956, '
           '138.73213 36.0007, 138.73229 36.00189, 138.7357 36.01209, 138.74143 36.01987, 138.75074 36.02718, '
           '138.76427 36.03217, 138.78272 36.03517, 138.85827 36.07273, 138.95703 36.11113, 139.01821 36.12891, '
           '139.03377 36.13867, 139.04074 36.14976, 139.04229 36.16441, 139.04229 36.17573, 139.04436 36.18665, '
           '139.04963 36.1965, 139.08963 36.24903, 139.10823 36.26874, 139.11185 36.27086, 139.13805 36.2706, '
           '139.17763 36.25838, 139.19278 36.25761, 139.19872 36.25443, 139.23241 36.24218, 139.30429 36.22823, '
           '139.3786 36.22249, 139.4125 36.21174, 139.44423 36.19632, 139.47307 36.17808))')

Poly_sai = {
    "Name": ["Saitama"],
    "Population": [2000000],
    "geometry": [saitama],
}

gdf_sai = gpd.GeoDataFrame(Poly_sai)

print(gdf_sai.head())

gdf_sai_GeoSeries = gpd.GeoDataFrame(Poly_sai, geometry=gpd.GeoSeries.from_wkt(Poly_sai['geometry']))

ax = gdf_sai_GeoSeries.plot(
    facecolor='none',  # transparent fill
    edgecolor='black',  # boundary line color (change as desired)
    linewidth=1,  # boundary line thickness
    linestyle='solid'  # optional: 'dashed', 'dotted', etc.
)

plt.title("Saitama Prefecture Boundary")
plt.show()
