## <span style="color: #1565C0;">Reading 1: Rates and Returns</span>

### 🎯 Introduction

Welcome, future charterholder! Think of **returns** like measuring a car's performance. 🚗💨 You could measure its speed at one specific moment (**holding period return**), its average speed over a whole trip (**arithmetic mean**), or the steady speed you would have needed to finish in the same amount of time (**geometric mean**). This reading is your dashboard for understanding and calculating all the different ways we measure **investment performance**. We'll learn how to break down an **interest rate** into its core components, compare different types of returns, and make sure we're always comparing apples to apples. Let's start the engine!

-----

### <span style="color: #1565C0;">Part 1: What's Inside an Interest Rate & How Do We Measure Returns? 🔬</span>

An <b>interest rate</b> isn't just a single number; it's a bundle of expectations and compensations for risk. It can be seen in three ways:
  * <b>Required rate of return</b>: The minimum return you need to justify making an investment.
  * <b>Discount rate</b>: The rate used to calculate the present value of future cash flows.
  * <b>Opportunity cost</b>: The return you give up by spending your money today instead of saving and investing it.

The interest rates you see in the market (<b>nominal rates</b>) are built from several layers, like a cake 🎂.

  1.  <b>Real Risk-Free Rate</b>: This is the pure time value of money, assuming zero inflation and zero risk. It's the compensation you demand just for waiting, without any other worries.
  2.  <b>Inflation Premium</b>: This is the extra return you need to protect your purchasing power from being eroded by expected <b>inflation</b>.
  3.  <b>Default Risk Premium</b>: Compensation for the risk that the borrower won't pay you back.
  4.  <b>Liquidity Premium</b>: Compensation for the risk that you can't sell your investment quickly at a fair price.
  5.  <b>Maturity Premium</b>: Extra return for tying up your money in a longer-term bond, which is more sensitive to interest rate changes.

So, the formula is: <b>Nominal Rate</b> = Real Risk-Free Rate + Inflation Premium + Default Risk Premium + Liquidity Premium + Maturity Premium.

#### <span style="color: #6A1B9A;">1.1 Basic Return: The Holding Period Return (HPR)</span>

The most fundamental return measure is the <b>holding period return (HPR)</b>. It's the total return you earned over the time you held an investment.

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$HPR = \frac{P_1 - P_0 + Div_1}{P_0}$$

</div>

Where:
  * $P_1$ = Price at the end of the period
  * $P_0$ = Price at the beginning of the period
  * $Div_1$ = Dividend or income received during the period

#### <span style="color: #6A1B9A;">1.2 Averaging Returns: Which Mean to Use? 🤔</span>

When you have returns over multiple periods, there are a few ways to find the "average."

##### <span style="color: #E65100;">1.2.1 Theory 🧠</span>

  * <b>Arithmetic Mean</b>: The simple average. Just add up the returns and divide by the number of periods. It's the best guess for a <b>single period's</b> return in the future but can be misleading over multiple periods.
  * <b>Geometric Mean</b>: This is your compound growth rate. It tells you what you <b>actually</b> earned per year, on average, over the entire time. Because it accounts for compounding, it's always less than or equal to the arithmetic mean.
  * <b>Harmonic Mean</b>: This is a special-purpose average. It's perfect for figuring out the average cost per share when you invest a fixed amount of money at regular intervals (like in a Systematic Investment Plan or SIP).

##### <span style="color: #E65100;">1.2.2 Example 🧮</span>

Let's say you invested in a stock with the following annual returns:
  * Year 1: +20%
  * Year 2: -10%
  * Year 3: +15%

