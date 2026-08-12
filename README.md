# ⚡ TickBytes — Daily Indian F&O Market Data Feed

[![Data Status](https://img.shields.io/badge/Data_Feed-Active_Daily-green?style=flat-square)](#)
[![Resolutions](https://img.shields.io/badge/Resolutions-Tick_%7C_1--Sec_%7C_1--Min-blue?style=flat-square)](#)
[![Depth](https://img.shields.io/badge/Depth-Level_2_(5_levels)-orange?style=flat-square)](#)

TickBytes provides high-fidelity, daily market data feeds for Indian equity indices, futures, and complete option chains recorded directly from raw exchange feeds throughout every trading session (09:15 AM to 03:30 PM IST).

---

## Daily Data Subscription — What Subscribers Get

We offer a **daily data feed subscription** to help cover high-performance cloud server, exchange WebSocket API, and storage infrastructure costs.

### **What Included in the Daily Subscription:**

1. **3-in-1 Daily Resolution Package:**
   * **Tick-by-Tick Feed:** Raw execution ticks + **Level 2 Market Depth** (Top-5 Bid/Ask order book) + Option Greeks.
   * **1-Second Snapshots:** High-frequency 1-second OHLCV snapshots for execution and slippage modeling.
   * **1-Minute Aggregated Bars:** 1-minute OHLCV bars + Volume + Open Interest (OI) + **All 16 Option Greeks** (1st, 2nd, 3rd order, and dual Greeks).

2. **Full Market Coverage (Every Single Trading Day):**
   * **6 Index Underlyings:** `NIFTY 50`, `BANKNIFTY`, `FINNIFTY`, `MIDCPNIFTY`, `BSE SENSEX`, and `BSE BANKEX`.
   * **All Instrument Segments:** Spot Index, Futures, and **Complete Option Chains** (Nearest 3 to 5 active expiries across all ITM, ATM, and deep OTM strikes).

3. **Daily Automated EOD Delivery:**
   * Compressed, high-efficiency `.parquet` files packaged in daily `.zip` archives.
   * Uploaded every afternoon post-market close (between 04:00 PM and 05:00 PM IST) directly to a **Private Subscriber Download Drive / Secure Feed**.
   * One-click download directly on desktop or mobile.

4. **Developer & Analytics Toolkit:**
   * Access to ready-to-use Python scripts for high-speed loading into **Pandas**, **Polars**, **DuckDB**, or **TimescaleDB/ClickHouse**.

---

### **How to Subscribe & Get Access:**

* **Direct Inquiries:** Send a Direct Message on Reddit to get access details.

---

## Dataset Coverage & Sample Matrix

Representative 50-row sample files are provided in the repository for all 6 indices across all 3 timeframes:

| Underlying | Asset Type | Exchange Segment | Sample Files (Tick / 1-Sec / 1-Min) |
|---|---|---|---|
| **NIFTY** | Spot Index, Futures & Option Chain | NSE / NFO | [Tick](samples/tick_data/NIFTY/NIFTY_SPOT.csv) \| [1-Sec](samples/1sec_data/NIFTY/NIFTY_SPOT.csv) \| [1-Min](samples/1min_data/NIFTY/NIFTY_OPT.csv) |
| **BANKNIFTY** | Spot Index, Futures & Option Chain | NSE / NFO | [Tick](samples/tick_data/BANKNIFTY/BANKNIFTY_SPOT.csv) \| [1-Sec](samples/1sec_data/BANKNIFTY/BANKNIFTY_SPOT.csv) \| [1-Min](samples/1min_data/BANKNIFTY/BANKNIFTY_SPOT.csv) |
| **FINNIFTY** | Spot Index, Futures & Option Chain | NSE / NFO | [Tick](samples/tick_data/FINNIFTY/FINNIFTY_SPOT.csv) \| [1-Sec](samples/1sec_data/FINNIFTY/FINNIFTY_SPOT.csv) \| [1-Min](samples/1min_data/FINNIFTY/FINNIFTY_SPOT.csv) |
| **MIDCPNIFTY** | Spot Index, Futures & Option Chain | NSE / NFO | [Tick](samples/tick_data/MIDCPNIFTY/MIDCPNIFTY_SPOT.csv) \| [1-Sec](samples/1sec_data/MIDCPNIFTY/MIDCPNIFTY_SPOT.csv) \| [1-Min](samples/1min_data/MIDCPNIFTY/MIDCPNIFTY_SPOT.csv) |
| **SENSEX** | Spot Index, Futures & Option Chain | BSE / BFO | [Tick](samples/tick_data/SENSEX/SENSEX_SPOT.csv) \| [1-Sec](samples/1sec_data/SENSEX/SENSEX_SPOT.csv) \| [1-Min](samples/1min_data/SENSEX/SENSEX_SPOT.csv) |
| **BANKEX** | Spot Index, Futures & Option Chain | BSE / BFO | [Tick](samples/tick_data/BANKEX/BANKEX_SPOT.csv) \| [1-Sec](samples/1sec_data/BANKEX/BANKEX_SPOT.csv) \| [1-Min](samples/1min_data/BANKEX/BANKEX_SPOT.csv) |

---

## Captured Data Fields & Greeks

* **Level 1 Fields:** Last Traded Price (LTP), Last Traded Quantity (LTQ), Traded Time (LTT), Volume, Open Interest (OI), Total Buy/Sell Quantity, Average Traded Price (ATP).
* **Level 2 Market Depth:** Top-5 Bid & Ask prices and quantities updated real-time per tick.
* **16 Option Greeks Included:**
  * **1st Order:** `delta`, `vega`, `theta`, `rho`
  * **2nd Order:** `gamma`, `vanna`, `charm`, `vomma`
  * **3rd Order:** `speed`, `zomma`, `color`, `veta`, `ultima`
  * **Dual Greeks:** `dual_delta`, `dual_gamma`
  * **Volatility:** `iv` (Implied Volatility)

---

## 📁 Repository Structure

```
tickbytes/
├── README.md                     # Repository Homepage
├── LICENSE                       # MIT License
├── CHANGELOG.md                  # Release Changelog
│
├── docs/
│   ├── README.md                 # Docs Index
│   ├── dataset_coverage.md       # Target Universe & Daily Specifications
│   ├── data_dictionary.md       # Data Column Definitions
│   ├── schema.md                 # SQL/DataFrame Schema Definitions
│   ├── naming_conventions.md     # Daily File Directory Layouts
│   └── examples/
│       ├── python.ipynb          # Interactive Jupyter Notebook
│       ├── pandas.py             # Basic Loading with Pandas
│       └── polars.py             # High-Performance Loading with Polars
│
└── samples/
    ├── tick_data/                # Tick-by-Tick Samples (NIFTY, BANKNIFTY, FINNIFTY, MIDCPNIFTY, SENSEX, BANKEX)
    │   └── <INDEX_SYMBOL>/       # Contains SPOT.csv, FUT.csv, OPT.csv
    ├── 1sec_data/                # 1-Second Resolution Samples (NIFTY, BANKNIFTY, FINNIFTY, MIDCPNIFTY, SENSEX, BANKEX)
    │   └── <INDEX_SYMBOL>/       # Contains SPOT.csv, FUT.csv, OPT.csv
    └── 1min_data/                # 1-Minute Aggregated Samples (NIFTY, BANKNIFTY, FINNIFTY, MIDCPNIFTY, SENSEX, BANKEX)
        └── <INDEX_SYMBOL>/       # Contains SPOT.csv, FUT.csv, OPT.csv
```

---

## Code & Analysis Examples

We provide ready-to-use Python scripts to load and analyze daily Parquet files:
* **Pandas Loader:** [`docs/examples/pandas.py`](docs/examples/pandas.py)
* **Polars High-Performance Loader:** [`docs/examples/polars.py`](docs/examples/polars.py)
* **Jupyter Notebook:** [`docs/examples/python.ipynb`](docs/examples/python.ipynb)
