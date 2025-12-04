# 🌊 Sea Level Predictor

### 🚀 Project Overview
This project analyzes global average sea level change data since 1880 and uses **statistical algorithms** to predict future sea level rise through the year 2050. It demonstrates the application of linear regression to model long-term climate trends.

**Key Objective:** Visualize historical sea level data and generate two predictive models (lines of best fit) to compare historical trends vs. recent acceleration.

### 📊 Visualizations & Predictions
This project generates a comprehensive matplotlib visualization (`sea_level_plot.png`) containing:

#### 1. Historical Data (Scatter Plot)
* Visualizes the `CSIRO Adjusted Sea Level` from 1880 to 2014.

#### 2. Long-Term Prediction (1880–2050)
* **Model:** Linear Regression (using `scipy.stats.linregress`).
* **Scope:** Uses the entire dataset (1880-2014) to calculate the historical rate of rise.
* **Projection:** Extrapolates this line to predict sea levels in 2050.

#### 3. Recent Trend Prediction (2000–2050)
* **Model:** Linear Regression focused on recent data (2000 onwards).
* **Insight:** Demonstrates that the rate of sea level rise has accelerated in recent decades, resulting in a steeper projection for 2050 compared to the historical average.

### 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas
* **Visualization:** Matplotlib
* **Statistics:** Scipy (Linear Regression, Slope, Intercept)

### 📂 Project Structure
* `sea_level_predictor.py`: Contains the logic for data loading, regression calculation, and plotting.
* `main.py`: Entry point for testing the predictor.
* `test_module.py`: Unit tests to verify the accuracy of the regression lines and plot labels.
* `epa-sea-level.csv`: Dataset sourced from the US Environmental Protection Agency (CSIRO/NOAA data).

### 🏆 Certification
This project is the **Final Capstone** for the **FreeCodeCamp Data Analysis with Python Certification**.