**Arithmetic Mean**: `(20% - 10% + 15%) / 3 = 8.33%`

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\text{Geometric Mean} = \sqrt[{(1+0.20)(1-0.10)(1+0.15)} - 1 = \sqrt[{(1.2)(0.9)(1.15)} - 1 = 7.46\%$$

</div>

Notice the geometric mean is lower! It reflects the true compounded growth of your investment.

Now, imagine you invest ₹1,000 each month in a mutual fund. The prices per unit are ₹10, ₹12, and ₹14. What's the average price you paid?

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\text{Harmonic Mean} = \frac{3}{\frac{1}{10} + \frac{1}{12} + \frac{1}{14}} = \frac{3}{0.1 + 0.0833 + 0.0714} \approx 11.75$$

</div>

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️:For returns over time, the <b>geometric mean</b> is the more accurate measure of past performance. The <b>arithmetic mean</b> is statistically the best estimator of the <b>next</b> period's return. The exam loves to test this distinction. Also, remember the hierarchy: For volatile returns, <b>Arithmetic Mean</b> > <b>Geometric Mean</b> > <b>Harmonic Mean</b>.

</div>
</div>

-----

### <span style="color: #1565C0;">Part 2: Whose Return Is It Anyway? Money-Weighted vs. Time-Weighted ⏱️</span>

When a portfolio has cash flowing in and out (like when a client adds or withdraws money), the way we calculate returns gets tricky. The two main methods give very different answers because they measure different things.

#### <span style="color: #6A1B9A;">2.1 Money-Weighted Return 💰</span>

The <b>money-weighted rate of return (MWRR)</b> measures the performance of the <b>investor's money</b>. It's simply the <b>Internal Rate of Return (IRR)</b> of the portfolio, considering all cash inflows (deposits, initial investment) and outflows (withdrawals, final value).

  * <b>What it measures:</b> The actual return earned by the investor.
  * <b>Sensitive to:</b> The timing and size of cash flows. If an investor adds a lot of money right before a market rally, their MWRR will be high. If they add money right before a crash, their MWRR will be low.
  * <b>Best for:</b> Evaluating an investor's own performance, especially when they control the timing of cash flows.

#### <span style="color: #6A1B9A;">2.2 Time-Weighted Return ⏳</span>

The <b>time-weighted rate of return (TWRR)</b> measures the performance of the <b>portfolio manager's strategy</b>, stripping out the effects of cash flows. It calculates the compound growth rate of $1 invested in the portfolio.

  * <b>How it works:</b>
    * Break the total period into sub-periods every time there's a significant cash flow.
    * Calculate the HPR for each sub-period.
    * Link the sub-period returns together geometrically: $(1+HPR_1) \times (1+HPR_2) \times ... \times (1+HPR_n) - 1$.
  * <b>What it measures:</b> The performance of the fund manager's investment decisions.
  * <b>Sensitive to:</b> Only the manager's skill. It's not affected by when clients add or withdraw money.
  * <b>Best for:</b> Comparing the performance of different fund managers. This is the industry standard (required by GIPS).

#### <span style="color: #00838F;">2.3 Global & Local Context 🌍</span>

A global investment firm like BlackRock must report <b>time-weighted returns</b> to clients when showing the performance of its mutual funds. This ensures that a fund's track record isn't unfairly boosted just because a lot of new money happened to come in at a lucky time. An Indian AMC like HDFC Mutual Fund does the same, allowing investors to compare the HDFC Flexi Cap Fund against the ICICI Prudential Bluechip Fund based on the manager's skill, not the flow of investor money.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️:If a portfolio manager has <b>no control</b> over the timing of cash flows, the <b>time-weighted return</b> is the appropriate measure of their performance. If the investor <b>does</b> have control (e.g., managing their own personal account), the <b>money-weighted return</b> is more appropriate to measure their personal result.

</div>
</div>

-----

### <span style="color: #1565C0;">Part 3: Apples to Apples: Standardizing & Refining Returns 🍎</span>

To compare investments or understand performance properly, we often need to adjust the raw HPR.

  * <b>Annualized Return</b>: To compare returns over different time periods (e.g., 90 days vs. 500 days), we convert them to an annual basis.

    <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
    $$Annualized~Return = (1 + HPR)^{\frac{365}{days}} - 1$$
    </div>

  * <b>Continuously Compounded Return</b>: This is a special type of return used in complex financial models, especially for derivatives. It's calculated using the natural logarithm. A key feature is that continuously compounded returns are additive over time.

    <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
    $$R_{cc} = \ln(1+HPR)$$
    </div>

  * <b>Other Key Return Measures</b>:
    * <b>Gross Return vs. Net Return</b>: <b>Gross return</b> is the total return <b>before</b> deducting management fees and administrative costs. <b>Net return</b> is what's left <b>after</b> those fees are taken out. Trading commissions are deducted for both.
    * <b>Pretax vs. After-Tax Return</b>: Returns can be stated before or after taxes are paid.
    * <b>Real Return vs. Nominal Return</b>: <b>Nominal return</b> is the simple percentage gain. <b>Real return</b> is the nominal return adjusted for inflation, showing the true increase in your purchasing power.

      <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
      $$\text{Real Return} \approx \text{Nominal Return} - \text{Inflation Rate}$$
      </div>

    * <b>Leveraged Return</b>: This is the return on a position that was funded with borrowed money (leverage). Leverage magnifies both gains and losses. A common example is buying real estate with a mortgage.

#### <span style="color: #00838F;">3.1 Global & Local Context 🌍</span>

If you earned a <b>nominal return</b> of 12% on your investment in the Nifty 50 index, but inflation in India for that year was 5%, your <b>real return</b> (your actual increase in purchasing power) was approximately 7%. Similarly, an investor in the US earning 8% on the S&P 500 with 3% inflation has a real return of about 5%. This shows why comparing returns across countries requires looking at real returns.

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Holding Period Return (HPR):**

$$HPR = \frac{P_1 - P_0 + Div_1}{P_0}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Arithmetic Mean Return:**

$$\bar{R} = \frac{\sum_{i=1}^{n} R_i}{n}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Geometric Mean Return:**

$$R_G = [\prod_{i=1}^{n} (1+R_i)]^{1/n} - 1$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Harmonic Mean:**

$$\bar{X}_H = \frac{N}{\sum_{i=1}^{N} \frac{1}{X_i}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Annualized Return:**

$$Annualized~Return = (1 + HPR)^{\frac{365}{days}} - 1$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Continuously Compounded Return:**

$$R_{cc} = \ln(1+HPR)$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Exact Real Return:**

$$\text{Real Return} = \frac{(1 + \text{Nominal Return})}{(1 + \text{Inflation Rate})} - 1$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Leveraged Return (on equity):**

$$Leveraged~Return = \frac{r(V_0 + V_B) - r_B V_B}{V_0}$$

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

  * <b>TWR vs. MWR is critical!</b> <b>Time-Weighted Return</b> measures the <b>manager's</b> skill and ignores cash flows. <b>Money-Weighted Return</b> measures the <b>investor's</b> actual outcome and is heavily influenced by cash flows.
  * <b>Know your means!</b> For performance over time, use the <b>Geometric Mean</b>. To forecast next period's return, use the <b>Arithmetic Mean</b>. For dollar-cost averaging, use the <b>Harmonic Mean</b>.
  * <b>Deconstruct the Nominal Rate.</b> Remember the building blocks: Real Risk-Free Rate + Premiums for Inflation, Default, Liquidity, and Maturity.
  * <b>Always Annualize.</b> When comparing returns over different periods, always convert them to an <b>annualized return</b> to make a fair comparison.
  * <b>Real Return Matters Most.</b> Your true gain is your <b>real return</b>, which is your nominal return minus the inflation rate. This measures your change in purchasing power.

</div>
</div>