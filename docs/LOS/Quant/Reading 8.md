## <span style="color: #1565C0;">Reading 8: Hypothesis Testing</span>

### <span style="color: #1565C0;">🎯 Introduction</span>

Welcome, future charterholder! Imagine you're a detective in a courtroom drama. 🏛️ A claim has been made—for example, "This mutual fund has an average return of zero." Your job is to challenge that claim. The starting assumption, the "innocent until proven guilty," is called the **null hypothesis** ($H_0$). You then gather evidence (your sample data) and perform a statistical test. If your evidence is strong enough (a high test statistic), you can **reject the null hypothesis** and declare that the fund's return is likely not zero. If the evidence is weak, you **fail to reject** it, meaning you didn't have enough proof. This reading is your guide to conducting these financial trials, from setting up the case to making the final verdict!

-----

### <span style="color: #1565C0;">Part 1: The Rules of the Courtroom: Hypothesis Testing Basics (LOS 8.a, 8.b) ⚖️</span>

**Hypothesis testing** is a formal procedure for deciding between two competing statements about a population parameter. The process follows a clear set of steps.

#### <span style="color: #6A1B9A;">1.1 Hypothesis Testing Procedure</span>

* **State the Hypotheses:** Null vs Alternative
* **Choose the test statistic** (e.g., z-stat, t-stat)
* **Set the significance level** (alpha)
* **State the decision rule** (critical value)
* **Collect data and calculate the test statistic**
* **Make a decision:** reject or fail to reject $H_0$

  * **Null Hypothesis ($H_0$):** This is the initial belief or the "statement of no effect" that you are trying to disprove. It **always** includes the "equal to" sign (=, ≤, or ≥). Example: $H_0: \mu = 0$.
  * **Alternative Hypothesis ($H_a$):** This is what you conclude if you reject the null. It's usually what you're trying to prove. Example: $H_a: \mu \neq 0$.

#### <span style="color: #6A1B9A;">1.2 Making a Decision: Test Statistic vs. Critical Value</span>

Your **test statistic** is calculated from your sample data. It measures how far your sample result is from the value claimed in the null hypothesis.

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\text{Test Statistic} = \frac{\text{Sample Statistic} - \text{Hypothesized Value}}{\text{Standard Error of the Sample Statistic}}$$

</div>

The **critical value** is your threshold for proof. It's determined by your chosen **significance level ($\alpha$)**, which is the probability of making a Type I error. Common levels are 5% (0.05) or 1% (0.01). If your test statistic is more extreme than your critical value, you have enough evidence to reject the null hypothesis.

#### <span style="color: #6A1B9A;">1.3 Errors in Judgment: Type I and Type II Errors</span>

Just like in a real trial, you can make mistakes.

| Decision                 | True Condition: $H_0$ is True             | True Condition: $H_0$ is False                |
| :----------------------- | :---------------------------------------- | :-------------------------------------------- |
| **Do not reject $H_0$** | Correct Decision ✅ (Confidence = 1-α)     | **Type II Error** ❌ (Prob = $\beta$)         |
| **Reject $H_0$** | **Type I Error** ❌ (Prob = $\alpha$)     | Correct Decision ✅ (**Power** = 1 - $\beta$) |

  * **Type I Error:** Rejecting a true null hypothesis. The probability of this is your **significance level, $\alpha$**.
  * **Type II Error:** Failing to reject a false null hypothesis. The probability of this is $\beta$.
  * **Power of a Test:** Correctly rejecting a false null hypothesis. This is what you want! **Power = 1 - $\beta$**.

There's a trade-off: decreasing your chance of a Type I error (e.g., moving from $\alpha=5\%$ to $\alpha=1\%$) makes it harder to reject the null, which *increases* your chance of a Type II error and *reduces* the power of your test.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️: The exam will test the relationship between **Type I error**, **Type II error**, and **Power**. For a given sample size, Power and Type I error ($\alpha$) move together: increasing $\alpha$ (e.g., from 1% to 5%) makes it easier to reject the null, which raises the test's power but also increases the chance of a Type I error.

