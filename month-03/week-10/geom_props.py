import geopandas as gpd

file_path = "data/processed/eastern_cape_renewable_energy.gpkg"

gdf = gpd.read_file(file_path, layer="renewable_projects")

print("Geometry types:")
print(gdf.geom_type.value_counts())

print("\nGeometry validity:")
print(gdf.geometry.is_valid.value_counts())

print("\nTotal features:")
print(len(gdf))

print("\nTotal bounds:")
print(gdf.total_bounds)