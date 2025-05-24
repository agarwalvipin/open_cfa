## Week 5: Key Formulas 🧪

### Reading 7: Estimation and Inference – Sampling & Central Limit Theorem

* **Standard Error of the Sample Mean (Population Variance Known)**:
    Used to measure the dispersion of sample means around the population mean when the population standard deviation is known.
    $$ \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} $$
    where:
    * $\sigma_{\bar{x}}$ = standard error of the sample mean [cite: 4234]
    * $\sigma$ = standard deviation of the population [cite: 4234]
    * $n$ = size of the sample [cite: 4234]

* **Standard Error of the Sample Mean (Population Variance Unknown)**:
    Used to estimate the dispersion of sample means when the population standard deviation is unknown and the sample standard deviation is used instead.
    $$ s_{\bar{x}} = \frac{s}{\sqrt{n}} $$
    where:
    * $s_{\bar{x}}$ = standard error of the sample mean (estimated) [cite: 4235]
    * $s$ = standard deviation of the sample [cite: 4235]
    * $n$ = size of the sample [cite: 4235]

---
### Reading 8: Hypothesis Testing

* **General Formula for a Test Statistic**:
    Compares the sample statistic to the hypothesized value, scaled by the standard error.
    $$ \text{Test Statistic} = \frac{\text{Sample Statistic} - \text{Hypothesized Value}}{\text{Standard Error of the Sample Statistic}} $$
    [cite: 4309]

* **Test Statistic for Hypothesis Test of a Single Population Mean (z-test for large samples or known variance, t-test for small samples with unknown variance)**:
    For a sample mean $\bar{x}$, hypothesized population mean $\mu_0$:
    If population variance $\sigma^2$ is known (or large sample $n \ge 30$ allows use of sample variance $s^2$ as estimate for z-test):
    $$ z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} $$
    If population variance is unknown and sample is small (typically $n < 30$) and population is normally distributed (t-test):
    $$ t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}} $$
    (with $n-1$ degrees of freedom)

* **Test Statistic for Difference Between Means (Independent Samples, Variances Assumed Equal)**:
    Used to test if the means of two independent, normally distributed populations are equal, assuming their unknown variances are equal.
    $$ t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_p^2}{n_1} + \frac{s_p^2}{n_2}}} $$
    where the pooled variance $s_p^2$ is:
    $$ s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2} $$
    (with $n_1 + n_2 - 2$ degrees of freedom) [cite: 4370]

* **Test Statistic for Paired Comparisons Test (Means of Dependent Samples)**:
    Used when samples are dependent (e.g., before and after measurements on the same subjects).
    $$ t = \frac{\bar{d} - \mu_{dz}}{s_{\bar{d}}} $$
    where:
    * $\bar{d}$ = sample mean difference between paired observations [cite: 4396]
    * $\mu_{dz}$ = hypothesized mean of paired differences (commonly 0) [cite: 4396]
    * $s_{\bar{d}} = \frac{s_d}{\sqrt{n}}$ (standard error of the mean difference) [cite: 4396]
    * $s_d$ = sample standard deviation of the paired differences $d_i$ [cite: 4396]
    * $n$ = number of paired observations
    (with $n-1$ degrees of freedom)

* **Test Statistic for Hypothesis Test of a Single Population Variance (Chi-Square Test)**:
    Used for tests concerning the variance of a normally distributed population.
    $$ \chi^2 = \frac{(n-1)s^2}{\sigma_0^2} $$
    where:
    * $s^2$ = sample variance
    * $\sigma_0^2$ = hypothesized population variance
    * $n-1$ = degrees of freedom
    [cite: 4429]

* **Test Statistic for Comparing Two Population Variances (F-Test)**:
    Used to test the hypothesis of equality of variances of two normally distributed populations, based on independent samples.
    $$ F = \frac{s_1^2}{s_2^2} $$
    where $s_1^2$ is conventionally the larger sample variance.
    (with $n_1 - 1$ numerator degrees of freedom and $n_2 - 1$ denominator degrees of freedom) [cite: 4448]

---
*Ethical and Professional Standards (Readings 92-93) are generally not formula-based but focus on principles, standards, and their application.*