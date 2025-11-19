Greetings, Stock Options Samurai\! 🗡️

Your journey through spreads has prepared you for the next phase: mastering the defensive power of **Puts**. Chapter 9 shifts our focus entirely to strategies using Put options, which are the mirror image of the Call strategies you have just learned.

This chapter combines the concepts of directional spread betting (like Chapter 7/8) with the risk profile of the Ratio Write (Chapter 6), all using Puts\!

-----

## <span style="color: #1565C0;">Chapter 9: Put Spreads, Ratio Put Spreads, and Put Spread Combinations — The Defensive Mirror 🛡️</span>

### <span style="color: #1565C0;">🎯 Part 1: Bull Put Spreads (The "Credit" Play)</span>

The **Bull Put Spread** is one of the most popular strategies for income generation. It is used when you are **Bullish or Neutral** on a stock—you believe the price will *not fall* below a certain level.

It is often called a **Credit Spread** because you receive money (a credit) when you open the position.

#### <span style="color: #6A1B9A;">**The Structure (Selling Protection)**</span>

You create a Bull Put Spread by:

1.  **Selling (Writing)** a Put Option at a **Higher Striking Price** ($X_H$). This brings in premium.
2.  **Buying (Going Long)** a Put Option at a **Lower Striking Price** ($X_L$). This acts as the protective hedge.

Since the higher strike Put ($X_H$) is more expensive than the lower strike Put ($X_L$), you receive a **Net Credit** when the spread is established.

#### <span style="color: #6A1B9A;">**The Samurai’s Profit Metrics**</span>

| Metric | Formula | Mnemonic: **B.P.C. = Bullish, Profit Credit** |
| :--- | :--- | :--- |
| **Maximum Profit (Max Reward)** | **Net Credit** Received + Commissions | Max profit is the money you keep if the options expire worthless. |
| **Maximum Loss (Max Risk)** | $\text{Spread Width} - \text{Net Credit}$ | $\text{Loss} = (X_H - X_L) - \text{Net Credit}$ |
| **Break-Even Point (BEP)** | $X_H - \text{Net Credit}$ | $\text{BEP} = \text{Higher Strike} - \text{Credit}$ |

The goal is for the stock price to finish **above the higher strike ($X_H)$** so both options expire worthless, and you keep the **Net Credit**.

<div style="text-align: center; margin: 20px 0;">
<p style="font-weight: bold;">Bull Put Spread Profit Profile (Credit Received)</p>
<pre data-lang="vega-lite">
{
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "background": "#f9f9f9",
    "description": "Bull Put Spread profit profile (credit received) — example values",
    "data": {
        "values": [
            { "S": 80, "profit": -3 },
            { "S": 90, "profit": -3 },
            { "S": 95, "profit": -3 },
            { "S": 98, "profit": 0 },
            { "S": 100, "profit": 2 },
            { "S": 110, "profit": 2 },
            { "S": 120, "profit": 2 }
        ]
    },
    "width": "container",
    "height": 320,
    "encoding": {
        "x": { "field": "S", "type": "quantitative", "title": "Stock Price at Expiration ($)" },
        "y": { "field": "profit", "type": "quantitative", "title": "Profit ($)" },
        "tooltip": [
            { "field": "S", "type": "quantitative", "title": "Stock Price" },
            { "field": "profit", "type": "quantitative", "title": "Profit" }
        ]
    },
    "layer": [
        {
            "mark": { "type": "area", "color": "#94f0a6", "opacity": 0.2 },
            "transform": [ { "filter": "datum.profit >= 0" } ]
        },
        {
            "mark": { "type": "area", "color": "#ffc7ce", "opacity": 0.2 },
            "transform": [ { "filter": "datum.profit <= 0" } ]
        },
        {
            "mark": { "type": "rule", "color": "black" },
            "encoding": { "y": { "datum": 0 } }
        },
        {
            "mark": { "type": "line", "color": "#1f77b4" }
        },
        {
            "mark": { "type": "point", "filled": true, "size": 80 },
            "encoding": {
                "color": {
                    "condition": [
                        { "test": "datum.profit > 0", "value": "#2ca02c" },
                        { "test": "datum.profit < 0", "value": "#d62728" }
                    ],
                    "value": "gray"
                }
            }
        },
        {
            "mark": { "type": "rule", "color": "gray", "strokeDash": [ 4, 2 ] },
            "encoding": { "x": { "datum": 100 }, "opacity": { "value": 0.6 } }
        },
        {
            "mark": { "type": "rule", "color": "gray", "strokeDash": [ 4, 2 ] },
            "encoding": { "x": { "datum": 95 }, "opacity": { "value": 0.6 } }
        }
    ]
}
</pre>
*You receive the maximum profit (the credit) if the stock is above the higher strike at expiration.*
</div>

