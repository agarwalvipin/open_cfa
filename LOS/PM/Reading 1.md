# Learning Module 1: Portfolio Risk and Return—Part I

---

## Table of Contents

- Historical Return vs. Expected Return
- Major Asset Classes: Characteristics
- Risk and Return in Indian Context
- Risk–Return Trade-off Explained
- Other Investment Characteristics (Skewness, Kurtosis, Liquidity)
- Risk Aversion and Portfolio Selection
- Utility Theory and Indifference Curves
- Application: Constructing an Optimal Portfolio
- Key Formulas in This Module
- Quick Exam-Day Pointers

---

## 1. Historical Return vs. Expected Return

**Historical Return**: What was actually earned in the past (e.g., Sensex average annual return over the last 20 years).
**Expected Return**: What you anticipate earning in the future, considering current economic scenarios.

> _Example (India):_  
Suppose from 2004–2024, Nifty 50 gave a **historical return** of about 12% p.a. You are now investing in 2025, but your **expected return** may be 9%-10% due to current interest rates and government policy.

**Exam Tip:**  
CFA may test both how to calculate historical returns (using past data) and how to conceptually distinguish from expected returns. You must know that past returns do not guarantee future results.

---

## 2. Major Asset Classes: Characteristics

### a. Equities (Stocks)
- **High return/high risk**.
- In India: HDFC Bank, Reliance, Infosys.  
- Over the long-term, Indian stocks have outperformed most traditional assets but with greater volatility.

### b. Bonds (Fixed Income)
- **Moderate return/moderate risk**.
- E.g., Indian government bonds (G-Secs), State Development Loans, debentures by Indian corporates.
- In downturns, bonds can outperform stocks.

### c. Treasury Bills (T-bills)
- **Low return/very low risk**.
- Examples: 91-day, 182-day T-bills sold by RBI. Used by mutual funds for parking cash.

### d. Real Estate/Gold (India Context)
- Popular alternative assets; physical gold is frequently held as “safe haven.”
- Real estate returns are location-dependent and less liquid.

**Exam Importance**:  
Know characteristics—not just return/risk, but also liquidity and inflation protection, and typical Indian investor behavior.

---

## 3. Risk and Return in Indian Context

- **Small-cap stocks:** High risk (e.g., penny stocks on BSE), potentially high return—can have wild swings.
- **Large-cap stocks:** More stable (Reliance, TCS).
- **Government bonds:** India 10-year G-sec; relatively safe.
- **T-bills:** RBI-issued, as safe as it gets but returns are usually lower than inflation.

> _Example:_  
In 2020, equity markets dropped >20% during Covid but recovered; Indian gold funds soared over 25%, showing gold’s “crisis hedge” value.

**Formula Example:**  
To compute **historical mean return**:  
[
\text{Mean Return} = \frac{\sum_{i=1}^n R_i}{n}
]  
Where \(R_i\) = return in year \(i\), \(n\) = number of years.

**Exam Tip:**  
You may be asked to calculate variance, standard deviation or mean using return data series (practice doing this quickly without a calculator).

---

## 4. Risk–Return Trade-off Explained

- **Higher returns require accepting higher risk.**
- For Indian investors: FDs (fixed deposits) offer low returns (~6-7%) but virtually zero risk. Equities offer higher (potentially double-digit) returns but prices can fall sharply.

> _Real World:_  
Choosing a recurring deposit, you know what you’ll get in 12 months. Investing in an IPO (like Zomato in India), returns could be 50% or minus 50%.

**Key Exam Pointer:**  
Understand that risk and return are positively correlated. Assets with negative historical or expected returns (after inflation) are poor investments—inflation adjustment is very relevant in India.

---

## 5. Other Investment Characteristics

**a. Skewness**  
Stock returns might have negative skew (one big loss year can offset many good years).

**b. Kurtosis (Fat Tails)**  
Indian equity returns occasionally show “fat tails”—extreme moves (e.g., 2020 Covid crash).

**c. Liquidity**  
- Reliance shares: high liquidity.
- Small-town property: can take months to sell (illiquid).
- Indian corporate bonds: less liquid during market panic.

> _Example:_  
Trading penny stocks in India may expose you to wider “bid-ask spreads.”

**Exam Tip:**  
Remember that non-normality (skewness, kurtosis) increases true risk; liquidity matters especially for large transactions.

---

## 6. Risk Aversion and Portfolio Selection

- **Risk-averse investor:** Prefers certain outcomes over risky ones with same expected value.
- **Risk-neutral:** Cares only about return.
- **Risk-seeker:** Might buy lottery tickets or derivatives for thrill.

> _Example:_  
Typical Indian middle-class savers are risk-averse—prefer FDs, PPF, and gold over equities unless “forced” by higher returns.

**Key CFA Formula (Utility):**  
[
U = E(r) - 0.5A\sigma^2
]  
Where \(U\): utility, \(E(r)\): expected return, \(A\): risk aversion coefficient, \(\sigma^2\): variance.

---

## 7. Utility Theory and Indifference Curves

- **Indifference curve**: Shows combinations of risk and return giving same satisfaction.
- The more risk-averse, the steeper and more convex the curve (needs a lot more return to accept more risk!).

> _Example (India):_  
Someone might demand a 5% higher return than FD to consider even investing in an equity NFO.

**Exam Tip:**  
Be able to sketch or identify which indifference curves suit risk-averse, risk-neutral, and risk-seeking investors; and relate utility formula to risk attitudes.

---

