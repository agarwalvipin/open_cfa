# 🧪 Quantitative Methods Formulas

## 📊 Reading 1: Rates and Returns

- 💵 **Nominal Risk-Free Rate (Approximation):**

  $$\text{Nominal Risk-Free Rate} \approx \text{Real Risk-Free Rate} + \text{Expected Inflation Rate}$$

- 📈 **Nominal Rate of Interest (Components):**

  $$\text{Nominal Rate} = \text{Real Risk-Free Rate} + \text{Inflation Premium} + \text{Default Risk Premium} + \text{Liquidity Premium} + \text{Maturity Premium}$$

- 🎯 **Holding Period Return (HPR):** ⭐ **KEY FORMULA**

  $$\text{HPR} = \frac{\text{End Value}}{\text{Beginning Value}} - 1$$
  
  $$\text{HPR (with Dividends)} = \frac{P_1 - P_0 + \text{Div}_1}{P_0}$$

- 📊 **Multi-Period HPR:**

  $$\text{HPR}_{\text{Total}} = (1 + \text{HPR}_1)(1 + \text{HPR}_2)...(1 + \text{HPR}_n) - 1$$

- 📈 **Arithmetic Mean Return:**

  $$\bar{R}_{\text{Arithmetic}} = \frac{R_1 + R_2 + ... + R_n}{n}$$

- 📉 **Geometric Mean Return:**

  $$R_G = \sqrt[n]{(1 + R_1)(1 + R_2)...(1 + R_n)} - 1$$

- ⚖️ **Harmonic Mean:**

  Mean = N / (Sum of 1/X_i for i=1 to N)
  
  $$H = \frac{N}{\sum_{i=1}^{N} \frac{1}{X_i}}$$

- 📅 **Annualized Return (from HPR):**

  $$\text{Annualized Return} = (1 + \text{HPR})^{\frac{365}{\text{days}}} - 1$$

- 💰 **Present Value (PV) with Compounding:**

  $$PV = FV_N \left(1 + \frac{r}{m}\right)^{-mN}$$

- 📊 **Continuously Compounded Return (Rcc):**

  $$R_{cc} = \ln(1 + \text{HPR}) = \ln\left(\frac{\text{Ending Value}}{\text{Beginning Value}}\right)$$

- 🔄 **Exact Real Return:**

  $$\text{Real Return} = \frac{1 + \text{Nominal Return}}{1 + \text{Inflation Rate}} - 1$$

- 📈 **Leveraged Return (Rate):**

  $$\text{Leveraged Return Rate} = \frac{r(V_0 + V_B) - r_B V_B}{V_0}$$

---

## 💰 Reading 2: The Time Value of Money in Finance

- 🔮 **Future Value (FV):** ⭐ **KEY FORMULA**

  $$FV = PV(1 + r)^t$$

- 📊 **Present Value (PV):** ⭐ **KEY FORMULA**

  $$PV = \frac{FV}{(1 + r)^t} = FV(1 + r)^{-t}$$

- 📈 **FV (Continuous Compounding):**

  $$FV = PV \times e^{rt}$$

- 📉 **PV (Continuous Compounding):**

  $$PV = FV \times e^{-rt}$$

- 🔄 **PV of a Perpetuity:**

  $$PV_{\text{Perpetuity}} = \frac{\text{Payment}}{r}$$

- 💳 **Annuity Payment:**

  $$\text{Annuity Payment} = \frac{r \times PV}{1 - (1 + r)^{-t}}$$

- 📈 **Preferred Stock Value:**

  $$\text{Value} = \frac{D_p}{k_p}$$

- 🌱 **Constant Growth DDM (Gordon Growth Model):** ⭐ **KEY FORMULA**

  $$V_0 = \frac{D_1}{k_e - g_c}$$

- 🔧 **Implied Required Return (Constant Growth DDM):**

  $$k_e = \frac{D_1}{V_0} + g_c$$

- 📊 **Implied Growth Rate (Constant Growth DDM):**

  $$g_c = k_e - \frac{D_1}{V_0}$$

