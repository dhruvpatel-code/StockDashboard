import yfinance as yf
import ta
from server import cache

def get_data(cache, selected_dropdown, start_date, end_date):
    @cache.memoize()
    def _get_data(selected_dropdown, start_date, end_date):
        try:
            # Download stock data using yfinance
            df = yf.download(selected_dropdown, start=start_date, end=end_date)
            
            # Sort the dataframe by date
            df.sort_values('Date', inplace=True)

            # Add SMA and RSI to the dataframe
            df['SMA'] = ta.trend.sma_indicator(df['Close'], window=14)
            df['RSI'] = ta.momentum.rsi(df['Close'], window=14)

            return df
        except Exception as e:
            print(f"Error: {str(e)}")
            return None
    
    return _get_data(selected_dropdown, start_date, end_date)


