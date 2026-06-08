---
name: Options Trading System — project state
description: Automated bull call spread system on Mag 7 stocks; strategy spec complete, backtesting next before build
type: project
originSessionId: dd93ed9c-37d7-4b2a-b77c-f58fdf262257
---
Samuel is building a deterministic options trading system to run autonomously. Full strategy spec saved at 10_Projects/Options Trading System/Strategy-Spec.md.

**Why:** Give a small portion of his portfolio ($2,000) to an automated system based on his existing manual bull call spread strategy on Mag 7 stocks.

**How to apply:** When resuming this project, load the spec file first -- it is the source of truth for all agreed rules. Do not re-derive rules from conversation.

**Current status (2026-06-08):** Strategy spec complete and locked. Next step is backtesting discussion before any build begins.

**Key decisions locked:**
- Instrument: bull call spread (debit spread), $5-10 wide
- Universe: Mag 7 only
- DTE: 14-21 at entry
- Max per trade: $650 ceiling, not default
- Max concurrent: 2 positions
- Entry: daily RSI(14) < 35 + lower Bollinger band + 200 EMA above and sloping up + 4hr confirmation
- IV rank filter: below 55 at entry
- Market regime: SPY above 200 EMA
- Take profit: trailing -- activates at 40%, exits if drops 10pp from peak, hard ceiling at 100%
- Stop loss: 50% of premium paid
- Time stop: 7 DTE
- Event stop: close at 2pm ET day before Fed/macro events
- Earnings blackout: 7 days pre-earnings, no entry or hold
- Orders: limit at midpoint for entries/TP; aggressive limit for stops; never market orders

**Open items:**
- Broker decision (Robinhood unofficial API vs. Tastytrade/Tradier official API)
- Backtesting methodology
- Data sources (IV rank, Greeks, earnings calendar, macro event calendar)
- Execution environment (local vs. cloud)
