The following is a detailed summary of **Chapter 19: The Sale of a Put** from the book *Options as a Strategic Investment*.

# 🎯 Chapter 19: The Sale of a Put 📉

Welcome back, Strategist. We have explored buying puts to profit from a decline. Now, we flip the coin to the **Sale of a Put**.

Selling (writing) a put is a **bullish** to **neutral** strategy. It is the mirror image of buying a put. Instead of paying a premium for the right to sell, you **receive a premium** and accept the **obligation to buy** the stock at the strike price. This strategy is favored by those who want to generate income or acquire stock at a discount.

-----

## <span style="color: #1565C0;">1. The Uncovered (Naked) Put Sale</span>

Writing a naked put means selling a put option without having a corresponding short stock position (which would "cover" the risk).

### <span style="color: #6A1B9A;">The Concept: Being the Insurer</span>

When you sell a put, you are essentially selling insurance to someone else.

  * **The Buyer** (Insured) pays a premium to be protected if the stock falls.
  * **The Seller** (You/Insurer) keeps the premium. If the stock stays stable or rises, you profit. If the stock crashes, you must buy the "damaged" stock at the strike price.

### <span style="color: #6A1B9A;">Profit & Risk Profile</span>

  * **Maximum Profit:** Limited to the **premium received**. This occurs if the stock finishes at or above the strike price (the put expires worthless).
  * **Maximum Risk:** Substantial (nearly unlimited). If the stock falls to zero, you must still buy it at the strike price.
  * **Break-Even:** Strike Price - Premium Received.

**Example:**

  * **XYZ Stock:** $50
  * **Action:** Sell 1 XYZ July 50 Put for $4.
  * **Result:**
      * **If XYZ > 50:** Put expires. You keep the $400.
      * **If XYZ < 46:** You begin to lose money.
      * **If XYZ = 40:** You lose $600 ($1,000 loss on stock value - $400 premium).

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 Samurai Mnemonic: "Put-To-Me"**
When you sell a Put, you are saying, "You can **Put** the stock **To Me**." You are obligated to buy it if assigned.

</div>
</div>

### <span style="color: #1565C0;">Profit Profile: Short Put</span>

The following chart visualizes the profit and loss profile of selling a Put Option. Notice that profits are capped, but losses can grow significantly if the stock crashes.

<div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin: 10px 0;">
<pre data-lang="vega-lite">
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "background": "#f9f9f9",
  "title": "P/L Diagram: Short Put (Strike 50, Premium 4)",
  "description": "Profit and Loss profile for a Short Put option.",
  "width": "container",
  "height": 300,
  "data": {
    "values": [
      {"Stock Price": 20, "P/L": -26},
      {"Stock Price": 30, "P/L": -16},
      {"Stock Price": 40, "P/L": -6},
      {"Stock Price": 46, "P/L": 0},
      {"Stock Price": 50, "P/L": 4},
      {"Stock Price": 60, "P/L": 4},
      {"Stock Price": 70, "P/L": 4}
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

## <span style="color: #1565C0;">2. Follow-Up Action</span>

As a naked put writer, you must be vigilant. If the stock drops, your losses grow.

### <span style="color: #6A1B9A;">Defensive Measures</span>

1.  **Close the Position:** If the stock drops, the simplest action is to buy back the put (usually at a loss) to prevent further bleeding.
2.  **Rolling Down?** Unlike covered call writing, rolling down (buying back the current put and selling a lower strike put) is **not** as advantageous.
      * *Why?* You do not save on stock commissions (since you don't own the stock yet), and you are merely realizing a loss to take a new position that brings in less premium.
      * *Better Choice:* Close the position and look for a better opportunity elsewhere.

### <span style="color: #6A1B9A;">Evaluating Returns</span>

Calculating returns on naked puts is tricky because it involves margin (collateral), not just cash.

  * **Initial Margin:** Typically 20% of the stock price + Put Premium - Out-of-the-money amount (Subject to minimums).
  * **Conservative Approach:** Always allow enough collateral to cover a drop in the stock to a specific "bail-out" point. Don't just use the minimum margin; use enough capital to survive a move against you.

<div style="background-color: #FFF3E0; border-left: 5px solid #FFB300; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**⚠️ Quick Pointer: The Cash-Secured Put**
To reduce risk and avoid margin calls, some traders keep the full strike price value in cash (or T-Bills) in their account. This is called "Cash-Secured Put Writing." It yields less percentage return but is much safer than naked writing on margin.

</div>
</div>

-----

## <span style="color: #1565C0;">3. Buying Stock Below Market Price</span>

One of the most strategic uses of selling puts is to acquire stock at a target price lower than the current market.

### <span style="color: #6A1B9A;">The Strategy</span>

You want to buy XYZ, but it is trading at $60. You feel it is a good buy at $55.

1.  **Instead of placing a limit order** at $55 (which might never get filled), you **sell a Put** with a strike of $55.
2.  **Scenario A (Stock stays above 55):** You keep the put premium as income. You missed the stock, but got paid for waiting.
3.  **Scenario B (Stock drops below 55):** You are assigned. You buy the stock at $55. Since you kept the premium (say $3), your **net cost** is actually $52 ($55 Strike - $3 Premium).

**Verdict:** This is a superior way to place a limit order for a stock you willingly want to own.

-----

## <span style="color: #1565C0;">4. Other Put Strategies (And Why They Are Inferior)</span>

McMillan briefly touches on two other strategies but generally dismisses them in favor of their Call equivalents.

### <span style="color: #6A1B9A;">The Covered Put Sale</span>

  * **Structure:** Sell Stock Short + Sell a Put.
  * **Equivalent To:** A Naked Call Write.
  * **Why avoid it?** You must pay dividends on the short stock, and puts generally have less time value than calls. Naked Call writing is usually more efficient.

### <span style="color: #6A1B9A;">Ratio Put Writing</span>

  * **Structure:** Sell Stock Short + Sell 2 Puts (for every 100 shares short).
  * **Equivalent To:** Ratio Call Writing.
  * **Why avoid it?** Again, dividend payments on short stock reduce profitability. The Ratio Call Write (Buy Stock, Sell 2 Calls) collects dividends and usually captures higher premiums.

-----

## <span style="color: #1565C0;">Summary: The Samurai's Checklist ✅</span>

<div style="background-color: #E8F5E9; border-left: 5px solid #4CAF50; padding: 15px; margin: 20px 0;">

### 🥋 The Samurai's Scroll

  * **Naked Put Writing:** A bullish strategy that profits from time decay and stable/rising prices.
  * **Equivalence:** Selling a Naked Put has the same profit/loss shape as **Covered Call Writing**.
  * **Acquisition Tool:** An excellent way to buy stock at a discount. If the stock doesn't fall to your strike, you keep the premium as a consolation prize.
  * **Risk Warning:** The risk is that the stock crashes. You are obligated to buy a falling knife. Ensure you have the capital and the willingness to own the stock at the strike price.
  * **Assignment Risk:** Be aware of early assignment if the put becomes deep in-the-money and the time premium disappears.

</div>