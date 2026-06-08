# Options Trading System -- Strategy Spec
Last updated: 2026-06-08

---

## Overview

- **Instrument**: Bull call spread (debit spread)
- **Universe**: Dynamic top 10 by market cap, rebalanced monthly. BRK.A and BRK.B permanently excluded (options behave unusually). In 2015 this included energy/financial names; by 2025 it converges toward today's Mag 7.
- **Expiration target**: 14-21 DTE at entry
- **Total allocated capital**: $2,000
- **Max risk per trade**: $650 (not a default -- a ceiling)
- **Max concurrent positions**: 2

---

## Entry Conditions

All conditions must be true simultaneously before the system considers a trade.

### Daily chart (signal layer)
1. Price is above the 200 EMA
2. The 200 EMA slope is positive (pointing upward, not flat or declining)
3. RSI(14) is below 35
4. Price is at or below the lower Bollinger Band (20-period, 2 standard deviations)

### 4-hour chart (timing layer)
5. Price is stabilizing or showing early signs of a bounce -- confirms the daily signal before entry is placed

### Filters (all must pass)
6. IV rank is below 55
7. SPY is above its own 200 EMA
8. The underlying is NOT within 7 days of its earnings date
9. Today is NOT a Fed rate decision day, major macro event day, or the day before either

---

## Strike Selection

- Long call delta: 35-45
- Spread width: $5-10 wide
- R:R filter: net premium paid must be less than 50% of spread width (max profit >= max loss)

---

## Exit Rules

### Take profit (trailing)
- Mechanism activates when the position reaches 40% of max profit
- Once active: exit if profit drops 10 percentage points below the highest point reached
- Hard ceiling: exit immediately at 100% of max profit

### Stop loss
- Exit if the position loses 50% of premium paid
- Uses aggressive limit orders (execution speed priority over price)

### Time stop
- Auto-close any position at 7 DTE regardless of P&L

### Event stop
- Close any open position at 2pm ET on the day before a Fed rate decision or major macro event

### Earnings stop
- Any open position that enters a 7-day pre-earnings window is closed immediately

---

## Order Execution

- **Entries**: limit order at bid-ask midpoint; if no fill after 2 minutes, adjust toward market and retry
- **Take profit**: limit order at bid-ask midpoint; same retry logic
- **Stop loss**: aggressive limit order near the bid -- speed over precision
- **Market orders**: never used for entries or take profit

---

## Risk Management

- Max 2 concurrent positions at any time
- Max 1 position per underlying at any time
- No new bullish spreads when SPY is below its 200 EMA
- No entries within 7 days of earnings
- No entries on or the day before scheduled Fed/macro events
- Max loss on any single trade is the full premium paid (gap risk acknowledged)

---

## Broker

- Current: Robinhood via unofficial API (robin_stocks) -- ToS risk acknowledged, low probability of suspension at this trade frequency
- Recommended alternative: Tastytrade or Tradier (both have official APIs, built for options)
- Decision deferred -- to be resolved before build begins

---

## Open Items (to address before build)

- [ ] Backtesting methodology and historical validation
- [ ] Broker decision (Robinhood vs. Tastytrade vs. Tradier)
- [ ] Specific strike selection logic (how the system picks exact strikes within the delta/width rules)
- [ ] Data source for IV rank, Greeks, earnings dates, macro event calendar
- [ ] Execution environment (local script vs. cloud hosted)
