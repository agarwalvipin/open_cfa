# 📈 Formula Sheet: Week 5 - Estimation, Inference & Hypothesis Testing

## Reading 7: Estimation and Inference

### LOS 7.a: Compare and contrast simple random, stratified random, cluster, convenience, and judgmental sampling and their implications for sampling error in an investment problem.

*(This LOS is primarily descriptive and does not introduce specific calculation formulas.)*

---

### LOS 7.b: Explain the central limit theorem and its importance for the distribution and standard error of the sample mean.

* **Central Limit Theorem (CLT)**
    * States that for a simple random sample of size $n$ (sufficiently large, typically $n \ge 30$) from a population with mean $\mu$ and finite variance $\sigma^2$, the sampling distribution of the sample mean $\bar{x}$ approaches a normal distribution. [cite: 974]
    * **Mean of the sampling distribution of $\bar{x}$** = $\mu$ (Population mean) [cite: 980]
    * **Variance of the sampling distribution of $\bar{x}$** = $\frac{\sigma^2}{n}$ [cite: 981]

* **Standard Error of the Sample Mean ($\sigma_{\bar{x}}$)**
    * When population standard deviation ($\sigma$) is known:
        ```math
        \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
        ```
        [cite: 983]
        Where:
        * $\sigma$ = Population standard deviation
        * $n$ = Sample size

* **Estimated Standard Error of the Sample Mean ($s_{\bar{x}}$)**
    * When population standard deviation ($\sigma$) is unknown (and estimated by sample standard deviation $s$):
        ```math
        s_{\bar{x}} = \frac{s}{\sqrt{n}}
        ```
        [cite: 984]
        Where:
        * $s$ = Sample standard deviation
        * $n$ = Sample size

---

### LOS 7.c: Describe the use of resampling (bootstrap, jackknife) to estimate the sampling distribution of a statistic.

*(This LOS is primarily descriptive of techniques and does not introduce specific calculation formulas for the methods themselves in this reading.)*

---
---

## Reading 8: Hypothesis Testing

### LOS 8.a: Explain hypothesis testing and its components, including statistical significance, Type I and Type II errors, and the power of a test.

* **Test Statistic (General Form)**
    ```math
    \text{Test Statistic} = \frac{\text{Sample Statistic} - \text{Hypothesized Value}}{\text{Standard Error of the Sample Statistic}}
    ```
    [cite: 1058]

* **Standard Error of the Sample Statistic (when the statistic is the sample mean, $\bar{x}$)**
    * If population standard deviation ($\sigma$) is known:
        ```math
        \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
        ```
        [cite: 1059]
    * If population standard deviation ($\sigma$) is unknown (estimated using sample standard deviation $s$):
        ```math
        s_{\bar{x}} = \frac{s}{\sqrt{n}}
        ```
        [cite: 1059]

* **Power of a Test**
    ```math
    \text{Power of a Test} = 1 - P(\text{Type II error})
    ```
    [cite: 1074]

---

### LOS 8.b: Construct hypothesis tests and determine their statistical significance, the associated Type I and Type II errors, and power of the test given a significance level.

#### Tests Concerning the Value of a Population Mean

* **t-statistic (when population variance is unknown)**
    (Used for hypotheses about a single population mean, e.g., $H_0: \mu = \mu_0$)
    ```math
    t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}
    ```
    Degrees of freedom (df) = $n-1$. [cite: 1109]
    (Note: For large samples ($n \ge 30$), the z-distribution can be used as an approximation. [cite: 1110])

---

#### Tests Concerning Differences Between Means

* **t-test for Difference Between Means (Independent Samples, Population Variances Assumed Equal)**
    (Used for hypotheses like $H_0: \mu_1 - \mu_2 = 0$)
    1.  **Pooled Variance ($s_p^2$)**:
        ```math
        s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}
        ```
        [cite: 1119]
    2.  **t-statistic**:
        ```math
        t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)_H}{\sqrt{\frac{s_p^2}{n_1} + \frac{s_p^2}{n_2}}}
        ```
        [cite: 1119]
        Where $(\mu_1 - \mu_2)_H$ is the hypothesized difference (often 0).
        Degrees of freedom (df) = $n_1 + n_2 - 2$. [cite: 1119]

* **Paired Comparisons t-test (Means of Dependent Samples)**
    (Used for hypotheses about the mean difference $\mu_d$, e.g., $H_0: \mu_d = \mu_{dz}$, where $\mu_{dz}$ is often 0)
    1.  **Sample Mean Difference ($\bar{d}$)**:
        ```math
        \bar{d} = \frac{1}{n}\sum_{i=1}^{n}d_i
        ```
        [cite: 1145]
        Where $d_i$ is the difference for the $i^{th}$ pair.
    2.  **Sample Standard Deviation of Differences ($s_d$)**:
        ```math
        s_d = \sqrt{\frac{\sum_{i=1}^{n}(d_i - \bar{d})^2}{n-1}}
        ```
        [cite: 1145]
    3.  **Standard Error of the Mean Difference ($s_{\bar{d}}$)**:
        ```math
        s_{\bar{d}} = \frac{s_d}{\sqrt{n}}
        ```
        [cite: 1145]
    4.  **t-statistic**:
        ```math
        t = \frac{\bar{d} - \mu_{dz}}{s_{\bar{d}}}
        ```
        [cite: 1145]
        Degrees of freedom (df) = $n-1$ (where $n$ is the number of paired observations). [cite: 1145]

---

#### Tests Concerning Variances

* **Chi-Square ($\chi^2$) Test for the Value of a Single Population Variance**
    (Used for hypotheses like $H_0: \sigma^2 = \sigma_0^2$)
    ```math
    \chi^2 = \frac{(n-1)s^2}{\sigma_0^2}
    ```
    Where:
    * $s^2$ = Sample variance
    * $\sigma_0^2$ = Hypothesized population variance
    * $n$ = Sample size
    Degrees of freedom (df) = $n-1$. [cite: 1178]

* **F-test for Comparing Two Population Variances (Independent Samples from Normal Populations)**
    (Used for hypotheses like $H_0: \sigma_1^2 = \sigma_2^2$)
    ```math
    F = \frac{s_1^2}{s_2^2}
    ```
    [cite: 1197]
    Where, by convention, $s_1^2$ is the larger sample variance and $s_2^2$ is the smaller sample variance.
    Degrees of freedom for the numerator (df1) = $n_1 - 1$.
    Degrees of freedom for the denominator (df2) = $n_2 - 1$. [cite: 1197]

---

### LOS 8.c: Compare and contrast parametric and nonparametric tests, and describe situations where each is the more appropriate type of test.

*(This LOS is primarily descriptive and compares test types. A "runs test" is mentioned as an example of a nonparametric test, but its formula is not provided in this reading for calculation.)*

---