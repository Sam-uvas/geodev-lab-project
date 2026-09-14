# Renewable Energy Development in the Eastern Cape

## Project Question

**How are renewable-energy projects spatially distributed across the Eastern Cape, and what relationship do their locations have with renewable-resource conditions, terrain and electricity infrastructure?**

---

## Study Area

**Eastern Cape, South Africa**

The Eastern Cape is the geographic extent of the project and all spatial analysis will be conducted within the provincial boundary.

---

## Project Aim

Renewable-energy development is not distributed evenly across space.

This project aims to investigate the spatial and temporal distribution of renewable-energy development across the Eastern Cape and examine the physical and infrastructure characteristics associated with where renewable-energy projects are located.

The analysis will compare existing renewable-energy project locations with solar radiation, wind speed, elevation and electricity infrastructure.

The project will ultimately contribute to the development of an **Eastern Cape Renewable Energy Opportunity & Development Atlas**.

---

## Objectives

The project will:

1. Map the spatial distribution of renewable-energy projects across the Eastern Cape.
2. Examine the development of renewable-energy projects over time.
3. Identify the main renewable-energy technologies represented in the province.
4. Examine how renewable-energy development varies between municipalities.
5. Investigate the relationship between wind-energy projects and wind-speed conditions.
6. Investigate the relationship between Solar PV projects and solar-radiation conditions.
7. Examine the relationship between renewable-energy development and elevation/terrain.
8. Investigate the spatial relationship between renewable-energy projects and electricity infrastructure.
9. Identify spatial patterns that may indicate areas requiring further investigation for future renewable-energy development.

---

# Datasets

## 1. Renewable Energy EIA Applications

The renewable-energy EIA dataset is the core dataset for the project.

It provides information about renewable-energy projects and applications, including project locations, technology types, capacity, application dates, project status and municipal information.

This dataset will be used to identify where renewable-energy development has occurred and to examine the spatial and temporal patterns of development.

**Source:** Department of Forestry, Fisheries and the Environment (DFFE)

**Source link:**  
https://www.dffe.gov.za/egis

**Role in analysis:** Existing renewable-energy development

---

## 2. Municipal Boundaries

Municipal boundaries will provide the administrative framework for analysing renewable-energy development across the Eastern Cape.

The boundaries will be used to determine the distribution of projects between municipalities and to support municipal-level spatial analysis.

**Source:** Municipal Demarcation Board (MDB)

**Source link:**  
https://www.demarcation.org.za/

**Role in analysis:** Administrative boundaries and municipal comparison

---

## 3. Solar Radiation

Solar-radiation data will be used to investigate the relationship between Solar PV development and solar-resource conditions across the Eastern Cape.

The project uses the ERA5-Land Daily Aggregated dataset. Daily solar-radiation data for the period 2016–2025 was processed in Google Earth Engine and exported as a GeoTIFF for analysis in QGIS.

The selected variable is:

`surface_solar_radiation_downwards_sum`

The resulting data was converted from J/m²/day to kWh/m²/day.

**Source dataset:** ECMWF ERA5-Land Daily Aggregated

**Google Earth Engine collection:**  
`ECMWF/ERA5_LAND/DAILY_AGGR`

**Period:** 2016–2025

**Processing platform:** Google Earth Engine

**Output:** GeoTIFF raster for QGIS

**Role in analysis:** Solar-resource conditions

---

## 4. Wind Speed

Wind-resource data will be used to investigate the relationship between wind-energy development and wind-speed conditions across the Eastern Cape.

The project uses the ERA5-Land Hourly dataset for the period 2016–2025.

The 10 m wind-speed variable is derived from the horizontal wind components:

- `u_component_of_wind_10m`
- `v_component_of_wind_10m`

Wind speed is calculated as:

**Wind Speed = √(U² + V²)**

The mean 10 m wind speed for 2016–2025 was calculated in Google Earth Engine and exported as a GeoTIFF for analysis in QGIS.

**Source dataset:** ECMWF ERA5-Land Hourly

**Google Earth Engine collection:**  
`ECMWF/ERA5_LAND/HOURLY`

**Period:** 2016–2025

