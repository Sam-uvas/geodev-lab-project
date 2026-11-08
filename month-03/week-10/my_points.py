import geopandas as gpd

input_file = "data/processed/eastern_cape_renewable_energy.gpkg"
output_file = "month-03/week-10/my_project_points.gpkg"

projects = gpd.read_file(
    input_file,
    layer="renewable_projects"
)

points = projects.copy()
points["geometry"] = projects.geometry.representative_point()


points.to_file(
    output_file,
    layer="renewable_project_points",
    driver="GPKG"
)

print("Point conversion completed.")
print("Number of points:", len(points))
print("Geometry type:", points.geom_type.unique())
print("Saved to:", output_file)