- ⚖️ **No-Arbitrage Forward Rate (from Spot Rates):**

  $$(1 + S_n)^n = (1 + S_k)^k (1 + (n-k)yky)$$
  
  $$(1 + 1y1y) = \frac{(1 + S_2)^2}{(1 + S_1)}$$

- 🌍 **No-Arbitrage Forward Exchange Rate:**

  $$\frac{\text{Forward}}{\text{Spot}} = \frac{(1 + r_p)}{(1 + r_b)}$$
  
  where $r_p$ is the price currency interest rate and $r_b$ is the base currency interest rate

- 🛡️ **Binomial Model Hedge Ratio (h):**

  $$h = \frac{c_1^u - c_1^d}{S_1^u - S_1^d}$$

---

## 📊 Reading 3: Statistical Measures of Asset Returns

- 📈 **Sample Mean (Arithmetic):**

  $$\bar{X} = \frac{\sum_{i=1}^{n} X_i}{n}$$

- 📏 **Range:**

  $$\text{Range} = \text{Maximum Value} - \text{Minimum Value}$$

- 🎯 **Mean Absolute Deviation (MAD):**

  $$\text{MAD} = \frac{\sum_{i=1}^{n} |X_i - \bar{X}|}{n}$$

- 📐 **Sample Variance:** ⭐ **KEY FORMULA**

  $$s^2 = \frac{\sum_{i=1}^{n} (X_i - \bar{X})^2}{n - 1}$$

- 📊 **Sample Standard Deviation:** ⭐ **KEY FORMULA**

  $$s = \sqrt{\frac{\sum_{i=1}^{n} (X_i - \bar{X})^2}{n - 1}}$$

- 📈 **Coefficient of Variation (CV):**

  $$\text{CV} = \frac{s}{\bar{X}}$$

- 🎯 **Target Downside Deviation (Target Semideviation):**

  $$s_{\text{target}} = \sqrt{\frac{\sum (X_i - B)^2}{n - 1}}$$
  
  where the sum is over all $X_i \leq B$

- 📉 **Sample Skewness (Approximation):**

  $$\text{Skewness} \approx \frac{n}{(n-1)(n-2)} \frac{\sum (X_i - \bar{X})^3}{s^3}$$
  
  *(Note: Simplified version often used conceptually)*

- 📊 **Sample Kurtosis (Approximation):**

  $$\text{Kurtosis} \approx \frac{n(n+1)}{(n-1)(n-2)(n-3)} \frac{\sum (X_i - \bar{X})^4}{s^4}$$
  
  *(Note: Simplified version often used conceptually)*

- 📈 **Excess Kurtosis:**

  $$\text{Excess Kurtosis} = \text{Sample Kurtosis} - 3$$

- 🔗 **Sample Covariance:**

  $$s_{XY} = \frac{\sum_{i=1}^{n} \{ [X_i - \bar{X}] [Y_i - \bar{Y}] \}}{n - 1}$$

- 📊 **Correlation Coefficient:**

  $$\rho_{XY} = r_{XY} = \frac{s_{XY}}{s_X s_Y}$$
  
  $$s_{XY} = \rho_{XY} s_X s_Y$$

---

## 🌳 Reading 4: Probability Trees and Conditional Expectations

- 🎯 **Expected Value:**

  $$E(X) = \sum P(x_i) x_i = P(x_1)x_1 + P(x_2)x_2 + ... + P(x_n)x_n$$

- 📊 **Variance (from Probability Model):**

  $$\sigma^2(X) = \text{Var}(X) = E[ (X - E(X))^2 ] = \sum P(x_i) [x_i - E(X)]^2$$

- 📈 **Standard Deviation (from Probability Model):**

  $$\sigma(X) = \sqrt{\text{Var}(X)}$$

- 🔄 **Bayes' Formula (Updated Probability):**

  $$P(I|O) = \frac{P(O|I)}{P(O)} \times P(I)$$
  
  Where:
  - $P(I)$ = Prior probability of event I
  - $P(O|I)$ = Conditional probability of new information O given event I
  - $P(O)$ = Unconditional probability of new information O
  - $P(I|O)$ = Updated probability of event I given new information O

---

## 📈 Reading 5: Portfolio Mathematics

