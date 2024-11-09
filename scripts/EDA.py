import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Define date range for analysis
start_date = '2015-01-01'
end_date = '2024-10-31'

# Function to download and clean data for a given ticker
def load_and_clean_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    data['Date'] = data.index
    data.fillna(method='ffill', inplace=True)
    data.fillna(method='bfill', inplace=True)
    data['Date'] = pd.to_datetime(data['Date'])
    data['Daily Return'] = data['Adj Close'].pct_change()
    data.to_csv(f"../data/{ticker}_proccessed_data.csv", index=True)
    return data

# Function to display basic statistics and missing values
def display_basic_stats(data, ticker):
    print(f"Basic Statistics for {ticker}:\n", data.describe())
    print(f"\nMissing Values for {ticker}:\n", data.isnull().sum())

# Function to plot adjusted close price over time
def plot_adjusted_close(data, ticker):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Adj Close'], label='Adjusted Close')
    plt.title(f"{ticker} Adjusted Close Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Adjusted Close Price")
    plt.legend()
    plt.show()

# Function to plot daily percentage change (volatility)
def plot_daily_return(data, ticker):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Daily Return'], label='Daily Return')
    plt.title(f"{ticker} Daily Percentage Change (Volatility)")
    plt.xlabel("Date")
    plt.ylabel("Daily Return")
    plt.legend()
    plt.show()

# Function to plot rolling mean and standard deviation
def plot_rolling_stats(data, ticker):
    rolling_mean = data['Adj Close'].rolling(window=30).mean()
    rolling_std = data['Adj Close'].rolling(window=30).std()
    
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Adj Close'], label='Adjusted Close')
    plt.plot(data['Date'], rolling_mean, color='orange', label='30-Day Rolling Mean')
    plt.plot(data['Date'], rolling_std, color='red', label='30-Day Rolling Std Dev')
    plt.title(f"{ticker} Rolling Mean and Standard Deviation")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

def plot_seasonal_decomposition(data, ticker, width=15, height=8):  # Added width and height arguments
  """
  Performs seasonal decomposition and plots the results with a wider figure.

  Args:
      data (pandas.Series): The time series data to decompose.
      ticker (str): The ticker symbol for the data.
      width (float, optional): The desired width of the plot in inches. Defaults to 12.
      height (float, optional): The desired height of the plot in inches. Defaults to 6.
  """

  decomposition = seasonal_decompose(data['Adj Close'], model='multiplicative', period=252)
  fig, axes = plt.subplots(4, 1, figsize=(width, height))  # Adjust figure size

  decomposition.trend.plot(ax=axes[0])
  axes[0].set_title('Trend')

  decomposition.seasonal.plot(ax=axes[1])
  axes[1].set_title('Seasonal')

  decomposition.resid.plot(ax=axes[2])
  axes[2].set_title('Residual')

  data['Adj Close'].plot(ax=axes[3])
  axes[3].set_title('Original')

  plt.suptitle(f"Seasonal Decomposition of {ticker} Adjusted Close Price")
  plt.tight_layout()  # Adjust spacing between subplots
  plt.show()

# Function to detect and display outliers based on Z-score
def detect_outliers(data, ticker):
    data['Z-Score'] = (data['Daily Return'] - data['Daily Return'].mean()) / data['Daily Return'].std()
    outliers = data[(data['Z-Score'] > 3) | (data['Z-Score'] < -3)]
    print(f"\nOutliers in {ticker} based on Z-Score:\n", outliers[['Date', 'Daily Return', 'Z-Score']])

# Function to calculate and display volatility metrics
def calculate_volatility_metrics(data, ticker):
    VaR_99 = data['Daily Return'].quantile(0.01)
    Sharpe_Ratio = data['Daily Return'].mean() / data['Daily Return'].std()
    
    print(f"\nVolatility Metrics for {ticker}:")
    print(f"99% Value at Risk (VaR): {VaR_99}")
    print(f"Sharpe Ratio: {Sharpe_Ratio}")





def plot_autocorrelation(data, ticker, width=15, height=6, lags=30):
  """
  Plots both autocorrelation (ACF) and partial autocorrelation (PACF) for adjusted close data.

  Args:
      data (pandas.Series): The time series data to decompose.
      ticker (str): The ticker symbol for the data.
      width (float, optional): The desired width of the plot in inches. Defaults to 15.
      height (float, optional): The desired height of the plot in inches. Defaults to 6.
      lags (int, optional): The number of lags to compute for ACF and PACF. Defaults to 30.
  """

  plt.figure(figsize=(width, height))

  # Plot ACF on first subplot
  ax1 = plt.subplot(211)
  plot_acf(data['Adj Close'].dropna(), lags=lags, ax=ax1)
  plt.title(f"Autocorrelation of Adjusted Close for {ticker}")

  # Plot PACF on second subplot
  ax2 = plt.subplot(212)
  plot_pacf(data['Adj Close'].dropna(), lags=lags, ax=ax2)
  plt.title(f"Partial Autocorrelation of Adjusted Close for {ticker}")

  # Adjust layout for better spacing
  plt.tight_layout()

  plt.show()
