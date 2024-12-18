# DataScience-RealEstateTrendAnalysis


## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Data Scraping](#data-scraping)
  - [Data Cleaning](#data-cleaning)
  - [EDA](#eda)
  - [Machine Learning Models](#machine-learning-models)
- [Evaluation Metrics](#evaluation-metrics)
- [Results](#results)
- [Analysis](#analysis)
- [Acknowledgments](#acknowledgments)

---

## Overview


---

## Dataset
The dataset for this project consists of housing price data collected from two websites: rever.com and cafeland.vn. The data contains information about real estate listings, including prices, location, property type, area, and other relevant features. This dataset is used for building machine learning models to predict property prices and classify property types.

The dataset for this project includes the following columns:

- **Price (billion VND)**:
   - The price of the property in billion Vietnamese Dong (VND).

- **Area (m2)**:
   - The area of the property in square meters (m²).

- **Property Type**:
   - The type of the property (e.g., house, apartment, land, villa, etc.).

- **Bedrooms**:
   - The number of bedrooms in the property.

- **Bathrooms**:
   - The number of bathrooms in the property.

- **Address**:
   - The detailed address of the property.

- **Law Document**:
   - The legal status of the property, such as ownership documents or other legal papers.

- **Post Date**:
   - The date the property was listed for sale or rent.

- **Latitude**:
    - The latitude of the property, used to determine its geographical location on a map.

- **Longitude**:
    - The longitude of the property.

- **Postal Code**:
    - The postal code for the area where the property is located.

- **Importance**:
    - The importance or priority of the property....

- **Place Rank**:
    - The ranking of the property based on ...
    - **Example**: `1`, `2`, `3`.

- **City**:
    - The city or region where the property is located.
---

## Requirements

The following libraries and frameworks are required for running the project:

- Python 3.10
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- XGBoost

...

To install these dependencies, you can use the provided `requirements.txt` file.

### Example:

```
pip install -r requirements.txt
```

---

## Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/Thanh-2004/DataScience-RealEstateTrendAnalysis.git
   cd DataScience-RealEstateTrendAnalysis
   ```

2. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

   Alternatively, install required libraries individually using `pip`.
   

---

## Usage

### Data Scraping

### Data Cleaning
Data crawled from [rever.com](https://rever.vn/) is complete and clean. Therefore, our efforts is spent in cleaning data from [CafeLand.com](https://cafeland.vn/).
#### Data Preprocessing
- **Data Extraction**: Raw data is extracted and formatted for proper usage from `.json` files generated from our spider. The details can be found in `DataCleaning/ExtractingFeatures.py`.

- **Data Preprocessing**: `DataCleaning/CleanData.py`
  - One of our main purposes is to predict real estate price based on common characteristics that properties share. To serve this, all data with missing value in **Price (billion VND)** is dropped.
  - We also drop features with the NaN percentage crossing a certain threshold **(60% in this case)**.
  - Since real estate from [CafeLand.com](https://cafeland.vn/) should be those in Hanoi, all houses not in Hanoi are excluded as well.
  - **Address**, **Latitude**, and **Longitude** are used to impute each other with the help from [free GeoCoding API](https://geocode.maps.co/).
  
- **Data Imputation**: `DataCleaning/Imputer.py`
  - **Multivariate Imputation by Chained Equations (MICE)**: Apply for features satisfying the additive assumption in regression.
  - **Predictive Mean Matching (PMM)**: Apply for features where high correlation (multi-collinearity) exists.
  
- **Addition of related data**: `DataCleaning/AdditionalInfo.py`
Making use of the properties' coordinates and `geopy.Nominatim`, the following fields are added:
  - **Place Rank**: Describe the extend and importance of a place
  - **Importance**: How likely it is that an user will search for a given place.
  - **Postal Code**
  
To run the cleaning process, remember to get your GeoCoding API from [free GeoCoding API](https://geocode.maps.co/):
```
python3 main-clean.py
```
or
```
python main-clean.py
```

After cleaning, data from [rever.com](https://rever.vn/) and [CafeLand.com](https://cafeland.vn/) is stacked. Outliers are removed using the Interquatile Range (`DataCleaning/Outliers.py`)

### EDA

### Machine Learning Models

You can find notebooks used to train the ML models in `MachineLearningModels/notebooks`. Each notebook is used to train models using a ML algorithm for the two problems: estate price prediction and property type classification.

To run the demonstration on price prediction, run:
```
python3 PricePredictionDemo.py
```
or
```
python PricePredictionDemo.py
```

This will run a window to select a random record from the testing dataset and display it, along with the predicted price by a model trained on the training dataset and the actual price of the estate for comparison.


---

## Evaluation Metrics

For ML models, the following metrics are used to evaluate how well the models perform:

- For the price prediction problem: Root Mean Squared Error (RMSE), Mean and Median Absolute Error (MAE & MedAE), Mean and Median Absolute Percentage Error (MAPE & MedAPE)
- For the property type classification problem: Accuracy, Precision, Recall, F1 score

---

## Results

---

## Analysis

---

## Acknowledgments

---
