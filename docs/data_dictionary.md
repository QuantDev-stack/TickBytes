# Data Dictionary

This document details the definition and purpose of each column present in the TickBytes daily files.

---

## 📌 Common / Core Fields

These columns are present across almost all tick datasets:

| Column Name | Description |
|---|---|
| `datetime` | High-precision tick timestamp in local time (`YYYY-MM-DD HH:MM:SS.mmm`). |
| `name` | The underlying asset index name (e.g. `NIFTY`, `BANKNIFTY`, `BANKEX`). |
| `symbol` | The exact trading contract symbol (e.g. `NIFTY FUT 25 AUG 26`, `BANKEX 66000 CE 27 AUG 26`). For spot index, this matches the underlying index name. |
| `type` | Asset instrument type: `INDEX` (Spot), `FUT` (Futures), or `CE`/`PE` (Options). |
| `segment` | Exchange segment: `INDICES`, `NFO-FUT` (NSE Futures), `NFO-OPT` (NSE Options), `BFO-FUT` (BSE Futures), `BFO-OPT` (BSE Options). |
| `ltp` | Last Traded Price at the moment of the tick. |
| `ltt` | Last Traded Time (epoch milliseconds). |
| `ltq` | Last Traded Quantity (tick volume). |
| `volume` | Cumulative daily volume traded up to the current tick. |
| `open` | Daily Opening Price. |
| `high` | Daily High Price up to the current tick. |
| `low` | Daily Low Price up to the current tick. |
| `close` | Daily Closing Price (or previous close before market open). |
| `cp` | Close Price (previous day's closing price). |

---

## F&O Specific Fields

These columns are specific to derivative contracts (Futures & Options):

| Column Name | Description |
|---|---|
| `oi` | Daily Open Interest (cumulative active contract count) at the current tick. |
| `expiry` | Contract expiry date (`YYYY-MM-DD`). |
| `strike` | Options strike price (set to `0.0` or null for Spot/Futures). |
| `atp` | Average Traded Price (cumulative volume-weighted price of the day). |
| `tbq` | Total Buy Quantity (aggregate order book buy depth volume). |
| `tsq` | Total Sell Quantity (aggregate order book sell depth volume). |
| `vtt` | Total Traded Volume (raw transaction count / volume metric). |
| `ohlc_vol` | Resampling helper volume metric. |
| `ohlc_ts` | Resampling helper timestamp (epoch ms). |

---

## Level 2 Market Depth Fields

These columns represent the top 5 levels of the limit order book, updated at each tick. They are present in the **Futures** and **Options** tick feeds:

| Column Name | Description |
|---|---|
| `bid_px` / `bid_qty` | Best bid (buy) price and quantity (Level 1). |
| `ask_px` / `ask_qty` | Best ask (sell) price and quantity (Level 1). |
| `bid_px_2` / `bid_qty_2` | Second level bid price and quantity (Level 2). |
| `ask_px_2` / `ask_qty_2` | Second level ask price and quantity (Level 2). |
| `bid_px_3` / `bid_qty_3` | Third level bid price and quantity (Level 3). |
| `ask_px_3` / `ask_qty_3` | Third level ask price and quantity (Level 3). |
| `bid_px_4` / `bid_qty_4` | Fourth level bid price and quantity (Level 4). |
| `ask_px_4` / `ask_qty_4` | Fourth level ask price and quantity (Level 4). |
| `bid_px_5` / `bid_qty_5` | Fifth level bid price and quantity (Level 5). |
| `ask_px_5` / `ask_qty_5` | Fifth level ask price and quantity (Level 5). |

---

## Options Greeks Fields (16 Complete Greeks)

Captured and calculated options Greeks present in option contract feeds:

| Column Name | Order Category | Description |
|---|---|---|
| `iv` | Volatility | Implied Volatility (annualized, as a decimal). |
| `delta` | 1st Order | Sensitivity of option price to underlying index change. |
| `vega` | 1st Order | Option price sensitivity to a 1% change in Implied Volatility. |
| `theta` | 1st Order | Rate of option price decay per day. |
| `rho` | 1st Order | Option price sensitivity to interest rate changes. |
| `gamma` | 2nd Order | Rate of change of Delta per index point change. |
| `vanna` | 2nd Order | Sensitivity of Delta with respect to Implied Volatility (dDelta / dVol). |
| `charm` | 2nd Order | Delta decay over time (dDelta / dTime). |
| `vomma` | 2nd Order | Volatility convexity — rate of change of Vega with respect to IV (dVega / dVol). |
| `speed` | 3rd Order | Rate of change of Gamma with respect to underlying price (dGamma / dSpot). |
| `zomma` | 3rd Order | Rate of change of Gamma with respect to Implied Volatility (dGamma / dVol). |
| `color` | 3rd Order | Gamma decay over time (dGamma / dTime). |
| `veta` | 3rd Order | Vega decay over time (dVega / dTime). |
| `ultima` | 3rd Order | Sensitivity of Vomma with respect to Implied Volatility (dVomma / dVol). |
| `dual_delta` | Dual Greek | Sensitivity of option price to changes in strike price. |
| `dual_gamma` | Dual Greek | Rate of change of Dual Delta with respect to strike price. |
