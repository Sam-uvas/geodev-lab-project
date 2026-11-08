import geopandas as gpd

file_path = "data/processed/eastern_cape_renewable_energy.gpkg"

layers = gpd.list_layers(file_path)

print("Available layers:")
print(layers)

gdf = gpd.read_file(file_path, layer=layers.iloc[0]["name"])

print("\nFirst five records:")
print(gdf.head())

print("\nDataset information:")
print(gdf.info())

print("\nCoordinate reference system:")
print(gdf.crs)
