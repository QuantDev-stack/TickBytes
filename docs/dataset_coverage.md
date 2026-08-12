# Daily Dataset Coverage & Specifications

TickBytes records raw market data daily throughout the trading session for all major Indian equity indices and their F&O derivative segments. This document details our daily target universe, contract coverage, and resolution specifications.

---

## 1. Daily Universe & Covered Underlyings

We capture data daily across **3 Resolutions** (**Tick-by-Tick**, **1-Second**, and **1-Minute**) for **6 major underlyings** covering both NSE/NFO (National Stock Exchange) and BSE/BFO (Bombay Stock Exchange) segments:

| Index Name | Symbol | Exchange Segment | Expiries Tracked | Contracts Filter | Supported Resolutions |
|---|---|---|---|---|---|
| **Nifty 50** | `NIFTY` | NSE / NFO | Nearest 3-5 expiries | Complete Option Chain | Tick, 1-Sec, 1-Min |
| **Nifty Bank** | `BANKNIFTY` | NSE / NFO | Nearest 3-5 expiries | Complete Option Chain | Tick, 1-Sec, 1-Min |
| **Nifty Financial Services** | `FINNIFTY` | NSE / NFO | Nearest 3-5 expiries | Complete Option Chain | Tick, 1-Sec, 1-Min |
| **Nifty Midcap Select** | `MIDCPNIFTY` | NSE / NFO | Nearest 3-5 expiries | Complete Option Chain | Tick, 1-Sec, 1-Min |
| **BSE SENSEX** | `SENSEX` | BSE / BFO | Nearest 3-5 expiries | Complete Option Chain | Tick, 1-Sec, 1-Min |
| **BSE BANKEX** | `BANKEX` | BSE / BFO | Nearest 3-5 expiries | Complete Option Chain | Tick, 1-Sec, 1-Min |

---

## 2. Sample Files Grid (Organized by Timeframe ➔ Index ➔ Instrument)

Representative 50-row sample files are provided in the repository for all 6 indices across all 3 timeframes (Spot, Futures, Options):

### A. Tick-by-Tick Level 2 Samples (`samples/tick_data/`)
* **NIFTY:** [SPOT](samples/tick_data/NIFTY/NIFTY_SPOT.csv) \| [FUT](samples/tick_data/NIFTY/NIFTY_FUT.csv) \| [OPT](samples/tick_data/NIFTY/NIFTY_OPT.csv)
* **BANKNIFTY:** [SPOT](samples/tick_data/BANKNIFTY/BANKNIFTY_SPOT.csv) \| [FUT](samples/tick_data/BANKNIFTY/BANKNIFTY_FUT.csv) \| [OPT](samples/tick_data/BANKNIFTY/BANKNIFTY_OPT.csv)
* **FINNIFTY:** [SPOT](samples/tick_data/FINNIFTY/FINNIFTY_SPOT.csv) \| [FUT](samples/tick_data/FINNIFTY/FINNIFTY_FUT.csv) \| [OPT](samples/tick_data/FINNIFTY/FINNIFTY_OPT.csv)
* **MIDCPNIFTY:** [SPOT](samples/tick_data/MIDCPNIFTY/MIDCPNIFTY_SPOT.csv) \| [FUT](samples/tick_data/MIDCPNIFTY/MIDCPNIFTY_FUT.csv) \| [OPT](samples/tick_data/MIDCPNIFTY/MIDCPNIFTY_OPT.csv)
* **SENSEX:** [SPOT](samples/tick_data/SENSEX/SENSEX_SPOT.csv) \| [FUT](samples/tick_data/SENSEX/SENSEX_FUT.csv) \| [OPT](samples/tick_data/SENSEX/SENSEX_OPT.csv)
* **BANKEX:** [SPOT](samples/tick_data/BANKEX/BANKEX_SPOT.csv) \| [FUT](samples/tick_data/BANKEX/BANKEX_FUT.csv) \| [OPT](samples/tick_data/BANKEX/BANKEX_OPT.csv)

