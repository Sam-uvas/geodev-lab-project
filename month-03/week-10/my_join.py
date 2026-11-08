import geopandas as gpd

input_file = "month-03/week-10/my_project_points.gpkg"
source_file = "data/processed/eastern_cape_renewable_energy.gpkg"
output_file = "month-03/week-10/my_projects_by_municipality.gpkg"

points = gpd.read_file(
    input_file,
    layer="renewable_project_points"
)

municipalities = gpd.read_file(
    source_file,
    layer="eastern_cape_municipalities"
)

joined = gpd.sjoin(
    points,
    municipalities[["MUNICNAME", "DISTRICT", "geometry"]],
    how="left",
    predicate="within"
)

joined.to_file(
    output_file,
    layer="projects_by_municipality",
    driver="GPKG"
)

print("Spatial join completed.")
print("Total projects:", len(joined))
print("\nProjects by municipality:")
print(joined["MUNICNAME"].value_counts(dropna=False))

print("\nProjects without municipality match:", joined["MUNICNAME"].isna().sum())
print("Saved to:", output_file)