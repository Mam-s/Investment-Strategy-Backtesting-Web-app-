import yfinance as yf
import pandas as pd

class Asset:
    def __init__(self, ticker: str):
        self.ticker = ticker
        
        self.current_price = 0.0
        self.historical_intraday = None # 5-minute interval 
        self.historical_daily = None    # Daily interval 
        self.refresh_data()

    def refresh_data(self):
        print(f"--- Fetching data for {self.ticker} ---")
        try:
            asset_ticker = yf.Ticker(self.ticker)
            
            # 1. Intraday (5m) - Max 60 days
            df_intraday = asset_ticker.history(period="60d", interval="5m")
            
            if not df_intraday.empty:
                self.historical_intraday = df_intraday
                self.current_price = df_intraday['Close'].iloc[-1]
                print(f"✔ Intraday (5m) loaded into 'historical_intraday'.")
            else:
                print("✘ Warning: No intraday data found.")

            # 2. Daily (1d) - 5 Years
            df_daily = asset_ticker.history(period="5y", interval="1d")
            
            if not df_daily.empty:
                self.historical_daily = df_daily
                print(f"✔ Daily data loaded into 'historical_daily'.")
            else:
                print("✘ Warning: No daily data found.")

        except Exception as e:
            print(f"Error fetching data: {e}")

