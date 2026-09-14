# Week 02 Data Note

## Renewable Energy Development in the Eastern Cape

This data note documents the datasets collected for the Renewable Energy Development in the Eastern Cape project.

The datasets were selected to investigate the spatial distribution of renewable-energy development and its relationship with renewable resources, terrain and electricity infrastructure.

The data has been sourced from external providers and prepared or inspected in QGIS and Google Earth Engine where applicable.

---

# 1. Renewable Energy EIA Applications

## Dataset

Renewable Energy EIA Applications

## Source

Department of Forestry, Fisheries and the Environment (DFFE)

## Source Link

https://www.dffe.gov.za/egis

## Purpose

This is the core project dataset. It represents renewable-energy-related EIA applications and provides the observed locations and attributes of renewable-energy development.

The dataset will be used to investigate where renewable-energy development has occurred, which technologies are represented, and how development varies spatially and temporally.

## Geometry Type

Point

## Feature Count

254 records were identified within the Eastern Cape during initial data exploration.

## Key Attributes

Important information available in the dataset includes:

- Technology type
- Project information
- Capacity
- Application date
- Project status
- Municipality
- Location information

## Technology Categories Observed

The initial dataset exploration identified the following technology categories:

- Wind
- Solar PV
- Wind & Solar
- Biomass/Biofuels
- Petroleum

Wind and Solar PV account for the majority of the records identified in the Eastern Cape.

## Data Quality Observations

The dataset contains different project types and statuses, so the attributes will need to be checked for missing or inconsistent values before detailed analysis.

Application records also represent project/development information and should not automatically be interpreted as completed operational facilities.

---

# 2. Municipal Boundaries

## Dataset

Eastern Cape Municipal Boundaries

## Source

Municipal Demarcation Board (MDB)

## Source Link

https://www.demarcation.org.za/

## Purpose

Municipal boundaries provide the administrative framework for the project.

They will be used to:

- Define the municipal geography of the Eastern Cape
- Determine which municipalities contain renewable-energy projects
- Compare renewable-energy development between municipalities
- Support spatial aggregation and analysis

## Geometry Type

Polygon

## Feature Count

To be recorded from the final QGIS layer properties.

## Key Attributes

Expected administrative attributes include:

- Municipality name
- Municipality code
- Administrative identifiers

## Data Quality Observations

Municipality names and codes should be checked for missing or inconsistent values before using the boundaries for joins or aggregation.

The boundary dataset will also be checked to ensure that it correctly represents the Eastern Cape study area.

---

# 3. Solar Radiation

## Dataset

Eastern Cape Solar Radiation 2016–2025

## Source

Google Earth Engine processing using the selected solar-resource dataset.

## Source / Dataset Reference

The solar-resource data was processed in Google Earth Engine and exported as a GeoTIFF for use in QGIS.

## Purpose

The solar-radiation raster represents spatial variation in solar-resource intensity across the study area.

It will be used to investigate whether Solar PV development is associated with areas receiving relatively higher solar radiation.

## Geometry Type

Raster

## Raster Bands

1

## Raster Dimensions

75 × 43 pixels

## Data Type

Float64

## Compression

LZW

## Value Range

0 to approximately 5.848

## Mean

Approximately 4.871

## Valid Pixels

Approximately 53.98%

## Data Quality Observations

Approximately 46.02% of the raster cells were identified as NoData/not valid during the initial QGIS inspection.

This will need to be investigated before the raster is used for detailed spatial analysis to determine whether the missing cells result from the processing extent, masking or the source dataset.

## Reference Period

2016–2025

---

# 4. Wind Speed

## Dataset

Eastern Cape Mean Wind Speed 2016–2025

## Source

Google Earth Engine processing using the selected wind-resource dataset.

## Source / Dataset Reference

The wind-resource data was processed in Google Earth Engine and exported as a GeoTIFF for use in QGIS.

## Purpose

The wind-speed raster represents the spatial distribution of mean wind speed across the Eastern Cape.

It will be used to investigate whether existing wind-energy development is associated with areas experiencing stronger wind conditions.

## Geometry Type

Raster

## Raster Bands

1

## Raster Dimensions

75 × 43 pixels

## Pixel Size

Approximately 0.100000457° × 0.100000457°

## Data Type

Float64

## Compression

LZW

## Value Range

Approximately 1.80–5.60 m/s

## Mean

Approximately 2.923 m/s

## Standard Deviation

Approximately 0.684 m/s

## Valid Pixels

Approximately 51.13%

## Data Quality Observations

Approximately 48.87% of the raster cells were identified as NoData/not valid during the initial QGIS inspection.

