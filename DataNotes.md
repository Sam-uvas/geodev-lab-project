# Week 02 — Data Notes

## Renewable Energy Development in the Eastern Cape

This document records the datasets collected for the Renewable Energy Development in the Eastern Cape project.

The datasets were selected to support the investigation of the spatial distribution of renewable-energy development and its relationship with environmental conditions, terrain and electricity infrastructure.

Environmental raster datasets were processed using Google Earth Engine and exported as GeoTIFF files for inspection and analysis in QGIS.

---

# 1. Renewable Energy EIA Applications

### Dataset

Renewable Energy EIA Applications

### Source

Department of Forestry, Fisheries and the Environment (DFFE)

### Source Link

https://www.dffe.gov.za/egis

### Purpose

This is the main project dataset. It contains renewable-energy project and EIA application information and provides the observed locations of renewable-energy development.

The dataset will be used to investigate:

- Where renewable-energy projects are located
- Which technologies are represented
- How projects are distributed spatially
- How development has changed over time
- How development varies between municipalities

### Geometry Type

Point

### Feature Count

**254 records** were identified within the Eastern Cape during initial exploration.

### Key Attributes

Important attributes include information relating to:

- Technology type
- Project information
- Capacity
- Application date
- Project status
- Municipality
- Location

### Technology Categories Observed

The initial exploration identified:

- Wind
- Solar PV
- Wind & Solar
- Biomass/Biofuels
- Petroleum

### Data Quality Observations

The dataset contains multiple technology categories and project statuses.

Attributes should be checked for missing or inconsistent values before detailed analysis.

Project/application records should also be distinguished from completed or operational facilities where applicable.

---

# 2. Municipal Boundaries

### Dataset

Municipal Boundaries

### Source

Municipal Demarcation Board (MDB)

### Source Link

https://www.demarcation.org.za/

### Purpose

Municipal boundaries provide the administrative framework for the project.

They will be used to:

- Define municipal areas within the Eastern Cape
- Determine which municipalities contain renewable-energy projects
- Compare project distribution between municipalities
- Support municipal-level spatial analysis

### Geometry Type

Polygon

### Feature Count

**To be confirmed from the QGIS layer properties.**

### Key Attributes

Relevant attributes include:

- Municipality name
- Municipality code
- Administrative identifiers

### Data Quality Observations

Municipality names and codes will be checked for missing or inconsistent values.

The boundaries will also be checked to ensure that they correctly represent the Eastern Cape study area.

---

# 3. Solar Radiation

### Dataset

ERA5-Land Daily Aggregated

### Original Source

European Centre for Medium-Range Weather Forecasts (ECMWF)

### Google Earth Engine Collection

`ECMWF/ERA5_LAND/DAILY_AGGR`

### Variable Used

`surface_solar_radiation_downwards_sum`

### Period

2016–2025

### Access and Processing

The ERA5-Land dataset was accessed and processed using Google Earth Engine.

The daily solar-radiation data was averaged over the 2016–2025 period, clipped to the Eastern Cape and converted from J/m²/day to kWh/m²/day.

The resulting raster was exported as a GeoTIFF and opened in QGIS.

### Purpose

The dataset represents the spatial distribution of solar radiation and will be used to investigate the relationship between Solar PV development and solar-resource conditions.

### Geometry Type

Raster

### Raster Bands

1

### Raster Dimensions

75 × 43 pixels

### Data Type

Float64

### Compression

LZW

### Value Range

Approximately 0 to 5.848

### Mean

Approximately 4.871

### Valid Pixels

Approximately 53.98%

### Data Quality Observations

Approximately 46.02% of raster cells were identified as NoData/not valid during the initial inspection.

The NoData areas should be investigated before detailed analysis to determine whether they result from the processing extent, masking or the source dataset.

---

# 4. Wind Speed

### Dataset

ERA5-Land Hourly

### Original Source

European Centre for Medium-Range Weather Forecasts (ECMWF)

### Google Earth Engine Collection

`ECMWF/ERA5_LAND/HOURLY`

