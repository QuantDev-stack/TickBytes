import pandas as pd
from pathlib import Path

def analyze_tick_data(filepath: Path):
    """
    Loads, cleans, and analyzes Level 2 tick-by-tick data using Pandas.
    """
    print(f"=== Loading Tick Data from {filepath.name} ===")
    
    # Load dataset
    df = pd.read_csv(filepath)
    print(f"Rows: {len(df)}")
    print("Columns:", df.columns.tolist()[:10])
            
    # Ensure datetime index
    df["datetime"] = pd.to_datetime(df["datetime"])
    df.set_index("datetime", inplace=True)
    df.sort_index(inplace=True)
    
    # Print descriptive statistics
    print("\n--- Summary Statistics (LTP) ---")
    print(df["ltp"].describe())
    
    # Calculate Spread (Level 2 Bid/Ask Spread)
    if "bid_px" in df.columns and "ask_px" in df.columns:
        df["spread"] = df["ask_px"] - df["bid_px"]
        print("\n--- Level 2 Bid/Ask Spread ---")
        print(df["spread"].describe())
        
    # Resample tick data to 1-minute OHLCV candles
    print("\n--- Resampling Ticks to 1-Minute Candles ---")
    ohlc = df["ltp"].resample("1min").ohlc()
    volume = df["ltq"].resample("1min").sum()
    candles = ohlc.join(volume.rename("volume")).dropna()
    print(candles.head())
    
    return df

if __name__ == "__main__":
    # Test with NIFTY options sample
    sample_file = Path("../../samples/options/NIFTY_OPT.csv")
    if sample_file.exists():
        analyze_tick_data(sample_file)
    else:
        print(f"Sample file not found: {sample_file.resolve()}")
