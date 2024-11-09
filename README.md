
# Time Series Forecasting for Portfolio Management Optimization

This project focuses on applying time series forecasting and statistical analysis for portfolio management, enabling optimized asset allocation and better risk management. By analyzing historical stock data, this project aims to provide actionable insights for a financial advisory firm, Guide Me in Finance (GMF) Investments.

## Project Overview

### Business Objective
Guide Me in Finance (GMF) Investments is a financial advisory firm specializing in personalized portfolio management. The firm uses advanced data-driven insights to predict market trends and optimize asset allocation, with the goal of helping clients achieve their financial objectives by minimizing risks and capitalizing on market opportunities.

As a Financial Analyst at GMF Investments, your task is to apply time series forecasting to historical financial data to enhance portfolio management strategies. 

### Data Sources
Historical financial data is sourced from [Yahoo Finance](https://pypi.org/project/yfinance/) for three assets:
- **TSLA (Tesla)**: High-growth, high-risk stock in the consumer discretionary sector.
- **BND (Vanguard Total Bond Market ETF)**: A bond ETF offering stability and low risk.
- **SPY (S&P 500 ETF)**: An ETF tracking the S&P 500, providing diversified, moderate-risk market exposure.

The dataset includes:
- Date
- Open, High, Low, Close (Adjusted Close)
- Volume
- Volatility (calculated during analysis)

The data covers the period from January 1, 2015, to October 31, 2024.

### Data Preprocessing and Exploratory Data Analysis (EDA)

#### Objective
Task 1 involves loading, cleaning, and understanding the data to prepare it for further modeling. Specifically, it covers data extraction, cleaning, exploratory data analysis, seasonality analysis, and volatility metrics.

#### Requirements Fulfilled

1. **Data Extraction**: 
   - Load historical data for TSLA, BND, and SPY using the Yahoo Finance API.
   - Clean missing values using forward and backward fill methods.

2. **Data Cleaning and Basic Statistics**:
   - Check for data types and ensure no missing values remain.
   - Display basic statistics for each asset (mean, standard deviation, etc.).

3. **Exploratory Data Analysis (EDA)**:
   - **Trend Analysis**: Visualize adjusted close prices over time to observe long-term trends.
   - **Daily Volatility Analysis**: Calculate and plot daily returns to understand volatility.
   - **Rolling Statistics**: Analyze rolling mean and standard deviations for short-term trends.
   - **Outlier Detection**: Identify days with unusually high or low returns using Z-scores.
   
4. **Seasonality and Trend Analysis**:
   - Decompose time series into trend, seasonal, and residual components for each asset.

5. **Volatility Analysis**:
   - Calculate Value at Risk (VaR) at 99% confidence level and the Sharpe Ratio, providing insights on potential losses and risk-adjusted returns.
6. **Autocorrelation Analysis**: Plot ACF and PACF for further pattern recognition.

## Installation

1. **Clone this repository**:
   ```bash
   git https://github.com/yohannestayez/Time-Series-Forecasting-for-Portfolio-Management-Optimization.git
   cd Time-Series-Forecasting-for-Portfolio-Management-Optimization
   ```

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Make sure `yfinance`, `pandas`, `numpy`, `matplotlib`, `seaborn`, and `statsmodels` are installed.

## Usage

1. **Run the Notebook**:
   Open `Preprocess_and_Explore_the_Data.ipynb` in Jupyter Notebook to execute the analysis.
   
2. **Modular Analysis Functions**:
   Each section in Task 1 is modularized into functions, so you can apply them individually to different assets or run them all sequentially.

3. **Key Insights**:
   Key insights from each analysis section are documented within the notebook, providing an overview of trends, volatility, and risk metrics for each asset.

## Key Files and Structure

```   
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── .gitignore
├── requirements.txt                   # Required packages
├── README.md                       # Project documentation
├── src/
│   └── __init__.py
├── notebooks/
│   ├── __init__.py
│   └── Preprocess_and_Explore_the_Data.ipynb
|
├── data/  
|
├── tests/
│   └── __init__.py
└── scripts/
    ├── __init__.py
    ├── EDA.py
    └── README.md
```


## Next Steps

Following this, the next phase will involve building forecasting models to predict future asset prices and support optimized portfolio management decisions.



