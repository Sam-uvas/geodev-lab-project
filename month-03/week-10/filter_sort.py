import geopandas as gpd
import pandas as pd

file_path = "data/processed/eastern_cape_renewable_energy.gpkg"

gdf = gpd.read_file(
    file_path,
    layer="renewable_projects"
)

gdf["MEGAWATT"] = pd.to_numeric(
    gdf["MEGAWATT"],
    errors="coerce"
)

print("Available technologies:")
print(gdf["TECHNOLOGY"].value_counts())

print("\nProjects with capacity above 50 MW:")

filtered = gdf[gdf["MEGAWATT"] > 50]

sorted_data = filtered.sort_values(
    by="MEGAWATT",
    ascending=False
)

print(
    sorted_data[
        ["PROJ_TITLE", "TECHNOLOGY", "MEGAWATT"]
    ].head(10)
)