Based on the structure of the book **"Options as a Strategic Investment"** (5th Edition), **Chapter 18** covers **Ratio Put Spreads**.

This chapter is the "mirror image" of Chapter 11 (Ratio Call Spreads). It applies the same logic—selling more options than you buy—to the **Put** side of the market.

Here is the detailed summary for **Chapter 18**, formatted in your "Samurai" style with the necessary Vega-Lite visualization code.

-----

# 🎯 Chapter 18: Ratio Put Spreads 📉⚖️

Welcome back, Strategist. In Chapter 11, we looked at the Ratio *Call* Spread for neutral-to-bullish markets. Now, we flip the board.

**Chapter 18** introduces the **Ratio Put Spread**. This strategy is for the trader who is **moderately bearish** but suspects the stock has a "floor" (support level) where it will stop falling. It is a strategy of precision: you profit if the stock drops, but you face **severe risk** if the stock crashes *too* hard.

-----

## <span style="color: #1565C0;">1. The Structure: The Bear's Trap</span>

The mechanics are the inverse of the Call Ratio. You generally Buy one higher-strike Put and Sell two (or more) lower-strike Puts.

### <span style="color: #6A1B9A;">The Setup (2:1 Ratio)</span>

| Action | Quantity | Option | Rationale |
| :--- | :--- | :--- | :--- |
| **Buy** (Long) | 1 | Higher Strike Put ($X_H$) | Usually At-the-Money or slightly Out-of-the-Money. |
| **Sell** (Short) | 2 | Lower Strike Put ($X_L$) | Out-of-the-Money. Finances the long put. |

**The Objective:** You want the stock to fall exactly to the lower strike price ($X_L$) at expiration.

### <span style="color: #6A1B9A;">The Credit vs. Debit Dilemma</span>

Unlike vertical spreads, the entry cost varies significantly:

1.  **Credit (Preferred):** If the premium from the 2 short puts covers the cost of the 1 long put, you have **no upside risk**. If the stock rallies, all puts expire worthless, and you keep the credit.
2.  **Debit:** If you pay a debit, you suffer a loss if the stock rallies (the puts expire worthless, and you lose your debit).

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 Samurai Mnemonic: "The Limit of the Fall"**
Think of the Short Strike ($X_L$) as a concrete floor. You want the stock to fall and hit the floor, but not smash through it into the basement.

</div>
</div>

-----

## <span style="color: #1565C0;">2. Profit & Loss Dynamics</span>

The risk profile is unique because it combines limited risk in one direction (up) with massive risk in the other (down).

  * **Upside (Stock Rises):**
      * If established for a **Credit**: You keep the credit (Profit).
      * If established for a **Debit**: You lose the debit (Loss).
  * **The Sweet Spot:** The stock closes exactly at the Short Strike ($X_L$). The long put has intrinsic value, and the short puts expire worthless.
  * **Downside (The Crash):** This is the danger zone. Below the lower strike, you are essentially **Naked Short** one put. As the stock drops toward zero, losses mount rapidly.

### <span style="color: #1565C0;">The Visual: The Inverse Tent</span>

The chart below visualizes a **2:1 Ratio Put Spread**.

  * **Scenario:** Stock at $50.
  * **Long:** 1 x 50 Put @ $3.00.
  * **Short:** 2 x 45 Puts @ $1.50.
  * **Net Cost:** $0.00 (Even Money).

