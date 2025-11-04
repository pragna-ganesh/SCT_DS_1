# README.md

# Global Population Visualization using Python

This project visualizes the **total population by world region** for the year 2020 using World Bank data.

Dataset Indicator used: **SP.POP.TOTL** (Total Population)

---

## Features
- Reads World Bank .zip dataset directly
- Automatically detects main CSV file inside the ZIP
- Extracts selected world regions
- Converts population values to **Billions**
- Plots a clean vertical bar chart using matplotlib

---

## Requirements

bash
pip install pandas matplotlib

## Data Source

World Bank Indicator Data:
https://data.worldbank.org/indicator/SP.POP.TOTL

## Output Chart

-Vertical bar chart
-Shows regions on X-axis
-Population (Billions) on Y-axis
-Labels shown on top of each bar
-Year currently set to: 2020
