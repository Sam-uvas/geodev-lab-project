# Week 3 — Data Preparation

## 1. Working Coordinate Reference System

The project uses **EPSG:9221 — Hartebeesthoek94 / ZAF BSU Albers 25E** as the working coordinate reference system.

EPSG:9221 was selected because the study area covers the entire Eastern Cape Province and extends across more than one UTM zone. A single UTM zone would therefore not provide a consistent province wide working system.

EPSG:9221 is a projected, metre based coordinate system and uses an Albers Equal Area projection, making it suitable for province wide spatial analysis and area based comparisons.

---

## 2. Data Reprojection

The source datasets did not all use the same coordinate reference system.

The following datasets were reprojected to the project working CRS, **EPSG:9221**:

- Renewable energy project data
- Eastern Cape municipal boundaries
- Electricity grid infrastructure
- Solar resource data
- Wind resource data
- Copernicus DEM GLO30

The reprojection was performed using QGIS for the vector datasets and appropriate raster reprojection tools for the raster datasets.

The original source datasets were retained in `data/raw/`, while the reprojected versions were saved in `data/processed/`.

---

## 3. Data Clipping

All project datasets were clipped to the **Eastern Cape provincial boundary**, which defines the study area.

Vector datasets were clipped using QGIS.

The raster datasets were clipped to the Eastern Cape study area using Google Earth Engine before being prepared for analysis.

The clipping process ensured that the prepared datasets correspond to the same study area.

---

## 4. Analysis-Ready GeoPackage

The prepared vector datasets were saved as an analysis ready GeoPackage:

`data/processed/eastern_cape_renewable_energy.gpkg`

The GeoPackage contains the prepared vector layers used in the project:

- `renewable_projects`
- `municipalities`
- `electricity_grid`

The processed raster datasets are stored separately in the `data/processed/` directory as GeoTIFF files.

---

## 5. Data Quality Checks

Five quality checks were performed on the prepared datasets.

### 5.1 CRS Consistency

**Check:**  
The CRS of the prepared datasets was checked to ensure that the layers could be used consistently in the project.

**Result:**  
The prepared analytical datasets use **EPSG:9221 — Hartebeesthoek94 / ZAF BSU Albers 25E**.

**Problem identified:**  
The source datasets originally used different coordinate reference systems.

**Action:**  
Datasets requiring reprojection were transformed to EPSG:9221. The original datasets were retained in `data/raw/`.

---

### 5.2 Geometry Validity

**Check:**  
The geometries of the prepared vector datasets were checked for invalid or problematic geometries.

**Result:**  
No geometry problems affecting the prepared analytical datasets were identified.

**Problem identified:**  
No geometry problems were identified.

**Action:**  
The prepared geometries were retained for analysis.

---

### 5.3 Duplicate Features

**Check:**  
The prepared datasets were checked for duplicate features or repeated records that could affect the analysis.

**Result:**  
The renewable energy project dataset was checked for duplicate records/features.

**Problem identified:**  
No duplicate features affecting the analysis were identified.

**Action:**  
The prepared dataset was retained.

---

### 5.4 Missing or Null Attributes

**Check:**  
Important attribute fields were checked for missing or null values.

The check focused on attributes relevant to the renewable energy analysis, including:

- Technology
- Project information
- Municipality
- Capacity where available
- Project status

**Result:**  
The attribute information was checked for completeness.

**Problem identified:**  
Some source attributes do contain missing information.

**Action:**  
Available source values were retained. Missing information was not replaced with assumed values and will be treated as a limitation where relevant to later analysis.

---

### 5.5 Spatial Extent and Clipping

**Check:**  
The spatial extent of the prepared datasets was checked to confirm that they correspond to the Eastern Cape study area.

**Result:**  
The datasets were clipped to the Eastern Cape provincial boundary.

**Problem identified:**  
Source datasets contained data outside the defined study area.

**Action:**  
The datasets were clipped to the Eastern Cape boundary and the processed versions were retained in `data/processed/`.

---

## 6. Quality Check Summary

| Quality Check | Result | Action |
|---|---|---|
| CRS consistency | Prepared datasets use EPSG:9221 | Required datasets were reprojected |
| Geometry validity | No geometry problems identified | Prepared geometries retained |
| Duplicate features | No duplicates identified | Prepared datasets retained |
| Missing/null attributes | Some source attributes did contain missing information | Source values retained and limitations flagged |
| Spatial extent/clipping | Datasets correspond to the Eastern Cape study area | Datasets clipped and retained |

---

## 7. Prepared Data Location

The main analysis ready vector dataset is located at:

`data/processed/eastern_cape_renewable_energy.gpkg`

The processed raster datasets are located in:

`data/processed/`

The original source datasets are retained in:

`data/raw/`

---

## 8. Week 3 Preparation Summary

The Week 3 data preparation requirements were completed by:

- Reprojecting the required datasets to the selected working CRS.
- Clipping the datasets to the Eastern Cape study area.
- Saving the prepared vector datasets as an analysis-ready GeoPackage.
- Preparing the raster datasets for analysis.
- Performing five data quality checks.
- Recording the results of the quality checks.
- Identifying and documenting problems and the actions taken.
- Retaining the original source datasets separately from the processed datasets.

The prepared datasets are now ready for the next stage of the Eastern Cape Renewable Energy Opportunity & Development Atlas analysis.