-----

### <span style="color: #1565C0;">🎯 Part 2: Ratio Put Spreads (The "Double-Barrel" Bear)</span>

Just as the Ratio Call Write (Chapter 6) combined covered and naked calls, the **Ratio Put Spread** combines a long put with one or more short puts. This is a higher-risk strategy used when you are **Neutral to Slightly Bearish** on a stock.

#### <span style="color: #6A1B9A;">**The Structure**</span>

The most common version is the **1x2 Ratio Put Spread**:

1.  **Buy (Go Long)** $\mathbf{1}$ Put Option at a **Higher Striking Price** ($X_H$)—this is your protection.
2.  **Sell (Go Short)** $\mathbf{2}$ Put Options at a **Lower Striking Price** ($X_L$)—this brings in premium.

<!-- end list -->

  * **Net Result:** This is often established for a **Net Credit** or near zero debit.

#### <span style="color: #6A1B9A;">**Risk/Reward Profile: Unlimited Downside Risk**</span>

This is the most critical point for a beginner:

  * **Max Profit:** Achieved if the stock lands **right on the lower short strike ($X_L)$** at expiration. This is where your one long put is fully ITM, and your two short puts expire worthless or expire right at the peak loss point for the short legs.
  * **Upside Break-Even:** The stock can rise indefinitely, and you will not lose money, as all puts expire worthless, and you keep the initial credit.
  * **Downside Risk: UNLIMITED.** If the stock price falls significantly *below* the lower short strike ($X_L$), the **naked short put** begins to lose money without limit (the loss equals the strike price minus the stock price).

**Mnemonic: R.P.U.**

  * **R**atio **P**ut = **U**nlimited Downside Risk.

<div style="text-align: center; margin: 20px 0;">
<p style="font-weight: bold;">Ratio Put Spread Profit Profile</p>
<pre data-lang="vega-lite">
{
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "background": "#f9f9f9",
    "description": "Ratio Put Spread (1x2) profit profile",
    "data": {
        "values": [
            { "S": 70, "profit": -18 },
            { "S": 80, "profit": -8 },
            { "S": 88, "profit": 0 },
            { "S": 90, "profit": 2 },
            { "S": 92, "profit": 0 },
            { "S": 100, "profit": -8 },
            { "S": 108, "profit": 0 },
            { "S": 110, "profit": 2 },
            { "S": 120, "profit": 2 }
        ]
    },
    "width": "container",
    "height": 320,
    "encoding": {
        "x": {
            "field": "S",
            "type": "quantitative",
            "title": "Stock Price at Expiration ($)"
        },
        "y": {
            "field": "profit",
            "type": "quantitative",
            "title": "Profit ($)"
        },
        "tooltip": [
            { "field": "S", "type": "quantitative", "title": "Stock Price" },
            { "field": "profit", "type": "quantitative", "title": "Profit" }
        ]
    },
    "layer": [
        {
            "mark": { "type": "area", "color": "#94f0a6", "opacity": 0.2 },
            "transform": [ { "filter": "datum.profit >= 0" } ]
        },
        {
            "mark": { "type": "area", "color": "#ffc7ce", "opacity": 0.2 },
            "transform": [ { "filter": "datum.profit <= 0" } ]
        },
        {
            "mark": { "type": "rule", "color": "black" },
            "encoding": { "y": { "datum": 0 } }
        },
        {
            "mark": { "type": "line", "color": "#1f77b4" }
        },
        {
            "mark": { "type": "point", "filled": true, "size": 80 },
            "encoding": {
                "color": {
                    "condition": [
                        { "test": "datum.profit > 0", "value": "#2ca02c" },
                        { "test": "datum.profit < 0", "value": "#d62728" }
                    ],
                    "value": "gray"
                }
            }
        },
        {
            "mark": { "type": "rule", "color": "gray", "strokeDash": [4, 2] },
            "encoding": { "x": { "datum": 90 }, "opacity": { "value": 0.6 } }
        },
        {
            "mark": { "type": "rule", "color": "gray", "strokeDash": [4, 2] },
            "encoding": { "x": { "datum": 100 }, "opacity": { "value": 0.6 } }
        }
    ],
    "config": {
        "view": {"stroke": null}
    }
}
</pre>
</div>

-----

### <span style="color: #1565C0;">🎯 Part 3: Put Spread Combinations</span>

Chapter 9 also explores ways to combine Put Spreads with other instruments to achieve specific goals, often involving portfolio risk management:

1.  **Adding a Stock Position (The Protective Hedge):**

      * **Goal:** To buy stock but offset the cost and protect against a downturn.
      * **Strategy:** Buy Stock + Buy Bear Put Spread. This is generally equivalent to selling a Bull Put Spread, but it's a way to actively manage an existing stock position.

