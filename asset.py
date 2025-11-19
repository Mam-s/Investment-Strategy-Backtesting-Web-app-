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
            # Renamed variable to be explicit
            df_intraday = asset_ticker.history(period="60d", interval="5m")
            
            if not df_intraday.empty:
                self.historical_intraday = df_intraday
                self.current_price = df_intraday['Close'].iloc[-1]
                print(f"✔ Intraday (5m) loaded into 'historical_intraday'.")
            else:
                print("✘ Warning: No intraday data found.")

            # 2. Daily (1d) - 5 Years
            # Renamed variable to be explicit
            df_daily = asset_ticker.history(period="5y", interval="1d")
            
            if not df_daily.empty:
                self.historical_daily = df_daily
                print(f"✔ Daily data loaded into 'historical_daily'.")
            else:
                print("✘ Warning: No daily data found.")

        except Exception as e:
            print(f"Error fetching data: {e}")


    

# 1. Initialize
tesla = Asset("TSLA")

print(tesla)
# 2. Check Intraday (5m)
# Renamed: historical_data -> historical_intraday
print("\n--- Last 3 entries of 5-minute Data (Intraday) ---")
if tesla.historical_intraday is not None:
    print(tesla.historical_intraday.tail(3)[['Close', 'Volume']])

# 3. Check Long Term (Daily)
# Renamed: historical_long -> historical_daily
print("\n--- First 3 entries of Daily Data (5 Years ago) ---")
if tesla.historical_daily is not None:
    print(tesla.historical_daily.head(3)[['Close', 'Volume']])

# 4. Simple Analysis: Compare volatility
if tesla.historical_intraday is not None and tesla.historical_daily is not None:
    volatility_5m = tesla.historical_intraday['Close'].std()
    volatility_daily = tesla.historical_daily['Close'].std()
    print(f"\nIntraday Volatility (5m): {volatility_5m:.2f}")
    print(f"Long-term Volatility (Daily): {volatility_daily:.2f}")