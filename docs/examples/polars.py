import polars as pl
from pathlib import Path

def analyze_tick_data_polars(filepath: Path):
    """
    High-performance Level 2 tick-by-tick data loading and resampling using Polars.
    """
    print(f"=== Loading Tick Data (Polars) from {filepath.name} ===")
    
    # Load dataset lazily for memory efficiency
    q = pl.scan_csv(filepath)
    
    # Cast datetime and sort
    q = q.with_columns(
        pl.col("datetime").str.strptime(pl.Datetime, format="%Y-%m-%d %H:%M:%S%.3f")
    ).sort("datetime")
    
    # Execute query
    df = q.collect()
    print(f"Loaded {len(df)} rows.")
    
    # Summary stats
    print("\n--- Summary Statistics (LTP) ---")
    print(df.select(pl.col("ltp").describe()))
    
    # Level 2 Spread calculation
    if "bid_px" in df.columns and "ask_px" in df.columns:
        df = df.with_columns(
            (pl.col("ask_px") - pl.col("bid_px")).alias("spread")
        )
        print("\n--- Level 2 Spread Statistics ---")
        print(df.select(pl.col("spread").describe()))
        
    # High-speed resampling to 1-minute OHLCV candles
    print("\n--- Resampling Ticks to 1-Minute Candles ---")
    resampled = (
        df.group_by_dynamic("datetime", every="1m")
        .agg([
            pl.col("ltp").first().alias("open"),
            pl.col("ltp").max().alias("high"),
            pl.col("ltp").min().alias("low"),
            pl.col("ltp").last().alias("close"),
            pl.col("ltq").sum().alias("volume")
        ])
        .drop_nulls()
    )
    print(resampled.head())
    
    return df

if __name__ == "__main__":
    # Test with NIFTY options sample
    sample_file = Path("../../samples/options/NIFTY_OPT.csv")
    if sample_file.exists():
        analyze_tick_data_polars(sample_file)
    else:
        print(f"Sample file not found: {sample_file.resolve()}")
