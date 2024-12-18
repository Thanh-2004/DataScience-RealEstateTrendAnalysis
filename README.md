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
