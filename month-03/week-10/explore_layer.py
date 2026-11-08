import geopandas as gpd

path = "data/processed/eastern_cape_renewable_energy.gpkg"

layers = gpd.list_layers(path)

for _, layer in layers.iterrows():
    print(f"\nLayer: {layer['name']}")
    print(f"Geometry: {layer['geometry_type']}")

    gdf = gpd.read_file(path, layer=layer["name"])

    print("Records:", len(gdf))
    print("Columns:", gdf.columns.tolist())
    print("CRS:", gdf.crs)