Okay, highlighting the *most* important formulas for CFA Level 1 involves focusing on fundamental concepts and those frequently tested. While many formulas are useful, these are often considered critical building blocks:

***

## Most Important Formulas for CFA Level 1 (Book 1 Focus)

### Time Value of Money (TVM) & Rates/Returns

* **Present Value (PV) / Future Value (FV):** The absolute foundation of finance.
    $$PV = \frac{FV}{(1 + r)^t} \quad \text{and} \quad FV = PV(1 + r)^t$$
* **PV of a Perpetuity:** Crucial for valuing perpetual cash flows like some preferred stocks.
    $$PV_{\text{Perpetuity}} = \frac{\text{Payment}}{r}$$
* **Geometric Mean Return:** The standard for calculating compound investment returns over time.
    $$R_G = \sqrt[n]{(1 + R_1)(1 + R_2)...(1 + R_n)} - 1$$
* **Annualized Return (from HPR):** Essential for comparing returns over different periods.
    $$\text{Annualized Return} = (1 + \text{HPR})^{\frac{\text{Periods per Year}}{\text{Periods in HPR}}} - 1$$
    *(Often `365/days` or `12/months` etc.)*

***

### Quantitative Methods: Statistics & Probability

* **Sample Variance / Standard Deviation:** Key measures of risk (dispersion). Memorize the `n-1` denominator for *sample* variance.
    $$s^2 = \frac{\sum_{i=1}^{n} (X_i - \bar{X})^2}{n - 1} \quad \text{and} \quad s = \sqrt{s^2}$$
* **Covariance & Correlation:** Essential for understanding how assets move together and the benefits of diversification.
    $$\text{Cov}_{XY} = s_{XY} = \frac{\sum_{i=1}^{n} \{ [X_i - \bar{X}] [Y_i - \bar{Y}] \}}{n - 1}$$
    $$\rho_{XY} = r_{XY} = \frac{\text{Cov}_{XY}}{s_X s_Y}$$
* **Expected Value (Probability Model):** Calculating the weighted average outcome.
    $$E(X) = \sum P(x_i) x_i$$
* **Variance / Standard Deviation (Probability Model):** Calculating risk based on probabilities.
    $$\sigma^2(X) = \sum P(x_i) [x_i - E(X)]^2 \quad \text{and} \quad \sigma(X) = \sqrt{\sigma^2(X)}$$
* **Bayes' Formula:** Important for updating probabilities based on new information.
    $$P(I|O) = \frac{P(O|I)}{P(O)} \times P(I)$$

***

### Portfolio Management

* **Expected Portfolio Return:** Simple weighted average.
    $$E(R_p) = \sum_{i=1}^{n} w_i E(R_i)$$
* **Variance of a 2-Asset Portfolio:** Absolutely critical for understanding diversification. Know both forms (with covariance and correlation).
    $$\sigma_P^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \text{Cov}_{AB}$$
    $$\sigma_P^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \rho_{AB} \sigma_A \sigma_B$$
* **Safety-First Ratio (SFRatio):** Key ratio for shortfall risk.
    $$\text{SFRatio} = \frac{E(R_P) - R_L}{\sigma_P}$$

***

### Hypothesis Testing & Regression

* **Test Statistic (General Concept & t-stat for Mean):** Understand the structure and how to apply the t-test for a population mean.
    $$\text{Test Stat} = \frac{\text{Sample Stat} - \text{Hypothesized Val}}{\text{Standard Error}}$$
    $$t_{n-1} = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$$
* **t-Statistic for Correlation = 0:** Testing the significance of a correlation.
    $$t_{n-2} = \frac{r \sqrt{n - 2}}{\sqrt{1 - r^2}}$$
* **Coefficient of Determination (R²):** Measures the goodness-of-fit in regression.
    $$R^2 = \frac{\text{Explained Variation (SSR)}}{\text{Total Variation (SST)}}$$
* **t-Statistic for Regression Slope Coefficient:** Tests the significance of an independent variable.
    $$t = \frac{\hat{b}_1 - b_1}{s_{\hat{b}_1}}$$

***

### Economics

* **No-Arbitrage Forward Exchange Rate (Interest Rate Parity):** Connects interest rates and FX rates.
    $$\frac{\text{Forward}}{\text{Spot}} = \frac{(1 + i_{\text{price currency}})}{(1 + i_{\text{base currency}})}$$

***

### Corporate Issuers / Equity