</div>
</div>

#### <span style="color: #00838F;">1.4 Global & Local Context 🌍</span>

* **Global Example:** Financial institutions worldwide use hypothesis testing to validate investment strategy performance claims.
* **Local Example (India):** SEBI requires mutual funds to validate risk metrics using statistical tests for regulatory compliance.

-----

### <span style="color: #1565C0;">Part 2: Choosing Your Weapon: Types of Hypothesis Tests (LOS 8.c, 8.d) ⚔️</span>

Different questions require different statistical tools. Here are the main tests you need to know for Level 1, along with their test statistic formulas.

| Hypothesis Test of...            | Use as Test Statistic                   | With Degrees of Freedom (df):       |
| :------------------------------- | :-------------------------------------- | :---------------------------------- |
| **One** population **mean** | t-statistic (or z-statistic for large n) | $n-1$                               |
| **Two** population **means** | t-statistic                             | Varies ($n_1+n_2-2$ or more complex) |
| **One** population **variance** | Chi-square statistic ($\chi^2$)         | $n-1$                               |
| **Two** population **variances** | F-statistic                             | $n_1-1$ (num), $n_2-1$ (den)      |

#### <span style="color: #6A1B9A;">2.1 Tests for Population Means (t-tests)</span>

  * **Test of a Single Mean:** Used to test if a population mean is equal to a specific value.
    * *Question*: "Is the average monthly return of this fund significantly different from zero?"
    * *Test Statistic*:
      <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
      
      $$t_{n-1} = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$$
      
      </div>
      Where $\bar{x}$ = sample mean, $\mu_0$ = hypothesized population mean, $s$ = sample standard deviation, $n$ = sample size.

  * **Test for Difference in Means (Independent Samples, Variances Assumed Equal):** Used to compare the means of two separate, independent groups.
    * *Question*: "Is the average return of growth stocks different from the average return of value stocks?"
    * *Test Statistic*:
      <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
      
      $$t_{n_1+n_2-2} = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_p^2}{n_1} + \frac{s_p^2}{n_2}}}$$
      
      $$s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$$
      
      </div>
      Where $\bar{x}_1, \bar{x}_2$ = sample means, $(\mu_1 - \mu_2)$ = hypothesized difference (often 0), $n_1, n_2$ = sample sizes, and $s_p^2$ is the pooled variance.

  * **Paired Comparisons Test (Dependent Samples):** Used for "before and after" tests on the same group, or when two samples are related.
    * *Question*: "Did the average beta of companies in the Indian telecom sector change *after* the introduction of 5G?"
    * *Test Statistic*:
      <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
      
      $$t_{n-1} = \frac{\bar{d} - \mu_{dz}}{s_{\bar{d}}}$$
      
      </div>
      Where $\bar{d}$ = sample mean of differences, $\mu_{dz}$ = hypothesized mean difference (often 0), $s_{\bar{d}} = s_d / \sqrt{n}$ is the standard error of the mean difference, $s_d$ is the sample standard deviation of the differences, and $n$ = number of pairs.

#### <span style="color: #6A1B9A;">2.2 Tests for Population Variances ($\chi^2$ and F-tests)</span>

  * **Chi-Square ($\chi^2$) Test:** Used to test if the variance of a single population is equal to a specific value.
    * *Question*: "An ETF prospectus claims its annual return volatility (standard deviation) is 15%. Based on our sample from the last 3 years, is this claim still valid?"
    * *Test Statistic*:
      <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
      
      $$\chi^2_{n-1} = \frac{(n-1)s^2}{\sigma_0^2}$$
      
      </div>
      Where $n$ = sample size, $s^2$ = sample variance, $\sigma_0^2$ = hypothesized population variance.

  * **F-Test:** Used to compare the variances of two independent populations.
    * *Question*: "Is the volatility of earnings for the Indian IT industry the same as the volatility of earnings for the US IT industry?"
    * *Test Statistic*:
      <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
      
      $$F_{n_1-1, n_2-1} = \frac{s_1^2}{s_2^2}$$
      
      </div>
      Where $s_1^2$ and $s_2^2$ are the sample variances (conventionally, place the larger $s^2$ in the numerator). $n_1-1$ are the numerator degrees of freedom, and $n_2-1$ are the denominator degrees of freedom.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️: Identify the appropriate test for the question. Two independent groups comparing means → difference-in-means t-test. Same group before-and-after → paired comparisons t-test. Comparing two variances → F-test. Testing a single variance → Chi-square test.

