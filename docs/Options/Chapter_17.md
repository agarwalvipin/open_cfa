# 🎯 Chapter 17: Put Buying in Conjunction with Common Stock Ownership 📉

Welcome back, Strategist. In the previous chapter, we explored buying puts as an aggressive, speculative strategy. Now, we shift our focus to a more defensive and strategic use of put options.

This chapter covers **using puts to protect your stock portfolio**, effectively acting as an insurance policy. We will also explore strategies like the **"No-Cost Collar"** and discuss the tax implications of these defensive moves.

-----

## <span style="color: #1565C0;">1. The Married Put: Protection for Your Stock</span>

The most straightforward defensive strategy is the **Married Put** (or Protective Put). This involves owning the underlying stock and simultaneously buying a put option on that same stock.

### <span style="color: #6A1B9A;">The Concept: Insurance for Your Portfolio</span>

Buying a put option gives you the right to **sell** your stock at a specific strike price, no matter how low the market price drops. This effectively places a "floor" under your stock position.

  * **Scenario:** You own XYZ stock at $52. You are worried about a short-term decline but want to hold the stock for the long term.
  * **Action:** Buy an XYZ October 50 Put for $2.
  * **Result:**
      * **If XYZ drops to $30:** You can exercise your put and sell your stock at $50. Your loss is limited to the difference between your purchase price ($52) and the strike ($50), plus the cost of the put ($2). Total loss = $4.
      * **If XYZ rises to $80:** The put expires worthless (you lose the $2 premium), but you participate in all the upside of the stock above $54 (your break-even point).

### <span style="color: #6A1B9A;">Profit Profile: Synthetic Long Call</span>

Interestingly, the profit profile of a **Long Stock + Long Put** is identical to that of a **Long Call** option. You have limited risk (the stock price minus the strike price plus the put premium) and unlimited upside potential.

<div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin: 10px 0;">
<pre data-lang="vega-lite">
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "background": "#f9f9f9",
  "title": "P/L Diagram: Protective Put (Stock @ 52, Long 50 Put @ 2)",
  "description": "Profit and Loss profile for owning stock and buying a protective put.",
  "width": "container",
  "height": 300,
  "data": {
    "values": [
      {"Stock Price": 30, "P/L": -400},
      {"Stock Price": 40, "P/L": -400},
      {"Stock Price": 50, "P/L": -400},
      {"Stock Price": 54, "P/L": 0},
      {"Stock Price": 60, "P/L": 600},
      {"Stock Price": 70, "P/L": 1600},
      {"Stock Price": 80, "P/L": 2600}
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
      "mark": {"type": "line", "color": "#00838F", "strokeWidth": 3}
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
    }
  ],
  "config": {
    "view": {"stroke": null}
  }
}
</pre>
</div>

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 Samurai Mnemonic: "The Married Put"**
Think of this as a marriage between your stock and a put option. The put promises to protect the stock from falling too hard ("for poorer"), while the stock allows you to enjoy the good times if the market rises ("for richer").

</div>
</div>

-----

## <span style="color: #1565C0;">2. Selecting Which Put to Buy</span>

Just as with speculative put buying, you must choose the right strike price. The trade-off is between **cost** and **protection**.

### <span style="color: #6A1B9A;">In-the-Money vs. Out-of-the-Money</span>

  * **Out-of-the-Money (OTM) Put:** Less expensive upfront cost ("deductible"). It provides "disaster insurance." You are only protected if the stock crashes significantly below the strike price.
  * **In-the-Money (ITM) Put:** More expensive. It provides tighter protection but limits your upside potential until the stock rallies past the premium paid.

**Recommendation:** Generally, a **slightly out-of-the-money put** offers the best balance between cost and protection.

### <span style="color: #6A1B9A;">Tax Considerations</span>

Using puts to protect stock can have tax consequences.

  * If you buy a put on a stock you have held **short-term** (less than one year), your holding period for the stock is **wiped out**. It starts over only when you dispose of the put.
  * This does not apply if you are already a long-term holder or if you buy the stock and put on the same day (a "married put").

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Samurai Pointers

<div style="color: #000000; font-weight: 500;">

  * **Dividend Capture:** If you use a put to protect a stock just to capture a dividend, be careful. The cost of the put might exceed the dividend income\!
  * **Constructive Sale:** Be aware of tax rules. Buying a put against a short-term stock holding kills your holding period accumulation.

</div>
</div>

-----

## <span style="color: #1565C0;">3. The "No-Cost" Collar</span>

Many investors balk at the cost of buying protective puts. A popular strategy to offset this cost is the **Collar**.

### <span style="color: #6A1B9A;">The Structure</span>

A Collar is constructed by:

1.  **Owning** the stock.
2.  **Buying** an OTM Put (for protection).
3.  **Selling** an OTM Call (to finance the put).

If structured correctly, the premium received from selling the call can completely pay for the put, creating a **"No-Cost" Collar**.

  * **The Trade-off:** You get free downside protection, BUT you cap your upside potential at the strike price of the call you sold.

### <span style="color: #6A1B9A;">Decision Flow: To Collar or Not?</span>

```mermaid
graph TD
    A[Own Stock, Worried about Downside] --> B{Willing to pay for Put?}
    B -- Yes --> C[Buy Protective Put]
    B -- No --> D{Willing to Cap Upside?}
    D -- Yes --> E["Establish Collar (Buy Put / Sell Call)"]
    D -- No --> F["Do Nothing / Sell Stock"]
    
    style C fill:#bbdefb,stroke:#333,stroke-width:2px
    style E fill:#e1bee7,stroke:#333,stroke-width:2px
    style F fill:#ffc7ce,stroke:#333,stroke-width:2px
```

### <span style="color: #6A1B9A;">Zero-Cost Collar Example</span>

  * **Stock Price:** $100
  * **Buy:** Put strike $90 (Cost: $2)
  * **Sell:** Call strike $115 (Credit: $2)
  * **Net Cost:** $0
  * **Result:** You are protected below $90, and you participate in gains up to $115.

-----

## <span style="color: #1565C0;">Summary: The Samurai's Checklist ✅</span>

<div style="background-color: #E8F5E9; border-left: 5px solid #4CAF50; padding: 15px; margin: 20px 0;">

### 🥋 The Samurai's Scroll

  * **Protective Put:** Buying a put against stock you own creates a synthetic long call. It limits risk while preserving unlimited upside.
  * **Cost:** The put premium is the cost of insurance. It raises your break-even point.
  * **The Collar:** Selling a call to fund the put purchase can reduce or eliminate the out-of-pocket cost, but it caps your upside profit potential.
  * **Tax Rule:** Buying a put on a short-term stock holding resets your holding period for capital gains tax purposes.

</div>