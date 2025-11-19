import yfinance as yf
import pandas as pd

class Asset:
    """
    Represents a financial asset with intraday and long-term data.
    
    Attributes:
    - ticker (str): The financial symbol.
    - stock (int): The quantity owned.
    - current_price (float): The latest market price.
    - historical_daily (pd.DataFrame): Short-term data (Interval: 5m, Period: 5 days).
    - historical_long (pd.DataFrame): Long-term data (Interval: 1d, Period: 5 years).
    """

    def __init__(self, ticker: str, stock: int):
        self.ticker = ticker
        self.stock = stock
        
        # Initialize attributes
        self.current_price = 0.0
        self.historical_daily = None  # 5-minute interval
        self.historical_long = None  # Daily interval

        # Fetch all data immediately
        self.refresh_data()

    def refresh_data(self):
        """
        Fetches both intraday (5m) and long-term (1d) data from Yahoo Finance.
        """
        print(f"--- Fetching data for {self.ticker} ---")
        
        try:
            # Initialize Ticker object once
            asset_ticker = yf.Ticker(self.ticker)
            
            # 1. Fetch Intraday Data (5 minutes)
            # We use period="5d" to ensure we have enough 5-minute candles for recent analysis
            df_intraday = asset_ticker.history(period="60d", interval="5m")
            
            if not df_intraday.empty:
                self.historical_daily = df_intraday
                # Update current price based on the very last 5m close
                self.current_price = df_intraday['Close'].iloc[-1]
                print(f"✔ Intraday data (5m) loaded. Current Price: ${self.current_price:.2f}")
            else:
                print("✘ Warning: No intraday data found.")

            # 2. Fetch Long-Term Data (Daily)
            # We use period="5y" (5 years) for the daily history
            df_daily = asset_ticker.history(period="5y", interval="1d")
            
            if not df_daily.empty:
                self.historical_long = df_daily
                print(f"✔ Long-term data (Daily) loaded. ({len(df_daily)} days)")
            else:
                print("✘ Warning: No daily data found.")

        except Exception as e:
            print(f"Error fetching data: {e}")

    def calculate_total_value(self) -> float:
        return self.current_price * self.stock

    def __str__(self):
        return (f"Asset: {self.ticker} | Stock: {self.stock} | "
                f"Price: ${self.current_price:.2f}")