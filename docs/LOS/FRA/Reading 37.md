## Reading 37: Financial Analysis Techniques 🚀

### 🎯 Introduction

Welcome, aspiring analyst\! Think of financial statements as a company's story written in numbers. But reading just the raw numbers is like reading a novel in a foreign language – you get some words, but miss the plot\! Financial analysis techniques, especially **ratio analysis**, are your translation tools 🛠️ and magnifying glass 🔍. They help you decode the story, spot trends, compare characters (companies), and ultimately understand the company's health, efficiency, and potential. This reading equips you with the essential toolkit to become a financial detective\!

-----

### Part 1: What Are the Analyst's Main Tools? 🤔 (LOS 37.a)

Analysts use several tools to dissect financial statements:

1.  **Ratio Analysis:** The core tool\! Expressing relationships between financial statement items as ratios (e.g., profit margin = net income / sales). Ratios standardize numbers, allowing comparisons over time (**time-series analysis**) or between companies (**cross-sectional analysis**).
2.  **Common-Size Analysis:** Expressing financial statement items as percentages of a base figure.
    * **Vertical Common-Size:** Income statement items as % of revenue; balance sheet items as % of total assets. Great for spotting trends in margins or asset composition.
    * **Horizontal Common-Size:** Expressing each line item as a percentage of its value in a base year. Highlights growth rates over time.
3.  **Graphical Analysis:** Visualizing data and ratios using charts (like stacked columns or line graphs) makes trends and comparisons easier to spot. 📊
4.  **Regression Analysis:** Statistical technique to identify relationships between variables (e.g., how sales relate to GDP) often used for forecasting.

**Limitations to Keep in Mind ⚠️:**

* Ratios aren't useful in isolation; they need comparison points (history, industry peers).
* Different accounting methods (e.g., LIFO vs. FIFO) hinder comparability. Adjustments might be needed.
* Finding comparable peers can be tough, especially for conglomerates.
* Interpreting ratios requires judgment – is a high ratio good or bad? Context matters\!
* Balance sheet data is just a snapshot at one point in time.

#### **Theory: Common-Size Example 🧠**

Imagine Company A has Sales of ₹1,000 Cr and Net Income of ₹100 Cr. Company B has Sales of ₹500 Cr and Net Income of ₹75 Cr.

* **Absolute:** Company A has higher Net Income.
* **Vertical Common-Size:**
    * Company A Net Profit Margin = ₹100 Cr / ₹1,000 Cr = 10%
    * Company B Net Profit Margin = ₹75 Cr / ₹500 Cr = 15%
    * **Conclusion:** Company B is more profitable relative to its sales.

#### **Global & Local Context 🌍**

* **Global Example:** An analyst comparing Apple's (USA) profit margins over the last 5 years (time-series) or comparing Apple's margins to Samsung's (South Korea) margins in the latest year (cross-sectional).
* **Indian Example:** Comparing HDFC Bank's Return on Assets (ROA) to ICICI Bank's ROA over the past three years to assess relative profitability and efficiency trends within the Indian banking sector.

> [\!TIP]
> **CFA Exam Tip ✍️:** Understand the *purpose* of each tool. Common-size analysis is great for comparing companies of different sizes or tracking internal trends. Ratio analysis provides specific insights into liquidity, solvency, profitability, etc. Be aware of the limitations – they are favorite exam topics\!

-----

### Part 2: The Core Ratios: Activity, Liquidity, Solvency & Profitability 🧮 (LOS 37.b)

Ratios are typically grouped by what they measure:

#### **2.1 Ratio Categories Overview**

> **💡 MNEMONIC: "ALPS" for Main Ratio Categories**
> - **A**ctivity (efficiency/turnover ratios)
> - **L**iquidity (short-term solvency)
- **P**rofitability (margins & returns)
- **S**olvency (long-term leverage & coverage)

#### **2.2 Activity Ratios (Efficiency/Turnover)**

These show how efficiently a company manages its assets. Generally, higher turnover is better (means assets are working harder to generate sales), but context is key.

* **Inventory Turnover:** `COGS / Average Inventory`
    * Measures how quickly inventory is sold.
