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

> [!TIP]
> **CFA Exam Tip ✍️:** Focus on *understanding* the concepts behind these formulas, not just memorizing them. Level 1 often tests application and interpretation. Know when to use which formula and what the result means! Practice using your calculator efficiently for TVM, stats, and NPV/IRR.