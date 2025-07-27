# Learning Module 2: Portfolio Risk and Return – Part II

---

## Contents

- Capital Market Theory: Risk-Free and Risky Assets
- The Capital Market Line (CML)
- Passive and Active Portfolios
- Leveraged Portfolios & Different Lending/Borrowing Rates
- Systematic and Nonsystematic Risk
- Return-Generating Models & Beta
- Capital Asset Pricing Model (CAPM)
    - Assumptions and Security Market Line (SML)
    - Calculating Expected Return (using Beta)
- Portfolio Performance Measures: Sharpe, Treynor, M², Jensen’s Alpha
- Beyond CAPM: Limitations and Extensions
- Formulas List (for Exam)
- Quick Exam-Day Pointers

---

## Capital Market Theory: Risk-Free and Risky Assets

- **Risk-Free Asset:** e.g., Indian Treasury Bills, RBI 91-Day T-bills – no default risk, return is fixed.
- **Risky Asset:** e.g., Nifty 50 ETF, Infosys share – prices fluctuate.

### Portfolio of a Risk-Free and Risky Asset

If you combine ₹5,000 in T-bills (risk-free) and ₹5,000 in SBI shares (risky):

- **Portfolio Expected Return:**
  $$
  E(R_p) = w_f R_f + (1 - w_f) E(R_m)
  $$

Where:
- $w_f$ = proportion in risk-free asset
- $R_f$ = risk-free rate
- $E(R_m)$ = expected return on risky asset

- **Portfolio Std. Dev. (Risk):**
  $$
  \sigma_p = (1 - w_f)\sigma_m
  $$
  Where $\sigma_m$ = risk (std. dev.) of the risky asset

> **EXAM POINTER:** CFA test will give you weights and asset returns/risks and ask you to compute these portfolio values or interpret their meaning.

---

## The Capital Market Line (CML)

- **Definition:** The set of portfolios optimally combining risk-free asset and the market portfolio.
- **Equation:**
  $$
  E(R_c) = R_f + \frac{E(R_m) - R_f}{\sigma_m} \cdot \sigma_c
  $$
Where:
- $E(R_c)$ = expected return on a CML portfolio (could be leveraged/unleveraged)
- $\sigma_c$ = portfolio risk
- $E(R_m)$, $\sigma_m$ = return/risk of market
- $R_f$ = risk-free rate

__Indian Example__: If Nifty Bees ETF is your "market," the CML describes all risk-return combinations you could get by mixing Nifty ETF with T-bills—and even borrowing at the risk-free rate to buy more Nifty (leveraging).

> **IMPORTANT:** Only efficient portfolios (i.e., combinations of *all* risky assets and risk-free asset) lie on the CML.

---

## Passive and Active Portfolios

- **Passive:** Simply track a market index (e.g., Nifty Index Fund).
- **Active:** Try to beat the market via stock-picking (e.g., Indian Small Cap Mutual Funds).

> _Indian Example:_ Many Indian investors are shifting to passive index funds due to low fees and difficulty beating the market.

**Exam pointer:** Understand the benefit of passive investing and the concept of the ‘market’ portfolio.

---

## Leveraged Portfolios & Different Lending/Borrowing Rates

- **Leverage:** Borrow at risk-free rate to invest more in risky market.
  - Example: Using margin to buy Nifty ETF.
- When borrowing rate ($R_b$) > lending rate ($R_f$), the CML bends at the market portfolio and a new "kinked" line is created for higher risk portfolios.

  - CFA will test calculations and concept!

---

## Systematic and Nonsystematic Risk

