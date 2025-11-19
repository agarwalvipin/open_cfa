This is the final chapter of **Part II: Call Option Strategies**. You have now explored every dimension of Call buying and selling.

Chapter 14 teaches you how to "diagonalize" a spread. By mixing different expiration months (Time) with different strike prices (Price), you create a strategy that is less rigid than a vertical spread and offers unique follow-up opportunities.

Here is the detailed summary for **Chapter 14**, complete with the visual profit profile.

# 🎯 Chapter 14: Diagonalizing a Spread 📅📉

In a standard **Vertical Spread**, both options expire in the same month. In a **Diagonal Spread**, you stagger the expirations.

Typically, you will **Buy the Long-Term** option and **Sell the Short-Term** option. This allows you to take advantage of the faster time decay ($\Theta$) of the near-term option while holding a core position for the longer term.

-----

## <span style="color: #1565C0;">1. The Diagonal Bull Spread</span>

A standard Bull Spread involves buying the lower strike and selling the higher strike (same month). A **Diagonal Bull Spread** does the same, but pushes the Long Call further out in time.

### <span style="color: #6A1B9A;">The Structure</span>

| Action | Strike Price | Expiration | Rationale |
| :--- | :--- | :--- | :--- |
| **Buy** (Long) | Lower Strike ($X_L$) | **Distant Month** | The "Core" bullish position. Decays slowly. |
| **Sell** (Short) | Higher Strike ($X_H$) | **Near Month** | Generates income. Decays rapidly. |

**Example:** Stock XYZ at 32.

  * **Vertical:** Long **April** 30 Call / Short **April** 35 Call. (Debit: $2.00$)
  * **Diagonal:** Long **July** 30 Call / Short **April** 35 Call. (Debit: $3.00$)

### <span style="color: #6A1B9A;">The Trade-Off</span>

  * **Cost:** The Diagonal costs more (higher debit) because the Long-Term option has more time value.
  * **Benefit:** If the stock stays flat or drops slightly, the Near-Term short option expires worthless, and you *still own* the Long-Term call. You can then sell another call against it (e.g., May 35), reducing your cost further.
  * **Risk:** If the stock rockets up immediately, your profit is slightly lower than the Vertical Spread because the Long-Term call gains delta slower than the Near-Term call loses it (due to Gamma).

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 Samurai Mnemonic: "The Reusable Rocket"**
In a Vertical Spread, the rocket flies once and is done. In a Diagonal Spread, if the launch is delayed (stock stays flat), the booster (short option) falls off, but the rocket (long option) is still on the pad, ready to be fitted with a new booster (selling the next month).

</div>
</div>

-----

## <span style="color: #1565C0;">2. Profit Profile: The "Soft Cap"</span>

At the near-term expiration, the profit curve of a Diagonal Bull Spread is smoother than a Vertical Spread. It doesn't have a hard "shelf" because the Long Call still has time value.

However, if the stock rises too far, the spread behaves like a vertical spread, and profits flatten out.

