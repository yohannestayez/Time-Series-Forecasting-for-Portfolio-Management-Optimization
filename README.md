
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

## Notebooks
### 1. Preprocess_and_Explore_the_Data.ipynb
The process begins with **data extraction**, where historical data for TSLA, BND, and SPY is loaded using the Yahoo Finance API. Missing values are then addressed through forward and backward fill methods. During **data cleaning and basic statistics**, the data types are checked, and any remaining missing values are handled, followed by the display of basic statistics for each asset, such as mean and standard deviation. The next step involves **exploratory data analysis (EDA)**, which includes visualizing the adjusted close prices over time to identify long-term trends, calculating and plotting daily returns to assess volatility, and analyzing rolling mean and standard deviations to capture short-term trends. Additionally, **outlier detection** is conducted by identifying days with extreme returns using Z-scores. **Seasonality and trend analysis** is performed by decomposing each asset's time series into its trend, seasonal, and residual components. In **volatility analysis**, Value at Risk (VaR) is calculated at a 99% confidence level, alongside the Sharpe Ratio, providing insights into potential losses and risk-adjusted returns. Finally, **autocorrelation analysis** is conducted by plotting the Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) to uncover further patterns in the data.


### 2. Time_Series_Forecasting_Tesla_SPY_BND.ipynb
This notebook focuses on developing time series forecasting models for financial data, specifically for Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY). It includes a thorough preprocessing step to ensure the data is clean and suitable for modeling. Stationarity is checked and enforced through differencing where necessary, as time series models like ARIMA require stationary input. Three types of forecasting models are implemented: ARIMA, SARIMA, and LSTM using PyTorch. The notebook also evaluates the models' performance using metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Mean Absolute Percentage Error (MAPE). Additionally, it includes visualizations to analyze trends, volatility, and forecast accuracy, making it an end-to-end solution for time series forecasting.

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
   
   Make sure `yfinance`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `statsmodels`, `scikit-learn`, `torch`and `pmdarima` are installed.

## Usage

1. **Run the Notebook**:
   Open the notebooks Jupyter Notebook to execute the analysis.
   
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
│   ├── Preprocess_and_Explore_the_Data.ipynb
│   └── Time_Series_Forecasting_Tesla_SPY_BND.ipynb
│
|
├── data/  
|
├── tests/
│   └── __init__.py
└── scripts/
    ├── __init__.py
    ├── EDA.py
    ├── Train_model.py
    └── README.md
```








