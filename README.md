# NORP-Pollution-Analysis

This project investigates the relationship between air pollution, income, healthcare access, and chronic health outcomes at the county level across the United States.  
It integrates data from multiple public sources focusing on 2015–2025, with pollution, demographic, health, and climate variables merged using FIPS codes.

---

## Project Overview
We analyze how air quality (PM2.5, Ozone) and socioeconomic conditions influence health outcomes such as life expectancy, obesity, and chronic disease prevalence.  
The data is collected from federal sources such as the EPA, CDC, HRSA, IRS, USDA, and NOAA to ensure accuracy and reproducibility.

---

## Previous Research
- [Study on Air Pollution & Life Expectancy (PubMed)](https://pubmed.ncbi.nlm.nih.gov/35717994/)

---

## Air Pollution and Quality Data
- **EPA AirData (AQS Annual & Daily Summary Files)**  
  https://aqs.epa.gov/aqsweb/airdata/download_files.html  
  Use “Annual Summary by County” for PM2.5, Ozone, NO₂, SO₂, and CO concentrations.

- **EPA Daily AQI and Concentration Data**  
  https://www.epa.gov/outdoor-air-quality-data/download-daily-data  
  Daily Air Quality Index data per county or monitoring station.

---

## Health Outcomes and Behavioral Data
- **500 Cities Project (2016–2019)**  
  https://www.cdc.gov/places/about/500-cities-2016-2019/index.html  
  City-level health data used prior to the PLACES project.

- **CDC PLACES: Local Data for Better Health (2020–2024)**  
  - [2024 County Data (GIS Friendly Format)](https://data.cdc.gov/500-Cities-Places/PLACES-County-Data-GIS-Friendly-Format-2024-releas/i46a-9kgh)  
  - [2023 County Data](https://data.cdc.gov/500-Cities-Places/PLACES-Place-Data-GIS-Friendly-Format-2023-release/xx8k-iu94/about_data)  
  - [2022 County Data](https://data.cdc.gov/500-Cities-Places/PLACES-County-Data-GIS-Friendly-Format-2022-releas/xyst-f73f)  
  - [2021 County Data](https://data.cdc.gov/500-Cities-Places/PLACES-Census-Tract-Data-GIS-Friendly-Format-2021-/mb5y-ytti/about_data)  
  - [2020 County Data](https://data.cdc.gov/500-Cities-Places/PLACES-County-Data-GIS-Friendly-Format-2020-releas/mssc-ksj7)

---

## Healthcare Access and Workforce
- **HRSA Area Health Resources Files (AHRF)**  
  https://data.hrsa.gov/topics/health-workforce/ahrf  
  Contains county-level data on physicians, hospitals, healthcare access, and insurance coverage.

- **HRSA Data Downloads Portal**  
  https://data.hrsa.gov/data/download  

- **AHRF Variable Definitions**  
  https://data.hrsa.gov/Content/Documents/topics/AHRF%20Definition.pdf  

---

## Socioeconomic and Demographic Controls
- **USDA ERS County-Level Data Sets**  
  https://www.ers.usda.gov/data-products/county-level-data-sets/county-level-data-sets-download-data  
  Includes variables such as poverty, education, unemployment, and median income.

- **USDA Atlas of Rural & Small-Town America**  
  https://www.ers.usda.gov/data-products/atlas-of-rural-and-small-town-america/download-the-data  
  Comprehensive CSV integrating demographic and economic indicators.

- **U.S. Census / ACS Data Access**  
  https://data.census.gov  
  For additional 5-year estimates (population, education, income).

---

## Migration and Population Movement
- **IRS SOI County-to-County Migration Data**  
  https://www.irs.gov/statistics/soi-tax-stats-migration-data  
  Tracks population inflow/outflow per county based on tax return data.

---

## Climate and Environmental Controls
- **NOAA Climate at a Glance (County Time Series)**  
  https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/county/time-series  
  Provides county-level average temperature and precipitation data (monthly or annual).

---