The missing areas should be investigated before detailed analysis.

## Reference Period

2016–2025

---

# 5. Electricity Infrastructure

## Dataset

South Africa Electricity Transmission and Distribution Infrastructure

## Source

World Bank / EnergyData.info

## Source Link

https://energydata.info/dataset/south-africa-electricity-transmission-and-distribution-2017

## Purpose

Electricity infrastructure provides an important infrastructure context for renewable-energy development.

The dataset will be used to investigate the spatial relationship between renewable-energy projects and electricity infrastructure, including transmission lines and substations where available.

It can later support proximity or distance analysis between renewable-energy projects and the electricity network.

## Geometry Type

Vector

The extracted infrastructure may contain line and/or point features depending on the specific layer used.

## Feature Count

To be recorded from the final QGIS layer properties.

## Key Attributes

Relevant attributes may include:

- Infrastructure type
- Asset name or identifier
- Location
- Other available infrastructure attributes

## Reference Period

2017

## Data Quality Observations

The dataset has a 2017 reference period.

The coverage of transmission lines and substations should be checked in QGIS, together with any missing infrastructure attributes, before performing proximity analysis.

---

# 6. Elevation

## Dataset

Copernicus DEM GLO-30

## Source

Copernicus / Google Earth Engine

## Source Link

https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_DEM_GLO30

## Purpose

Elevation provides topographic context for the renewable-energy analysis.

It will be used to investigate whether elevation varies between areas where renewable-energy projects have developed and other parts of the Eastern Cape.

The elevation raster can also be used later to derive additional terrain information, such as slope.

## Geometry Type

Raster

## Resolution

Approximately 30 m

## Data Type

Digital Elevation Model / Digital Surface Model

## Raster Information

Final raster dimensions, CRS, elevation range and NoData information will be recorded from the QGIS layer properties after the exported GeoTIFF has been inspected.

## Data Quality Observations

The Copernicus DEM is a Digital Surface Model (DSM). Its elevation values represent the surface and may therefore include features such as vegetation and buildings.

The raster should be checked for NoData values, extent and consistency with the Eastern Cape study area before analysis.

---

# 7. Dataset Summary

| Dataset | Source | Geometry | Main Purpose |
|---|---|---|---|
| Renewable Energy EIA Applications | DFFE | Point | Existing renewable-energy development |
| Municipal Boundaries | MDB | Polygon | Administrative analysis |
| Solar Radiation | Google Earth Engine / selected solar dataset | Raster | Solar-resource conditions |
| Wind Speed | Google Earth Engine / selected wind dataset | Raster | Wind-resource conditions |
| Electricity Infrastructure | World Bank / EnergyData.info | Vector | Grid/infrastructure context |
| Elevation | Copernicus / Google Earth Engine | Raster | Terrain/topographic context |

---

# 8. Relationship Between the Datasets

The datasets provide three main categories of information for the project.

### Observed Development

The renewable-energy EIA dataset shows where renewable-energy development has been recorded.

### Environmental and Terrain Conditions

Wind speed, solar radiation and elevation provide information about the environmental and physical characteristics of the study area.

### Infrastructure and Administrative Context

Electricity infrastructure provides information about the relationship between development and the electricity network, while municipal boundaries provide administrative context.

Together, these datasets will allow the project to move from simply showing where renewable-energy projects exist to investigating the spatial conditions associated with their development.

---

# 9. Initial Data Assessment

The initial exploration confirms that the project has access to multiple real geospatial datasets relevant to the research question.

The renewable-energy dataset provides the observed development locations, while the wind, solar and elevation datasets provide environmental and terrain context.

Electricity infrastructure provides an additional infrastructure dimension, and municipal boundaries provide the administrative framework for comparison.

The datasets will be further cleaned, validated and standardised before detailed spatial analysis.

---

# 10. Week 02 Progress

### Completed

- Renewable-energy project data sourced
- Renewable-energy records filtered/examined for the Eastern Cape
- Renewable-energy technology categories identified
- Solar-radiation raster generated/exported
- Wind-speed raster generated/exported
- Elevation dataset selected and prepared
- Datasets loaded or prepared for QGIS inspection
- Initial data-quality observations recorded

### Remaining Checks

- Confirm final feature counts for vector datasets
- Record final QGIS properties for the elevation raster
- Check missing values and NoData areas
- Confirm CRS consistency
- Organise data files in the GitHub repository
- Commit Week 02 work with a clear commit message

---

# Week 02 Status

**Data collection and initial inspection — In progress / completed as datasets are verified.**
