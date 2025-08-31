## Reading 46: Equity Valuation: Concepts and Basic Tools

Welcome, Vipin, to one of the most exciting topics in finance\! At its heart, equity valuation is about figuring out what a company's share is truly worth. Is the price you see on the National Stock Exchange (NSE) the "right" price? Or is it overvalued or undervalued? This reading gives you the basic toolkit to answer that question.

-----

### **Module 46.1: Dividends, Splits, and Repurchases**

This first module sets the stage. Before we can value a company, we need to understand the different ways it returns value to its shareholders and the basic principles of valuation.

#### **LOS 46.a: Overvalued, Fairly Valued, or Undervalued**

The core of active investment management is to find mispriced securities. The process is straightforward:

1.  **Estimate Intrinsic Value ($V_0$):** You, the analyst, use various models and all your knowledge to calculate what you believe a stock is *truly* worth. This is its intrinsic or fundamental value.
2.  **Compare to Market Price ($P_0$):** You then compare your estimated value to the current market price of the stock.
3.  **Make a Decision:**
      * If $V_0 > P_0 \\rightarrow$ The stock is **undervalued**. You'd issue a "Buy" recommendation.
      * If $V_0 < P_0 \\rightarrow$ The stock is **overvalued**. You'd issue a "Sell" or "Don't Buy" recommendation.
      * If $V_0 \\approx P_0 \\rightarrow$ The stock is **fairly valued**. You'd issue a "Hold" recommendation.

**Real-World Example (Indian Context):**

Imagine it's early 2024, and **Tata Motors** is trading at ₹900 per share. As an analyst, you've studied their push into electric vehicles (EVs), their strong performance at Jaguar Land Rover (JLR), and their domestic market growth. After building a detailed financial model, you estimate the intrinsic value of a Tata Motors share to be **₹1,050**.

  * Your Estimated Intrinsic Value ($V_0$) = ₹1,050
  * Current Market Price ($P_0$) = ₹900

Since your estimated value is higher than the market price, you would conclude that Tata Motors is **undervalued** and recommend a **Buy**.

> **⭐ CFA Exam Tip:** Valuation is as much an art as it is a science. Your inputs (like growth rates) are estimates, and small changes can significantly alter the final value. The exam will test your ability to apply the models and interpret the output. Always be clear about the relationship: if your calculated value is greater than the market price, it's a buy (undervalued).

-----

#### **LOS 46.b: Major Categories of Equity Valuation Models**

There are many ways to estimate a stock's intrinsic value, but they all fall into three main buckets.

1.  **Present Value Models (or Discounted Cash Flow - DCF - Models):**

      * **Idea:** A stock's value is the present value of all the cash flows it's expected to generate for its shareholders in the future (either dividends or free cash flow).
      * **Analogy:** Think of it like a fixed deposit (FD). The value of your FD today is based on the future interest payments and the principal you'll get back, all discounted to today's value.

2.  **Multiplier Models (or Relative Valuation Models):**

      * **Idea:** A stock's value can be estimated by comparing its price multiple (like the Price-to-Earnings or P/E ratio) to that of a similar company or to the industry average.
      * **Analogy:** This is like valuing a house. You look at the price per square foot of similar houses recently sold in the same neighborhood to determine if the house you're looking at is fairly priced.

3.  **Asset-Based Models:**

      * **Idea:** A stock's value is the fair market value of the company's assets minus the fair market value of its liabilities.
      * **Analogy:** This is like calculating your personal net worth. You add up all your assets (cash, investments, property) and subtract your liabilities (loans). What's left is your net worth. This model is often used for companies that are going out of business (liquidation).

-----

#### **LOS 46.c & 46.d: Dividends, Splits, Repurchases & Chronology**

Companies have several ways to return cash or value to their shareholders.

**1. Dividends:**
A portion of the company's profits is paid out to shareholders.

  * **Regular Dividends:** Paid on a consistent schedule (e.g., quarterly or annually). Indian blue-chip companies like **ITC** and **Hindustan Unilever** are known for their consistent dividend payments.
  * **Special Dividends:** A one-time payment made during favorable circumstances, in addition to any regular dividends. Cyclical companies like **Vedanta** often use this to share windfall profits without committing to a permanent higher dividend.

