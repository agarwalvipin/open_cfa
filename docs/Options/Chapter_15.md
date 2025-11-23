# 🎯 Chapter 15: Put Option Basics 📉

Welcome back, Strategist. You have mastered the Call option—the sword of the bull. Now, we must turn our attention to the shield of the bear: the **Put Option**.

While calls give you the right to *buy*, puts give you the right to **sell**. This chapter introduces the fundamental properties of put options, which are essential for profiting in bear markets or protecting your portfolio from downside risk.

-----

## <span style="color: #1565C0;">1. The Put Option: A Mirror Image</span>

A **Put Option** gives the holder (buyer) the right to **sell** the underlying security at a specific price (the striking price) for a limited period of time. The writer (seller) of the put has the obligation to *buy* the stock if assigned.

### <span style="color: #6A1B9A;">The Value Relationship</span>

The relationship between the stock price and the put option is the inverse of the call option.

  * **Bearish Strategy:** The put buyer hopes for the stock price to **decline**.
  * **In-the-Money:** A put is in-the-money when the stock price is **below** the striking price.
  * **Out-of-the-Money:** A put is out-of-the-money when the stock price is **above** the striking price.

The price of a put is composed of **Intrinsic Value** and **Time Value Premium**, just like a call.

**Formula for Intrinsic Value (In-the-Money Put):**
$$\text{Intrinsic Value} = \text{Striking Price} - \text{Stock Price}$$

| Stock Price | Strike Price | Put Status | Intrinsic Value |
| :--- | :--- | :--- | :--- |
| **40** | 50 | In-the-Money | 10 |
| **47** | 50 | In-the-Money | 3 |
| **50** | 50 | At-the-Money | 0 |
| **55** | 50 | Out-of-the-Money | 0 |

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 Samurai Mnemonic: "Put it Down"**
When you buy a **Put**, you want the stock to go **Down**. A Put allows you to "put" (sell) the stock to someone else at a higher price than the current market value.

</div>
</div>

-----

## <span style="color: #1565C0;">2. Pricing and The Effect of Dividends</span>

The same six factors that influence call prices also influence put prices, but sometimes in different ways.

### <span style="color: #6A1B9A;">Factors Influencing the Put Premium</span>

1.  **Stock Price:** As the stock falls, the put premium rises.
2.  **Striking Price:** Higher strikes have higher premiums (the right to sell at $50 is worth more than the right to sell at $40).
3.  **Time:** More time generally means a higher premium.
4.  **Volatility:** Higher volatility increases the put premium (greater chance of a big drop).
5.  **Interest Rates:** Higher interest rates lower put premiums (inverse relationship).
6.  **Dividends:** **Higher dividends increase put premiums.**

### <span style="color: #6A1B9A;">The Dividend Dynamic</span>

Unlike calls, where dividends hurt the value, dividends are the put buyer's friend. When a stock goes **ex-dividend**, its price drops by the amount of the dividend. This drop increases the value of the put.

  * **Rule:** The larger the dividend, the more valuable the put option.
  * **Arbitrage Alert:** If the time value of an in-the-money put is less than the impending dividend, it is a candidate for early assignment (dividend arbitrage).

### <span style="color: #1565C0;">Profit Profile: Long Put</span>

The following chart visualizes the profit and loss profile of buying a Put Option. Notice how profits increase as the stock price falls below the breakeven point.

<div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin: 10px 0;">
<pre data-lang="vega-lite">
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "background": "#f9f9f9",
  "title": "P/L Diagram: Long Put (Strike 50, Premium 4)",
  "description": "Profit and Loss profile for a Long Put option.",
  "width": "container",
  "height": 300,
  "data": {
    "values": [
      {"Stock Price": 20, "P/L": 26},
      {"Stock Price": 30, "P/L": 16},
      {"Stock Price": 40, "P/L": 6},
      {"Stock Price": 46, "P/L": 0},
      {"Stock Price": 50, "P/L": -4},
      {"Stock Price": 60, "P/L": -4},
      {"Stock Price": 70, "P/L": -4}
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

-----

## <span style="color: #1565C0;">Summary: The Samurai's Checklist ✅</span>

<div style="background-color: #E8F5E9; border-left: 5px solid #4CAF50; padding: 15px; margin: 20px 0;">

### 🥋 The Samurai's Scroll

  * **The Put Option:** A contract giving the right to sell. It profits when the market falls.
  * **Intrinsic Value:** Exists only when the stock price is **below** the strike price.
  * **Time Decay:** Like calls, puts lose value as expiration approaches ("wasting asset").
  * **Assignment Risk:** Put writers may be assigned early, especially if the put is deep in-the-money and the time premium is less than the dividend (or close to zero).
  * **Conversion:** Put and Call prices are linked. If Puts get too cheap, arbitrageurs do "Conversions" (Buy Put, Buy Stock, Sell Call). If Puts get too expensive, they do "Reversals."

</div>