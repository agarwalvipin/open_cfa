## Reading 46: Equity Valuation: Concepts and Basic Tools 🚀

### 🎯 Introduction

Imagine you're buying a mango tree. How much should you pay for it? You could estimate the value of all the mangoes it will produce in the future and discount that back to today's value (a **Discounted Cash Flow Model**). You could see what similar mango trees in the neighborhood are selling for (a **Price Multiple Model**). Or, you could calculate what the tree would be worth if you cut it down and sold the wood (an **Asset-Based Model**). Equity valuation is just like this. It's the art and science of determining a stock's **intrinsic value** using a toolkit of different models to decide if it's a bargain, overpriced, or fairly valued.

-----

### <span style="color: #1565C0;">Part 1: The Building Blocks of Valuation 🧱</span>

#### <span style="color: #6A1B9A;">1.1 Intrinsic Value vs. Market Price</span>
* **Undervalued:** Market Price < Estimated Intrinsic Value (Signal to BUY 🟢)
* **Fairly Valued:** Market Price ≈ Estimated Intrinsic Value (Signal to HOLD 🟡)
* **Overvalued:** Market Price > Estimated Intrinsic Value (Signal to SELL 🔴)

#### <span style="color: #6A1B9A;">1.2 The Three Major Valuation Categories</span>
1.  **Present Value Models (or Discounted Cash Flow - DCF):** Value a stock as the present value of its future cash flows (dividends or free cash flow).
2.  **Multiplier Models (or Market Multiple Models):** Value a stock by comparing its price multiple (like P/E) to that of a benchmark or peer companies.
3.  **Asset-Based Models:** Value a stock based on the market value of its assets minus its liabilities.

#### <span style="color: #6A1B9A;">1.3 Corporate Actions Affecting Value</span>
* **Dividends:**
  * **Regular Dividends:** Consistent payments, often quarterly.
  * **Special Dividends:** One-time cash payments during unusually profitable times.
* **Stock Splits & Stock Dividends:** A **stock split** (e.g., 2-for-1) or **stock dividend** (e.g., 10%) increases the number of shares but decreases the price per share. The total value of your holding remains the same. It's like getting two 500-rupee notes in exchange for one 1000-rupee note—you have more notes, but the total value is unchanged.
* **Reverse Stock Splits:** The opposite of a split; the number of shares is reduced, and the price per share increases. Often used by companies to avoid being delisted.
* **Share Repurchases:** When a company buys back its own stock from the market. This is an alternative to dividends for returning cash to shareholders and reduces the number of shares outstanding.

#### <span style="color: #6A1B9A;">1.4 Dividend Payment Chronology 🗓️</span>
1.  **Declaration Date:** The board of directors announces the dividend.
2.  **Ex-Dividend Date:** The first day the stock trades *without* the dividend. If you buy the stock on or after this date, you **do not** get the dividend. The stock price typically drops by about the dividend amount on this day.
3.  **Holder-of-Record Date:** The date on which you must be a registered shareholder to receive the dividend.
4.  **Payment Date:** The date the dividend is actually paid.

-----

### <span style="color: #1565C0;">Part 2: What Are Future Dividends Worth Today? (DDM) 💰</span>

The **Dividend Discount Model (DDM)** is a core present value model. It states that a stock's value today is the present value of all its future dividends.

A variation is the **Free Cash Flow to Equity (FCFE) Model**, which discounts future **FCFE** instead of dividends. **FCFE** is the cash left over for shareholders after all expenses and reinvestment needs are met. It's useful for companies that don't pay dividends.

#### <span style="color: #6A1B9A;">2.1 Valuing Preferred Stock</span>
Preferred stock usually pays a fixed dividend forever. Its value is a simple perpetuity:

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
$$V_p = \frac{D_p}{k_p}$$
</div>

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
**Example 🧮**
* **Preferred Stock Valuation:**  
  * A preferred stock from Tata Steel pays a fixed annual dividend of ₹80.  
  * Required return ($k_p$) is 10%.  
  * Calculation: ₹80 / 0.10 = ₹800  
  * **Key takeaway:** Value of a perpetuity is dividend divided by required return.