**2. Stock Splits & Stock Dividends (Bonus Issues):**
These actions increase the number of shares outstanding but do not change the total value of the company or a shareholder's stake.

  * **Stock Split:** A 2-for-1 split means you get two shares for every one you own, but the price is halved. If **MRF Ltd.** (which trades at over ₹1,00,000) were to do a 10-for-1 split, the price would drop to around ₹10,000, making it more accessible to retail investors.
  * **Bonus Issue:** This is the term more commonly used in India for a stock dividend. It's an accounting entry that capitalizes reserves and issues new shares.

**3. Share Repurchases (Buybacks):**
The company buys back its own shares from the open market. This is an alternative to paying dividends.

  * **Effect:** It reduces the number of shares outstanding. This increases Earnings Per Share (EPS) and often signals management's confidence that the stock is undervalued.
  * **Indian Context:** IT giants like **TCS** and **Wipro** are famous for their regular, large-scale share buybacks.

**Dividend Payment Chronology:**
This is a critical and frequently tested concept.

  * **Declaration Date:** The company's board of directors announces ("declares") the dividend.
  * **Ex-Dividend Date:** The first day the stock trades *without* the dividend. To get the dividend, you must buy the stock *before* this date. The stock price usually drops by the amount of the dividend on this morning.
  * **Holder-of-Record Date:** The company checks its records to see who the official shareholders are on this date. If you're on the list, you get paid. This is typically one or two business days after the ex-dividend date.
  * **Payment Date:** The day the dividend is actually paid to shareholders.

> **⭐ CFA Exam Tip:** The relationship between the **ex-dividend date** and the **record date** is crucial. The market enforces the ex-date rule. If you buy on the ex-date, the seller's name is still on the records on the record date, so the seller gets the dividend. That's why the stock price drops on the ex-date—the share is now worth less because it no longer carries the right to that specific upcoming dividend.

-----

### **Module 46.2: Dividend Discount Models**

This is where the real work begins\! We'll learn how to convert the idea of "future cash flows" into a concrete number—the intrinsic value of a stock. The simplest and most intuitive cash flow to shareholders is the dividend.

#### **LOS 46.e: Rationale for DDM & FCFE Models**

The logic is simple: the price you should pay for a stock today is the sum of the present values of all future dividends you expect to receive. This is the core of the **Dividend Discount Model (DDM)**.

The general formula looks like this:

$$V_0 = \sum_{t=1}^{\infty} \frac{D_t}{(1+k_e)^t} \text{ }$$

Where:

  * $V_0$ = Intrinsic value of the stock today
  * $D_t$ = Expected dividend in period 't'
  * $k_e$ = Required rate of return on equity (or the discount rate)

**What if a company doesn't pay dividends?**

Many great companies, especially in their growth phase, don't pay dividends. They reinvest all their profits back into the business to grow faster.

  * **Indian Context:** Think about a company like **Zomato**. It's a fantastic, growing business, but it doesn't pay dividends. Does that mean its stock has no value? Of course not\!

In such cases, we use the **Free Cash Flow to Equity (FCFE)** model. FCFE represents the cash flow available to be paid to shareholders *after* all expenses and reinvestment needs are met, 2752]. It's a measure of the company's *capacity* to pay dividends.

$$\text{FCFE} = \text{Cash Flow from Operations} - \text{Fixed Capital Investment} + \text{Net Borrowing} \text{ }$$

The valuation model is similar, just substituting FCFE for Dividends:

$$V_0 = \sum_{t=1}^{\infty} \frac{\text{FCFE}_t}{(1+k_e)^t} \text{ }$$

> **⭐ CFA Exam Tip:** For Level 1, you must understand the *rationale* for both DDM and FCFE.
> \* **DDM** is best for mature, profitable companies with a stable history of dividend payments (e.g., **ITC, Coal India, Power Grid Corp**).
> \* **FCFE** is more flexible and can be used for companies that don't pay dividends or have an unpredictable dividend policy (e.g., most tech startups, high-growth companies).