### Period

2016–2025

### Variables Used

- `u_component_of_wind_10m`
- `v_component_of_wind_10m`

### Derived Variable

10 m wind speed was calculated from the U and V wind components using:

**Wind speed = √(U² + V²)**

### Access and Processing

The ERA5-Land Hourly dataset was accessed and processed using Google Earth Engine.

Mean 10 m wind speed was calculated for the 2016–2025 period, clipped to the Eastern Cape and exported as a GeoTIFF for use in QGIS.

### Purpose

The dataset represents mean wind-speed conditions across the Eastern Cape.

It will be used to investigate the relationship between wind-energy project locations and wind-resource conditions.

### Geometry Type

Raster

### Raster Bands

1

### Raster Dimensions

75 × 43 pixels

### Pixel Size

Approximately 0.100000457° × 0.100000457°

### Data Type

Float64

### Compression

LZW

### Value Range

Approximately 1.80–5.60 m/s

### Mean

Approximately 2.923 m/s

### Standard Deviation

Approximately 0.684 m/s

### Valid Pixels

Approximately 51.13%

### Data Quality Observations

Approximately 48.87% of raster cells were identified as NoData/not valid during the initial inspection.

These areas should be investigated before detailed spatial analysis.

The relatively coarse spatial resolution should also be considered when comparing the raster with individual renewable-energy project locations.

---

# 5. Elevation

### Dataset

Copernicus DEM GLO-30

### Original Source

Copernicus

### Google Earth Engine Collection

`COPERNICUS/DEM/GLO30`

### Source Link

https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_DEM_GLO30

### Access and Processing

The Copernicus DEM GLO-30 dataset was accessed through Google Earth Engine.

The DEM tiles were mosaicked, clipped to the Eastern Cape and exported as a GeoTIFF at approximately 30 m resolution.

### Purpose

Elevation provides topographic context for investigating whether terrain characteristics are associated with renewable-energy development.

The elevation dataset may also be used to derive additional terrain variables, such as slope, if required during later analysis.

### Geometry Type

Raster

### Resolution

Approximately 30 m

### Data Type

Digital elevation/surface model raster

### Feature Count

Not applicable because this is a raster dataset.

### Key Raster Properties

The final raster dimensions, CRS, elevation range and NoData values will be recorded from the exported layer's QGIS properties.

### Data Quality Observations

The Copernicus DEM GLO-30 product is a Digital Surface Model. Elevation values can therefore represent surface features such as vegetation and buildings in addition to the underlying terrain.

The exported raster should be checked for NoData areas, extent and CRS consistency before analysis.

---

# 6. Electricity Infrastructure

### Dataset

South Africa Electricity Transmission and Distribution Infrastructure

### Source

World Bank / EnergyData.info

### Source Link

https://energydata.info/dataset/south-africa-electricity-transmission-and-distribution-2017

### Reference Period

2017

### Purpose

Electricity infrastructure data provides infrastructure context for the renewable-energy analysis.

The dataset will be used to investigate the spatial relationship between renewable-energy projects and electricity infrastructure, including transmission lines and substations where available.

It may also support proximity or distance analysis.

### Geometry Type

Vector

Depending on the specific infrastructure layer used, the data may contain:

- Lines representing transmission infrastructure
- Points representing infrastructure such as substations

### Feature Count

**To be confirmed from the QGIS layer properties.**

### Key Attributes

Relevant attributes may include:

- Infrastructure type
- Asset name or identifier
- Location
- Other available infrastructure information

### Data Quality Observations

The source dataset has a 2017 reference period.

Infrastructure coverage and missing attributes should be checked in QGIS before proximity analysis.

---

# 7. Eastern Cape Boundary

### Dataset

FAO GAUL 2015 — Level 1 Administrative Boundaries

### Source

Food and Agriculture Organization of the United Nations (FAO)

### Google Earth Engine Collection

`FAO/GAUL/2015/level1`

### Purpose

The boundary dataset was used to identify and define the Eastern Cape study area in Google Earth Engine.

