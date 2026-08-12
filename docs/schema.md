# Technical Schema Specifications

This specification details column datatypes, indexing fields, and nullability constraints for programmatic loading.

---

## Spot Index Schema

| Column Name | Pandas Dtype | Polars Dtype | Nullable | Notes |
|---|---|---|---|---|
| `datetime` | `datetime64[ns]` | `Datetime` | No | Tick timestamp |
| `name` | `object` (string) | `String` | No | Index name (e.g. `NIFTY`) |
| `open` | `float64` | `Float64` | No | Daily Open |
| `high` | `float64` | `Float64` | No | Daily High |
| `low` | `float64` | `Float64` | No | Daily Low |
| `close` | `float64` | `Float64` | No | Daily Close |
| `volume` | `int64` | `Int64` | No | Usually `0` for spot indices |
| `type` | `object` | `String` | No | Set to `"INDEX"` |
| `symbol` | `object` | `String` | No | Match index name |
| `ltp` | `float64` | `Float64` | No | Last Traded Price |
| `ltt` | `int64` | `Int64` | No | Epoch milliseconds |
| `ltq` | `int64` | `Int64` | No | Set to `0` for index |
| `cp` | `float64` | `Float64` | No | Previous close |
| `segment` | `object` | `String` | No | Set to `"INDICES"` |

---

## Futures & Options Schema (with Level 2 & Greeks)

| Column Name | Pandas Dtype | Polars Dtype | Nullable | Notes |
|---|---|---|---|---|
| `datetime` | `datetime64[ns]` | `Datetime` | No | Tick timestamp |
| `name` | `object` | `String` | No | Underlying name |
| `symbol` | `object` | `String` | No | Trading Symbol |
| `type` | `object` | `String` | No | `"FUT"`, `"CE"`, or `"PE"` |
| `expiry` | `object` (string) | `String` | No | Expiry date (`YYYY-MM-DD`) |
| `strike` | `float64` | `Float64` | Yes | Strike price (set to `0.0` for FUT) |
| `ltp` | `float64` | `Float64` | No | Last Traded Price |
| `ltq` | `int64` | `Int64` | No | Last Traded Quantity |
| `volume` | `int64` | `Int64` | No | Cumulative volume |
| `oi` | `int64` | `Int64` | No | Open Interest |
| `atp` | `float64` | `Float64` | No | Average Traded Price |
| `iv` | `float64` | `Float64` | Yes | Option Greek (null for FUT) |
| `delta` | `float64` | `Float64` | Yes | Option Greek (null for FUT) |
| `gamma` | `float64` | `Float64` | Yes | Option Greek (null for FUT) |
| `theta` | `float64` | `Float64` | Yes | Option Greek (null for FUT) |
| `vega` | `float64` | `Float64` | Yes | Option Greek (null for FUT) |
| `rho` | `float64` | `Float64` | Yes | Option Greek (null for FUT) |
| `bid_px` / `bid_qty` | `float64` / `int64` | `Float64` / `Int64` | Yes | Bid Level 1 |
| `ask_px` / `ask_qty` | `float64` / `int64` | `Float64` / `Int64` | Yes | Ask Level 1 |
| `bid_px_2..5` / `bid_qty_2..5` | `float64` / `int64` | `Float64` / `Int64` | Yes | Bid Levels 2 to 5 |
| `ask_px_2..5` / `ask_qty_2..5` | `float64` / `int64` | `Float64` / `Int64` | Yes | Ask Levels 2 to 5 |