<div style="text-align: center; margin: 20px 0;">
<p style="font-weight: bold;">Stock + Bear Put Spread Profit Profile</p>
<pre data-lang="vega-lite">
{
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "background": "#f9f9f9",
    "description": "Stock + Bear Put Spread profit profile",
    "data": {
        "values": [
            { "S": 80, "profit": -5 },
            { "S": 90, "profit": -5 },
            { "S": 95, "profit": -5 },
            { "S": 100, "profit": 0 },
            { "S": 105, "profit": 5 },
            { "S": 110, "profit": 10 },
            { "S": 120, "profit": 20 }
        ]
    },
    "width": "container",
    "height": 320,
    "encoding": {
        "x": {
            "field": "S",
            "type": "quantitative",
            "title": "Stock Price at Expiration ($)"
        },
        "y": {
            "field": "profit",
            "type": "quantitative",
            "title": "Profit ($)"
        },
        "tooltip": [
            { "field": "S", "type": "quantitative", "title": "Stock Price" },
            { "field": "profit", "type": "quantitative", "title": "Profit" }
        ]
    },
    "layer": [
        {
            "mark": { "type": "area", "color": "#94f0a6", "opacity": 0.2 },
            "transform": [ { "filter": "datum.profit >= 0" } ]
        },
        {
            "mark": { "type": "area", "color": "#ffc7ce", "opacity": 0.2 },
            "transform": [ { "filter": "datum.profit <= 0" } ]
        },
        {
            "mark": { "type": "rule", "color": "black" },
            "encoding": { "y": { "datum": 0 } }
        },
        {
            "mark": { "type": "line", "color": "#1f77b4" }
        },
        {
            "mark": { "type": "point", "filled": true, "size": 80 },
            "encoding": {
                "color": {
                    "condition": [
                        { "test": "datum.profit > 0", "value": "#2ca02c" },
                        { "test": "datum.profit < 0", "value": "#d62728" }
                    ],
                    "value": "gray"
                }
            }
        }
    ],
    "config": {
        "view": {"stroke": null}
    }
}
</pre>
</div>

2.  **Using Ratio Puts to Lower Cost of Stock Ownership:**

      * **Goal:** To lower the effective purchase price of stock.
      * **Strategy:** Buy Stock + Sell Ratio Put Spread (1x2). If the stock stays above $X_L$, you keep the credit, effectively lowering your cost basis.

<div style="text-align: center; margin: 20px 0;">
<p style="font-weight: bold;">Stock + Ratio Put Spread Profit Profile</p>
<pre data-lang="vega-lite">
{
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "background": "#f9f9f9",
    "description": "Stock + Ratio Put Spread profit profile",
    "data": {
        "values": [
            { "S": 70, "profit": -20 },
            { "S": 80, "profit": -10 },
            { "S": 90, "profit": 0 },
            { "S": 100, "profit": 10 },
            { "S": 110, "profit": 12 },
            { "S": 120, "profit": 22 }
        ]
    },
    "width": "container",
    "height": 320,
    "encoding": {
        "x": {
            "field": "S",
            "type": "quantitative",
            "title": "Stock Price at Expiration ($)"
        },
        "y": {
            "field": "profit",
            "type": "quantitative",
            "title": "Profit ($)"
        },
        "tooltip": [
            { "field": "S", "type": "quantitative", "title": "Stock Price" },
            { "field": "profit", "type": "quantitative", "title": "Profit" }
        ]
    },
    "layer": [
        {
            "mark": { "type": "area", "color": "#94f0a6", "opacity": 0.2 },
            "transform": [ { "filter": "datum.profit >= 0" } ]
        },
        {
            "mark": { "type": "area", "color": "#ffc7ce", "opacity": 0.2 },
            "transform": [ { "filter": "datum.profit <= 0" } ]
        },
        {
            "mark": { "type": "rule", "color": "black" },
            "encoding": { "y": { "datum": 0 } }
        },
        {
            "mark": { "type": "line", "color": "#1f77b4" }
        },
        {
            "mark": { "type": "point", "filled": true, "size": 80 },
            "encoding": {
                "color": {
                    "condition": [
                        { "test": "datum.profit > 0", "value": "#2ca02c" },
                        { "test": "datum.profit < 0", "value": "#d62728" }
                    ],
                    "value": "gray"
                }
            }
        }
    ],
    "config": {
        "view": {"stroke": null}
    }
}
</pre>
</div>

Mastering these put strategies gives you the flexibility to manage risk and generate income, whether you are betting on a subtle upward move (Bull Put) or attempting a complex, high-risk, high-reward bet on a price settling within a specific range (Ratio Put).