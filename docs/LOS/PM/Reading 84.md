Here is a detailed summary of Reading 84, crafted in the style of your "CFA Samurai" persona.

-----

## Reading 84: Portfolio Risk and Return: Part II ⚔️

### 🎯 Introduction

Greetings, Samurai. In our last lesson (Reading 83), we learned to forge a portfolio of risky assets, creating the **Efficient Frontier**. We learned that by combining assets, we can reduce risk.

Now, we complete our training. We introduce the ultimate weapon: the **risk-free asset**. Combining this with our risky portfolio unlocks a new level of power, allowing us to create a *single straight line* of optimal portfolios. This reading is the final step. We will build the legendary **Capital Market Line (CML)**, forge the **Security Market Line (SML)**, and learn the sacred equation that prices *all* assets in the universe: the **Capital Asset Pricing Model (CAPM)**. Finally, we'll learn the techniques to judge another manager's skill (Alpha).

This is the heart of modern portfolio theory. Pay close attention.

-----

### <span style="color: #1565C0;">Part 1: The Capital Allocation & Market Lines (LOS 84.a, 84.b)</span>

This is where we unite the two worlds: the risky and the risk-free.

#### <span style="color: #6A1B9A;">1.1 Combining Risky and Risk-Free Assets (LOS 84.a)</span>

When we combine a risky portfolio (Portfolio P) with a risk-free asset (like a T-bill), we get a powerful result.

  * The risk-free asset has zero standard deviation and zero correlation with *everything*.
  * Because of this, the math simplifies perfectly. The new portfolio's expected return and risk (standard deviation) are just the weighted averages of the two.
  * This creates a **straight line** of possible portfolios, connecting the risk-free asset to the risky portfolio. This line is called the **Capital Allocation Line (CAL)**.

#### <span style="color: #6A1B9A;">1.2 The Capital Allocation Line (CAL)</span>

The CAL shows all possible combinations of the risk-free asset and *any* risky portfolio. An investor's "best" CAL is the one that gives them the highest utility (the line that is tangent to their highest indifference curve).

But... what if everyone was a master samurai?

#### <span style="color: #6A1B9A;">1.3 The Capital Market Line (CML) (LOS 84.b)</span>

We make a powerful assumption: **Homogeneous Expectations**. This means every investor in the market has the same estimates for risk, return, and correlation for all assets.

  * If everyone has the same inputs, everyone will arrive at the *same* Efficient Frontier.
  * Therefore, everyone will identify the *same single portfolio* as the **optimal risky portfolio**—the one that, when combined with the risk-free asset, creates the best possible CAL (the one tangent to the Efficient Frontier).
  * If *everyone* holds this same optimal risky portfolio, what must it be? It must be the **Market Portfolio**—a portfolio containing all risky assets in existence, weighted by their market value.

This one, true, optimal CAL for *all* investors is the **Capital Market Line (CML)**.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**🧮 The CML Equation:**
$$E(R_P) = R_f + \left[ \frac{E(R_M) - R_f}{\sigma_M} \right] \sigma_P$$

  * $E(R_P)$ = Your portfolio's expected return
  * $R_f$ = The risk-free rate
  * $E(R_M)$ = The market's expected return
  * $\sigma_M$ = The market's standard deviation (total risk)
  * $\sigma_P$ = Your portfolio's standard deviation (total risk)
  * The term $(E(R_M) - R_f)$ is the **Market Risk Premium**.
  * The term $\left[ \frac{E(R_M) - R_f}{\sigma_M} \right]$ is the "price of risk"—the extra return you get for each unit of market risk you take.

</div>
</div>

