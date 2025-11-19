## Chapter 6: Ratio Call Writing — The Balanced Samurai Stance 🧘‍♂️

### <span style="color: #1565C0;">Introduction: What is a Ratio Write?</span>

A **Ratio Call Write** is a powerful combination strategy that blends the protection of **covered call writing** with the enhanced premium collection of **naked call writing**.

Simply put, you establish a ratio write by:

1.  **Buying/Owning a number of shares of the underlying stock**.
2.  **Selling (Writing) a greater number of Call Options** against those shares than you own.

The most common starting point for beginners is the **2:1 Ratio**.

  * **Example:** Buy 100 shares of stock and **Sell 2 Call Contracts**.

| Component | Number of Contracts/Shares |
| :--- | :--- |
| **Covered Portion** | Long 100 shares + Short 1 Call |
| **Naked Portion** | Short 1 additional Call |
| **Total Position** | **Long 100 Stock + Short 2 Calls (2:1 Ratio)** |

### <span style="color: #1565C0;">Risk & Reward: Two-Sided Mastery</span>

The Ratio Write is usually initiated with a **neutral market outlook**—you expect the stock price to remain relatively unchanged during the life of the calls. This strategy is designed to achieve its **maximum profit** in the price range that is **most probable** for the stock.

#### <span style="color: #6A1B9A;">The Two-Sided Risk</span>

The Ratio Write has two-sided risk, a quality absent from simple covered or naked writing:

1.  **Downside Risk (Like a Covered Write):** If the stock price falls, you lose money on the stock. The collected premium from the short calls offsets a large portion of this loss.
2.  **Unlimited Upside Risk (Like a Naked Write):** If the stock price rises **significantly** above the strike price, the extra naked call creates an unlimited loss potential.

#### <span style="color: #6A1B9A;">Profit Profile Diagram (The "Peak" Strategy)</span>

The diagram below shows how the ratio write's profit (the peak) is aligned with the most likely outcomes for a stock's movement (the bell curve).

<div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin: 10px 0;">
<pre data-lang="vega-lite">
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "background": "#f9f9f9",
  "title": "Ratio Call Write Profit vs Probability",
  "description": "Ratio Call Write Profit vs Probability",
  "width": "container",
  "height": 320,
  "params": [
    {
      "name": "curveColor",
      "value": "#cbd5e1",
      "bind": { "input": "color", "name": "Curve Color: " }
    },
    {
      "name": "curveOpacity",
      "value": 0.4,
      "bind": { "input": "range", "min": 0, "max": 1, "step": 0.1, "name": "Curve Opacity: " }
    }
  ],
  "layer": [
    {
      "data": { "sequence": { "start": 30, "stop": 70, "step": 0.5, "as": "S" } },
      "transform": [
        { "calculate": "14 * exp(-0.5 * pow((datum.S - 50) / 5, 2))", "as": "probability_scaled" }
      ],
      "mark": { 
        "type": "area", 
        "interpolate": "monotone",
        "color": { "expr": "curveColor" },
        "opacity": { "expr": "curveOpacity" }
      },
      "encoding": {
        "x": { "field": "S", "type": "quantitative" },
        "y": { "field": "probability_scaled", "type": "quantitative", "axis": null },
        "tooltip": [
            { "field": "S", "title": "Stock Price" },
            { "field": "probability_scaled", "title": "Relative Probability", "format": ".2f" }
        ]
      }
    },
    {
      "data": {
        "values": [
            { "S": 37, "profit": 0 },
            { "S": 40, "profit": 3 },
            { "S": 49, "profit": 12 },
            { "S": 50, "profit": 13 },
            { "S": 60, "profit": 3 },
            { "S": 63, "profit": 0 },
            { "S": 70, "profit": -7 }
        ]
      },
      "encoding": {
        "x": { "field": "S", "type": "quantitative", "title": "Stock Price at Expiration ($)" },
        "y": { "field": "profit", "type": "quantitative", "title": "Profit ($)" }
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
        { "mark": { "type": "rule", "color": "black" }, "encoding": { "y": { "datum": 0 } } },
        { "mark": { "type": "line", "color": "#1f77b4" } },
        {
            "mark": { "type": "point", "filled": true, "size": 80 },
            "encoding": {
                "color": {
                    "condition": [
                        { "test": "datum.profit > 0", "value": "#2ca02c" },
                        { "test": "datum.profit < 0", "value": "#d62728" }
                    ],
                    "value": "gray"
                },
                "tooltip": [
                    { "field": "S", "type": "quantitative", "title": "Stock Price" },
                    { "field": "profit", "type": "quantitative", "title": "Profit" }
                ]
            }
        },
        {
            "mark": { "type": "rule", "color": "gray", "strokeDash": [ 4, 2 ] },
            "encoding": { "x": { "datum": 50 }, "opacity": { "value": 0.5 } }
        },
        {
            "mark": { "type": "text", "align": "left", "dx": 5, "dy": -10, "text": "Peak Probability" },
            "encoding": { "x": { "datum": 50 }, "y": { "datum": 14 } }
        }
      ]
    }
  ]
}
</pre>
</div>

