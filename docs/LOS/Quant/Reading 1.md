## Reading 1: Rates and Returns

### 🎯 Introduction

Welcome, future charterholder! Think of returns like measuring a car's performance. 🚗💨 You could measure its speed at one specific moment (a holding period return), its average speed over a whole trip (arithmetic mean), or the steady speed you would have needed to finish in the same amount of time (geometric mean). This reading is your dashboard for understanding and calculating all the different ways we measure investment performance. We'll learn how to break down an interest rate into its core components, compare different types of returns, and make sure we're always comparing apples to apples. Let's start the engine!

***

### Part 1: What's Inside an Interest Rate & How Do We Measure Returns? 🔬

An **interest rate** isn't just a single number; it's a bundle of expectations and compensations for risk. It can be seen in three ways:
* A **required rate of return**: The minimum return you need to justify making an investment.
* A **discount rate**: The rate used to calculate the present value of future cash flows.
* An **opportunity cost**: The return you give up by spending your money today instead of saving and investing it.

The interest rates you see in the market (**nominal rates**) are built from several layers, like a cake 🎂.

1.  **Real Risk-Free Rate**: This is the pure time value of money, assuming zero inflation and zero risk. It's the compensation you demand just for waiting, without any other worries.
2.  **Inflation Premium**: This is the extra return you need to protect your purchasing power from being eroded by expected **inflation**.
3.  **Default Risk Premium**: Compensation for the risk that the borrower won't pay you back.
4.  **Liquidity Premium**: Compensation for the risk that you can't sell your investment quickly at a fair price.
5.  **Maturity Premium**: Extra return for tying up your money in a longer-term bond, which is more sensitive to interest rate changes.

So, the formula is: **Nominal Rate** = Real Risk-Free Rate + Inflation Premium + Default Risk Premium + Liquidity Premium + Maturity Premium.

#### **Basic Return: The Holding Period Return (HPR)**

The most fundamental return measure is the **holding period return (HPR)**. It's the total return you earned over the time you held an investment.

$$HPR = \frac{P_1 - P_0 + Div_1}{P_0}$$

Where:
* $P_1$ = Price at the end of the period
* $P_0$ = Price at the beginning of the period
* $Div_1$ = Dividend or income received during the period

#### **Averaging Returns: Which Mean to Use? 🤔**

When you have returns over multiple periods, there are a few ways to find the "average."

#### **Theory 🧠**

* **Arithmetic Mean**: The simple average. Just add up the returns and divide by the number of periods. It's the best guess for a *single period's* return in the future but can be misleading over multiple periods.
* **Geometric Mean**: This is your compound growth rate. It tells you what you *actually* earned per year, on average, over the entire time. Because it accounts for compounding, it's always less than or equal to the arithmetic mean.
* **Harmonic Mean**: This is a special-purpose average. It's perfect for figuring out the average cost per share when you invest a fixed amount of money at regular intervals (like in a Systematic Investment Plan or SIP).

#### **Example 🧮**

Let's say you invested in a stock with the following annual returns:
* Year 1: +20%
* Year 2: -10%
* Year 3: +15%

**Arithmetic Mean**: $\frac{(20\% - 10\% + 15\%)}{3} = 8.33\%$

**Geometric Mean**: $\sqrt[3]{(1+0.20)(1-0.10)(1+0.15)} - 1 = \sqrt[3]{(1.2)(0.9)(1.15)} - 1 = 7.46\%$

Notice the geometric mean is lower! It reflects the true compounded growth of your investment.

Now, imagine you invest ₹1,000 each month in a mutual fund. The prices per unit are ₹10, ₹12, and ₹14. What's the average price you paid?

**Harmonic Mean**: $\frac{3}{\frac{1}{10}+\frac{1}{12}+\frac{1}{14}} = \frac{3}{0.1 + 0.0833 + 0.0714} = ₹11.75$

> [\!TIP]
> **CFA Exam Tip ✍️:** For returns over time, the **geometric mean** is the more accurate measure of past performance. The **arithmetic mean** is statistically the best estimator of the *next* period's return. The exam loves to test this distinction. Also, remember the hierarchy: For volatile returns, **Arithmetic Mean > Geometric Mean > Harmonic Mean**.

***

### Part 2: Whose Return Is It Anyway? Money-Weighted vs. Time-Weighted ⏱️

When a portfolio has cash flowing in and out (like when a client adds or withdraws money), the way we calculate returns gets tricky. The two main methods give very different answers because they measure different things.

#### **Money-Weighted Return 💰**

The **money-weighted rate of return (MWRR)** measures the performance of the *investor's money*. It's simply the **Internal Rate of Return (IRR)** of the portfolio, considering all cash inflows (deposits, initial investment) and outflows (withdrawals, final value).

* **What it measures:** The actual return earned by the investor.
* **Sensitive to:** The timing and size of cash flows. If an investor adds a lot of money right before a market rally, their MWRR will be high. If they add money right before a crash, their MWRR will be low.
* **Best for:** Evaluating an investor's own performance, especially when they control the timing of cash flows.

#### **Time-Weighted Return ⏳**