Any portfolio on the CML is an **efficient portfolio**.

  * Portfolios between $R_f$ and the Market Portfolio (M) are **lending portfolios** (you're lending money at $R_f$).
  * Portfolios to the right of M are **borrowing portfolios** (you're borrowing at $R_f$ to invest *more* than 100% in the market).

-----

### <span style="color: #1565C0;">Part 2: The Two Faces of Risk (LOS 84.c)</span>

A critical concept emerges. The CML plots returns against **Total Risk** ($\sigma$). But why? Because all portfolios on the CML are *perfectly diversified*. They have no wasted risk.

But what about a *single stock*? It has two types of risk:

1.  **Systematic Risk:**

      * Also called **market risk** or **nondiversifiable risk**.
      * This is risk from factors that affect *all* assets (e.g., GDP growth, interest rate changes).
      * This risk **cannot** be eliminated by diversification.
      * This is the *only* risk the market will pay you to take.

2.  **Nonsystematic Risk:**

      * Also called **unique risk**, **firm-specific risk**, or **diversifiable risk**.
      * This is risk specific to a single company (e.g., a failed drug trial, a factory fire, an accounting scandal).
      * This risk **can be eliminated for free** simply by building a diversified portfolio (as you add more stocks, the firm-specific good and bad news cancels out).

> **The Sacred Law of Risk:**
> Total Risk = Systematic Risk + Nonsystematic Risk 
>
> Because nonsystematic risk can be eliminated for free, **the market will NOT compensate you for bearing it**. The *only* risk that determines an asset's expected return is its **systematic risk**.

-----

### <span style="color: #1565C0;">Part 3: The CAPM and the SML (LOS 84.d, 84.e, 84.f, 84.g, 84.h)</span>

If total risk ($\sigma$) doesn't determine the return for a single stock, what does? **Systematic Risk**. How do we measure it? With **Beta**.

#### <span style="color: #6A1B9A;">3.1 Return-Generating Models (LOS 84.d)</span>

These are models used to estimate an asset's expected return based on various factors.

  * **Multifactor Models:** Use several factors (e.g., GDP, inflation, firm size) , 2085, 2091.
  * **Single-Index Model:** The simplest model. It assumes all systematic risk is captured by *one* factor: the market return.
      * $R_i = \alpha_i + \beta_i R_m + e_i$. This is the **market model**.

#### <span style="color: #6A1B9A;">3.2 Beta: The Measure of Systematic Risk (LOS 84.e)</span>

**Beta ($\beta$)** is the *only* risk measure that matters for expected return. It tells you how sensitive an asset's return is to the overall market's return.

  * $\beta = 1.0$: Asset moves perfectly with the market.
  * $\beta > 1.0$: Asset is *more* volatile than the market (e.g., luxury goods).
  * $\beta < 1.0$: Asset is *less* volatile than the market (e.g., utility companies).
  * $\beta = 0$: Asset is uncorrelated with the market (e.g., the risk-free asset).

**Calculating Beta:**
$$\beta_i = \frac{Cov_{i,m}}{\sigma_m^2} \quad \text{or} \quad \beta_i = \rho_{i,m} \left( \frac{\sigma_i}{\sigma_m} \right)$$

We estimate beta by running a regression of the asset's excess returns against the market's excess returns. The slope of that line is beta. That line is called the **Security Characteristic Line (SCL)**.

#### <span style="color: #6A1B9A;">3.3 The Capital Asset Pricing Model (CAPM) (LOS 84.f, 84.g)</span>

The CML was the line for *efficient* portfolios, using *total risk* ($\sigma$).
Now, we create a line for *all* assets, using *systematic risk* ($\beta$). This line is the **Security Market Line (SML)**, and its equation is the **CAPM**.

<div style="background-color: #F3E5F5; border-left: 5px solid #7B1FA2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**🧮 The CAPM Equation (The SML):**
$$E(R_i) = R_f + \beta_i[E(R_m) - R_f]$$


  * $E(R_i)$ = The asset's expected (or required) return.
  * $R_f$ = The risk-free rate.
  * $\beta_i$ = The asset's beta (its systematic risk).
  * $[E(R_m) - R_f]$ = The Market Risk Premium.

This equation tells you the **exact required return** an investor *should* demand for any asset, given its systematic risk.

</div>
</div>

#### <span style="color: #6A1B9A;">3.4 CML vs. SML: The Ultimate Showdown</span>

This is a favorite exam topic. Do not confuse them\!

| Feature | Capital Market Line (CML) | Security Market Line (SML) |
| :--- | :--- | :--- |
| **Equation** | $E(R_P) = R_f + \left[ \frac{E(R_M) - R_f}{\sigma_M} \right] \sigma_P$ | $E(R_i) = R_f + \beta_i[E(R_m) - R_f]$ |
| **Risk Measure (X-axis)** | **Total Risk** (Standard Deviation, $\sigma$)  | **Systematic Risk** (Beta, $\beta$)  |
| **What plots on it?** | Only **efficient portfolios** (the market portfolio + lending/borrowing). | **ALL assets and portfolios** (efficient or not). |
| **What does it do?** | Prices *efficient* portfolios. | Prices *all* individual assets and portfolios. |

#### <span style="color: #6A1B9A;">3.5 Applications: Finding Mispriced Stocks (LOS 84.h)</span>

We can use the SML to find opportunities\!

1.  **Calculate** the stock's required return using CAPM (the SML).
2.  **Estimate** the stock's *expected* return based on your own forecasts.
3.  **Compare:**
      * If **Expected Return > Required Return:** The stock plots *above* the SML. It is **UNDERVALUED** (a buy\!).
      * If **Expected Return < Required Return:** The stock plots *below* the SML. It is **OVERVALUED** (a sell/short\!).
      * If **Expected Return = Required Return:** The stock plots *on* the SML. It is **FAIRLY VALUED**.

<div style="background-color: #F3E5F5; border-left: 5px solid #7B1FA2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**🧠 Samurai Mnemonic: "Over is Under, Under is Over"**

  * If the stock's plot is **OVER** the SML, it is **UNDER**valued.
  * If the stock's plot is **UNDER** the SML, it is **OVER**valued.

</div>
</div>

-----

### <span style="color: #1565C0;">Part 4: Measuring the Samurai's Skill (LOS 84.i)</span>

Now that we have the SML as our benchmark for a "fair" return, we can *finally* measure an active manager's skill. Did they *really* "beat the market," or did they just take on more risk?

| Measure | Calculation | What it Measures | When to Use It |
| :--- | :--- | :--- | :--- |
| **Sharpe Ratio** | $\frac{R_P - R_f}{\sigma_P}$  | Excess return per unit of **Total Risk ($\sigma$)**. | When the portfolio is the *entire* investment (i.e., not diversified with other managers). |
| **M-squared ($M^2$)** | $(R_P - R_f) \frac{\sigma_M}{\sigma_P} + R_f$  | Same as Sharpe, but stated in **% return**. It finds the return of a portfolio that was leveraged/deleveraged to have the *same risk as the market*. Ranks are identical to Sharpe. | Same as Sharpe. Good for explaining to clients. |
| **Treynor Ratio** | $\frac{R_P - R_f}{\beta_P}$  | Excess return per unit of **Systematic Risk ($\beta$)**. | When the portfolio is *part of a larger, well-diversified fund* (i.e., we only care about its systematic risk contribution). |
| **Jensen's Alpha ($\alpha$)** | $\alpha_P = R_P - [R_f + \beta_P(R_M - R_f)]$  | The **% return above** what the CAPM/SML predicted. A positive alpha means the manager "beat" their required return. | Same as Treynor. It's the literal distance the portfolio plots above (positive alpha) or below (negative alpha) the SML. |

-----

### 🧪 Formula Summary

  * **Portfolio Standard Deviation (with Risk-Free):** $\sigma_P = w_{risky} \times \sigma_{risky}$ 
  * **CML Equation:** $E(R_P) = R_f + \left[ \frac{E(R_M) - R_f}{\sigma_M} \right] \sigma_P$ 
  * **Total Risk:** Total Risk = Systematic Risk + Nonsystematic Risk 
  * **Beta (Covariance):** $\beta_i = \frac{Cov_{i,m}}{\sigma_m^2}$ 
  * **Beta (Correlation):** $\beta_i = \rho_{i,m} \left( \frac{\sigma_i}{\sigma_m} \right)$ 
  * **CAPM (SML) Equation:** $E(R_i) = R_f + \beta_i[E(R_m) - R_f]$ 
  * **Sharpe Ratio:** $SR = \frac{R_P - R_f}{\sigma_P}$ 
  * **Treynor Ratio:** $TR = \frac{R_P - R_f}{\beta_P}$ 
  * **Jensen's Alpha:** $\alpha_P = R_P - E(R_i)$ (where $E(R_i)$ is from CAPM) 
  * **M-squared:** $M^2 = (SR_P \times \sigma_M) + R_f$ 

-----

<div style="background-color: #E8F5E9; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

  * **CML vs. SML:** This is the #1 takeaway.
      * **CML** = Total Risk ($\sigma$) on X-axis. For **E**fficient portfolios only.
      * **SML** = Systematic Risk ($\beta$) on X-axis. For **S**ingle securities (and all portfolios).
  * **Risk:** The market only pays you for **Systematic (Beta)** risk. **Nonsystematic** (firm-specific) risk is uncompensated and should be diversified away.
  * **CAPM:** Know this equation by heart. It's the SML. It gives you the **required return** for any asset.
  * **Mispricing:** **"Over is Under, Under is Over"**. A plot *Over* the SML is *Under*valued. A plot *Under* the SML is *Over*valued.
  * **Performance Metrics:**
      * **Total Risk ($\sigma$) Metrics:** Sharpe & $M^2$. Use for a *total* portfolio.
      * **Systematic Risk ($\beta$) Metrics:** Treynor & Jensen's Alpha. Use for a *well-diversified* portfolio.
      * **Jensen's Alpha** is the only one in *percent return* that measures performance *relative to the SML*.

</div>
</div>

Would you like to run through a practice problem to identify a mispriced security using the SML?