* **Constant Growth DDM (Gordon Growth Model):** Core equity valuation model.
    $$V_0 = \frac{D_1}{k_e - g_c}$$
* **Weighted-Average Cost of Capital (WACC):** Fundamental concept for project evaluation and firm valuation (from Reading 25 in Book 1).
    $$\text{WACC} = w_d k_d (1 - t) + w_p k_p + w_e k_e$$
    *(Simplified: WACC = $w_d k_d (1-t) + w_e k_e$ if no preferred stock)*

***
Okay, here's a list of the most important formulas found in Book 2 (Financial Statement Analysis and Equity Investments) for the CFA Level 1 exam, based on the provided SchweserNotes PDF.

### Financial Ratio Analysis Formulas

1.  **Basic Earnings Per Share (EPS)**
    * Measures profitability per common share.
    * $$\text{Basic EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Number of Common Shares Outstanding}}$$

2.  **Diluted Earnings Per Share (EPS)**
    * Measures profitability per common share, considering all potentially dilutive securities.
    * $$\text{Diluted EPS} = \frac{(\text{Net Income} - \text{Preferred Dividends}) + \text{Conv. Pref. Dividends} + \text{Conv. Debt Interest}(1-t)}{\text{Weighted Avg Shares} + \text{Shares from Conv. of Pref. Shares} + \text{Shares from Conv. of Debt} + \text{Shares Issuable from Options/Warrants}}$$
    * *Note: Adjustment for options/warrants uses the Treasury Stock Method.*

3.  **DuPont Analysis (Original 3-Part)**
    * Decomposes Return on Equity (ROE).
    * $$\text{ROE} = \left( \frac{\text{Net Income}}{\text{Sales}} \right) \times \left( \frac{\text{Sales}}{\text{Average Total Assets}} \right) \times \left( \frac{\text{Average Total Assets}}{\text{Average Total Equity}} \right)$$
    * $$\text{ROE} = (\text{Net Profit Margin}) \times (\text{Total Asset Turnover}) \times (\text{Financial Leverage})$$

4.  **DuPont Analysis (Extended 5-Part)**
    * Further decomposes ROE.
    * $$\text{ROE} = \left( \frac{\text{Net Income}}{\text{EBT}} \right) \times \left( \frac{\text{EBT}}{\text{EBIT}} \right) \times \left( \frac{\text{EBIT}}{\text{Sales}} \right) \times \left( \frac{\text{Sales}}{\text{Average Total Assets}} \right) \times \left( \frac{\text{Average Total Assets}}{\text{Average Total Equity}} \right)$$
    * $$\text{ROE} = (\text{Tax Burden}) \times (\text{Interest Burden}) \times (\text{EBIT Margin}) \times (\text{Total Asset Turnover}) \times (\text{Financial Leverage})$$

5.  **Current Ratio**
    * Measures short-term liquidity.
    * $$\text{Current Ratio} = \frac{\text{Current Assets}}{\text{Current Liabilities}}$$

6.  **Quick Ratio (Acid-Test Ratio)**
    * A stricter measure of short-term liquidity.
    * $$\text{Quick Ratio} = \frac{\text{Cash} + \text{Marketable Securities} + \text{Accounts Receivable}}{\text{Current Liabilities}}$$

7.  **Inventory Turnover**
    * Measures efficiency of inventory management.
    * $$\text{Inventory Turnover} = \frac{\text{Cost of Goods Sold}}{\text{Average Inventory}}$$

8.  **Receivables Turnover**
    * Measures efficiency of collecting receivables.
    * $$\text{Receivables Turnover} = \frac{\text{Revenue}}{\text{Average Accounts Receivable}}$$

9.  **Total Asset Turnover**
    * Measures efficiency of using assets to generate sales.
    * $$\text{Total Asset Turnover} = \frac{\text{Revenue}}{\text{Average Total Assets}}$$

10. **Debt-to-Equity Ratio**
    * Measures financial leverage (solvency).
    * $$\text{Debt-to-Equity} = \frac{\text{Total Debt}}{\text{Total Equity}}$$
    * *Note: Definition of "Total Debt" can vary (e.g., includes all liabilities vs. only interest-bearing debt). Be mindful of context.*

11. **Interest Coverage Ratio**
    * Measures ability to cover interest payments from earnings.
    * $$\text{Interest Coverage} = \frac{\text{EBIT}}{\text{Interest Expense}}$$

12. **Gross Profit Margin**
    * Measures profitability after direct production costs.
    * $$\text{Gross Profit Margin} = \frac{\text{Gross Profit}}{\text{Revenue}}$$

