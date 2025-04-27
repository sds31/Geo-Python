import osgeo.ogr

osgeo.ogr.UseExceptions()

shapefile = osgeo.ogr.Open("tl_2012_us_state.shp")

numLayers = shapefile.GetLayerCount()
print("Shapefile contains %d layers" % numLayers)

for layerNum in range(numLayers):
    layer = shapefile.GetLayer(layerNum)
    spatialRef = layer.GetSpatialRef().ExportToProj4()
    numFeatures = layer.GetFeatureCount()

    print(f"Layer {layerNum} has")
    print(f"  Spatial Reference (Proj4): {spatialRef}")
    print(f"  Number of Features: {numFeatures}")

for featureNum in range(numFeatures):
    feature = layer.GetFeature(featureNum)
    featureName = feature.GetField("NAME")

    print("Feature %d has name %s" % (featureNum, featureName))

import matplotlib.pyplot as plt
from shapely.wkt import loads

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Reset reading to first feature
layer.ResetReading()

for featureNum in range(numFeatures):
    feature = layer.GetFeature(featureNum)
    geom = feature.GetGeometryRef()

    shapely_geom = loads(geom.ExportToWkt())

    if shapely_geom.geom_type == 'Polygon':
        x, y = shapely_geom.exterior.xy
        ax.plot(x, y, color='blue')
    elif shapely_geom.geom_type == 'MultiPolygon':
        for poly in shapely_geom.geoms:
            x, y = poly.exterior.xy
            ax.plot(x, y, color='blue')

ax.set_title('Map from Shapefile')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
plt.grid(True)
plt.show()