</div>
</div>

#### <span style="color: #6A1B9A;">2.2 The Gordon Growth Model (Constant Growth DDM)</span>
This is the most famous DDM. It assumes dividends will grow at a **constant rate (g)** forever.

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
$$V_0 = \frac{D_1}{k_e - g}$$
</div>

Where:
* $V_0$ = Intrinsic value today
* $D_1$ = Dividend expected *next year* ($D_1 = D_0 \times (1+g)$)
* $k_e$ = Required rate of return on equity
* $g$ = Constant dividend growth rate

**Crucial Assumptions:**
1.  The company pays dividends, and they grow at a constant rate.
2.  The growth rate (g) is less than the required return (kₑ). If g ≥ kₑ, the model breaks and gives a nonsensical negative or infinite value!

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
**Example 🧮**
* A stock just paid a dividend of $2.00 ($D_0$).  
* Dividends are expected to grow at 5% forever (g), and the required return is 10% (kₑ).  
* Step 1: Find next year's dividend: $D_1 = \$2.00 \times (1.05) = \$2.10$  
* Step 2: Plug into the model: $V_0 = \frac{\$2.10}{0.10 - 0.05} = \frac{\$2.10}{0.05} = \textbf{\$42.00}$  
* **Key takeaway:** Always use next year's dividend ($D_1$) in the numerator.
</div>
</div>

The **sustainable growth rate (SGR)** can be estimated as:

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
$$\text{SGR} = (1 - \text{Dividend Payout Ratio}) \times ROE$$
</div>

This is the rate at which a company can grow its dividends using only its own retained earnings.

#### <span style="color: #6A1B9A;">2.3 Multistage DDM</span>
Most companies don't grow at a constant rate forever. They often have a high-growth "supernormal" period, followed by a mature, stable growth period. A **multistage DDM** is used for this.

**How it works (for a 2-stage model):**
1.  Forecast each dividend individually during the high-growth period and find its present value.
2.  Use the Gordon Growth Model to find the stock's terminal value at the *end* of the high-growth period.
3.  Discount this terminal value back to today.
4.  Sum the present values from steps 1 and 3.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
**💡 CFA Exam Tip ✍️:** The Gordon Growth Model is extremely testable. Pay close attention to whether the question gives you **D₀** (the dividend *just paid*) or **D₁** (the dividend *expected next year*). You MUST use **D₁** in the numerator.
</div>
</div>

-----

### <span style="color: #1565C0;">Part 3: What's Everyone Else Paying? (Price Multiples) 📊</span>

This approach values a company by comparing its stock price to a key metric like earnings, sales, or book value. It's a form of relative valuation.

#### <span style="color: #6A1B9A;">3.1 Key Price Multiples</span>
* **Price-to-Earnings (P/E):** Price per share / Earnings per share. The most popular multiple.
* **Price-to-Sales (P/S):** Price per share / Sales per share. Useful for unprofitable or cyclical companies.
* **Price-to-Book (P/B):** Price per share / Book value per share. Often used for banks and industrial companies with significant tangible assets.
* **Price-to-Cash Flow (P/CF):** Price per share / Cash flow per share. Less subject to accounting manipulation than earnings.

#### <span style="color: #6A1B9A;">3.2 Justified P/E</span>
You can derive a "fundamental" or **justified P/E** ratio from the Gordon Growth Model. This tells you what the P/E ratio *should* be, based on fundamentals.

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
$$\text{Justified Leading P/E} = \frac{P_0}{E_1} = \frac{D_1/E_1}{k_e - g} = \frac{\text{Payout Ratio}}{k_e - g}$$
</div>

This shows that a company's P/E is directly related to its payout ratio and growth rate, and inversely related to its required return (risk).

-----

### <span style="color: #1565C0;">Part 4: Beyond Price Multiples: EV and Asset-Based Models 🏗️</span>