- **Systematic (Market) Risk:** Cannot diversify away; affects all assets (e.g., RBI policy, recession, war).
- **Unsystematic (Idiosyncratic) Risk:** Unique to a single stock (e.g., Maruti Suzuki's labor strike); can be reduced by diversification.

  $$
  \text{Total Risk} = \text{Systematic Risk} + \text{Unsystematic Risk}
  $$
- Adding more stocks to a portfolio removes unsystematic risk; only systematic risk remains.

> **EXAM CRITICAL:** Know the difference and the idea that only systematic risk is rewarded with higher expected return in the CAPM world.

---

## Return-Generating Models & Beta

### Single-Index (Market) Model

$$
R_i = \alpha_i + \beta_i R_m + \epsilon_i
$$

Where:
- $\alpha_i$ = asset-specific return
- $\beta_i$ = asset's sensitivity to market
- $R_m$ = return from market
- $\epsilon_i$ = firm-specific surprise (mean 0)

### Calculation of Beta

$$
\beta_i = \frac{\text{Cov}(R_i, R_m)}{\sigma_m^2}
$$

Where:
- $\text{Cov}(R_i, R_m)$ = covariance of asset and market returns
- $\sigma_m^2$ = variance of market returns

> **Real World:** Infosys' beta indicates its volatility relative to Nifty. A beta of 1.2 means if Nifty goes up 10%, Infosys “should” go up 12% (on average).

---

## Capital Asset Pricing Model (CAPM)

### Formula

$$
E(R_i) = R_f + \beta_i [ E(R_m) - R_f ]
$$

Where:
- $E(R_i)$ = expected return on asset $i$
- $R_f$ = risk-free rate
- $\beta_i$ = asset beta
- $E(R_m) - R_f$ = market risk premium

### Security Market Line (SML)
A graphical representation of the CAPM. Any asset or portfolio above the SML is "undervalued" (higher expected return for its risk); below is "overvalued."

---

### CAPM Assumptions (EXAM MUST-KNOW)

- Investors are rational and risk-averse.
- No taxes or transaction costs.
- All investors can borrow/lend at $R_f$.
- Homogeneous expectations, same time horizon.
- Markets are perfectly competitive (no one alone can influence price).

---

## Portfolio Performance Measures

### Sharpe Ratio

$$
\text{Sharpe} = \frac{E(R_p) - R_f}{\sigma_p}
$$

- Measures excess return per unit of *total* risk.

### Treynor Ratio

$$
\text{Treynor} = \frac{E(R_p) - R_f}{\beta_p}
$$

- Uses *systematic* risk (beta), not total risk.

### M² (Modigliani-Modigliani) Measure

$$
M^2 = [ E(R_p) - R_f ] \times \frac{\sigma_m}{\sigma_p} + R_f
$$

- Converts Sharpe into “market volatility units” for direct comparison.

### Jensen’s Alpha

$$
\alpha_p = E(R_p) - [ R_f + \beta_p ( E(R_m) - R_f ) ]
$$

- Measures portfolio’s excess return above that predicted by CAPM.

---

## Quick Formulas List

**Portfolio Expected Return (2 Assets):**
$$
E(R_p) = w_1 E(R_1) + w_2 E(R_2)
$$

---

**Portfolio Standard Deviation (2 Assets):**
$$
\sigma_p = \sqrt{ w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \sigma_1 \sigma_2 \rho_{1,2} }
$$

---

**Capital Market Line (CML):**
$$
E(R_c) = R_f + \frac{ E(R_m) - R_f }{ \sigma_m } \cdot \sigma_c
$$

---

**CAPM (Security Market Line):**
$$
E(R_i) = R_f + \beta_i \left[ E(R_m) - R_f \right]
$$

---

**Beta:**
$$
\beta_i = \frac{ \mathrm{Cov}(R_i, R_m) }{ \sigma_m^2 }
$$

---

**Sharpe Ratio:**
$$
\text{Sharpe} = \frac{ E(R_p) - R_f }{ \sigma_p }
$$

---

**Treynor Ratio:**
$$
\text{Treynor} = \frac{ E(R_p) - R_f }{ \beta_p }
$$

---

**Modigliani–Modigliani (M²) Measure:**
$$
M^2 = \left[ E(R_p) - R_f \right] \cdot \frac{ \sigma_m }{ \sigma_p } + R_f
$$

---

**Jensen’s Alpha:**
$$
\alpha_p = E(R_p) - \left[ R_f + \beta_p \left( E(R_m) - R_f \right) \right]
$$

---

## 🔥 Exam-Day Quick Pointers

- You must know formulas (Sharpe, Treynor, Jensen’s Alpha, Beta, CAPM, CML).
- Sharpe/SML (Security Market Line) vs. CML (Capital Market Line): SML plots expected return vs. Beta; CML vs. standard deviation.
- Know the difference between systematic and unsystematic risk—diversification only eliminates unsystematic risk.
- Be able to interpret and calculate alpha.