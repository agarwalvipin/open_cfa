# ⚖️ Formula Sheet: Week 6 - Tests of Independence & Regression

## Reading 9: Parametric and Non-Parametric Tests of Independence

### LOS 9.a: Explain parametric and nonparametric tests of the hypothesis that the population correlation coefficient equals zero, and determine whether the hypothesis is rejected at a given level of significance.

* **Test Statistic for Hypothesis that Population Correlation Coefficient ($\rho$) is Zero (Parametric Test)**
    (Assumes variables are normally distributed)
    ```math
    t = \frac{r\sqrt{n-2}}{\sqrt{1-r^2}}
    ```
    Where:
    * $r$ = Sample correlation coefficient
    * $n$ = Sample size
    * Degrees of freedom (df) = $n-2$

* **Spearman Rank Correlation Coefficient ($r_s$) (Nonparametric Test)**
    (Used when all ranks are integer values, i.e., no ties or average ranks are used for ties)
    ```math
    r_s = 1 - \frac{6\sum_{i=1}^{n} d_i^2}{n(n^2-1)}
    ```
    Where:
    * $d_i$ = Difference between the ranks for observation $i$ for the two variables
    * $n$ = Number of paired observations

* **Test Statistic for Significance of Spearman Rank Correlation ($r_s$)**
    (Applicable when sample size $n > 30$)
    ```math
    t = \frac{r_s\sqrt{n-2}}{\sqrt{1-r_s^2}}
    ```
    Degrees of freedom (df) = $n-2$

---

### LOS 9.b: Explain tests of independence based on contingency table data.

* **Chi-Square ($\chi^2$) Test Statistic for Independence (Contingency Table)**
    (Tests the hypothesis that two categorical variables are independent)
    ```math
    \chi^2 = \sum_{i=1}^{\text{rows}} \sum_{j=1}^{\text{columns}} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}
    ```
    Where:
    * $O_{ij}$ = Observed frequency in cell (row $i$, column $j$)
    * $E_{ij}$ = Expected frequency in cell (row $i$, column $j$)

* **Expected Frequency ($E_{ij}$) for a Cell in a Contingency Table**
    ```math
    E_{ij} = \frac{(\text{Row } i \text{ Total}) \times (\text{Column } j \text{ Total})}{\text{Grand Total (Overall Total Observations)}}
    ```

* **Degrees of Freedom for Chi-Square Test of Independence**
    ```math
    df = (\text{Number of Rows} - 1) \times (\text{Number of Columns} - 1)
    ```

---
---

## Reading 10: Simple Linear Regression

### LOS 10.a: Describe a simple linear regression model, how the least squares criterion is used to estimate regression coefficients, and the interpretation of these coefficients.

* **Simple Linear Regression Model (Population Model)**
    ```math
    Y_i = b_0 + b_1 X_i + \epsilon_i
    ```
    Where:
    * $Y_i$ = $i^{th}$ value of the dependent variable
    * $X_i$ = $i^{th}$ value of the independent variable
    * $b_0$ = True population intercept
    * $b_1$ = True population slope coefficient
    * $\epsilon_i$ = $i^{th}$ error term (residual)

* **Estimated Simple Linear Regression Equation (Sample Model)**
    ```math
    \hat{Y}_i = \hat{b}_0 + \hat{b}_1 X_i
    ```
    Where:
    * $\hat{Y}_i$ = Predicted value of $Y_i$
    * $\hat{b}_0$ = Estimated intercept
    * $\hat{b}_1$ = Estimated slope coefficient

* **Estimated Slope Coefficient ($\hat{b}_1$)**
    ```math
    \hat{b}_1 = \frac{\sum_{i=1}^{n}(X_i - \bar{X})(Y_i - \bar{Y})}{\sum_{i=1}^{n}(X_i - \bar{X})^2} = \frac{Cov(X,Y)}{Var(X)}
    ```

* **Estimated Intercept ($\hat{b}_0$)**
    ```math
    \hat{b}_0 = \bar{Y} - \hat{b}_1 \bar{X}
    ```

---

### LOS 10.b: Explain the assumptions underlying the simple linear regression model, and describe how residuals and residual plots indicate if these assumptions may have been violated.

*(This LOS is primarily descriptive regarding the assumptions: 1. Linear relationship, 2. Homoskedasticity (constant variance of residuals), 3. Independence of residuals, 4. Normality of residuals. Residual plots are used to check these.)*

---

### LOS 10.c: Calculate and interpret measures of fit and formulate and evaluate tests of fit and of regression coefficients in a simple linear regression.

*(Some measures of fit (like R²) are also tied to ANOVA in LOS 10.d)*

