# Naming Conventions & Partition Layouts

This document outlines contract symbology naming rules and storage layout conventions across our datasets.

---

## 1. Instrument Symbology Conventions

We preserve standard contract naming rules returned by the exchange and Upstox API:

1. **Spot Index Symbol:**
   - Represented as an upper-case index name matching the underlying index.
   - Examples: `NIFTY`, `BANKNIFTY`, `FINNIFTY`, `MIDCPNIFTY`, `SENSEX`, `BANKEX`.

2. **Futures Symbol Format:**
   - Format: `<UNDERLYING> FUT <DD> <MMM> <YY>`
   - Examples:
     * `NIFTY FUT 25 AUG 26` (Nifty futures expiring on August 25, 2026)
     * `BANKEX FUT 27 AUG 26` (BANKEX futures expiring on August 27, 2026)

3. **Options Symbol Format:**
   - Format: `<UNDERLYING> <STRIKE> <CE/PE> <DD> <MMM> <YY>`
   - Examples:
     * `NIFTY 25500 CE 25 AUG 26` (Nifty 25500 Call Option expiring on August 25, 2026)
     * `SENSEX 80300 CE 13 AUG 26` (SENSEX 80300 Call Option expiring on August 13, 2026)

---

## 2. Sample Directory Structure & File Hierarchy

Sample files in the repository are organized into a clean, hierarchical structure:

```
tickbytes/samples/
├── <TIMEFRAME>/                       # tick_data | 1sec_data | 1min_data
│   └── <INDEX_SYMBOL>/                # NIFTY | BANKNIFTY | FINNIFTY | MIDCPNIFTY | SENSEX | BANKEX
│       ├── <INDEX_SYMBOL>_SPOT.csv    # Spot Index Sample
│       ├── <INDEX_SYMBOL>_FUT.csv     # Futures Contract Sample
│       └── <INDEX_SYMBOL>_OPT.csv     # Options Contract Sample
```

---

## 3. Daily Production Partition Layout

Production daily dataset exports are organized across date-partitioned Parquet archives structured as follows:

```
DATASETS/
├── tick_data/                         # Tick-by-Tick Level 2 Dataset (Level 2 Depth & Greeks)
│   └── <SYMBOL>/<YYYY-MM-DD>/
│       ├── <SYMBOL>_SPOT_TICK_DATA_<YYYY-MM-DD>.parquet
│       ├── <SYMBOL>_FUTURES_TICK_DATA_<YYYY-MM-DD>.parquet
│       └── <SYMBOL>_OPTIONS_TICK_DATA_<YYYY-MM-DD>.parquet
│
├── 1sec_data/                         # 1-Second Resolution Dataset
│   └── <SYMBOL>/<YYYY-MM-DD>/
│       └── <SYMBOL>_TICK_DATA_<YYYY-MM-DD>.parquet
│
└── 1min_data/                         # 1-Minute Aggregated Dataset (OHLCV + Volume + OI + Greeks)
    └── <SYMBOL>/<YYYY-MM-DD>/
        ├── SPOT/<SYMBOL>_<YYYY-MM-DD>_SPOT.parquet
        ├── FUTURES/<SYMBOL>_<YYYY-MM-DD>_FUT.parquet
        └── OPTIONS/<SYMBOL>_<YYYY-MM-DD>_OPT.parquet
```