13. **Net Profit Margin**
    * Measures overall profitability after all expenses and taxes.
    * $$\text{Net Profit Margin} = \frac{\text{Net Income}}{\text{Revenue}}$$

14. **Return on Assets (ROA)**
    * Measures profitability relative to total assets.
    * $$\text{ROA} = \frac{\text{Net Income}}{\text{Average Total Assets}}$$

15. **Return on Equity (ROE)**
    * Measures profitability relative to shareholders' equity.
    * $$\text{ROE} = \frac{\text{Net Income}}{\text{Average Total Equity}}$$

### Equity Valuation Formulas

16. **Dividend Discount Model (DDM) - General Form**
    * Values a stock as the present value of its future dividends.
    * $$V_0 = \sum_{t=1}^{\infty} \frac{D_t}{(1+k_e)^t}$$

17. **Gordon Growth Model (Constant Growth DDM)**
    * Values a stock assuming dividends grow at a constant rate forever.
    * $$V_0 = \frac{D_1}{k_e - g} = \frac{D_0 (1+g)}{k_e - g}$$
    * *Requires $k_e > g$*

18. **Sustainable Growth Rate (g)**
    * The rate at which earnings/dividends can grow indefinitely without changing leverage.
    * $$g = \text{Retention Rate} \times \text{ROE} = (1 - \text{Dividend Payout Ratio}) \times \text{ROE}$$

19. **Preferred Stock Valuation**
    * Values preferred stock as a perpetuity.
    * $$V_p = \frac{D_p}{k_p}$$

20. **Price-to-Earnings (P/E) Ratio**
    * Compares stock price to earnings per share. Can be trailing (using past EPS) or leading (using forecast EPS).
    * $$\text{P/E} = \frac{\text{Price per Share}}{\text{Earnings per Share}}$$

21. **Justified P/E Ratio (Leading, based on Gordon Growth)**
    * Relates P/E ratio to fundamentals.
    * $$\frac{P_0}{E_1} = \frac{D_1 / E_1}{k_e - g} = \frac{\text{Payout Ratio}}{k_e - g}$$

22. **Price-to-Book (P/B) Ratio**
    * Compares stock price to book value per share.
    * $$\text{P/B} = \frac{\text{Price per Share}}{\text{Book Value per Share}}$$

23. **Price-to-Sales (P/S) Ratio**
    * Compares stock price to sales per share.
    * $$\text{P/S} = \frac{\text{Price per Share}}{\text{Sales per Share}}$$

24. **Enterprise Value (EV)**
    * Represents the total value of the company attributable to all investors.
    * $$\text{EV} = \text{Market Value of Common Equity} + \text{Market Value of Debt} + \text{Market Value of Preferred Stock} - \text{Cash and Cash Equivalents}$$

25. **EV/EBITDA Multiple**
    * Compares enterprise value to earnings before interest, taxes, depreciation, and amortization.
    * $$\text{EV/EBITDA} = \frac{\text{Enterprise Value}}{\text{EBITDA}}$$

### Other Key Formulas

26. **Free Cash Flow to the Firm (FCFF) - starting from Net Income**
    * Cash available to all investors (debt and equity).
    * $$\text{FCFF} = \text{NI} + \text{NCC} + [\text{Int} \times (1 - \text{tax rate})] - \text{FCInv} - \text{WCInv}$$

27. **Free Cash Flow to the Firm (FCFF) - starting from CFO**
    * $$\text{FCFF} = \text{CFO} + [\text{Int} \times (1 - \text{tax rate})] - \text{FCInv}$$

28. **Free Cash Flow to Equity (FCFE)**
    * Cash available to common shareholders.
    * $$\text{FCFE} = \text{CFO} - \text{FCInv} + \text{Net Borrowing}$$

29. **Margin Call Price (Long Position)**
    * The price at which a margin call occurs.
    * $$P_0 \times \frac{(1 - \text{Initial Margin})}{(1 - \text{Maintenance Margin})}$$

This list covers many of the core calculation-based concepts in FSA and Equity for Level 1. Remember to understand the *interpretation* of these formulas, not just how to calculate them\!
***
> [!TIP]
> **CFA Exam Tip ✍️:** Focus on *understanding* the concepts behind these formulas, not just memorizing them. Level 1 often tests application and interpretation. Know when to use which formula and what the result means! Practice using your calculator efficiently for TVM, stats, and NPV/IRR.