#### <span style="color: #6A1B9A;">4.1 Enterprise Value (EV) Multiples</span>
**Enterprise Value (EV)** represents the total value of a company, including both its equity and its debt. It's the theoretical takeover price.

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
$$EV = \text{Market Value of Equity} + \text{Market Value of Debt} - \text{Cash \& Cash Equivalents}$$
</div>

The most common EV multiple is **EV/EBITDA**.
* **Why it's useful:** Because EV includes debt, the denominator (EBITDA) should also be a pre-debt, pre-tax figure. This makes EV/EBITDA excellent for comparing companies with different capital structures and tax rates. It's often positive even when EPS is negative.

#### <span style="color: #6A1B9A;">4.2 Asset-Based Valuation</span>
This method values a company's equity by subtracting the market value of its liabilities from the market value of its assets.

* **Equity Value = Market Value of Assets – Market Value of Liabilities**
* **When to use it:** It's most useful for companies with significant tangible assets that have ready market values, like natural resource firms or holding companies. It's less useful for service or tech companies where the value comes from intangible assets.

-----

### <span style="color: #1565C0;">Part 5: Choosing Your Weapon: Pros and Cons of Each Model ⚖️</span>

| Model Category | Advantages 👍 | Disadvantages 👎 |
| :--- | :--- | :--- |
| **Present Value (DCF)** | Based on solid finance theory; forces you to think about underlying drivers of value. | Very sensitive to assumptions (especially growth and discount rates); less useful for non-dividend paying firms. |
| **Price Multiples** | Easy to calculate and understand; widely used; good for cross-sectional comparisons. | Can be skewed by accounting differences; difficult for cyclical firms; doesn't tell you if the *entire* industry is overvalued. |
| **Asset-Based** | Provides a "floor" value; useful for valuing distressed companies or those rich in tangible assets. | Market values of assets can be hard to find; ignores future growth potential and intangible assets. |

-----

### <span style="color: #00838F;">Global & Local Context 🌍</span>
* **Global Example:** U.S. equity markets often rely heavily on price multiples (P/E, EV/EBITDA), while emerging markets may see more asset-based valuations due to less reliable earnings data.
* **Indian Example:** Asset-based models are frequently used for valuing companies in sectors like real estate and natural resources, where tangible assets dominate.

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**Preferred Stock Value:**  
$$V_p = \frac{D_p}{k_p}$$
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**Gordon Growth Model (GGM):**  
$$V_0 = \frac{D_1}{k_e - g}$$
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**Next Year's Dividend:**  
$$D_1 = D_0 \times (1+g)$$
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**Sustainable Growth Rate (SGR):**  
$$g = (1 - \text{Payout Ratio}) \times ROE$$
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**Justified Leading P/E:**  
$$\frac{P_0}{E_1} = \frac{\text{Payout Ratio}}{k_e - g}$$
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**Enterprise Value (EV):**  
$$EV = \text{Mkt Cap} + \text{Mkt Value of Debt} - \text{Cash}$$
</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">
### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">
* **D₀ vs. D₁:**  
  * The Gordon Growth Model formula requires **D₁** (next year's dividend).  
  * If you're given D₀ (the last dividend), you MUST grow it by `(1+g)` first.
* **k > g:**  
  * The required return (**k**) *must* be greater than the growth rate (**g**) for the Gordon Growth Model to work.  
  * If g is higher, the formula is invalid.
* **Multiples Need Context:**  
  * A P/E of 30 isn't inherently "high."  
  * It depends on the company's growth prospects, risk, and what peers are trading at.
* **Use EV/EBITDA for Different Capital Structures:**  
  * When comparing a company with a lot of debt to one with no debt, P/E can be misleading.  
  * EV/EBITDA provides a better apples-to-apples comparison.
* **Asset-Based is for "Hard" Assets:**  
  * This model works best for companies where the value is in tangible assets (real estate, oil reserves), not intangibles (brand value, R&D).
</div>
</div>