<div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin: 10px 0;">
<pre data-lang="vega-lite">
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "Ratio Put Spread P/L Chart",
  "width": "container",
  "height": 300,
  "data": {
    "values": [
      {"Stock Price": 30, "P/L": -1000, "Label": "Unlimited Risk"},
      {"Stock Price": 35, "P/L": -500},
      {"Stock Price": 40, "P/L": 0, "Label": "Break-Even"},
      {"Stock Price": 45, "P/L": 500, "Label": "Max Profit"},
      {"Stock Price": 50, "P/L": 0},
      {"Stock Price": 55, "P/L": 0},
      {"Stock Price": 60, "P/L": 0}
    ]
  },
  "encoding": {
    "x": {
      "field": "Stock Price",
      "type": "quantitative",
      "title": "Stock Price at Expiration ($)",
      "axis": {"grid": true, "labelFontSize": 11, "titleFontSize": 12}
    },
    "y": {
      "field": "P/L",
      "type": "quantitative",
      "title": "Profit / Loss ($)",
      "axis": {"grid": true, "labelFontSize": 11, "titleFontSize": 12}
    }
  },
  "layer": [
    {
      "mark": {"type": "area", "color": "#94f0a6", "opacity": 0.3},
      "transform": [{"filter": "datum['P/L'] >= 0"}]
    },
    {
      "mark": {"type": "area", "color": "#ffc7ce", "opacity": 0.3},
      "transform": [{"filter": "datum['P/L'] <= 0"}]
    },
    {
      "mark": {"type": "rule", "color": "black"},
      "encoding": {"y": {"datum": 0}}
    },
    {
      "mark": {"type": "rule", "color": "gray", "strokeDash": [4, 4]},
      "encoding": {"x": {"datum": 40}}
    },
    {
      "mark": {"type": "line", "color": "#D32F2F", "strokeWidth": 3}
    },
    {
      "mark": {"type": "point", "filled": true, "size": 80},
      "encoding": {
        "color": {
          "condition": [
            {"test": "datum['P/L'] > 0", "value": "#2ca02c"},
            {"test": "datum['P/L'] < 0", "value": "#d62728"}
          ],
          "value": "gray"
        },
        "tooltip": [
          {"field": "Stock Price", "type": "quantitative", "title": "Stock Price"},
          {"field": "P/L", "type": "quantitative", "title": "Profit/Loss"}
        ]
      }
    },
    {
      "mark": {"type": "text", "dy": -15, "fontSize": 11, "fontWeight": "bold"},
      "encoding": {
        "text": {"field": "Label"},
        "color": {"value": "black"}
      },
      "transform": [{"filter": "datum.Label != null"}]
    }
  ],
  "config": {
    "view": {"stroke": null}
  }
}
</pre>
</div>

-----

## <span style="color: #1565C0;">3. Break-Even Analysis</span>

There are two potential break-even points, but usually only the downside one matters if you established the trade for a credit.

1.  **Upside Break-Even:** None (if Credit) or $X_H - Debit$ (if Debit).

2.  **Downside Break-Even ($BE_{down}$):** This is where the loss begins.
    $$BE_{down} = X_L - (\text{Max Profit} / \text{Number of Naked Puts})$$

    *In our example:*

      * Max Profit is at $45 ($50 - 45 = 5$ points profit).
      * We have 1 "extra" short put.
      * $BE_{down} = 45 - 5 = 40$.
      * **Risk:** If the stock falls below $40, you lose money point-for-point.

-----

## <span style="color: #1565C0;">Summary: The Samurai's Checklist ✅</span>

<div style="background-color: #E8F5E9; border-left: 5px solid #4CAF50; padding: 15px; margin: 20px 0;">

### 🥋 The Samurai's Scroll

  * **Strategy:** Ratio Put Spread.
  * **Market Outlook:** **Moderately Bearish**. You expect a decline, but not a crash.
  * **Risk Profile:** **Unlimited Downside Risk** (down to stock price of 0).
  * **The "Naked" Reality:** This strategy is functionally similar to a **Naked Put** written at the lower Break-Even point, but with a "profit kicker" in the middle.
  * **Golden Rule:** Do not use this on a stock that is prone to gaps down or bankruptcy rumors. You are standing in front of a freight train if the market crashes.

</div>

-----

**Would you like me to explain the "repair" strategies McMillan suggests if the stock drops through your short strikes?**