**Processing platform:** Google Earth Engine

**Output:** GeoTIFF raster for QGIS

**Role in analysis:** Wind-resource conditions

---

## 5. Elevation

Elevation data will be used to investigate whether terrain characteristics are associated with the spatial distribution of renewable-energy development.

The project uses the Copernicus DEM GLO-30 dataset.

The elevation data was accessed and processed through Google Earth Engine, mosaicked and clipped to the Eastern Cape before being exported as a GeoTIFF for QGIS.

**Source dataset:** Copernicus DEM GLO-30

**Google Earth Engine collection:**  
`COPERNICUS/DEM/GLO30`

**Resolution:** Approximately 30 m

**Processing platform:** Google Earth Engine

**Output:** GeoTIFF raster for QGIS

**Role in analysis:** Elevation and terrain conditions

---

## 6. Electricity Infrastructure

Electricity infrastructure data will be used to investigate the relationship between renewable-energy development and existing electricity infrastructure.

The analysis will consider infrastructure such as transmission lines and substations where available.

The dataset may be used for proximity and distance analysis to investigate whether renewable-energy projects are spatially associated with existing electricity infrastructure.

**Source:** World Bank / EnergyData.info

**Source link:**  
https://energydata.info/dataset/south-africa-electricity-transmission-and-distribution-2017

**Reference period:** 2017

**Role in analysis:** Electricity-grid and infrastructure context

---

# Data Processing

The project combines vector and raster datasets.

The renewable-energy project data, municipal boundaries and electricity infrastructure are vector datasets.

Solar radiation, wind speed and elevation are raster datasets.

Google Earth Engine is used to process selected environmental datasets before exporting them as GeoTIFF files for further analysis in QGIS.

QGIS is used for:

- Data inspection
- Layer management
- Spatial visualisation
- Data preparation
- Spatial analysis
- Map production

---

# Planned Spatial Analysis

The analysis will be conducted in several stages.

### 1. Renewable-Energy Distribution

Map the locations of renewable-energy projects across the Eastern Cape.

### 2. Technology Analysis

Compare the spatial distribution of different technologies, particularly:

- Wind
- Solar PV
- Wind & Solar
- Other recorded technologies

### 3. Temporal Analysis

Use application/development dates to investigate how renewable-energy development has changed over time.

### 4. Municipal Analysis

Compare the number and distribution of renewable-energy projects between municipalities.

### 5. Solar Analysis

Compare Solar PV project locations with the spatial distribution of solar radiation.

### 6. Wind Analysis

Compare wind-energy project locations with mean 10 m wind-speed conditions.

### 7. Terrain Analysis

Investigate the relationship between renewable-energy project locations and elevation.

Additional terrain variables, such as slope, may be derived from the elevation dataset if they are relevant to the analysis.

### 8. Infrastructure Analysis

Investigate the proximity of renewable-energy projects to electricity infrastructure.

---

# Expected Outcome

The project will produce a spatial understanding of renewable-energy development across the Eastern Cape.

The final output will contribute to an:

**Eastern Cape Renewable Energy Opportunity & Development Atlas**

The atlas will bring together:

- Renewable-energy development
- Technology patterns
- Development history
- Solar-resource conditions
- Wind-resource conditions
- Terrain characteristics
- Electricity infrastructure
- Municipal geography

The purpose is to identify and communicate spatial patterns that can support further investigation of renewable-energy opportunities.

The project will not treat environmental or infrastructure conditions alone as proof that an area is suitable for development. Instead, these factors will be used to understand the spatial characteristics associated with existing development and to identify areas that may warrant further investigation.

---

# Week 1 Progress

Week 1 focused on defining the spatial question, selecting the Eastern Cape as the study area and identifying the datasets required for the investigation.

The renewable-energy project dataset was sourced and initially explored in QGIS.

Initial exploration identified **254 renewable-energy records within the Eastern Cape**.

The dataset contains several technology categories, including:

- Wind
- Solar PV
- Wind & Solar
- Biomass/Biofuels
- Petroleum

Wind and Solar PV represent the majority of the records identified during the initial exploration.

**Status: Week 1 — Complete**

---