-----

#### **LOS 46.g: How to Value Preferred Stock**

Preferred stock is a hybrid security—it's like a stock, but it often pays a fixed dividend, similar to the coupon on a bond. Because the dividend is fixed and the stock (usually) has an indefinite maturity, we can value it as a **perpetuity**.

The formula is very simple:

$$V_p = \frac{D_p}{k_p} \text{ }$$

Where:

  * $V_p$ = Value of the preferred stock
  * $D_p$ = The annual preferred dividend
  * $k_p$ = The required rate of return on the preferred stock

**Real-World Example (Indian Context):**

Suppose **Tata Power** has a preferred stock outstanding with a par value of ₹100 that pays an 8% dividend. Your required rate of return for a security of this risk level is 10%.

  * Annual Dividend ($D_p$) = 8% of ₹100 = ₹8
  * Required Return ($k_p$) = 10% or 0.10

$$V_p = \frac{₹8}{0.10} = ₹80$$

You would not be willing to pay more than ₹80 for this preferred share.

-----

#### **LOS 46.h: The Gordon Growth Model & Multistage Models**

What if dividends aren't fixed but are expected to grow at a steady rate forever? For that, we use the **Gordon Growth Model (GGM)**, also called the Constant Growth Model.

**Gordon Growth Model (GGM)**

The GGM is a cornerstone of equity valuation and is derived from the general DDM formula.

$$V_0 = \frac{D_1}{k_e - g} \text{ }$$

Where:

  * $D_1$ = **Next year's** expected dividend
  * $k_e$ = Required rate of return on equity
  * $g$ = The constant, perpetual dividend growth rate

> **⚠️ VERY IMPORTANT CFA Exam Tip:** This formula is tested heavily. Pay close attention to whether the question gives you $D_0$ (the dividend *just paid*) or $D_1$ (the dividend *expected next year*), 2767].
>
>   * If you are given $D_0$, you **must** calculate $D_1$ first: $D_1 = D_0 \times (1+g)$.
>     \* The model also has two key assumptions: the growth rate '$g$' is constant forever, and **$k_e$ must be greater than $g$** for the formula to work.

**How do we estimate the growth rate, 'g'?**
One of the best ways is to calculate the **Sustainable Growth Rate (SGR)**. This is the rate at which a company can grow its earnings and dividends without changing its financing policy.

$$g = \text{Retention Rate (RR)} \times \text{Return on Equity (ROE)} \text{ }$$

  * **Retention Rate (RR)** = $1 - \\text{Dividend Payout Ratio}$ 

**Real-World Example (GGM):**

Let's value **Hindustan Unilever (HUL)**, a mature consumer staples company.

  * Suppose HUL just paid a dividend ($D_0$) of ₹30 per share.
  * You analyze the company and find its ROE is consistently 20%, and it pays out 60% of its earnings as dividends.
  * Your required rate of return ($k_e$) for HUL is 12%.

**Step 1: Calculate the sustainable growth rate (g).**

  * Dividend Payout Ratio = 60%
  * Retention Rate (RR) = 1 - 0.60 = 40%
  * $g = RR \times ROE = 0.40 \times 20% = 8%$

**Step 2: Calculate next year's dividend ($D_1$).**

  * $D_1 = D_0 \times (1+g) = ₹30 \times (1.08) = ₹32.40$

**Step 3: Value the stock using GGM.**

  * $V_0 = \\frac{D_1}{k_e - g} = \\frac{₹32.40}{0.12 - 0.08} = \\frac{₹32.40}{0.04} = ₹810$

Your estimate for HUL's intrinsic value is ₹810 per share. You'd then compare this to its market price.

**Multistage DDM**

The GGM assumes constant growth forever, which is unrealistic for most companies. A **multistage model** is more flexible, allowing for a period of high, non-constant growth followed by a stable, perpetual growth phase, 2782].

A common version is the **Two-Stage DDM**. Here's the process:

