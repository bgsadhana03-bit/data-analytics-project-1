# data-analytics-project-1
Data Analytics Project 1 — Data Cleaning and Preparation using Python and pandas.
# DecodeLabs Data Analytics Project 1

## Project Overview
This project focuses on data cleaning and preparation using Python and Pandas. The goal is to improve data quality and validate the dataset before analysis.

## Dataset
- **Rows:** 1,200
- **Columns:** 14
- **Original file:** `Dataset for Data Analytics.xlsx`
- **Cleaned file:** `Cleaned_Data_Analytics.xlsx`

## Tools Used
- Python
- Pandas
- OpenPyXL
- Visual Studio Code

# Data Cleaning and Preparation
- Inspected the dataset's columns and data types.
- Checked for missing values.
- Checked for duplicate rows and duplicate OrderIDs.
- Verified date formats and checked for invalid dates.
- Checked that `TotalPrice` matches `Quantity × UnitPrice`.
- Removed leading and trailing spaces from text columns.
- Saved the cleaned dataset to a separate Excel file, preserving the original.

# Validation Results
- Rows in the saved dataset: 1,200
- Columns in the saved dataset: 14
- Duplicate OrderIDs: 0
- Invalid or missing dates: 0
- Rows with incorrect `TotalPrice`: 0
- Missing `CouponCode` values: 309

# Missing Values
The 309 missing `CouponCode` values were preserved rather than replaced with assumed values. Their meaning should be confirmed against the business rules before deciding whether any further treatment is needed.

# Output
The cleaned dataset is saved as `Cleaned_Data_Analytics.xlsx`.

# Learning Outcome
This project provided hands-on practice in inspecting, cleaning, validating, and exporting data using Python and Pandas.