</div>
</div>

#### <span style="color: #00838F;">2.3 Global & Local Context 🌍</span>

* **Global Example:** U.S. mutual funds use t-tests to validate claims about average returns or volatility in prospectuses.
* **Local Example (India):** Indian portfolio managers use F-tests to compare volatility across different market sectors (IT vs. Pharma).

-----

### <span style="color: #1565C0;">Part 3: Parametric vs. Nonparametric Tests: Picky vs. Flexible Tools (LOS 8.e) 🛠️</span>

#### <span style="color: #6A1B9A;">3.1 Parametric Tests</span>

**Parametric Tests** (like the t-test, F-test, and $\chi^2$-test) are powerful but picky. They rely on **assumptions** about the population's distribution, most commonly that the population is **normally distributed**. If the assumptions hold, these tests are the most powerful.

#### <span style="color: #6A1B9A;">3.2 Nonparametric Tests</span>

**Nonparametric Tests** are the flexible "multi-tools" of statistics. They make few or no assumptions about the population's distribution. You would use a nonparametric test when:

* The assumptions for a parametric test are violated (e.g., the data is clearly not normal).
* The data are **ranks** (ordinal) instead of values (e.g., ranking mutual funds from 1st to 10th based on performance).
* The hypothesis itself doesn't involve a parameter (e.g., testing if data is random).

While less powerful than parametric tests when assumptions are met, they are essential when your data doesn't play by the normal rules.

#### <span style="color: #00838F;">3.3 Global & Local Context 🌍</span>

* **Global Example:** International hedge funds use nonparametric tests when analyzing non-normal return distributions.
* **Local Example (India):** Indian analysts may use nonparametric tests for small-cap stocks where return distributions are highly skewed.

-----

### <span style="color: #1565C0;">🧪 Formula Summary</span>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**General Test Statistic Structure:**

$$\text{Test Statistic} = \frac{\text{Sample Statistic} - \text{Hypothesized Value}}{\text{Standard Error of the Sample Statistic}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Single Mean t-test:**

$$t_{n-1} = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Difference in Means t-test:**

$$t_{n_1+n_2-2} = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_p^2}{n_1} + \frac{s_p^2}{n_2}}}$$

$$s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Paired Comparisons t-test:**

$$t_{n-1} = \frac{\bar{d} - \mu_{dz}}{s_{\bar{d}}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Chi-Square Test:**

$$\chi^2_{n-1} = \frac{(n-1)s^2}{\sigma_0^2}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**F-Test:**

$$F_{n_1-1, n_2-1} = \frac{s_1^2}{s_2^2}$$

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* **$H_0$ always includes an equality.** The null hypothesis contains =, ≤, or ≥.
* **Reject if extreme.** Reject the null when the calculated test statistic lies in the rejection region (more extreme than the critical value).
* **Know your errors.** Type I error (probability = $\alpha$): rejecting a true null. Type II error (probability = $\beta$): failing to reject a false null. Power = $1 - \beta$.
* **Match the test to the question.** Choose t, Chi-square, or F based on means vs variances and one vs two populations.
* **Parametric tests need assumptions (especially normality).** Use nonparametric tests when assumptions fail.

</div>
</div>