*The "peak" of maximum profit is in the range of most likely stock prices.*
</div>

-----

-----

### <span style="color: #1565C0;">Selection & Calculation for a 2:1 Ratio Write</span>

The key to selecting a good ratio write is ensuring your **profit range is wide in relation to the volatility** of the stock. Generally, **volatile stocks** are the best candidates, as they offer the largest premium (call price) to take in.

#### <span style="color: #6A1B9A;">The Break-Even Formulas</span>

To quickly calculate your risk boundaries for a standard 2:1 ratio (100 shares long, 2 calls short):

| Concept | Formula (Use the short formula for quick checks\!) |
| :--- | :--- |
| **Points of Maximum Profit (PMP)** | `Strike Price - Stock Price + 2 x Call Price`  |
| **Downside Break-Even (DBE)** | `Stock Price - (2 x Call Price)`  |
| **Upside Break-Even (UBE)** | `Strike Price + PMP`  |

#### <span style="color: #6A1B9A;">Example Calculation</span>

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

  * **Setup:** Buy 100 XYZ at **$49**. Sell 2 October **$50** Calls at **$6** each.
  * **PMP:** $50 - 49 + (2 \times 6) = 1 + 12 = 13 (Max profit is $1,300).
  * **DBE:** $49 - (2 \times 6) = 49 - 12 = 37 (The stock can fall 12 points before you lose money).
  * **UBE:** $50 + 13 = 63.

</div>
</div>

-----

### <span style="color: #1565C0;">The Variable Ratio Write (Trapezoidal Hedge)</span>

If you are a bit more flexible in your outlook, you can create a structure with two different strike prices. This is known as a **Variable Ratio Write** or, due to its profit shape, a **Trapezoidal Hedge**.

  * **Structure:** Buy 100 shares of stock. Sell one call at a lower strike price ($X_L$) and another call at a higher strike price ($X_H$).
  * **Maximum Profit Zone:** The maximum profit is achieved if the stock price lands **anywhere between the two strikes** at expiration (i.e., $X_L < \text{Stock Price} < X_H$).
  * **Maximum Profit Amount:** The maximum profit is simply the total **time value** premium collected when the trade was initiated.

<div style="background-color: #F3E5F5; border-left: 5px solid #7B1FA2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**Variable Ratio Write Mnemonics: T-V-S**

  * **T**rapezoid (The shape of the profit graph).
  * **V**ariable (Uses different strikes, not just one).
  * **S**afe Spot (Max profit is in the **middle** of the two strikes).

</div>
</div>

-----

### <span style="color: #1565C0;">Follow-Up Action: Being a Responsive Samurai</span>

Because the Ratio Write has unlimited risk on the upside, you cannot simply set it and forget it. You must have a follow-up plan.

#### <span style="color: #6A1B9A;">1. Rolling Up (The Offensive Maneuver)</span>

If the stock starts to rally (moves against your neutral position), you can **roll up** the position to re-establish a neutral profit range:

1.  **Buy back** the original short calls (which will result in a loss on the calls). This loss effectively **increases your cost basis** in the stock.
2.  **Sell (Write) a new set of calls** at a higher strike price.

#### <span style="color: #6A1B9A;">2. Equivalent Stock Position (ESP) & Delta-Neutrality</span>

