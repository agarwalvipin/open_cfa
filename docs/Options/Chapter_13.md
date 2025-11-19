That is a fair critique. While the Butterfly (Chapter 10) is about precision and stillness, Chapter 13 introduces the chaos-loving strategies. These are trades for when you expect the market to explode, but you aren't sure which way—or when you want to be "Paid to Play."

The most visually critical strategy here is the **Backspread**, which has a unique "Checkmark" or "Valley" profit profile.

Here is the detailed summary for **Chapter 13**, complete with the requested diagram.

# 🎯 Chapter 13: Reverse Spreads 💥

Greetings, Volatility Hunter. While most spread traders try to sell premium and hope the market stays quiet, the **Reverse Spreader** prays for chaos.

This chapter covers two primary strategies: the **Reverse Calendar Spread** and the **Reverse Ratio Spread (Backspread)**. Both are designed to profit from **instability** and **volatility**.

-----

## <span style="color: #1565C0;">1. The Reverse Calendar Spread</span>

In a standard Calendar Spread, you sell the near-term and buy the long-term (hoping for stability). Here, you flip the script.

### <span style="color: #6A1B9A;">The Structure</span>

  * **Sell** (Short) 1 **Long-Term** Call.
  * **Buy** (Long) 1 **Near-Term** Call (same strike).

### <span style="color: #6A1B9A;">The Logic</span>

This is a specialized trade that profits if:

1.  **The Stock Moves Big:** If the stock flies away from the strike price in *either* direction, the near-term option you bought tracks the move, while the long-term option you sold (which has less Gamma) lags behind or loses value.
2.  **Implied Volatility (IV) Collapses:** Since you are Net Short Vega (you sold the expensive long-term option), you profit if IV crashes.

**Risk:** The stock stays exactly at the strike price. The near-term option you bought rots away to zero, while the long-term option you sold retains its value. This is the "Valley of Death."

-----

## <span style="color: #1565C0;">2. The Backspread (Reverse Ratio Spread)</span>

This is the star of the chapter. A **Backspread** involves selling a call at a lower strike and buying **more** calls at a higher strike.

### <span style="color: #6A1B9A;">The Structure (2:1 Call Backspread)</span>

| Action | Quantity | Option | Rationale |
| :--- | :--- | :--- | :--- |
| **Sell** (Short) | 1 | Lower Strike Call ($X_L$) | Finances the trade. |
| **Buy** (Long) | 2 | Higher Strike Call ($X_H$) | Provides unlimited upside potential. |

### <span style="color: #6A1B9A;">The "Paid to Play" Dynamic</span>

Because you are selling a valuable In-the-Money or At-the-Money option to buy cheap Out-of-the-Money options, this trade is often done for a **Net Credit**.

  * **Scenario A (Stock Crashes):** Good\! All calls expire worthless. You keep the initial **Net Credit** as profit.
  * **Scenario B (Stock Rockets):** Great\! You are Long 2 calls and Short 1. You have net long exposure. Your profit is **Unlimited**.
  * **Scenario C (The Trap):** The stock grinds slowly higher and settles exactly at your long strike ($X_H$). This is your **Maximum Loss**.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 Samurai Mnemonic: "The Valley of Death"**
Picture the profit graph as a valley. You are safe on the high ground to the left (bearish profit) and safe on the mountain peak to the right (bullish profit). Do not get caught camping in the valley (the difference between the strikes) at expiration.

</div>
</div>

-----

## <span style="color: #1565C0;">3. Profit and Risk Diagram: The "Checkmark"</span>

The Backspread has one of the most distinctive P/L curves in options trading. It creates a "V" or checkmark shape.

<div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin: 10px 0;">
<pre data-lang="vega-lite">
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "background": "#f9f9f9",
  "title": "Profit/Loss Diagram: Call Backspread (2:1)",
  "description": "Sell 1 Call @ 100 ($6.00), Buy 2 Calls @ 110 ($2.50 ea). Net Credit $1.00.",
  "width": "container",
  "height": 300,
  "data": {
    "values": [
      {"Stock Price": 80, "P/L": 1.0},
      {"Stock Price": 90, "P/L": 1.0},
      {"Stock Price": 100, "P/L": 1.0},
      {"Stock Price": 105, "P/L": -4.0},
      {"Stock Price": 110, "P/L": -9.0},
      {"Stock Price": 115, "P/L": -4.0},
      {"Stock Price": 119, "P/L": 0.0},
      {"Stock Price": 125, "P/L": 6.0},
      {"Stock Price": 130, "P/L": 11.0}
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
      "title": "Profit / Loss ($100s)",
      "axis": {"grid": true, "labelFontSize": 11, "titleFontSize": 12}
    }
  },
  "layer": [
    {
      "mark": {"type": "area", "color": "#94f0a6", "opacity": 0.2},
      "transform": [{"filter": "datum['P/L'] >= 0"}]
    },
    {
      "mark": {"type": "area", "color": "#ffc7ce", "opacity": 0.2},
      "transform": [{"filter": "datum['P/L'] <= 0"}]
    },
    {
      "mark": {"type": "rule", "color": "black"},
      "encoding": {"y": {"datum": 0}}
    },
    {
      "mark": {"type": "line", "color": "#D81B60"}
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
          {"field": "P/L", "type": "quantitative", "title": "Profit/Loss ($100s)"}
        ]
      }
    },
    {
      "mark": {"type": "text", "align": "right", "dx": -5, "dy": -5, "text": "Safe Zone - Keep Credit"},
      "encoding": {"x": {"datum": 95}, "y": {"datum": 1}}
    },
    {
      "mark": {"type": "text", "align": "center", "dy": 10, "text": "Max Loss Zone"},
      "encoding": {"x": {"datum": 110}, "y": {"datum": -9}}
    }
  ],
  "config": {
    "view": {"stroke": null}
  }
}
</pre>
</div>

*The Call Backspread shows the distinctive "V" or checkmark profit curve - safe on the left (keep credit if stock drops), maximum loss at the long strike ($110), and unlimited profit on the right (if stock rallies hard).*

**Key Takeaways from the Chart:**

  * **The Left Flank (Bearish):** If the stock drops, your long calls die, but your short call also dies. You keep the **Net Credit** ($1.00 in the example).
  * **The Valley (Neutral/Slight Bull):** If the stock rises to 110, you lose on the short call ($100 strike) but haven't made money on the long calls ($110 strike) yet. This is the max loss point.
  * **The Right Flank (Bullish):** Once the stock passes the upper breakeven, your 2 Long Calls overpower the 1 Short Call, leading to **Unlimited Profit**.

-----

## <span style="color: #1565C0;">Summary: The Samurai's Checklist ✅</span>

<div style="background-color: #E8F5E9; border-left: 5px solid #4CAF50; padding: 15px; margin: 20px 0;">

### 🥋 The Samurai's Scroll

  * **Strategy:** Call Backspread (Reverse Ratio).
  * **Outlook:** **Volatile / Bullish**. You want a massive move up, but you are hedged if the market crashes.
  * **Worst Case:** The market grinds slowly up to your long strike ($X_H$) and stops.
  * **Best Case:** The market explodes to the upside (Unlimited Profit) OR collapses completely (Profit = Net Credit).
  * **The "Free" Trade:** Ideally, enter for a **Credit**. If you pay a debit, you lose the "safety net" on the downside.

</div>