* **Days of Inventory on Hand (DOH):** `365 / Inventory Turnover`
    * Average days inventory sits before being sold. Too high = slow sales/obsolescence risk; too low = potential stockouts.
* **Receivables Turnover:** `Revenue / Average Accounts Receivable`
    * Measures how quickly credit sales are collected.
* **Days of Sales Outstanding (DSO):** `365 / Receivables Turnover`
    * Average days to collect cash after a sale. Too high = poor collection/credit risk; too low = overly strict credit terms losing sales.
* **Payables Turnover:** `Purchases / Average Accounts Payable`
    * Measures how quickly the company pays its suppliers. (*Note: Purchases = Ending Inventory - Beginning Inventory + COGS*).
* **Number of Days of Payables:** `365 / Payables Turnover`
    * Average days the company takes to pay suppliers. Too high = trouble paying bills?; too low = not using available supplier credit effectively.
* **Working Capital Turnover:** `Revenue / Average Working Capital`
    * How effectively working capital (Current Assets - Current Liabilities) generates sales. High is good, but can be volatile if working capital is near zero.
* **Fixed Asset Turnover:** `Revenue / Average Net Fixed Assets`
    * Measures sales generated per unit of fixed assets (PP&E).
* **Total Asset Turnover:** `Revenue / Average Total Assets`
    * Overall efficiency in using all assets to generate sales.

#### **2.3 Liquidity Ratios**

These measure the company's ability to meet its short-term obligations. 💧

* **Current Ratio:** `Current Assets / Current Liabilities`
    * Most common measure. Higher = more liquid. < 1.0 suggests potential trouble.
* **Quick Ratio (Acid-Test):** `(Cash + Short-term Marketable Securities + Receivables) / Current Liabilities`
    * Stricter measure, excludes inventory (less liquid).
* **Cash Ratio:** `(Cash + Short-term Marketable Securities) / Current Liabilities`
    * Most conservative measure.
* **Defensive Interval Ratio:** `(Cash + Short-term Marketable Securities + Receivables) / Average Daily Expenditures`
    * Days the company can operate using only its current liquid assets.
* **Cash Conversion Cycle (CCC):** `DOH + DSO - Number of Days of Payables`
    * Length of time from paying cash for inventory to receiving cash from customers. Shorter is generally better (less cash tied up).

#### **2.4 Solvency Ratios (Leverage)**

These measure the company's ability to meet long-term obligations and its use of debt financing. 🏛️

* **Debt Ratios:** Measure leverage.
    * **Debt-to-Assets:** `Total Debt / Total Assets`
    * **Debt-to-Capital:** `Total Debt / (Total Debt + Total Shareholders' Equity)`
    * **Debt-to-Equity:** `Total Debt / Total Shareholders' Equity`
    * **Financial Leverage Ratio:** `Average Total Assets / Average Total Equity` (Higher = more leverage)
    * *Note: "Total Debt" usually means interest-bearing debt, but definitions vary. Check the specifics\!*
* **Coverage Ratios:** Measure ability to cover debt payments.
    * **Interest Coverage Ratio (TIE):** `EBIT / Interest Payments`
        * How many times earnings before interest and taxes can cover interest expense. Higher is better.
    * **Fixed Charge Coverage Ratio:** `(EBIT + Lease Payments) / (Interest Payments + Lease Payments)`
        * Broader measure including lease payments (another fixed obligation). Higher is better.

#### **2.5 Profitability Ratios**

These measure the company's ability to generate profits from its sales and investments. 💰

* **Return on Sales:**
    * **Gross Profit Margin:** `Gross Profit / Revenue`
    * **Operating Profit Margin:** `Operating Profit (EBIT) / Revenue`
    * **Pretax Margin:** `EBT (Earnings Before Tax) / Revenue`
    * **Net Profit Margin:** `Net Income / Revenue`
* **Return on Investment:**
    * **Operating ROA:** `Operating Income / Average Total Assets`
    * **Return on Assets (ROA):** `Net Income / Average Total Assets`
    * **Return on Total Capital (ROTC):** `EBIT / Average Total Capital (Debt + Equity)`
    * **Return on Equity (ROE):** `Net Income / Average Total Equity`
    * **Return on Common Equity:** `(Net Income - Preferred Dividends) / Average Common Equity`
        * Focuses specifically on returns to common shareholders.