1.  **Forecast** the dividends for each year in the initial high-growth period.
2.  **Discount** each of these dividends to its present value.
3.  **Calculate the terminal value** of the stock at the end of the high-growth period. This is the value of all future dividends from that point on, calculated using the GGM.
4.  **Discount** the terminal value back to the present.
5.  **Sum** the present values from steps 2 and 4 to get the intrinsic value of the stock.

> **⭐ CFA Exam Tip:** This looks complex, but it's just a multi-step time value of money problem. Draw a timeline on your scrap paper during the exam to keep track of the cash flows. The most common mistake is forgetting to discount the terminal value back to today.

-----

#### **LOS 46.i: Which Model for Which Company?**

Matching the right model to the company's characteristics is a key analytical skill.

  * **Gordon Growth Model:** Best for stable, mature, non-cyclical firms with a long history of dividend payments.
      * **Indian Examples:** Utility companies like **NTPC**, FMCG giants like **Nestle India**.
  * **Two-Stage Model:** Best for companies that have a period of high growth but are expected to mature and settle into a more stable growth rate later.
      * **Indian Examples:** A company like **Asian Paints**, which has had strong growth for years but will eventually mature as the market saturates.
  * **Three-Stage Model:** Best for young companies with very high initial growth, which then slows down during a transition period before finally settling into a stable mature growth rate.
      * **Indian Examples:** A successful tech company that is still in its early hyper-growth phase.

-----

### **Module 46.3: Relative Valuation Measures**

While discounted cash flow models are theoretically pure, they can be very sensitive to your assumptions. To balance this, analysts almost always use relative valuation, which involves comparing a company's valuation multiple to its peers.

#### **LOS 46.j: Rationale for Using Price Multiples**

The core idea here is the **Law of One Price**: identical assets should trade at the same price. In equity valuation, we apply this by saying *similar* companies should trade at *similar* multiples.

**The Link to Fundamentals (The "Justified" Multiple)**

A multiple isn't just a random number; it's directly linked to the company's fundamentals. We can use the Gordon Growth Model to see this:

$$\frac{P_0}{E_1} = \frac{D_1/E_1}{k_e - g} = \frac{\text{Dividend Payout Ratio}}{k_e - g} \text{ }$$

This powerful formula shows that a company's P/E ratio is determined by three fundamental factors:

1.  **Higher Dividend Payout Ratio** $\\rightarrow$ Higher P/E
2.  **Higher Growth Rate (g)** $\\rightarrow$ Higher P/E
3.  **Lower Required Return ($k_e$)** (i.e., lower risk) $\\rightarrow$ Higher P/E

> **⭐ CFA Exam Tip:** This is a crucial concept. The exam will test you on *why* one company deserves a higher multiple than another. The answer will always lie in its fundamentals: higher expected growth, a better payout policy, or lower perceived risk.

-----

#### **LOS 46.k: The Main Price Multiples**

Here are the workhorse multiples you must know.

  * **Price-to-Earnings (P/E):** `Market Price per Share / Earnings per Share`. It tells you how much investors are willing to pay for one rupee of a company's earnings.
  * **Price-to-Book (P/B):** `Market Price per Share / Book Value per Share`. Compares market value to the company's accounting net worth.
  * **Price-to-Sales (P/S):** `Market Price per Share / Sales per Share`. Useful for companies with negative earnings or in cyclical industries.
  * **Price-to-Cash Flow (P/CF):** `Market Price per Share / Cash Flow per Share`. Many analysts prefer this to P/E because cash flow is less susceptible to accounting manipulation.

**Real-World Example (Indian Context):**

Let's compare two top private sector banks, **HDFC Bank** and **ICICI Bank**, using hypothetical but realistic multiples.

| Multiple | HDFC Bank | ICICI Bank | Interpretation |
| :--- | :---: | :---: | :--- |
| **P/E** | 20x | 18x | The market is willing to pay more for each rupee of HDFC Bank's earnings, likely due to its historical consistency and perceived lower risk. |
| **P/B** | 3.5x | 3.0x | HDFC Bank commands a higher premium over its book value, signaling strong investor confidence in its ability to generate high Return on Equity (ROE). |

