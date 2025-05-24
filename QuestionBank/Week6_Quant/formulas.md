## Week 6: Key Formulas 🧪

### Reading 9: Parametric and Non-Parametric Tests of Independence

* **t-statistic for Hypothesis Test of Population Correlation Coefficient ($\rho$):**
    (Null Hypothesis: $H_0: \rho = 0$)
    $$ t = \frac{r\sqrt{n-2}}{\sqrt{1-r^2}} $$
    where:
    * $r$ = sample correlation coefficient
    * $n$ = sample size
    * Degrees of freedom = $n-2$

* **Spearman Rank Correlation Coefficient ($r_s$):**
    (For integer ranks, no ties or adjustments for ties shown here for simplicity)
    $$ r_s = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2-1)} $$
    where:
    * $d_i$ = difference between the ranks for observation $i$
    * $n$ = number of paired observations

* **t-statistic for Significance of Spearman Rank Correlation ($r_s$):**
    (For sample size $n > 30$)
    $$ t = \frac{r_s\sqrt{n-2}}{\sqrt{1-r_s^2}} $$
    * Degrees of freedom = $n-2$

* **Expected Frequency for a Cell in a Contingency Table ($E_{ij}$):**
    $$ E_{ij} = \frac{(\text{Total of Row } i) \times (\text{Total of Column } j)}{\text{Grand Total}} $$

* **Chi-square ($\chi^2$) Test Statistic for Independence (Contingency Table):**
    $$ \chi^2 = \sum_{i=1}^{r}\sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}} $$
    where:
    * $O_{ij}$ = observed frequency in cell (row $i$, column $j$)
    * $E_{ij}$ = expected frequency in cell (row $i$, column $j$)
    * $r$ = number of rows
    * $c$ = number of columns
    * Degrees of freedom = $(r-1)(c-1)$

---
### Reading 10: Simple Linear Regression

* **Simple Linear Regression Model (Population):**
    $$ Y_i = b_0 + b_1 X_i + \epsilon_i $$
    where:
    * $Y_i$ = dependent variable
    * $X_i$ = independent variable
    * $b_0$ = population intercept
    * $b_1$ = population slope coefficient
    * $\epsilon_i$ = error term

* **Estimated Simple Linear Regression Equation (Sample):**
    $$ \hat{Y}_i = \hat{b}_0 + \hat{b}_1 X_i $$
    where:
    * $\hat{Y}_i$ = predicted value of Y
    * $\hat{b}_0$ = estimated intercept
    * $\hat{b}_1$ = estimated slope coefficient

* **Slope Coefficient Estimate ($\hat{b}_1$):**
    $$ \hat{b}_1 = \frac{\text{Cov}(X,Y)}{s_X^2} = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{\sum_{i=1}^{n} (X_i - \bar{X})^2} $$

* **Intercept Coefficient Estimate ($\hat{b}_0$):**
    $$ \hat{b}_0 = \bar{Y} - \hat{b}_1 \bar{X} $$

* **Total Sum of Squares (SST):**
    $$ \text{SST} = \sum_{i=1}^{n} (Y_i - \bar{Y})^2 $$

* **Regression Sum of Squares (SSR):**
    $$ \text{SSR} = \sum_{i=1}^{n} (\hat{Y}_i - \bar{Y})^2 $$

* **Sum of Squared Errors (SSE) or Residual Sum of Squares:**
    $$ \text{SSE} = \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2 = \sum_{i=1}^{n} \hat{\epsilon}_i^2 $$

* **Relationship between SST, SSR, and SSE:**
    $$ \text{SST} = \text{SSR} + \text{SSE} $$

* **Coefficient of Determination ($R^2$):**
    $$ R^2 = \frac{\text{SSR}}{\text{SST}} = 1 - \frac{\text{SSE}}{\text{SST}} $$
    (For simple linear regression, $R^2 = r^2$, where $r$ is the sample correlation coefficient between X and Y)

* **Standard Error of Estimate (SEE or $s_e$):**
    $$ \text{SEE} = \sqrt{\frac{\text{SSE}}{n-2}} = \sqrt{\text{MSE}} $$
    where MSE is the Mean Squared Error.

* **t-statistic for Hypothesis Test of Regression Coefficient (e.g., $b_1$):**
    (Null Hypothesis: $H_0: b_1 = \text{hypothesized value}$)
    $$ t = \frac{\hat{b}_1 - b_{1, H_0}}{s_{\hat{b}_1}} $$
    where:
    * $s_{\hat{b}_1}$ = standard error of the slope coefficient
    * Degrees of freedom = $n-2$ (for simple linear regression)

* **F-statistic for Overall Significance of Regression (Simple Linear Regression):**
    $$ F = \frac{\text{MSR}}{\text{MSE}} = \frac{\text{SSR}/k}{\text{SSE}/(n-k-1)} $$
    For simple linear regression, $k=1$:
    $$ F = \frac{\text{SSR}/1}{\text{SSE}/(n-2)} $$
    (Note: For simple linear regression, $F = t_{\text{slope}}^2$)
    * Degrees of freedom = $k$ for numerator, $n-k-1$ for denominator. (So, 1 and $n-2$ for simple linear regression)

* **Predicted Value for Dependent Variable ($\hat{Y}_f$):**
    $$ \hat{Y}_f = \hat{b}_0 + \hat{b}_1 X_f $$
    where $X_f$ is the forecasted value of the independent variable.

* **Prediction Interval for $\hat{Y}_f$:**
    $$ \hat{Y}_f \pm t_c \times s_f $$
    where:
    * $t_c$ = critical t-value for a given confidence level with $n-2$ degrees of freedom
    * $s_f$ = standard error of the forecast

* **Variance of the Forecast Error ($s_f^2$):**
    $$ s_f^2 = s_e^2 \left[1 + \frac{1}{n} + \frac{(X_f - \bar{X})^2}{(n-1)s_X^2}\right] $$
    (Note: The calculation of $s_f$ is complex; for exam purposes, it's often provided if a prediction interval needs to be constructed.)

* **Functional Forms of Simple Linear Regressions:**
    * Log-lin model: $\ln(Y_i) = b_0 + b_1 X_i + \epsilon_i$
    * Lin-log model: $Y_i = b_0 + b_1 \ln(X_i) + \epsilon_i$
    * Log-log model: $\ln(Y_i) = b_0 + b_1 \ln(X_i) + \epsilon_i$

---
*Reading 11 (Introduction to Big Data Techniques) is primarily conceptual and does not feature calculation-based formulas in the same way as Readings 9 and 10.*