### B. 1-Second Resolution Snapshots (`samples/1sec_data/`)
* **NIFTY:** [SPOT](samples/1sec_data/NIFTY/NIFTY_SPOT.csv) \| [FUT](samples/1sec_data/NIFTY/NIFTY_FUT.csv) \| [OPT](samples/1sec_data/NIFTY/NIFTY_OPT.csv)
* **BANKNIFTY:** [SPOT](samples/1sec_data/BANKNIFTY/BANKNIFTY_SPOT.csv) \| [FUT](samples/1sec_data/BANKNIFTY/BANKNIFTY_FUT.csv) \| [OPT](samples/1sec_data/BANKNIFTY/BANKNIFTY_OPT.csv)
* **FINNIFTY:** [SPOT](samples/1sec_data/FINNIFTY/FINNIFTY_SPOT.csv) \| [FUT](samples/1sec_data/FINNIFTY/FINNIFTY_FUT.csv) \| [OPT](samples/1sec_data/FINNIFTY/FINNIFTY_OPT.csv)
* **MIDCPNIFTY:** [SPOT](samples/1sec_data/MIDCPNIFTY/MIDCPNIFTY_SPOT.csv) \| [FUT](samples/1sec_data/MIDCPNIFTY/MIDCPNIFTY_FUT.csv) \| [OPT](samples/1sec_data/MIDCPNIFTY/MIDCPNIFTY_OPT.csv)
* **SENSEX:** [SPOT](samples/1sec_data/SENSEX/SENSEX_SPOT.csv) \| [FUT](samples/1sec_data/SENSEX/SENSEX_FUT.csv) \| [OPT](samples/1sec_data/SENSEX/SENSEX_OPT.csv)
* **BANKEX:** [SPOT](samples/1sec_data/BANKEX/BANKEX_SPOT.csv) \| [FUT](samples/1sec_data/BANKEX/BANKEX_FUT.csv) \| [OPT](samples/1sec_data/BANKEX/BANKEX_OPT.csv)

### C. 1-Minute Aggregated Samples (`samples/1min_data/`)
* **NIFTY:** [SPOT](samples/1min_data/NIFTY/NIFTY_SPOT.csv) \| [FUT](samples/1min_data/NIFTY/NIFTY_FUT.csv) \| [OPT](samples/1min_data/NIFTY/NIFTY_OPT.csv)
* **BANKNIFTY:** [SPOT](samples/1min_data/BANKNIFTY/BANKNIFTY_SPOT.csv) \| [FUT](samples/1min_data/BANKNIFTY/BANKNIFTY_FUT.csv) \| [OPT](samples/1min_data/BANKNIFTY/BANKNIFTY_OPT.csv)
* **FINNIFTY:** [SPOT](samples/1min_data/FINNIFTY/FINNIFTY_SPOT.csv) \| [FUT](samples/1min_data/FINNIFTY/FINNIFTY_FUT.csv) \| [OPT](samples/1min_data/FINNIFTY/FINNIFTY_OPT.csv)
* **MIDCPNIFTY:** [SPOT](samples/1min_data/MIDCPNIFTY/MIDCPNIFTY_SPOT.csv) \| [FUT](samples/1min_data/MIDCPNIFTY/MIDCPNIFTY_FUT.csv) \| [OPT](samples/1min_data/MIDCPNIFTY/MIDCPNIFTY_OPT.csv)
* **SENSEX:** [SPOT](samples/1min_data/SENSEX/SENSEX_SPOT.csv) \| [FUT](samples/1min_data/SENSEX/SENSEX_FUT.csv) \| [OPT](samples/1min_data/SENSEX/SENSEX_OPT.csv)
* **BANKEX:** [SPOT](samples/1min_data/BANKEX/BANKEX_SPOT.csv) \| [FUT](samples/1min_data/BANKEX/BANKEX_FUT.csv) \| [OPT](samples/1min_data/BANKEX/BANKEX_OPT.csv)

---

## 3. Daily Contract Selection Strategy

To ensure zero missing data during trading hours:
1. **Active Expiries:** The nearest **3 to 5 weekly or monthly expiries** are subscribed to at the start of each session.
2. **Option Chain Coverage:** We capture the **complete option chain** for each active expiry (deep ITM, ATM, and deep OTM). No strike boundary limits are applied.
3. **Daily EOD Processing:** At market close (03:30 PM IST), raw tick data and aggregated bars are compiled into compressed Parquet files and uploaded to subscribers.