-----

#### **LOS 46.l: Enterprise Value (EV) Multiples**

Price multiples like P/E only look at the value of a company's equity. But what if you're comparing two companies with very different debt levels? The P/E ratio can be misleading.

**Enterprise Value (EV)** represents the total value of the company, including both its equity and debt. Think of it as the theoretical takeover price.

$$\text{EV} = \text{Market Cap} + \text{Market Value of Debt} - \text{Cash \& Cash Equivalents}$$

The most common EV multiple is **EV/EBITDA**.

  * **Why EBITDA?** Because EV represents the value to *all* capital providers, the denominator should be a flow available to all providers. EBITDA is perfect because it's earnings *before* interest and taxes.

> **⭐ CFA Exam Tip:** EV multiples are excellent for comparing companies with different capital structures or tax rates. They provide a more "apples-to-apples" comparison of the underlying business's valuation.

-----

#### **LOS 46.m: Asset-Based Valuation**

This is the most straightforward approach. The value of equity is simply what's left over after paying off all liabilities.

$$\text{Equity Value} = (\text{Fair Market Value of Assets}) - (\text{Fair Market Value of Liabilities})$$

  * **When is it useful?** This model works best for companies with a lot of tangible assets that are easy to value, like manufacturing firms or real estate holding companies. It's also often used as a "floor value" in a liquidation scenario.
  * **When is it not useful?** It's not helpful for service or technology companies where the main assets (brand name, intellectual property) are intangible and not fully reflected on the balance sheet.

-----

#### **LOS 46.f: Advantages and Disadvantages of Valuation Models**

No single model is perfect. A good analyst uses several models to get a range of values.

| Model Category | Advantages | Disadvantages |
| :--- | :--- | :--- |
| **Present Value Models (DDM, FCFE)** | • Based on sound financial theory .<br>• Widely accepted. | • **Extremely sensitive** to inputs.<br>• Requires making forecasts far into the future. |
| **Multiplier Models** | • Easy to calculate and understand.<br>• Captures current market sentiment. | • Can be difficult to find truly comparable companies.<br>• Can perpertuate market mispricing. |
| **Asset-Based Models** | • Can provide a conservative "floor" value.<br>• Useful for liquidation scenarios. | • Fair market values of assets can be difficult to estimate.<br>• Ignores the "going concern" value of a business. |

-----

### **Final Summary for Reading 46**

Let's wrap it all up.

#### **Key Formulas**

  * **Preferred Stock Value:** $V_p = \\frac{D_p}{k_p}$
  * **Gordon Growth Model (GGM):** $V_0 = \\frac{D_1}{k_e - g}$
  * **Next Year's Dividend:** $D_1 = D_0 \times (1+g)$
  * **Sustainable Growth Rate:** $g = (1 - \\text{Payout Ratio}) \times \\text{ROE}$
  * **Justified Leading P/E:** $\\frac{P_0}{E_1} = \\frac{\\text{Payout Ratio}}{k_e - g}$
  * **Enterprise Value:** $\\text{EV} = \\text{Market Cap} + \\text{Market Value of Debt} - \\text{Cash}$

#### **⚡ Quick Exam-Day Pointers**

1.  **Read Carefully:** The most common mistake in GGM questions is mixing up $D_0$ ("just paid") and $D_1$ ("will pay"). Always calculate $D_1$ if you are given $D_0$.
2.  **Model Choice:** If a question describes a company (e.g., "mature, non-cyclical utility"), you should immediately think "Gordon Growth Model is appropriate". If it says "no dividends," think "FCFE or Multiples."
3.  **Two-Stage Logic:** For multistage problems, draw a timeline. Remember to calculate the terminal value at the *end* of the first stage and then discount it all the way back to today (time 0).
4.  **Multiples are Relative:** The output of a multiples analysis is a statement like "undervalued *relative to its peers*." It doesn't give an absolute intrinsic value.
5.  **EV for Capital Structure:** When you see companies with very different debt levels being compared, the best tool is an EV multiple like EV/EBITDA.