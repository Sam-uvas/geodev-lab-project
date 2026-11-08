import geopandas as gpd
import pandas as pd

input_file = "data/processed/eastern_cape_renewable_energy.gpkg"
output_folder = "month-03/week-10"

projects = gpd.read_file(input_file, layer="renewable_projects")
municipalities = gpd.read_file(input_file, layer="eastern_cape_municipalities")

# Save a CSV summary of projects by technology
projects["MEGAWATT"] = pd.to_numeric(projects["MEGAWATT"], errors="coerce")

summary = (
    projects.groupby("TECHNOLOGY", dropna=False)
    .agg(
        project_count=("DEA_REF", "count"),
        total_capacity_mw=("MEGAWATT", "sum")
    )
    .reset_index()
)

summary.to_csv(f"{output_folder}/wards_table.csv", index=False)

print("Saved wards_table.csv")
print(summary)