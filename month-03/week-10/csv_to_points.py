import geopandas as gpd

gdf = gpd.read_file(
    "data/processed/eastern_cape_renewable_energy.gpkg",
    layer="renewable_projects"
)

points = gdf.copy()
points["geometry"] = points.geometry.centroid

points = points.set_geometry("geometry")

print("First five point coordinates:")
print(points[["PROJ_TITLE", "geometry"]].head())

print("\nTotal points:")
print(len(points))