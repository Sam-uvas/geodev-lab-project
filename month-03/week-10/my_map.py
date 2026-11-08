import geopandas as gpd
import matplotlib.pyplot as plt

source_file = "data/processed/eastern_cape_renewable_energy.gpkg"
points_file = "month-03/week-10/my_projects_by_municipality.gpkg"
output_file = "month-03/week-10/my_map.png"

municipalities = gpd.read_file(
    source_file,
    layer="eastern_cape_municipalities"
)

projects = gpd.read_file(
    points_file,
    layer="projects_by_municipality"
)

fig, ax = plt.subplots(figsize=(12, 10))

municipalities.boundary.plot(
    ax=ax,
    color="grey",
    linewidth=0.7
)

projects.plot(
    ax=ax,
    column="TECHNOLOGY",
    categorical=True,
    legend=True,
    markersize=12,
    alpha=0.8
)

ax.set_title(
    "Eastern Cape Renewable Energy Project Locations",
    fontsize=14,
    pad=20
)

ax.set_axis_off()

plt.tight_layout()
plt.savefig(output_file, dpi=300, bbox_inches="tight")
plt.close()

print("Map saved to:", output_file)