## 8. Application: Constructing an Optimal Portfolio 

- Investor should choose portfolio on the **capital allocation line** (CAL), tangent to his/her highest indifference curve.
- For most CFA exam cases, you’re told risk aversion coefficient, risk/returns, and expected to find best portfolio using formulas.

> _Example:_  
Mixing Indian G-Secs (risk-free) and a Nifty 50 Index ETF (risky). Calculate expected risk and return for different weights and use the utility formula.

---

# All Formulas Used in This Reading

### 1. Expected Return (Probability Weighted)

$$
E(R) = \sum_{i=1}^{n} p_i \times R_i
$$

Where:
- $E(R)$ = Expected Return  
- $p_i$ = Probability of scenario $i$  
- $R_i$ = Return in scenario $i$  
- $n$ = Total number of scenarios  

---

### 2. Historical Mean Return (Simple Arithmetic Average)

$$
\bar{R} = \frac{1}{n} \sum_{i=1}^{n} R_i
$$

Where:
- $\bar{R}$ = Mean (average) return  
- $R_i$ = Return in observation $i$  
- $n$ = Number of observations  

---

### 3. Variance of Returns

$$
\sigma^2 = \frac{1}{n-1} \sum_{i=1}^{n} (R_i - \bar{R})^2
$$

Where:
- $\sigma^2$ = Variance of returns  
- $R_i$ = Return in observation $i$  
- $\bar{R}$ = Mean return  
- $n$ = Number of observations  

---

### 4. Standard Deviation (Risk)

$$
\sigma = \sqrt{ \frac{1}{n-1} \sum_{i=1}^{n} (R_i - \bar{R})^2 }
$$

---

### 5. Covariance Between Asset Returns

$$
\text{Cov}(R_A, R_B) = \frac{1}{n-1} \sum_{i=1}^{n} (R_{A,i} - \bar{R}_A)(R_{B,i} - \bar{R}_B)
$$

---

### 6. Correlation Coefficient

$$
\rho_{A,B} = \frac{ \text{Cov}(R_A, R_B) }{ \sigma_A \sigma_B }
$$

Where:
- $\rho_{A,B}$ = Correlation between assets A and B  
- $\sigma_A$ = Std. deviation of A  
- $\sigma_B$ = Std. deviation of B  

---

### 7. Portfolio Expected Return (2 Assets)

$$
E(R_p) = w_1 E(R_1) + w_2 E(R_2)
$$

Where:
- $E(R_p)$ = Expected return of the portfolio  
- $w_1, w_2$ = Weights of asset 1 and asset 2  
- $E(R_1), E(R_2)$ = Expected returns of assets 1 and 2  

---

### 8. Portfolio Variance (2 Assets)

$$
\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2w_1 w_2 \sigma_1 \sigma_2 \rho_{1,2}
$$

Where:
- $\sigma_p^2$ = Portfolio variance  
- $w_1, w_2$ = Weights of asset 1 and asset 2  
- $\sigma_1, \sigma_2$ = Std. deviations of asset 1 and 2  
- $\rho_{1,2}$ = Correlation between assets 1 and 2  

---

### 9. Portfolio Standard Deviation (2 Assets)

$$
\sigma_p = \sqrt{ w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2w_1 w_2 \sigma_1 \sigma_2 \rho_{1,2} }
$$

---

### 10. Utility Function (Risk & Return Trade-off)

$$
U = E(r) - 0.5 A \sigma^2
$$

Where:
- $U$ = Utility (investor's satisfaction)  
- $E(r)$ = Expected return  
- $A$ = Risk aversion coefficient  
- $\sigma^2$ = Variance of the investment  

---

### 11. Capital Allocation Line (CAL)

$$
E(R_p) = R_f + \left( \frac{ E(R_m) - R_f }{ \sigma_m } \right) \sigma_p
$$

Where:
- $R_f$ = Risk-free rate  
- $E(R_m)$ = Expected return on risky asset or market  
- $\sigma_m$ = Std. deviation of risky asset or market  
- $\sigma_p$ = Std. deviation of portfolio  

---

### 12. Expected Return (Including Real Rate, Inflation, Risk Premium)

$$
1 + E(R) = [1 + r_{RF}] \times [1 + E(\pi)] \times [1 + E(RP)]
$$

Where:
- $r_{RF}$ = Real risk-free rate  
- $E(\pi)$ = Expected inflation  
- $E(RP)$ = Expected risk premium  

---

### 13. Portfolio Std. Dev. (Risk-Free + Risky)

$$
\sigma_p = (1 - w_1) \sigma_i
$$

Where:
- $w_1$ = Weight in risk-free asset  
- $\sigma_i$ = Std. deviation of risky asset  

---

---

## Quick Exam-Day Pointers

- **Practice formulas till you can write and use them without reference.**
- **Read each question carefully**: Is it testing historical vs. expected, arithmetic vs. geometric mean?
- **Remember big ideas:** risk–return trade-off, types of risk (systematic, unsystematic), and the reasons for diversification.
- In Indian context, do not forget that bond yields and inflation are very dynamic—think about how these affect expected returns.
- Watch for **practical applications**: CFA likes investment selection and portfolio construction questions that blend theory with numbers.
- **Calculator proficiency:** Bring and know how to use your CFA-approved calculator for returns, variance, and risk calculations.
- Review **LOS (Learning Outcome Statements)**—they guide what you must master.
- When in doubt, relate investments to Indian examples you know—helps “anchor” abstract concepts for MCQs.

---