The **Equivalent Stock Position (ESP)** (also known as **Position Delta**) is a vital concept that reduces your entire, complex options position into a single number that tells you how the position will behave for a small movement in the stock price.

  * **Goal:** A total ESP of **0** is a perfectly **delta-neutral** position.
  * **Calculation:**
    $$\text{Total ESP} = (\text{Shares Long}) - (\text{Number of Short Calls} \times \text{Call Delta} \times 100)$$

If your ESP is negative (short), you are bearish. If it's positive (long), you are bullish. To adjust to neutral (ESP = 0), you could buy shares or buy back options.

**Important Caveat:** A position is only truly **delta-neutral** for a "nanosecond." As the stock moves, time passes, or volatility changes, the delta shifts, and the position is no longer neutral.

#### <span style="color: #6A1B9A;">3. Using Stop Orders (The Defensive Maneuver)</span>

To remove emotion, place a **buy stop** and a **sell stop** order as soon as you establish the position.

  * A **Buy Stop** (to close the short calls) is placed if the stock moves up to a certain point.
  * A **Sell Stop** (to close the stock) is placed if the stock moves down to a certain point.
  * **Caution:** This protects against large losses but is subject to loss if the stock **whipsaws** (reverses direction sharply).



-----

### <span style="color: #1565C0;">Introduction to Call Spread Strategies</span>

Chapter 6 concludes with a peek into the world of spreads, which are combinations of two or more options on the same underlying security. All spreads fall into three broad categories based on their relationship on an option price board:

<div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin: 10px 0;">
<pre data-lang="vega-lite">
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "background": "#f9f9f9",
  "title": "The Three Option Spread Types",
  "data": {
    "values": [
      {"Expiration": "Same", "Strike": "Different", "Type": "Vertical Spread", "Color": "#F4D03F", "Desc": "Same Expiration, Different Strikes"},
      {"Expiration": "Different", "Strike": "Same", "Type": "Horizontal Spread", "Color": "#5DADE2", "Desc": "Different Expiration, Same Strikes"},
      {"Expiration": "Different", "Strike": "Different", "Type": "Diagonal Spread", "Color": "#A93226", "Desc": "Different Expiration, Different Strikes"},
      {"Expiration": "Same", "Strike": "Same", "Type": "Not a Spread", "Color": "#E0E0E0", "Desc": "Same Expiration, Same Strike (Just a Position)"}
    ]
  },
  "width": "container",
  "height": 300,
  "encoding": {
    "x": {"field": "Expiration", "type": "nominal", "title": "Expiration Date", "sort": ["Same", "Different"], "axis": {"labelFontSize": 12, "titleFontSize": 14}},
    "y": {"field": "Strike", "type": "nominal", "title": "Strike Price", "sort": ["Same", "Different"], "axis": {"labelFontSize": 12, "titleFontSize": 14}}
  },
  "layer": [
    {
      "mark": "rect",
      "encoding": {
        "color": {"field": "Color", "type": "nominal", "scale": null},
        "tooltip": [
          {"field": "Type", "title": "Spread Type"},
          {"field": "Desc", "title": "Description"}
        ]
      }
    },
    {
      "mark": {"type": "text", "fontSize": 16, "fontWeight": "bold", "fill": "black"},
      "encoding": {
        "text": {"field": "Type"}
      }
    }
  ]
}
</pre>
</div>

</div>

1.  **Vertical Spread:** The calls have the **Same Expiration Date** but **Different Striking Prices** (think of columns running vertically in a newspaper listing).
2.  **Horizontal Spread (Calendar Spread):** The calls have the **Same Striking Price** but **Different Expiration Dates**.
3.  **Diagonal Spread:** A combination—calls have **Different Expiration Dates** as well as **Different Striking Prices**.

-----

### <span style="color: #1565C0;">Summary: The Samurai's Checklist ✅</span>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

  * **Neutral Outlook:** Best for stocks you expect to stay flat.
  * **2:1 Ratio:** Buy 100 shares, Sell 2 Calls.
  *   **Peak Profit:** Occurs at the strike price of the short calls.
  *   **Risk:** Unlimited upside risk if the stock rallies hard.

</div>

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Samurai Pointers

<div style="color: #000000; font-weight: 500;">

  * **Volatility:** High volatility increases premiums, widening your profit tent.
  * **Defense:** Always have a plan (Roll Up or Stop Loss) for the naked call portion.
  * **Patience:** This is a theta (time decay) strategy; let time work for you.

</div>
</div>