It was also used to clip the environmental raster datasets to the provincial boundary.

### Geometry Type

Polygon

### Key Attributes

The boundary was filtered using:

- `ADM0_NAME` = South Africa
- `ADM1_NAME` = Eastern Cape

### Data Quality Observations

The boundary is being used as the study-area boundary for environmental raster processing.

The final project analysis will use the selected municipal boundary dataset for detailed municipal-level analysis.

---

# 8. Dataset Summary

| Dataset | Original Source | Geometry | Main Use |
|---|---|---|---|
| Renewable Energy EIA Applications | DFFE | Point | Renewable-energy development |
| Municipal Boundaries | MDB | Polygon | Municipal analysis |
| ERA5-Land Daily Aggregated | ECMWF | Raster | Solar radiation |
| ERA5-Land Hourly | ECMWF | Raster | Wind speed |
| Copernicus DEM GLO-30 | Copernicus | Raster | Elevation/terrain |
| Electricity Infrastructure | World Bank / EnergyData.info | Vector | Electricity-grid context |
| FAO GAUL 2015 Level 1 | FAO | Polygon | Eastern Cape study boundary |

---

# 9. Data Processing Workflow

The environmental datasets were processed using Google Earth Engine.

The general workflow was:

**Original dataset**

↓

**Google Earth Engine**

↓

**Filter to 2016–2025 where applicable**

↓

**Calculate/derive required variable**

↓

**Clip to Eastern Cape**

↓

**Export as GeoTIFF**

↓

**Open and inspect in QGIS**

The renewable-energy project data, municipal boundaries and electricity infrastructure are used as vector datasets in QGIS.

---

# 10. Initial Data Quality Assessment

Initial inspection identified several considerations that need to be addressed before detailed analysis.

### Renewable-energy data

The renewable-energy dataset contains multiple technologies and project statuses. Attribute completeness and consistency will need to be checked.

### Solar raster

The initial raster inspection identified NoData areas covering approximately 46.02% of the raster cells.

### Wind raster

The initial raster inspection identified NoData areas covering approximately 48.87% of the raster cells.

### Elevation

The elevation raster requires final inspection of its QGIS layer properties, including its elevation range, CRS and NoData values.

### Electricity infrastructure

The infrastructure dataset has a 2017 reference period, so its temporal difference from more recent renewable-energy development should be considered when interpreting results.

---

# 11. Data Limitations

The datasets have different spatial resolutions, geometry types and reference periods.

The environmental rasters are therefore not directly equivalent to the point-based renewable-energy project data.

The renewable-energy EIA dataset also represents project/application information and should not automatically be interpreted as a complete inventory of operational renewable-energy facilities.

The analysis will account for these differences when comparing datasets.

---

# 12. Week 02 Status

### Completed

- Real renewable-energy project data sourced
- Eastern Cape renewable-energy records identified
- Renewable-energy data inspected in QGIS
- Solar-radiation data processed in Google Earth Engine
- Wind-speed data processed in Google Earth Engine
- Elevation data sourced and processed
- Electricity infrastructure dataset identified
- Municipal boundary data identified
- Environmental raster outputs exported for QGIS
- Initial data-quality observations recorded

### Remaining Checks

- Confirm municipal-boundary feature count
- Confirm electricity-infrastructure feature count
- Record final elevation raster statistics from QGIS
- Inspect missing values in vector datasets
- Investigate NoData areas in environmental rasters
- Ensure all datasets use compatible coordinate reference systems
- Commit the data note and Week 02 data work to GitHub

---

# Week 02 Conclusion

The Week 02 datasets provide the foundation for the next stage of the project.

The data represents three major components:

**1. Existing renewable-energy development**

Renewable-energy EIA project locations and attributes.

**2. Physical/environmental conditions**

Solar radiation, wind speed and elevation.

**3. Infrastructure and administrative context**

Electricity infrastructure and municipal boundaries.

These datasets will be integrated in QGIS during the next stages of the project to investigate the spatial characteristics associated with renewable-energy development in the Eastern Cape.