<div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin: 10px 0;">
<pre data-lang="vega-lite">
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "background": "#f9f9f9",
  "title": "P/L Diagram: Diagonal Bull Spread vs Vertical Bull Spread (at Near-Term Expiration)",
  "description": "Diagonal: Long July 30, Short April 35. Vertical: Long April 30, Short April 35.",
  "width": "container",
  "height": 300,
  "data": {
    "values": [
      {"Stock Price": 20, "P/L": -3.0, "Type": "Diagonal Spread"},
      {"Stock Price": 25, "P/L": -2.5, "Type": "Diagonal Spread"},
      {"Stock Price": 30, "P/L": -1.0, "Type": "Diagonal Spread"},
      {"Stock Price": 32, "P/L": 0.0, "Type": "Diagonal Spread"},
      {"Stock Price": 35, "P/L": 2.5, "Type": "Diagonal Spread"},
      {"Stock Price": 40, "P/L": 2.0, "Type": "Diagonal Spread"},
      {"Stock Price": 45, "P/L": 2.0, "Type": "Diagonal Spread"},
      {"Stock Price": 20, "P/L": -2.0, "Type": "Vertical Spread"},
      {"Stock Price": 30, "P/L": -2.0, "Type": "Vertical Spread"},
      {"Stock Price": 35, "P/L": 3.0, "Type": "Vertical Spread"},
      {"Stock Price": 45, "P/L": 3.0, "Type": "Vertical Spread"}
    ]
  },
  "encoding": {
    "x": {
      "field": "Stock Price",
      "type": "quantitative",
      "title": "Stock Price at April Expiration ($)",
      "axis": {"grid": true, "labelFontSize": 11, "titleFontSize": 12}
    },
    "y": {
      "field": "P/L",
      "type": "quantitative",
      "title": "Profit / Loss ($100s)",
      "axis": {"grid": true, "labelFontSize": 11, "titleFontSize": 12}
    },
    "color": {
      "field": "Type",
      "type": "nominal",
      "scale": {
        "domain": ["Diagonal Spread", "Vertical Spread"],
        "range": ["#1f77b4", "#ff7f0e"]
      },
      "legend": {"title": "Strategy Type"}
    }
  },
  "layer": [
    {
      "mark": {"type": "rule", "color": "black", "strokeWidth": 1},
      "encoding": {"y": {"datum": 0}}
    },
    {
      "mark": {"type": "line", "strokeWidth": 3}
    },
    {
      "mark": {"type": "point", "filled": true, "size": 80},
      "encoding": {
        "tooltip": [
          {"field": "Stock Price", "type": "quantitative", "title": "Stock Price"},
          {"field": "P/L", "type": "quantitative", "title": "Profit/Loss ($100s)"},
          {"field": "Type", "type": "nominal", "title": "Strategy"}
        ]
      }
    }
  ],
  "config": {
    "view": {"stroke": null}
  }
}
</pre>
</div>

*Notice how the **Diagonal Spread (Blue)** has a lower max profit if the stock shoots up (due to the higher debit paid), but it retains value better on the downside (around $30) because the July call holds its premium. The **Vertical Spread (Orange)** has a hard "shelf" at the strikes.*
</div>

-----

## <span style="color: #1565C0;">3. Advanced Tactics: "Free" Calls and Backspreads</span>

### <span style="color: #6A1B9A;">Owning a Call for "Free" (The Diagonal Bear)</span>

This strategy flips the script. You sell a **Near-Term, Lower Strike** (expensive) and buy a **Long-Term, Higher Strike** (cheaper).

  * **Goal:** If the stock drops, the expensive Near-Term call expires worthless. You keep the premium. If that premium > cost of the Long-Term call, you now own the Long-Term call for **zero net cost** (or a credit\!).
  * **Result:** A "Free Look" at the upside later in the year.

### <span style="color: #6A1B9A;">The Diagonal Backspread</span>

  * **Action:** Sell 1 Near-Term Lower Strike / Buy 2 (or more) Long-Term Higher Strike.
  * **Logic:** If the stock crashes, you keep the credit (short expires). If the stock rallies, your multiple long calls (which have more time) will eventually overpower the single short call.
  * **Advantage:** You are buying volatility and time simultaneously.

-----

## <span style="color: #1565C0;">Summary: The Samurai's Checklist ✅</span>

<div style="background-color: #E8F5E9; border-left: 5px solid #4CAF50; padding: 15px; margin: 20px 0;">

### 🥋 The Samurai's Scroll

  * **Strategy:** Diagonal Spread.
  * **Key Feature:** Different Strike Prices + Different Expiration Months.
  * **Best For:** Traders who want to stay in a position for the long haul but want to lower their cost basis by selling near-term premium against it.
  * **Primary Risk:** The stock moves too fast, too soon. You want a "slow grind," not an explosion.
  * **Conclusion of Part II:** This wraps up Call Strategies. You now possess the full arsenal of Bullish and Neutral tools. Next, we enter the realm of the Bear: **Put Options**.

</div>