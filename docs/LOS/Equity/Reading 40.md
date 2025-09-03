## Reading 40: Security Market Indexes 🚀

### 🎯 Introduction
Think of a security market index as a scorecard for a sports team. Instead of tracking one player, it tracks the combined performance of the most important players to give you a single score. This score tells you if the "team" (e.g., the stock market) is winning or losing. A **security market index** bundles together a group of individual stocks, bonds, or other assets (**constituent securities**) to represent the performance of a whole market or a segment of it. It gives us a quick snapshot of market sentiment and performance, just like checking the score of a cricket match!

***

### Part 1: What's in an Index Score? 🤔

A security index has a numerical value calculated from the prices of its constituent securities. The change in this value gives us the index return. There are two main ways to measure this return:

* **Price Return:** This measures the performance using only the price changes of the securities in the index. It's like judging a company's stock performance based only on its price going from ₹100 to ₹110, 3673].
* **Total Return:** This measures performance by including both price changes *and* the income received from the securities, such as dividends or interest payments. This is a more complete picture of the investment's performance.

```
Example 🧮
Imagine an index with two stocks, A and B.
• Stock A's price goes from $90 to $95.
• Stock B's price goes from $110 to $112, and it pays a $3 dividend.

Price Return calculation:
($95 + $112) / ($90 + $110) - 1 = 207/200 - 1 = 3.5%

Total Return calculation:
($95 + $112 + $3) / ($90 + $110) - 1 = 210/200 - 1 = 5.0%

As you can see, the total return is always higher than (or equal to) the price return.
```

***

### Part 2: How Are Indexes Built? 🏗️

Creating an index involves several key decisions. It's like deciding the rules for your sports team's scorecard.

| Decision Point | Description |
| :--- | :--- |
| **Target Market** 🎯 | What market is the index supposed to measure? The entire US stock market? Or something specific like Indian banking stocks?  |
| **Security Selection** 🧐 | Which specific stocks or bonds will be included? All of them, or just a representative sample?  |
| **Weighting Method** ⚖️ | How much influence does each security have on the index's value? This is the most crucial decision.  |
| **Rebalancing** 🔄 | How often are the weights adjusted to maintain the target weighting scheme?  |
| **Reconstitution** 📋 | When are securities added or removed from the index? 

#### Weighting Methods: The Heart of the Index ❤️

The weighting method determines how influential each security is. There are four main methods:

#### **Price-Weighted**

A **price-weighted index** gives more weight to stocks with higher prices. It's calculated by simply adding the prices of all constituent stocks and dividing by a divisor, 281].

* **How it Works:** The divisor is adjusted for stock splits to maintain the index's continuity, 3702].
* **Pros:** Simple to calculate.
* **Cons:** A stock's weight is determined by its price, not its underlying value or size. A stock split can drastically reduce a stock's influence on the index.
* **Examples 🌍:**
    * **Global:** Dow Jones Industrial Average (DJIA)
    * **India:** BSE Sensex

```
Example 🧮
Price-Weighted Index Impact:

Stock A: $90 price
Stock B: $10 price

If both stocks move by $1:
• Stock A: $90 → $91 (1.11% change)
• Stock B: $10 → $11 (10% change)

Index Impact:
• Stock A contributes 9x more to the index value than Stock B
• This is because price-weighted indexes simply add the prices
• Higher-priced stocks have disproportionate influence regardless of company size
```

#### **Equal-Weighted**

An **equal-weighted index** gives the same weight to every stock, regardless of its price or market size. It's like saying every player on the team contributes equally to the final score.

* **How it Works:** Calculated as the simple arithmetic average of the returns of all index stocks.
* **Pros:** Simple and avoids the market-cap bias.
* **Cons:** Requires frequent **rebalancing** (selling winners, buying losers) which leads to high transaction costs. It also gives a disproportionately large weight to smaller companies.
* **Examples 🌍:**
    * **Global:** S&P 500 Equal Weight Index
    * **India:** Nifty 50 Equal Weight Index

#### **Market-Cap Weighted**

A **market capitalization-weighted index** gives more weight to companies with a larger market value (Share Price × Number of Shares), 282]. This is the most common method.

* **How it Works:** The weight of each stock is its market cap divided by the total market cap of all stocks in the index.
* **Pros:** The weights automatically adjust with price changes, so no frequent **rebalancing** is needed. It reflects the actual investment landscape.
* **Cons:** The index can be dominated by a few large, potentially overvalued stocks, creating a momentum effect, 3694].
* **Examples 🌍:**
    * **Global:** S&P 500
    * **India:** Nifty 50

> **CFA Exam Tip ✍️**
> A variation is the **float-adjusted market capitalization-weighted index**, which only considers shares available for public trading (**market float**) and excludes shares held by controlling shareholders or governments. This is considered a better measure of the actual investment opportunity. The S&P 500 and Nifty 50 are both float-adjusted.

#### **Fundamental-Weighted**

