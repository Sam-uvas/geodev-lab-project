# Data Notes

## Renewable Energy Development in the Eastern Cape

This document records the datasets used for the project, their sources, structure, purpose, and initial data-quality observations.

---

## 1. Renewable Energy EIA Applications

**Source:** Department of Forestry, Fisheries and the Environment (DFFE)  
**Link:** https://www.dffe.gov.za/egis

| Property | Description |
|---|---|
| Feature count | 254 records within the Eastern Cape |
| Geometry | Polygon |
| Key fields | `TECHNOLOGY`, `MEGAWATT`, `PROJ_STATUS`, application/date fields, project information and municipal information |
| Purpose | Core dataset representing renewable-energy development in the Eastern Cape |
| Data quality | Some attribute fields contain missing values. Capacity, status and date fields require checking before analysis |

---

## 2. Municipal Boundaries

**Source:** Municipal Demarcation Board (MDB)  
**Link:** https://www.demarcation.org.za/

| Property | Description |
|---|---|
| Feature count | 52 records |
| Geometry | Polygon |
| Key fields | Municipality name, municipality code and administrative identifiers |
| Purpose | Used to examine the distribution of renewable-energy development across municipalities |
| Data quality | No obvious data-quality issues identified during initial inspection |

---

## 3. Solar Resource

**Dataset:** ERA5-Land Daily Aggregated  
**Original source:** ECMWF / Copernicus  
**Access and processing:** Google Earth Engine  
**Link:** https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_DAILY_AGGR

| Property | Description |
|---|---|
| Period | 2016–2025 |
| Variable | `surface_solar_radiation_downwards_sum` |
| Geometry | Raster |
| Resolution | Approximately 11.1 km |
| Dimensions | 75 × 43 cells |
| Output | GeoTIFF |
| Unit | kWh/m²/day |
| Feature count | Not applicable — raster dataset |
| Data quality | Approximately 53.98% of cells contain valid data in the exported raster |
| Purpose | Used to examine solar-resource conditions in relation to Solar PV development |

---

## 4. Wind Resource

**Dataset:** ERA5-Land Hourly  
**Original source:** ECMWF / Copernicus  
**Access and processing:** Google Earth Engine  
**Link:** https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_HOURLY

| Property | Description |
|---|---|
| Period | 2016–2025 |
| Variables | `u_component_of_wind_10m`, `v_component_of_wind_10m` |
| Derived variable | `wind_speed_10m` |
| Geometry | Raster |
| Resolution | Approximately 11.1 km |
| Dimensions | 75 × 43 cells |
| Output | GeoTIFF |
| Unit | m/s |
| Feature count | Not applicable — raster dataset |
| Data quality | Approximately 48.87% of cells were NoData/not valid in the exported raster |
| Purpose | Used to examine wind-resource conditions in relation to wind-energy development |

Wind speed was calculated from the 10 m U and V wind components.

---

## 5. Elevation

**Dataset:** Copernicus DEM GLO-30  
**Original source:** Copernicus  
**Access and processing:** Google Earth Engine  
**Link:** https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_DEM_GLO30_2024_1

| Property | Description |
|---|---|
| Resolution | 30 m |
| Dimensions | 27,679 × 15,624 cells |
| Geometry | Raster |
| Data type | Float32 |
| Band | `DEM` |
| Minimum elevation | -15.84 m |
| Maximum elevation | 1,975.42 m |
| Mean elevation | 973.60 m |
| Output | GeoTIFF |
| Feature count | Not applicable — raster dataset |
| Data quality | Approximately 50.9% of cells contain valid data |
| Purpose | Used to examine terrain and elevation as physical factors associated with renewable-energy development |

---

## 6. Electricity Infrastructure

**Source:** World Bank / EnergyData.info  
**Underlying data:** OpenStreetMap  
**Reference period:** 2017  
**Link:** https://energydata.info/dataset/south-africa-electricity-transmission-and-distribution-2017

| Property | Description |
|---|---|
| Feature count | 153 records |
| Geometry | Line |
| Key fields | Infrastructure type, voltage, status and other available infrastructure attributes |
| Purpose | Used to examine the spatial relationship between renewable-energy projects and electricity infrastructure |
| Data quality | No obvious data-quality issues identified during initial inspection |

---

## 7. Study Area Boundary

**Dataset:** FAO GAUL 2015 Level 1  
**Source:** Food and Agriculture Organization of the United Nations (FAO)  
**Access:** Google Earth Engine  
**Link:** https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level1

| Property | Description |
|---|---|
| Feature count | 1 Eastern Cape feature |
| Geometry | Polygon |
| Key fields | `ADM0_NAME`, `ADM1_NAME` |
| Purpose | Defines the Eastern Cape study area and was used to clip the environmental raster datasets |
| Data quality | No obvious issue identified with the selected Eastern Cape feature |

---

## Dataset Overview

| Dataset | Geometry | Main purpose |
|---|---|---|
| Renewable Energy EIA Applications | Polygon | Renewable-energy development |
| Municipal Boundaries | Polygon | Municipal distribution |
| Solar Resource | Raster | Solar-resource conditions |
| Wind Resource | Raster | Wind-resource conditions |
| Elevation | Raster | Terrain and physical conditions |
| Electricity Infrastructure | Line | Grid/infrastructure context |
| Eastern Cape Boundary | Polygon | Study-area definition |