- 💼 **Expected Return of a Portfolio:** ⭐ **KEY FORMULA**

  $$E(R_p) = \sum_{i=1}^{n} w_i E(R_i)$$

- ⚖️ **Portfolio Weight:**

  $$w_i = \frac{\text{Market Value of Investment in Asset } i}{\text{Market Value of the Portfolio}}$$

- 🔗 **Covariance (Probability Model):**

  $$\mathrm{Cov}(R_i, R_j) = E[(R_i - E(R_i))(R_j - E(R_j))]$$

- 📊 **Covariance (Sample Data):**

  $$s = \frac{1}{n-1} \sum_{t=1}^{n} (R^{(1)}_t - \bar{R}^{(1)})(R^{(2)}_t - \bar{R}^{(2)})$$
  
  where superscripts denote asset indices and subscript $t$ denotes time period

- 📉 **Variance of a 2-Asset Portfolio:** ⭐ **KEY FORMULA**

  $$\sigma_P^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \mathrm{Cov}(A,B)$$
  
  $$\sigma_P^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \rho(A,B) \sigma_A \sigma_B$$

- 📊 **Variance of a 3-Asset Portfolio:**

  $$\sigma_P^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + w_C^2 \sigma_C^2 + 2 w_A w_B \mathrm{Cov}(A,B) + 2 w_A w_C \mathrm{Cov}(A,C) + 2 w_B w_C \mathrm{Cov}(B,C)$$

- 🛡️ **Safety-First Ratio (SFRatio):**

  $$\text{SFRatio} = \frac{E(R_P) - R_L}{\sigma_P}$$

---

## 🎲 Reading 6: Simulation Methods

- 📈 **Lognormal Price Relationship:**

  $$P_T = P_0 e^{r_{0,T}}$$
  
  Where $r_{0,T}$ is the continuously compounded return from time 0 to T.

---

## 📊 Reading 7: Estimation and Inference

- 📐 **Standard Error of the Sample Mean (Population Variance Known):**

  $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$

- 📈 **Standard Error of the Sample Mean (Population Variance Unknown):**

  $$s_{\bar{x}} = \frac{s}{\sqrt{n}}$$

---

## 🧪 Reading 8: Hypothesis Testing

- 📐 **Test Statistic (General Form):**

  $$\text{Test Statistic} = \frac{\text{Sample Statistic} - \text{Hypothesized Value}}{\text{Standard Error of the Sample Statistic}}$$

- 🔍 **Test Statistic for Population Mean (Large Sample or Known Pop Var):** ⭐ **KEY FORMULA**

  $$z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} \quad \text{or} \quad z = \frac{\bar{x} - \mu_0}{s/\sqrt{n}} \text{ (if n large)}$$

- 📊 **Test Statistic for Population Mean (Small Sample, Unknown Pop Var):** ⭐ **KEY FORMULA**

  $$t_{n-1} = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$$

- ⚖️ **Test Statistic for Difference in Means (Independent, Equal Variances Assumed):**

  $$t_{n_1+n_2-2} = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_p^2}{n_1} + \frac{s_p^2}{n_2}}}$$
  
  Where Pooled Variance: $s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$

- 🔄 **Test Statistic for Paired Comparisons (Dependent Samples):**

  $$t_{n-1} = \frac{\bar{d} - \mu_{dz}}{s_{\bar{d}}}$$
  
  Where Standard Error of Mean Difference: $s_{\bar{d}} = \frac{s_d}{\sqrt{n}}$

- 📐 **Test Statistic for Single Population Variance:**

  $$\chi^2_{n-1} = \frac{(n - 1)s^2}{\sigma_0^2}$$

- ⚖️ **Test Statistic for Equality of Two Population Variances:**

  $$F_{n_1-1, n_2-1} = \frac{s_1^2}{s_2^2} \quad (\text{usually put larger variance in numerator})$$

---

## 🔍 Reading 9: Parametric and Non-Parametric Tests of Independence

- 🔗 **Test Statistic for Correlation Coefficient = 0:**

  $$t_{n-2} = \frac{r \sqrt{n - 2}}{\sqrt{1 - r^2}}$$

