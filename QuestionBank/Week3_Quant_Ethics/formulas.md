# CFA Level 1 - Week 3 Formula Sheet

## Reading 3: Statistical Measures of Asset Returns

### Measures of Central Tendency

* **Arithmetic Mean (Sample):**
    ```math
    \bar{x} = \frac{\sum_{i=1}^n x_i}{n}
    ```
    [cite: 3747]

### Measures of Dispersion

* **Range:**
    ```math
    \text{Range} = \text{Maximum Value} - \text{Minimum Value}
    ```
    [cite: 3788]

* **Mean Absolute Deviation (MAD):**
    ```math
    MAD = \frac{\sum_{i=1}^n |x_i - \bar{x}|}{n}
    ```
    [cite: 3789]

* **Sample Variance ($s^2$):**
    ```math
    s^2 = \frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n-1}
    ```
    [cite: 3793]

* **Sample Standard Deviation (s):**
    ```math
    s = \sqrt{\frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n-1}}
    ```
    [cite: 3806]

* **Coefficient of Variation (CV):**
    ```math
    CV = \frac{s}{\bar{x}}
    ```
    [cite: 3814]

* **Target Downside Deviation (Target Semideviation, $s_{target}$):**
    ```math
    s_{target} = \sqrt{\frac{\sum_{\text{for all } x_i \leq R_T} (x_i - R_T)^2}{n-1}}
    ```
    *Where $R_T$ is the target return.* [cite: 3825]

### Skewness and Kurtosis (Approximate Formulas for Large Samples)

* **Sample Skewness (Sk):**
    ```math
    Sk \approx \frac{1}{n} \frac{\sum_{i=1}^n (x_i - \bar{x})^3}{s^3}
    ```
    [cite: 3857]

* **Sample Kurtosis (K):**
    ```math
    K \approx \frac{1}{n} \frac{\sum_{i=1}^n (x_i - \bar{x})^4}{s^4}
    ```
    *Note: Excess Kurtosis = Sample Kurtosis - 3.* [cite: 3879]

### Covariance and Correlation

* **Sample Covariance ($Cov_{XY}$):**
    ```math
    Cov_{XY} = s_{XY} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{n-1}
    ```
    [cite: 3888]

* **Correlation Coefficient ($\rho_{XY}$ or $r_{XY}$):**
    ```math
    \rho_{XY} = r_{XY} = \frac{Cov_{XY}}{s_X s_Y}
    ```
    [cite: 3895]

## Reading 4: Probability Trees and Conditional Expectations

* **Expected Value of a Random Variable X (from probability model):**
    ```math
    E(X) = \sum_{i=1}^n P(x_i) x_i
    ```
    [cite: 3959]

* **Variance of a Random Variable X (from probability model):**
    ```math
    \sigma^2(X) = E[(X - E(X))^2] = \sum_{i=1}^n P(x_i) [x_i - E(X)]^2
    ```
    [cite: 3962, 3967]

* **Bayes' Formula:**
    ```math
    P(\text{Event}|\text{Information}) = \frac{P(\text{Information}|\text{Event})}{P(\text{Information})} \times P(\text{Event})
    ```
    *Used to update a prior probability, P(Event), given new Information.* [cite: 3984]