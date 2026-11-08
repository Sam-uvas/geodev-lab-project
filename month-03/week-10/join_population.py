import geopandas as gpd

path = "data/processed/eastern_cape_renewable_energy.gpkg"

projects = gpd.read_file(path, layer="renewable_projects")
municipalities = gpd.read_file(
    path, layer="eastern_cape_municipalities"
)

print("Municipality columns:")
print(municipalities.columns.tolist())

print("\nMunicipality records:")
print(len(municipalities))

print("\nProject CRS:", projects.crs)
print("Municipality CRS:", municipalities.crs)

if projects.crs != municipalities.crs:
    municipalities = municipalities.to_crs(projects.crs)

joined = gpd.sjoin(
    projects,
    municipalities,
    how="left",
    predicate="intersects",
    lsuffix="project",
    rsuffix="municipality"
)

print("\nJoined records:", len(joined))
print("\nFirst five joined records:")
print(joined.head())