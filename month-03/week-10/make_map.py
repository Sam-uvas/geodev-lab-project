import geopandas as gpd
import matplotlib.pyplot as plt

path = "data/processed/eastern_cape_renewable_energy.gpkg"

projects = gpd.read_file(path, layer="renewable_projects")
municipalities = gpd.read_file(
    path, layer="eastern_cape_municipalities"
)

if municipalities.crs != projects.crs:
    municipalities = municipalities.to_crs(projects.crs)

fig, ax = plt.subplots(figsize=(12, 10))

municipalities.boundary.plot(
    ax=ax,
    color="black",
    linewidth=0.6
)

projects.plot(
    ax=ax,
    column="TECHNOLOGY",
    legend=True,
    markersize=12,
    alpha=0.7
)

ax.set_title(
    "Renewable Energy Projects in the Eastern Cape",
    fontsize=14
)
ax.set_axis_off()

plt.tight_layout()
plt.savefig(
    "month-03/week-10/facilities_map.png",
    dpi=300,
    bbox_inches="tight"
)

print("Map saved: month-03/week-10/facilities_map.png")

plt.show()