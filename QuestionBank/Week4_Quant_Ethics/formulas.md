# 📐 Formula Sheet: Week 4 - Portfolio Math & Simulation Methods

## Reading 5: Portfolio Mathematics

### LOS 5.a: Calculate and interpret the expected value, variance, standard deviation, covariances, and correlations of portfolio returns.

* **Expected Return of a Portfolio ($E(R_p)$)**
    ```math
    E(R_p) = \sum_{i=1}^{n} w_i E(R_i) = w_1 E(R_1) + w_2 E(R_2) + \dots + w_n E(R_n)
    ```
    Where[cite: 781]:
    * $w_i$ = Weight of asset $i$ in the portfolio
    * $E(R_i)$ = Expected return of asset $i$
    * $n$ = Number of assets in the portfolio

* **Weight of an Asset in a Portfolio ($w_i$)**
    ```math
    w_i = \frac{\text{Market Value of Investment in Asset } i}{\text{Market Value of the Portfolio}}
    ```
    [cite: 783]

* **Covariance of Returns between Asset $i$ and Asset $j$ ($Cov(R_i, R_j)$ or $\sigma_{ij}$)**
    (Based on expectations from a probability model)
    ```math
    Cov(R_i, R_j) = E\{[R_i - E(R_i)][R_j - E(R_j)]\}
    ```
    [cite: 790]

* **Covariance of a Random Variable with Itself**
    ```math
    Cov(R_A, R_A) = Var(R_A) = \sigma_A^2
    ```
    [cite: 791, 792]

* **Sample Covariance between Returns of Asset 1 and Asset 2 ($s_{1,2}$)**
    (Based on historical sample data)
    ```math
    s_{1,2} = \frac{\sum_{k=1}^{n} \{[R_{1,k} - \bar{R}_1][R_{2,k} - \bar{R}_2]\}}{n-1}
    ```
    Where[cite: 795]:
    * $R_{1,k}$ = $k^{th}$ observed return for Asset 1
    * $R_{2,k}$ = $k^{th}$ observed return for Asset 2
    * $\bar{R}_1, \bar{R}_2$ = Sample mean returns for Asset 1 and Asset 2
    * $n$ = Number of observations in the sample

---

### Portfolio Variance (LOS 5.a Continued)

* **Variance of Portfolio Returns ($Var(R_p)$ or $\sigma_p^2$) - General Form**
    ```math
    Var(R_p) = \sum_{i=1}^{N} \sum_{j=1}^{N} w_i w_j Cov(R_i, R_j)
    ```
    [cite: 800]

* **Variance of a Two-Asset Portfolio (A and B)**
    ```math
    Var(R_p) = w_A^2 Var(R_A) + w_B^2 Var(R_B) + 2w_A w_B Cov(R_A, R_B)
    ```
    or using standard deviation notation:
    ```math
    \sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2w_A w_B Cov_{AB}
    ```
    [cite: 801]

* **Variance of a Three-Asset Portfolio (A, B, and C)**
    ```math
    \sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + w_C^2 \sigma_C^2 + 2w_A w_B Cov_{AB} + 2w_A w_C Cov_{AC} + 2w_B w_C Cov_{BC}
    ```
    [cite: 801]

---

### Correlation and its use in Portfolio Variance (LOS 5.a Continued)

* **Correlation Coefficient between Asset A and Asset B ($\rho_{AB}$)**
    ```math
    \rho_{AB} = \frac{Cov_{AB}}{\sigma_A \sigma_B}
    ```
    [cite: 805]

* **Covariance derived from Correlation**
    ```math
    Cov_{AB} = \rho_{AB} \sigma_A \sigma_B
    ```
    [cite: 805]

* **Variance of a Two-Asset Portfolio using Correlation**
    ```math
    \sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2w_A w_B \sigma_A \sigma_B \rho_{AB}
    ```
    [cite: 851]

---

### LOS 5.b: Calculate and interpret the covariance and correlation of portfolio returns using a joint probability function for returns.

* **Covariance of Returns from a Joint Probability Function**
    1.  Calculate Expected Returns for each asset:
        $E(R_A) = \sum_{i=1}^{S} P(S_i) R_{A,i}$
        $E(R_B) = \sum_{i=1}^{S} P(S_i) R_{B,i}$
        Where $S_i$ is state $i$, $P(S_i)$ is the probability of state $i$, and $R_{A,i}$ is the return of asset A in state $i$.
    2.  Calculate Covariance:
        ```math
        Cov(R_A, R_B) = \sum_{i=1}^{S} P(S_i) [R_{A,i} - E(R_A)] [R_{B,i} - E(R_B)]
        ```
        (This is derived from the structure of the example calculation in the SchweserNotes™ [cite: 817, 818, 819])
        The example shows using the joint probability directly for each outcome pair:
        ```math
        Cov(R_A,R_B) = \sum_{j=1}^{m} P(R_{A,j}, R_{B,j}) [R_{A,j} - E(R_A)] [R_{B,j} - E(R_B)]
        ```
        where $P(R_{A,j}, R_{B,j})$ is the joint probability of the $j^{th}$ pair of returns.

---

### LOS 5.c: Define shortfall risk, calculate the safety-first ratio, and identify an optimal portfolio using Roy's safety-first criterion.

* **Shortfall Risk**
    * The probability that a portfolio value or return will fall below a particular target value or return ($R_L$) over a given period. [cite: 821]
    * Minimize $P(R_p < R_L)$ [cite: 823]

* **Roy's Safety-First Ratio (SFR)**
    (To be maximized when choosing among portfolios)
    ```math
    SFR_p = \frac{E(R_p) - R_L}{\sigma_p}
    ```
    Where[cite: 823]:
    * $E(R_p)$ = Expected return of the portfolio
    * $R_L$ = Threshold level return (minimum acceptable return)
    * $\sigma_p$ = Standard deviation of portfolio returns

---
---

## Reading 6: Simulation Methods

### LOS 6.a: Explain the relationship between normal and lognormal distributions and why the lognormal distribution is used to model asset prices when using continuously compounded asset returns.

* **Asset Price Modeled with Lognormal Distribution (using continuously compounded returns)**
    ```math
    P_T = P_0 e^{r_{0,T}}
    ```
    Where[cite: 863]:
    * $P_T$ = Asset price at time T
    * $P_0$ = Asset price at time 0 (today)
    * $r_{0,T}$ = The continuously compounded return on the asset from time 0 to time T (this return $r_{0,T}$ is assumed to be normally distributed)
    * $e$ = Euler's number (approx. 2.71828)

*(Note: LOS 6.b (Monte Carlo simulation) and LOS 6.c (Bootstrap resampling) are primarily descriptive and do not introduce specific calculation formulas in this reading, beyond the general processes.)*

---