> [\!TIP]
> **CFA Exam Tip ✍️:** Memorizing the formulas is essential, but *understanding what each ratio measures* and whether a higher/lower value is generally better is more important. Be prepared to calculate ratios and interpret their meaning in context (e.g., comparing to industry averages or historical trends). Watch out for slight variations in definitions (e.g., "Total Debt").

-----

### Part 3: Connecting the Dots: Relationships Among Ratios 🔗 (LOS 37.c)

Ratios don't exist in a vacuum. Analyzing them together provides a richer picture.

* **Example 1:** If the **Current Ratio** is rising but the **Quick Ratio** is falling, what does it suggest? It likely means inventory is building up relative to other current assets and liabilities. This could signal slowing sales or poor inventory management.
* **Example 2:** If **Receivables Turnover** is high (low DSO) but **Revenue Growth** is slow compared to peers, it might indicate credit policies are too strict, potentially costing sales.
* **Example 3:** High **Financial Leverage** can boost **ROE** (as we'll see in DuPont analysis), but it also increases risk, which might be visible in lower **Interest Coverage Ratios**.

**Evaluating a Company:** The process involves comparing a company's ratios to:

1.  **Its own historical performance (Time-Series):** Are things getting better or worse?
2.  **Industry peers or averages (Cross-Sectional):** How does it stack up against competitors?

#### **Theory: Evaluation Example 🧠**

Let's say Company X has:

* Current Ratio: 2.5 (Industry Avg: 2.0) - Good liquidity.
* Total Asset Turnover: 1.2 (Industry Avg: 1.8) - Poor asset efficiency.
* Net Profit Margin: 8% (Industry Avg: 10%) - Lower profitability on sales.
* Debt-to-Equity: 0.9 (Industry Avg: 0.5) - Higher leverage.
* ROE: 15% (Industry Avg: 14%) - Higher return to shareholders.

**Interpretation:** Company X achieves a slightly higher ROE than the industry, but this seems driven by higher leverage rather than operational efficiency (low turnover) or profit margins. The high leverage increases risk. The low turnover and margins need investigation.

> [\!TIP]
> **CFA Exam Tip ✍️:** Exam questions often present a set of ratios and ask for an overall assessment or explanation of trends. Focus on identifying *conflicting signals* (like rising current ratio but falling quick ratio) and synthesizing the information to draw a conclusion.

-----

### Part 4: Decomposing ROE: The DuPont Analysis ✨ (LOS 37.d)

> **💡 MNEMONIC: "ROE = PaTaL" (3-Part DuPont)**
> - **P**rofitability (Net Profit Margin)
> - **T**urnover (Asset Turnover - efficiency)
> - **L**everage (Financial Leverage/Equity Multiplier)
> 
> For 5-Part, add: **T**ax burden + **I**nterest burden before margins

**DuPont analysis** breaks down Return on Equity (ROE) into its component parts, showing *how* a company achieves its return.

**1. The Original 3-Part DuPont:**

$$\text{ROE} = \left(\frac{\text{Net Income}}{\text{Revenue}}\right) \times \left(\frac{\text{Revenue}}{\text{Average Total Assets}}\right) \times \left(\frac{\text{Average Total Assets}}{\text{Average Total Equity}}\right)$$

$$\text{ROE} = (\text{Net Profit Margin}) \times (\text{Total Asset Turnover}) \times (\text{Financial Leverage Ratio})$$

* This shows ROE is driven by:
    * **Profitability** (Net Profit Margin)
    * **Efficiency** (Total Asset Turnover)
    * **Leverage** (Financial Leverage Ratio or Equity Multiplier)
* A company can increase ROE by improving any of these components. However, increasing leverage also increases risk.

**2. The Extended 5-Part DuPont:**

This further breaks down the Net Profit Margin:

$$\text{ROE} = \left(\frac{\text{Net Income}}{\text{EBT}}\right) \times \left(\frac{\text{EBT}}{\text{EBIT}}\right) \times \left(\frac{\text{EBIT}}{\text{Revenue}}\right) \times \left(\frac{\text{Revenue}}{\text{Average Total Assets}}\right) \times \left(\frac{\text{Average Total Assets}}{\text{Average Total Equity}}\right)$$

$$\text{ROE} = (\text{Tax Burden}) \times (\text{Interest Burden}) \times (\text{EBIT Margin}) \times (\text{Total Asset Turnover}) \times (\text{Financial Leverage Ratio})$$

* **Tax Burden:** `Net Income / EBT` (Lower tax rate = lower burden = higher ROE). Reflects how much profit is kept after tax. (1 - Tax Rate)
* **Interest Burden:** `EBT / EBIT` (Lower interest expense = lower burden = higher ROE). Reflects how much profit remains after interest.
* **EBIT Margin:** `EBIT / Revenue` (Operating profitability).

* This 5-part breakdown provides deeper insight into how taxes, interest expense, and operating margins contribute to ROE.

#### **Example: 3-Part DuPont 🧮**

Company Y has: Net Income = $10M, Revenue = $100M, Avg Assets = $50M, Avg Equity = $20M.

* ROE = $10M / $20M = 50%
* Net Profit Margin = $10M / $100M = 10%
* Total Asset Turnover = $100M / $50M = 2.0x
* Financial Leverage = $50M / $20M = 2.5x
* DuPont Check: 10% * 2.0 * 2.5 = 50%

#### **Global & Local Context 🌍**

* **Global Example:** Comparing the DuPont components of Coca-Cola vs. PepsiCo to see if differences in ROE are driven by margins (branding power?), turnover (distribution efficiency?), or leverage (capital structure choices).
* **Indian Example:** Analyzing the DuPont breakdown for Tata Motors vs. Maruti Suzuki. Is one company's higher ROE due to better operating margins from its product mix, more efficient use of its manufacturing plants (turnover), or a different financing strategy (leverage)?

> [\!TIP]
> **CFA Exam Tip ✍️:** Be comfortable calculating and interpreting both the 3-part and 5-part DuPont equations. Understand what each component represents (profitability, efficiency, leverage, tax burden, interest burden). Questions often ask *why* ROE changed by analyzing changes in the DuPont components.

-----

### Part 5: Beyond the Basics: Industry-Specific Ratios & Forecasting 🏭 (LOS 37.e, 37.f)

While the core ratios apply broadly, some industries have specific metrics analysts focus on:

* **Retail/Restaurants:** **Same-store sales** growth (excludes impact of new store openings). Sales per square foot.
* **Service/Consulting:** Net income per employee, sales per employee.
* **Financial Institutions:** **Net interest margin**, **capital adequacy ratios** (e.g., Tier 1 capital ratio), **loan loss provisions**.
* **Real Estate:** **Funds from operations (FFO)**, Occupancy rates.

**Business Risk Measures:** Standard deviation of revenue, operating income, or net income (often expressed as **coefficient of variation** = standard deviation / mean) can indicate volatility.

**Using Ratios for Forecasting:**

* Historical ratios (like profit margins or turnover) can be used as a starting point to forecast future performance, often in conjunction with sales forecasts.
* Analysts might assume ratios will revert to historical or industry averages over time.
* **Sensitivity Analysis:** Changing one assumption (e.g., sales growth) to see the impact on forecasted net income.
* **Scenario Analysis:** Examining outcomes based on different sets of assumptions (e.g., recession vs. boom).
* **Simulation:** Using probability distributions for key variables to generate a distribution of possible outcomes.

> [\!TIP]
> **CFA Exam Tip ✍️:** You don't need to memorize dozens of obscure industry ratios for Level 1, but be aware that specific industries have key performance indicators beyond the standard set. Understand how historical ratio analysis forms the basis for forecasting future results.

-----

### 🧪 Formula Summary

**Activity Ratios:**

* Inventory Turnover: $$\frac{\text{COGS}}{\text{Average Inventory}}$$
* DOH: $$\frac{365}{\text{Inventory Turnover}}$$
* Receivables Turnover: $$\frac{\text{Revenue}}{\text{Average Receivables}}$$
* DSO: $$\frac{365}{\text{Receivables Turnover}}$$
* Payables Turnover: $$\frac{\text{Purchases}}{\text{Average Payables}}$$
* Days of Payables: $$\frac{365}{\text{Payables Turnover}}$$
* Working Capital Turnover: $$\frac{\text{Revenue}}{\text{Average Working Capital}}$$
* Fixed Asset Turnover: $$\frac{\text{Revenue}}{\text{Average Net Fixed Assets}}$$
* Total Asset Turnover: $$\frac{\text{Revenue}}{\text{Average Total Assets}}$$

**Liquidity Ratios:**

* Current Ratio: $$\frac{\text{Current Assets}}{\text{Current Liabilities}}$$
* Quick Ratio: $$\frac{\text{Cash + Marketable Securities + Receivables}}{\text{Current Liabilities}}$$
* Cash Ratio: $$\frac{\text{Cash + Marketable Securities}}{\text{Current Liabilities}}$$
* Defensive Interval: $$\frac{\text{Cash + Marketable Securities + Receivables}}{\text{Average Daily Expenditures}}$$
* Cash Conversion Cycle: $$DOH + DSO - \text{Days of Payables}$$

**Solvency Ratios:**

* Debt-to-Assets: $$\frac{\text{Total Debt}}{\text{Total Assets}}$$
* Debt-to-Capital: $$\frac{\text{Total Debt}}{\text{Total Debt + Total Equity}}$$
* Debt-to-Equity: $$\frac{\text{Total Debt}}{\text{Total Equity}}$$
* Financial Leverage: $$\frac{\text{Average Total Assets}}{\text{Average Total Equity}}$$
* Interest Coverage (TIE): $$\frac{\text{EBIT}}{\text{Interest Payments}}$$
* Fixed Charge Coverage: $$\frac{\text{EBIT + Lease Payments}}{\text{Interest Payments + Lease Payments}}$$

**Profitability Ratios:**

* Gross Profit Margin: $$\frac{\text{Gross Profit}}{\text{Revenue}}$$
* Operating Profit Margin: $$\frac{\text{Operating Income (EBIT)}}{\text{Revenue}}$$
* Pretax Margin: $$\frac{\text{EBT}}{\text{Revenue}}$$
* Net Profit Margin: $$\frac{\text{Net Income}}{\text{Revenue}}$$
* Operating ROA: $$\frac{\text{Operating Income}}{\text{Average Total Assets}}$$
* ROA: $$\frac{\text{Net Income}}{\text{Average Total Assets}}$$
* ROTC: $$\frac{\text{EBIT}}{\text{Average Total Capital}}$$
* ROE: $$\frac{\text{Net Income}}{\text{Average Total Equity}}$$
* Return on Common Equity: $$\frac{\text{Net Income - Preferred Dividends}}{\text{Average Common Equity}}$$

**DuPont Analysis:**

* 3-Part: $$ROE = (\text{Net Profit Margin}) \times (\text{Asset Turnover}) \times (\text{Leverage})$$
* 5-Part: $$ROE = (\text{Tax Burden}) \times (\text{Interest Burden}) \times (\text{EBIT Margin}) \times (\text{Asset Turnover}) \times (\text{Leverage})$$

-----

> [\!IMPORTANT]
>
> ### 🎯 Quick Exam-Day Pointers
>
> * **Know the Categories:** Understand what Activity, Liquidity, Solvency, and Profitability ratios measure.
> * **Interpretation is Key:** Don't just calculate; understand if higher/lower is generally better and what the ratio tells you about the company's performance or risk.
> * **Context Matters:** Compare ratios to history and industry peers. A ratio in isolation is meaningless.
> * **DuPont Decomposition:** Master the 3-part and 5-part DuPont analysis to understand the *drivers* of ROE (Profitability, Efficiency, Leverage, Tax Burden, Interest Burden).
> * **Ratio Relationships:** Think about how different ratios interact (e.g., leverage boosting ROE but potentially hurting coverage ratios).
> * **Limitations:** Remember that different accounting policies can distort comparisons, and ratios are just one piece of the puzzle.