A **fundamental-weighted index** weights stocks based on fundamental measures like sales, earnings, or dividends, instead of market price or market cap. This method avoids the biases of market-cap weighting.

* **How it Works:** Weights are based on a company's fundamental size, not its market valuation.
* **Pros:** Avoids the momentum effect and has a "value" tilt, as it may overweight firms that the market is undervaluing.
* **Cons:** Can have a "contrarian" effect, leading to poor performance when value stocks are out of favor.

#### Index Maintenance: Rebalancing vs. Reconstitution 🛠️

* **Rebalancing:** This is the process of adjusting the weights of the securities in the index back to their target weights. It's most frequently required for **equal-weighted indexes** because as stock prices change, their equal weights drift apart, 3722].
* **Reconstitution:** This is the process of changing the actual securities included in an index. For example, when a company gets delisted from an exchange or no longer meets the index criteria (like being a "blue-chip" stock), it is removed and replaced by another company.

> [!TIP]
> **CFA Exam Tip ✍️:** Remember the key difference: **Rebalancing** adjusts weights, while **Reconstitution** changes the members. You'll likely be tested on which index type needs the most frequent rebalancing (Answer: Equal-weighted).

***

### Part 3: Why Do We Use Indexes? 🧭

Security market indexes are incredibly useful tools for investors and analysts.
* **Reflection of Market Sentiment 😃/😔:** They serve as a quick gauge of investor confidence.
* **Benchmark for Performance 📊:** Active portfolio managers are often judged by whether they can "beat the index." 
* **Measure of Market Return 📈:** Indexes are used to estimate the return on the market for models like the CAPM.
* **Model for Investment Products 💰:** They are the basis for **index funds** and **ETFs**, which are passive investment products that aim to replicate the index's performance.
* **Gauging Beta and Risk-Adjusted Returns:** An index helps in calculating a stock's **beta** and its risk-adjusted performance.

***

### Part 4: A World of Indexes: What Types Are Out There? 🗺️

Indexes can be categorized based on the assets they track.

#### Equity Indexes 株式
* **Broad Market Index:** Covers more than 90% of a market's value, like the Wilshire 5000 for the US market.
* **Multi-Market Index:** Tracks multiple countries, like the MSCI World Index.
* **Sector Index:** Focuses on a specific industry, like technology or healthcare, which is useful for sector-based investment strategies.
* **Style Index:** Groups stocks by characteristics like market cap (large-cap vs. small-cap) or valuation (value vs. growth).

#### Fixed-Income Indexes 債券
Fixed-income indexes are more complex than equity indexes due to the vast universe of bonds, their varying maturities, credit qualities, and features, 3743].
* **Challenges:**
    * The bond universe is huge, and bonds mature, leading to high turnover.
    * Bonds are traded by dealers, making price data less transparent and often illiquid.
    * It's difficult and expensive for a fund to fully replicate a broad bond index.

#### Alternative Investment Indexes  alternatif
These indexes track assets like commodities, real estate, and hedge funds.
* **Commodity Indexes:** Track the prices of commodities like oil and gold. They are based on the prices of futures contracts.
* **Real Estate Indexes:** Often use **Real Estate Investment Trusts (REITs)**, appraisal data, or repeat sales to track property values.
* **Hedge Fund Indexes:** These are often equally weighted and suffer from reporting biases, as underperforming funds may choose not to report their results, leading to an upward bias in the index performance, 3760].

***

### 🧪 Formula Summary

* **Price Return of an Index:**
    $R_{PI} = \frac{V_{PI1} - V_{PI0}}{V_{PI0}}$
    where $V_{PI1}$ is the index value at the end of the period and $V_{PI0}$ is the value at the beginning.

* **Total Return of an Index:**
    $R_{TRI} = \frac{V_{PI1} - V_{PI0} + Inc_I}{V_{PI0}}$
    where $Inc_I$ is the total income from all securities in the index over the period.

* **Price-Weighted Index Value:**
    $V_{PW} = \frac{\sum_{i=1}^{N} P_i}{\text{Divisor}}$

* **Market Cap-Weighted Index Value:**
    $V_{MCW} = \frac{\sum_{i=1}^{N} (\text{Market Cap})_i}{\text{Divisor}}$

* **Equal-Weighted Index Return (Simple Average):**
    $R_{EW} = \frac{1}{N} \sum_{i=1}^{N} R_i$

***

> [!IMPORTANT]
> ### 🎯 Quick Exam-Day Pointers
> * A **stock split** forces a change in the divisor of a **price-weighted** index to maintain continuity. It has no impact on a **market-cap weighted** index.
> * **Equal-weighted indexes** have a small-cap bias and require frequent rebalancing, which increases costs.
> * **Market-cap weighted indexes** have a large-cap bias and can be influenced by overpriced stocks, creating a momentum effect.
> * **Fixed-income indexes** are harder to create and replicate than equity indexes due to the sheer number of securities and their lack of liquidity.
> * Be wary of **hedge fund indexes**; they suffer from self-selection and survivorship biases, which can inflate their reported returns.