* **t-Test Statistic for Significance of a Regression Coefficient (e.g., $\hat{b}_1$)**
    (Used to test hypotheses like $H_0: b_1 = B_1$, where $B_1$ is often 0)
    ```math
    t = \frac{\hat{b}_1 - B_1}{s_{\hat{b}_1}}
    ```
    Where:
    * $\hat{b}_1$ = Estimated slope coefficient
    * $B_1$ = Hypothesized value for $b_1$ (typically 0 for significance testing)
    * $s_{\hat{b}_1}$ = Standard error of the slope coefficient $\hat{b}_1$
    Degrees of freedom (df) = $n-k-1$ (for simple linear regression, $k=1$, so df = $n-2$).

---

### LOS 10.d: Describe the use of analysis of variance (ANOVA) in regression analysis, interpret ANOVA results, and calculate and interpret the standard error of estimate in a simple linear regression.

* **Total Sum of Squares (SST)** (Total Variation)
    ```math
    SST = \sum_{i=1}^{n} (Y_i - \bar{Y})^2
    ```

* **Regression Sum of Squares (SSR)** (Explained Variation)
    ```math
    SSR = \sum_{i=1}^{n} (\hat{Y}_i - \bar{Y})^2
    ```

* **Sum of Squared Errors (SSE)** (Unexplained Variation / Residual Sum of Squares)
    ```math
    SSE = \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2 = \sum_{i=1}^{n} e_i^2
    ```

* **ANOVA Relationship**
    ```math
    SST = SSR + SSE
    ```

* **Mean Square Regression (MSR)**
    ```math
    MSR = \frac{SSR}{k}
    ```
    (For simple linear regression, $k=1$, so $MSR = SSR$)

* **Mean Squared Error (MSE)**
    ```math
    MSE = \frac{SSE}{n-k-1}
    ```
    (For simple linear regression, $k=1$, so $df_{error} = n-2$, and $MSE = \frac{SSE}{n-2}$)

* **Standard Error of Estimate (SEE or $s_e$)**
    ```math
    SEE = \sqrt{MSE} = \sqrt{\frac{SSE}{n-2}}
    ```

* **Coefficient of Determination ($R^2$)**
    ```math
    R^2 = \frac{SSR}{SST} = \frac{\text{Explained Variation}}{\text{Total Variation}}
    ```
    Also, $R^2 = 1 - \frac{SSE}{SST}$
    (For simple linear regression, $R^2 = (\text{correlation coefficient between X and Y})^2 = r_{XY}^2$)

* **F-Statistic (for overall significance of the regression model)**
    ```math
    F = \frac{MSR}{MSE} = \frac{SSR/k}{SSE/(n-k-1)}
    ```
    (For simple linear regression with $k=1$ independent variable and $n-2$ error df: $F = \frac{SSR/1}{SSE/(n-2)}$)
    (Note: For simple linear regression, $F = t_{\hat{b}_1}^2$)

---

### LOS 10.e: Calculate and interpret the predicted value for the dependent variable, and a prediction interval for it, given an estimated linear regression model and a value for the independent variable.

* **Predicted Value of Y ($\hat{Y}_p$) for a given value of X ($X_p$)**
    ```math
    \hat{Y}_p = \hat{b}_0 + \hat{b}_1 X_p
    ```

* **Confidence Interval for a Predicted Value of Y**
    ```math
    \hat{Y}_p \pm t_c \times s_f
    ```
    Where:
    * $\hat{Y}_p$ = Predicted value of Y
    * $t_c$ = Critical t-value for the desired confidence level with $n-2$ degrees of freedom
    * $s_f$ = Standard error of the forecast

* **Variance of the Forecast ($s_f^2$)**
    ```math
    s_f^2 = s_e^2 \left(1 + \frac{1}{n} + \frac{(X_p - \bar{X})^2}{\sum_{i=1}^{n}(X_i - \bar{X})^2}\right)
    ```
    Where:
    * $s_e^2 = MSE$ (Mean Squared Error)
    * $n$ = Number of observations
    * $X_p$ = Specific value of the independent variable for which the forecast is made
    * $\bar{X}$ = Mean of the independent variable
    *(Note: The text indicates you're unlikely to calculate $s_f$ on the Level I exam; it would likely be provided.)*

---

### LOS 10.f: Describe different functional forms of simple linear regressions.

* **Log-Lin Model** (Natural log of dependent variable, linear independent variable)
    ```math
    \ln(Y_i) = \hat{b}_0 + \hat{b}_1 X_i
    ```
    (Interpretation: A one-unit change in $X$ leads to an approximate $(\hat{b}_1 \times 100)\%$ change in $Y$.)

* **Lin-Log Model** (Linear dependent variable, natural log of independent variable)
    ```math
    Y_i = \hat{b}_0 + \hat{b}_1 \ln(X_i)
    ```
    (Interpretation: A 1% change in $X$ leads to an approximate $\hat{b}_1/100$ unit change in $Y$.)

* **Log-Log Model** (Natural log of both dependent and independent variables)
    ```math
    \ln(Y_i) = \hat{b}_0 + \hat{b}_1 \ln(X_i)
    ```
    (Interpretation: $\hat{b}_1$ is the elasticity; a 1% change in $X$ leads to an approximate $\hat{b}_1\%$ change in $Y$.)

---