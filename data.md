# Data Notes

## Renewable Energy Development in the Eastern Cape

This document describes the datasets collected for the project, their sources, structure, and initial data-quality observations. The datasets were obtained from external data providers and processed or inspected using QGIS and Google Earth Engine where applicable.

---

## 1. Renewable Energy EIA Applications

**Source:** Department of Forestry, Fisheries and the Environment (DFFE)  
**Source:** https://www.dffe.gov.za/egis

| Property | Description |
|---|---|
| Feature count | 254 records within the Eastern Cape |
| Geometry | Polygon |
| Key fields | `TECHNOLOGY`, `MEGAWATT`, `PROJ_STATUS`, application/date fields, project and municipal information |
| Purpose | Main dataset used to represent renewable-energy development in the province |
| Data quality | Some attributes contain missing values and require checking, particularly capacity, project status and date fields |

The dataset contains several technology categories, including **Solar PV, Wind, Wind & Solar, Biomass/Biofuels and Petroleum**.

---

## 2. Municipal Boundaries

**Source:** Municipal Demarcation Board (MDB)  
**Source:** https://www.demarcation.org.za/

| Property | Description |
|---|---|
| Feature count | To be confirmed from the final QGIS layer |
| Geometry | Polygon |
| Key fields | Municipality name, municipality code and administrative identifiers |
| Purpose | Used to analyse how renewable-energy development is distributed between municipalities |
| Data quality | No issue identified|

---

## 3. Solar Resource

**Dataset:** ERA5-Land Daily Aggregated  
**Original source:** ECMWF / Copernicus  
**Access and processing:** Google Earth Engine  
**Source:** https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_DAILY_AGGR

| Property | Description |
|---|---|
| Period | 2016–2025 |
| Variable | `surface_solar_radiation_downwards_sum` |
| Geometry | Raster |
| Resolution | Approximately 11.1 km |
| Output | GeoTIFF |
| Unit | kWh/m²/day |
| Feature count | Not applicable — raster dataset |
| Data quality | Initial QGIS inspection identified approximately 53.98% valid pixels |

The daily solar-radiation data was averaged over 2016–2025, clipped to the Eastern Cape and converted to kWh/m²/day before being exported from Google Earth Engine for use in QGIS.

---

## 4. Wind Resource

**Dataset:** ERA5-Land Hourly  
**Original source:** ECMWF / Copernicus  
**Access and processing:** Google Earth Engine  
**Source:** https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_HOURLY

| Property | Description |
|---|---|
| Period | 2016–2025 |
| Variables | `u_component_of_wind_10m`, `v_component_of_wind_10m` |
| Derived variable | 10 m wind speed |
| Geometry | Raster |
| Resolution | Approximately 11.1 km |
| Output | GeoTIFF |
| Feature count | Not applicable — raster dataset |
| Data quality | Initial QGIS inspection identified approximately 48.87% NoData/not-valid cells |

Wind speed was calculated from the U and V wind components and then averaged over 2016–2025. The resulting raster was clipped to the Eastern Cape and exported as a GeoTIFF.

---

## 5. Elevation

**Dataset:** Copernicus DEM GLO-30  
**Original source:** Copernicus  
**Access and processing:** Google Earth Engine  
**Source:** https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_DEM_GLO30_2024_1

| Item | Description |
|---|---|
| Dataset | Eastern Cape Copernicus DEM GLO-30 |
| Source | Copernicus DEM through Google Earth Engine |
| Source link | https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_DEM_GLO30_2024_1 |
| Resolution | 30 m |
| Raster dimensions | 27,679 × 15,624 cells |
| Geometry | Raster |
| Data type | Float32 |
| Band | `DEM` |
| Minimum elevation | -15.84 m |
| Maximum elevation | 1,975.42 m |
| Mean elevation | 973.60 m |
| Valid data | Approximately 50.9% of cells |
| Purpose | Used to investigate the influence of terrain and elevation on renewable-energy development |

The Copernicus DEM is a 30 m Digital Surface Model representing the Earth's surface, including features such as vegetation, buildings and infrastructure. The dataset uses the EGM2008 vertical datum. :contentReference[oaicite:3]{index=3}

The exported GeoTIFF was opened and inspected in QGIS. The raster contains one elevation band and is stored as a GeoTIFF.

---

## 6. Electricity Infrastructure

**Source:** World Bank / EnergyData.info  
**Underlying data:** OpenStreetMap  
**Reference period:** 2017  
**Source:** https://energydata.info/dataset/south-africa-electricity-transmission-and-distribution-2017

| Property | Description |
|---|---|
| Feature count | To be confirmed from the final QGIS layer |
| Geometry | Line |
| Key fields | Infrastructure type, voltage, status and other available infrastructure attributes |
| Purpose | Used to investigate the relationship between renewable-energy development and electricity infrastructure |
| Data quality | No issue identified |

The dataset provides historical electricity transmission and distribution infrastructure and is used as infrastructure context for the renewable-energy analysis.

---

## 7. Study Area Boundary

**Dataset:** FAO GAUL 2015 Level 1  
**Source:** Food and Agriculture Organization of the United Nations (FAO)  
**Access:** Google Earth Engine  
**Source:** https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level1

| Property | Description |
|---|---|
| Feature count | 1 Eastern Cape province feature |
| Geometry | Polygon |
| Key fields | `ADM0_NAME`, `ADM1_NAME` |
| Purpose | Defines the Eastern Cape study area and was used to clip the environmental datasets |
| Data quality | No issue identified with the selected Eastern Cape feature |




---

## Dataset Overview

| Dataset | Type | Main purpose |
|---|---|---|
| Renewable Energy EIA Applications | Polygon | Renewable-energy development |
| Municipal Boundaries | Polygon | Municipal analysis |
| Solar Resource | Raster | Solar resource conditions |
| Wind Resource | Raster | Wind resource conditions |
| Elevation | Raster | Physical/topographic conditions |
| Electricity Infrastructure | Line | Electricity-grid context |
| Eastern Cape Boundary | Polygon | Study-area definition |

---

## Initial Data Quality Notes

The datasets were obtained from different sources and therefore differ in spatial resolution, temporal coverage and data structure.

The renewable-energy EIA dataset represents **applications**, rather than necessarily representing operational renewable-energy facilities. The ERA5-Land environmental datasets provide relatively coarse spatial information compared with the 30 m elevation dataset. The electricity infrastructure data also has a **2017 reference period**, which should be considered when comparing it with more recent renewable-energy applications.

Further data-quality checks will be carried out in QGIS before the spatial analysis stage.