- 📊 **Spearman Rank Correlation Coefficient:**

  $$r_s = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}$$

- 🎲 **Chi-Square Test Statistic for Independence (Contingency Table):**

  $$\chi^2 = \sum_{i=1}^r \sum_{j=1}^c \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$
  
  Degrees of Freedom: $df = (r - 1)(c - 1)$
  
  Expected Frequency: $E_{ij} = \frac{\text{(Total Row i)} \times \text{(Total Column j)}}{\text{Grand Total}}$

---

## 📈 Reading 10: Simple Linear Regression

- 📊 **Simple Linear Regression Model:** ⭐ **KEY FORMULA**

  $$Y_i = b_0 + b_1 X_i + \epsilon_i$$

- 📈 **Estimated Regression Line:** ⭐ **KEY FORMULA**

  $$\hat{Y}_i = \hat{b}_0 + \hat{b}_1 X_i$$

- 🔧 **Estimated Slope Coefficient:** ⭐ **KEY FORMULA**

  $$\hat{b}_1 = \frac{\mathrm{Cov}(X, Y)}{\mathrm{Var}(X)} = r \frac{s_Y}{s_X}$$
  
  where $r$ is the correlation coefficient between X and Y

- 📐 **Estimated Intercept Coefficient:**

  $$\hat{b}_0 = \bar{Y} - \hat{b}_1 \bar{X}$$

- 📊 **Total Sum of Squares (SST):**

  $$\text{SST} = \sum_{i=1}^n (Y_i - \bar{Y})^2$$

- 📈 **Regression Sum of Squares (SSR):**

  $$\text{SSR} = \sum_{i=1}^n (\hat{Y}_i - \bar{Y})^2$$

- 📉 **Sum of Squared Errors (SSE):**

  $$\mathrm{SSE} = \sum (Y - \hat{Y})^2 = \sum \epsilon^2$$

- ⚖️ **Relationship between SST, SSR, SSE:**

  $$\mathrm{SST} = \mathrm{SSR} + \mathrm{SSE}$$

- 📊 **Mean Square Regression (MSR):**

  $$\mathrm{MSR} = \frac{\mathrm{SSR}}{k} \quad (k=1 \text{ for simple linear regression})$$

- 📉 **Mean Squared Error (MSE):**

  $$\mathrm{MSE} = \frac{\mathrm{SSE}}{n - k - 1} = \frac{\mathrm{SSE}}{n - 2}$$
  
  (for simple linear regression)

- 📏 **Standard Error of Estimate (SEE):**

  $$\text{SEE} = s_{\epsilon} = \sqrt{\text{MSE}}$$

- 📊 **Coefficient of Determination (R²):** ⭐ **KEY FORMULA**

  $$R^2 = \frac{\text{SSR}}{\text{SST}} = 1 - \frac{\text{SSE}}{\text{SST}}$$

- 📈 **F-Statistic (Simple Linear Regression):**

  $$F = \frac{\text{MSR}}{\text{MSE}} = \frac{\text{SSR}/1}{\text{SSE}/(n-2)}$$

- 🔍 **t-Statistic for Slope Coefficient:**

  $$t = \frac{\hat{b}_1 - b_1}{s_{\hat{b}_1}} \quad (\text{usually testing } b_1=0)$$

- 🔮 **Standard Error of the Forecast Variance:**

  $$s_f^2 = s_e^2 \left( 1 + \frac{1}{n} + \frac{(X - \bar{X})^2}{(n-1)s_X^2} \right)$$

- 📊 **Prediction Interval for Y:**

  $$\hat{Y} \pm t_c \times s_f$$

- 📈 **Log-Lin Model:**

  $$\ln Y_i = b_0 + b_1 X_i + \epsilon_i$$

- 📊 **Lin-Log Model:**

  $$Y_i = b_0 + b_1 \ln X_i + \epsilon_i$$

- 📉 **Log-Log Model:**

  $$\ln Y_i = b_0 + b_1 \ln X_i + \epsilon_i$$

---

## 🤖 Reading 11: Introduction to Big Data Techniques

This reading is primarily conceptual and does not contain specific mathematical formulas.

---