The **time-weighted rate of return (TWRR)** measures the performance of the *portfolio manager's strategy*, stripping out the effects of cash flows. It calculates the compound growth rate of $1 invested in the portfolio.

* **How it works:**
    1.  Break the total period into sub-periods every time there's a significant cash flow.
    2.  Calculate the HPR for each sub-period.
    3.  Link the sub-period returns together geometrically: $(1+HPR_1) \times (1+HPR_2) \times ... \times (1+HPR_n) - 1$.
* **What it measures:** The performance of the fund manager's investment decisions.
* **Sensitive to:** Only the manager's skill. It's not affected by when clients add or withdraw money.
* **Best for:** Comparing the performance of different fund managers. This is the industry standard (required by GIPS).

#### **Global & Local Context 🌍**

A global investment firm like BlackRock must report **time-weighted returns** to clients when showing the performance of its mutual funds. This ensures that a fund's track record isn't unfairly boosted just because a lot of new money happened to come in at a lucky time. An Indian AMC like HDFC Mutual Fund does the same, allowing investors to compare the HDFC Flexi Cap Fund against the ICICI Prudential Bluechip Fund based on the manager's skill, not the flow of investor money.

> [\!TIP]
> **CFA Exam Tip ✍️:** If a portfolio manager has **no control** over the timing of cash flows, the **time-weighted return** is the appropriate measure of their performance. If the investor *does* have control (e.g., managing their own personal account), the **money-weighted return** is more appropriate to measure their personal result.

***

### Part 3: Apples to Apples: Standardizing & Refining Returns 🍎

To compare investments or understand performance properly, we often need to adjust the raw HPR.

* **Annualized Return**: To compare returns over different time periods (e.g., 90 days vs. 500 days), we convert them to an annual basis.
    $$Annualized~Return = (1 + HPR)^{\frac{365}{days}} - 1$$

* **Continuously Compounded Return**: This is a special type of return used in complex financial models, especially for derivatives. It's calculated using the natural logarithm. A key feature is that continuously compounded returns are additive over time.
    $$R_{cc} = \ln(1+HPR)$$

* **Other Key Return Measures**:
    * **Gross Return vs. Net Return**: **Gross return** is the total return *before* deducting management fees and administrative costs. **Net return** is what's left *after* those fees are taken out. Trading commissions are deducted for both.
    * **Pretax vs. After-Tax Return**: Returns can be stated before or after taxes are paid.
    * **Real Return vs. Nominal Return**: **Nominal return** is the simple percentage gain. **Real return** is the nominal return adjusted for inflation, showing the true increase in your purchasing power.
        $$Real~Return \approx Nominal~Return - Inflation~Rate$$
    * **Leveraged Return**: This is the return on a position that was funded with borrowed money (leverage). Leverage magnifies both gains and losses. A common example is buying real estate with a mortgage.

#### **Global & Local Context 🌍**

If you earned a **nominal return** of 12% on your investment in the Nifty 50 index, but inflation in India for that year was 5%, your **real return** (your actual increase in purchasing power) was approximately 7%. Similarly, an investor in the US earning 8% on the S&P 500 with 3% inflation has a real return of about 5%. This shows why comparing returns across countries requires looking at real returns.

***

### 🧪 Formula Summary

* **Holding Period Return (HPR)**: $$HPR = \frac{P_1 - P_0 + Div_1}{P_0}$$
* **Arithmetic Mean Return**: $$\bar{R} = \frac{\sum_{i=1}^{n} R_i}{n}$$
* **Geometric Mean Return**: $$R_G = [\prod_{i=1}^{n} (1+R_i)]^{1/n} - 1$$
* **Harmonic Mean**: $$\bar{X}_H = \frac{N}{\sum_{i=1}^{N} \frac{1}{X_i}}$$
* **Annualized Return**: $$Annualized~Return = (1 + HPR)^{\frac{365}{days}} - 1$$
* **Continuously Compounded Return**: $$R_{cc} = \ln(1+HPR)$$
* **Exact Real Return**: $$Real~Return = \frac{(1 + Nominal~Return)}{(1 + Inflation~Rate)} - 1$$
* **Leveraged Return (on equity)**: $$Leveraged~Return = \frac{r(V_0 + V_B) - r_B V_B}{V_0}$$

***

> [\!IMPORTANT]
>
> ### 🎯 Quick Exam-Day Pointers
>
> * **TWR vs. MWR is critical\!** **Time-Weighted Return** measures the *manager's* skill and ignores cash flows. **Money-Weighted Return** measures the *investor's* actual outcome and is heavily influenced by cash flows.
> * **Know your means!** For performance over time, use the **Geometric Mean**. To forecast next period's return, use the **Arithmetic Mean**. For dollar-cost averaging, use the **Harmonic Mean**.
> * **Deconstruct the Nominal Rate.** Remember the building blocks: Real Risk-Free Rate + Premiums for Inflation, Default, Liquidity, and Maturity.
> * **Always Annualize.** When comparing returns over different periods, always convert them to an **annualized return** to make a fair comparison.
> * **Real Return Matters Most.** Your true gain is your **real return**, which is your nominal return minus the inflation rate. This measures your change in purchasing power.