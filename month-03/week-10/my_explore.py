import geopandas as gpd

path = "data/processed/eastern_cape_renewable_energy.gpkg"

projects = gpd.read_file(path, layer="renewable_projects")

print("Eastern Cape Renewable Energy Dataset")
print("-------------------------------------")
print("Number of projects:", len(projects))
print("CRS:", projects.crs)
print("\nTechnology distribution:")
print(projects["TECHNOLOGY"].value_counts())
print("\nMissing values:")
print(projects.isnull().sum())
print("\nFirst five projects:")
print(projects[["PROJ_TITLE", "TECHNOLOGY", "MEGAWATT"]].head())