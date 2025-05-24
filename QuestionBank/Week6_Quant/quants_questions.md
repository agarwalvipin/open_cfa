## 🟢 Q1 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_1
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.a explain parametric and nonparametric tests of the hypothesis that the population correlation coefficient equals zero, and determine whether the hypothesis is rejected at a given level of significance.
- question_type: mcq
- difficulty: easy
- tags: [Correlation, Parametric Test, Hypothesis Testing]
</details>

A parametric test for the hypothesis that the population correlation coefficient equals zero typically assumes that the two variables are:

- A) Ranked.
- B) Categorical.
- C) Normally distributed.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
The t-test used to determine the statistical significance of a correlation coefficient is a parametric test. Parametric tests rely on assumptions about the distribution of the population from which samples are drawn. For testing the population correlation coefficient, it's assumed that the two variables follow a bivariate normal distribution. [cite: 4507]

- A is incorrect because ranked data is typically used with non-parametric tests like the Spearman rank correlation.
- B is incorrect because categorical data is tested for independence using tests like the chi-square test.
</details>

---
## 🟢 Q2 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_2
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.a explain parametric and nonparametric tests of the hypothesis that the population correlation coefficient equals zero, and determine whether the hypothesis is rejected at a given level of significance.
- question_type: mcq
- difficulty: easy
- tags: [Correlation, Nonparametric Test, Spearman Rank]
</details>

The Spearman rank correlation coefficient is most appropriate to use when:

- A) The data for both variables are continuous and known to be normally distributed.
- B) The relationship between the variables is linear, and the data are measured on an interval scale.
- C) The data are ranked (ordinal scale) or the assumptions for a parametric test of correlation are not met.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
The Spearman rank correlation test is a nonparametric test used when the data are ranks (ordinal scale). It can also be used when the assumptions underlying parametric tests (like the t-test for Pearson correlation), such as the normality of the variables, are not met. [cite: 4515]

- A and B describe situations where the Pearson correlation coefficient (a parametric measure) would be more appropriate.
</details>

---
## 🟢 Q3 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_3
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.b explain tests of independence based on contingency table data.
- question_type: mcq
- difficulty: easy
- tags: [Independence Test, Chi-Square, Contingency Table]
</details>

A contingency table is primarily used to:

- A) Test the hypothesis that the means of two populations are equal.
- B) Display the joint frequencies of two categorical variables to test for independence.
- C) Determine the correlation coefficient between two continuous variables.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
A contingency table (or two-way table) shows the number of observations from a sample that fall into specific categories based on two characteristics. It is used to test the hypothesis that these two categorical variables are independent of each other using a chi-square test. [cite: 4519, 4521]

- A is tested using t-tests (difference in means test or paired comparisons test).
- C is typically analyzed using Pearson or Spearman correlation.
</details>

---
## 🟢 Q4 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_4
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.a explain parametric and nonparametric tests of the hypothesis that the population correlation coefficient equals zero, and determine whether the hypothesis is rejected at a given level of significance.
- question_type: mcq
- difficulty: easy
- tags: [Correlation, Hypothesis Testing, Null Hypothesis]
</details>

When testing the hypothesis that the population correlation coefficient (ρ) is equal to zero, the null hypothesis ($H_0$) is typically stated as:

- A) $H_0: \rho \neq 0$
- B) $H_0: \rho = 0$
- C) $H_0: \rho > 0$

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
In hypothesis testing for the significance of a correlation coefficient, the null hypothesis ($H_0$) is that there is no linear relationship between the two variables, meaning the population correlation coefficient (ρ) is zero. [cite: 4507] The alternative hypothesis ($H_a$) would then be that ρ is not equal to zero (for a two-tailed test).

- A represents a typical alternative hypothesis for a two-tailed test.
- C represents a one-tailed alternative hypothesis.
</details>

---
## 🟢 Q5 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_5
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.b explain tests of independence based on contingency table data.
- question_type: mcq
- difficulty: easy
- tags: [Chi-Square, Degrees of Freedom, Contingency Table]
</details>

In a chi-square test for independence using a contingency table with `r` rows and `c` columns, the degrees of freedom are calculated as:

- A) $n - 1$
- B) $(r - 1)(c - 1)$
- C) $r \times c - 1$

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
The degrees of freedom for a chi-square test of independence based on a contingency table with `r` rows and `c` columns are calculated as (number of rows - 1) multiplied by (number of columns - 1), or $(r - 1)(c - 1)$. [cite: 4525]
</details>

---
## 🟢 Q6 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_6
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.a explain parametric and nonparametric tests of the hypothesis that the population correlation coefficient equals zero, and determine whether the hypothesis is rejected at a given level of significance.
- question_type: mcq
- difficulty: easy
- tags: [Correlation, Parametric Test, Degrees of Freedom]
</details>

When testing the significance of a Pearson correlation coefficient using a t-test, the degrees of freedom for the test statistic are:

- A) $n - 1$
- B) $n - 2$
- C) $n$

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
The t-statistic used to test the hypothesis that the population correlation coefficient (Pearson) equals zero follows a t-distribution with $n - 2$ degrees of freedom, where $n$ is the number of observations in the sample. [cite: 4508]
</details>

---
## 🟢 Q7 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_7
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.b explain tests of independence based on contingency table data.
- question_type: mcq
- difficulty: easy
- tags: [Independence Test, Chi-Square, Categorical Data]
</details>

The chi-square test of independence is used to determine if there is a significant association between:

- A) Two continuous variables.
- B) Two categorical variables.
- C) A continuous variable and a categorical variable.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
The chi-square test of independence is specifically designed to analyze contingency table data, where observations are classified based on two or more categorical variables. The test determines whether these categorical variables are independent or associated. [cite: 4521]
</details>

---
## 🟡 Q8 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_8
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.a explain parametric and nonparametric tests of the hypothesis that the population correlation coefficient equals zero, and determine whether the hypothesis is rejected at a given level of significance.
- question_type: mcq
- difficulty: medium
- tags: [Correlation, Parametric Test, Hypothesis Testing]
</details>

An analyst calculates a sample correlation coefficient of 0.45 between the monthly returns of two stocks based on 30 observations. To test if this correlation is significantly different from zero, the appropriate test statistic to compute is a:

- A) Chi-square statistic.
- B) F-statistic.
- C) t-statistic.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
To test the hypothesis that the population correlation coefficient (Pearson) equals zero, a t-statistic is used, provided the variables are normally distributed. The formula for the t-statistic is $t = \frac{r\sqrt{n-2}}{\sqrt{1-r^2}}$, where $r$ is the sample correlation coefficient and $n$ is the sample size. This statistic follows a t-distribution with $n-2$ degrees of freedom. [cite: 4508]

- A (Chi-square) is used for tests of variance or independence of categorical variables.
- B (F-statistic) is used for tests comparing two variances or in ANOVA.
</details>

---
## 🟡 Q9 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_9
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.a explain parametric and nonparametric tests of the hypothesis that the population correlation coefficient equals zero, and determine whether the hypothesis is rejected at a given level of significance.
- question_type: mcq
- difficulty: medium
- tags: [Correlation, Nonparametric Test, Spearman Rank]
</details>

An analyst is studying the relationship between manager rankings in two consecutive years. The data consists of ranks (1st, 2nd, 3rd, etc.). Which correlation coefficient is most suitable for this analysis?

- A) Pearson correlation coefficient.
- B) Spearman rank correlation coefficient.
- C) Point biserial correlation coefficient.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
The Spearman rank correlation coefficient is designed to measure the association between two sets of ranked (ordinal) data. Since the data provided are manager rankings, the Spearman rank correlation is the most appropriate measure. [cite: 4515]

- A (Pearson) is used for continuous data that meet parametric assumptions.
- C (Point biserial) is used when one variable is continuous and the other is dichotomous (binary categorical).
</details>

---
## 🟡 Q10 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_10
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.b explain tests of independence based on contingency table data.
- question_type: mcq
- difficulty: medium
- tags: [Independence Test, Chi-Square, Expected Frequency]
</details>

In a contingency table analysis for independence, the expected frequency for a cell (Eij) is calculated as:

- A) (Observed frequency in cell ij) / (Grand Total)
- B) (Total of Row i × Total of Column j) / (Grand Total)
- C) (Total of Row i + Total of Column j) - (Grand Total)

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
When testing for independence using a contingency table, the expected frequency for a cell in row `i` and column `j` ($E_{ij}$) under the assumption of independence is calculated as:
$E_{ij} = \frac{(\text{Total of Row } i) \times (\text{Total of Column } j)}{\text{Grand Total}}$ [cite: 4526]
This calculation represents the frequency we would expect in that cell if the two categorical variables were indeed independent.
</details>

---
## 🟡 Q11 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_11
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.a explain parametric and nonparametric tests of the hypothesis that the population correlation coefficient equals zero, and determine whether the hypothesis is rejected at a given level of significance.
- question_type: mcq
- difficulty: medium
- tags: [Correlation, Parametric Test, Interpretation]
</details>

If a calculated t-statistic for testing the significance of a correlation coefficient is 2.50, and the critical t-value for a two-tailed test at a 5% significance level with $n-2$ degrees of freedom is 2.05, the analyst should:

- A) Fail to reject the null hypothesis that the population correlation is zero.
- B) Reject the null hypothesis and conclude that the population correlation is not zero.
- C) Conclude that the population correlation is positive.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
The decision rule for a two-tailed t-test is to reject the null hypothesis ($H_0: \rho = 0$) if the absolute value of the calculated t-statistic is greater than the critical t-value. Here, |2.50| > 2.05. Therefore, the analyst should reject the null hypothesis and conclude that the population correlation coefficient is significantly different from zero. [cite: 4511, 4512]

- A is incorrect because the test statistic falls in the rejection region.
- C is too specific for a two-tailed test; while the sample correlation was likely positive to yield a positive t-statistic, the two-tailed test only concludes it's *not zero*. A one-tailed test would be needed to conclude it's positive.
</details>

---
## 🟡 Q12 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_12
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.b explain tests of independence based on contingency table data.
- question_type: mcq
- difficulty: medium
- tags: [Independence Test, Chi-Square, Interpretation]
</details>

An analyst performs a chi-square test for independence between two categorical variables: "Investment Style" (Value, Growth, Blend) and "Fund Size" (Small, Medium, Large). If the calculated chi-square statistic is less than the critical chi-square value at the chosen significance level, the analyst should conclude that:

- A) Investment style and fund size are dependent.
- B) Investment style and fund size are independent.
- C. The fund size causes the investment style.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
The null hypothesis for a chi-square test of independence states that the two categorical variables are independent. If the calculated chi-square statistic is less than the critical value, the analyst fails to reject the null hypothesis. Therefore, the conclusion is that there is not enough evidence to suggest that investment style and fund size are dependent; thus, they are considered independent. [cite: 4530]

- A is incorrect because failing to reject the null of independence means we conclude independence.
- C is incorrect as correlation or association (or lack thereof) does not imply causation.
</details>

---
## 🟡 Q13 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_13
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.a explain parametric and nonparametric tests of the hypothesis that the population correlation coefficient equals zero, and determine whether the hypothesis is rejected at a given level of significance.
- question_type: mcq
- difficulty: medium
- tags: [Correlation, Parametric Test, Sample Size]
</details>

Holding the sample correlation coefficient ($r$) constant, how does an increase in sample size ($n$) affect the calculated t-statistic for testing if the population correlation is zero?

- A) The t-statistic increases.
- B) The t-statistic decreases.
- C) The t-statistic remains unchanged.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: A**

**Explanation:**
The formula for the t-statistic for testing the significance of a correlation coefficient is $t = \frac{r\sqrt{n-2}}{\sqrt{1-r^2}}$. As the sample size ($n$) increases, the term $\sqrt{n-2}$ in the numerator increases. Since $r$ and $\sqrt{1-r^2}$ are held constant, the overall value of the t-statistic will increase. [cite: 4509] This means that with a larger sample size, even a smaller sample correlation coefficient can be found to be statistically significant.
</details>

---
## 🟡 Q14 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_14
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.a explain parametric and nonparametric tests of the hypothesis that the population correlation coefficient equals zero, and determine whether the hypothesis is rejected at a given level of significance.
- question_type: mcq
- difficulty: medium
- tags: [Correlation, Nonparametric Test, Spearman Rank]
</details>

When using the Spearman rank correlation test with a sample size greater than 30, the significance of the rank correlation coefficient ($r_s$) is typically tested using a:

- A) Chi-square test with $n-1$ degrees of freedom.
- B) F-test with $(k, n-k-1)$ degrees of freedom.
- C) t-test with $n-2$ degrees of freedom.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
For sample sizes greater than 30, the significance of the Spearman rank correlation coefficient ($r_s$) can be tested using a t-test. The test statistic is calculated as $t = \frac{r_s\sqrt{n-2}}{\sqrt{1-r_s^2}}$, which follows a t-distribution with $n-2$ degrees of freedom. [cite: 4517]
</details>

---
## 🟡 Q15 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_15
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.b explain tests of independence based on contingency table data.
- question_type: mcq
- difficulty: medium
- tags: [Independence Test, Chi-Square, Test Statistic]
</details>

The chi-square test statistic for independence measures the:

- A) Degree of linear association between two categorical variables.
- B) Difference between observed and expected frequencies in a contingency table.
- C) Probability that the observed frequencies occurred by chance.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
The chi-square test statistic is calculated as the sum of the squared differences between observed frequencies ($O_{ij}$) and expected frequencies ($E_{ij}$), divided by the expected frequencies, for all cells in a contingency table: $\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$. [cite: 4525] A larger value of this statistic indicates a greater discrepancy between observed frequencies and the frequencies expected under the assumption of independence.

- A is incorrect as chi-square tests for association/independence, not specifically linear association.
- C describes a p-value, not the test statistic itself.
</details>

---
## 🟡 Q16 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_16
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.a explain parametric and nonparametric tests of the hypothesis that the population correlation coefficient equals zero, and determine whether the hypothesis is rejected at a given level of significance.
- question_type: mcq
- difficulty: medium
- tags: [Correlation, Nonparametric Test, Spearman Rank, Ties]
</details>

When calculating the Spearman rank correlation coefficient, if there are tied ranks in the data, how are these ties typically handled?

- A) Observations with tied ranks are removed from the analysis.
- B) The average of the ranks that would have been assigned is given to each tied observation.
- C) Tied observations are assigned the lowest of the ranks they would have occupied.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
When there are tied values in the data being ranked for the Spearman rank correlation, each of the tied observations is assigned the average of the ranks they would have occupied. For example, if two observations are tied for the 2nd and 3rd rank, both are assigned the rank of (2+3)/2 = 2.5. [cite: 4516]
</details>

---
## 🔴 Q17 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_17
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.a explain parametric and nonparametric tests of the hypothesis that the population correlation coefficient equals zero, and determine whether the hypothesis is rejected at a given level of significance.
- question_type: mcq
- difficulty: hard
- tags: [Correlation, Parametric Test, Nonparametric Test, Choice of Test]
</details>

An analyst wants to test for a monotonic relationship between two variables. Variable A is measured on an interval scale but is highly skewed. Variable B is measured on an ordinal scale. The most appropriate test statistic for this scenario is the:

- A) t-statistic for Pearson correlation.
- B) Spearman rank correlation coefficient tested with a t-statistic.
- C) Chi-square statistic.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
The Spearman rank correlation coefficient is suitable for measuring the strength and direction of a monotonic relationship between two variables. It is a nonparametric test and can be used when data are ordinal (like Variable B) or when the assumptions for the Pearson correlation (like normality for Variable A, which is highly skewed) are not met. For a sufficiently large sample, its significance can be tested using a t-statistic. [cite: 4515]

- A is not ideal because Variable A is highly skewed (violating normality assumption for Pearson's t-test) and Variable B is ordinal.
- C is used for testing independence between categorical variables, not for monotonic relationships between ordinal/interval variables.
</details>

---
## 🔴 Q18 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_18
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.b explain tests of independence based on contingency table data.
- question_type: mcq
- difficulty: hard
- tags: [Independence Test, Chi-Square, Interpretation, Small Expected Frequencies]
</details>

Which of the following conditions is a key concern when interpreting the results of a chi-square test for independence from a contingency table?

- A) The sample size is very large (e.g., > 1000).
- B) The expected frequency in one or more cells is very small (e.g., less than 5).
- C) The observed frequencies are equal to the expected frequencies in all cells.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
The chi-square test for independence relies on an approximation to the chi-square distribution, which can be poor if expected frequencies in the cells of the contingency table are too small. A common rule of thumb is that expected frequencies should generally be at least 5 in each cell for the test results to be reliable. Small expected frequencies can inflate the chi-square statistic and lead to an incorrect rejection of the null hypothesis.

- A is generally not a concern; large sample sizes usually improve the reliability of the test, assuming other conditions are met.
- C would result in a chi-square statistic of 0, leading to non-rejection of the null hypothesis of independence, and is not a condition of concern for interpretation itself, but rather an outcome.
</details>

---
## 🔴 Q19 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_19
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.a explain parametric and nonparametric tests of the hypothesis that the population correlation coefficient equals zero, and determine whether the hypothesis is rejected at a given level of significance.
- question_type: mcq
- difficulty: hard
- tags: [Correlation, Hypothesis Testing, Parametric Test, Power of Test]
</details>

An analyst conducts a t-test for the hypothesis that the population correlation coefficient is zero. The test fails to reject the null hypothesis. Which of the following statements is *least* likely to be a valid reason for this outcome?

- A) The true population correlation is indeed zero or very close to zero.
- B) The sample size was too small to detect a non-zero correlation (low power).
- C) The significance level (alpha) chosen for the test was too high.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
Failing to reject the null hypothesis means there isn't enough evidence to conclude the correlation is different from zero.
- A is a valid reason: If the true correlation is zero, the test is likely to (correctly) not reject the null.
- B is a valid reason: A small sample size leads to a less powerful test, making it harder to detect a true non-zero correlation.
- C is the least likely reason. A *higher* significance level (alpha) makes it *easier* to reject the null hypothesis (i.e., it increases the probability of a Type I error and increases the power of the test for a given effect size). If the alpha was too high, the analyst would be more likely to reject the null, not fail to reject it. A significance level that is too *low* (e.g., 0.001 instead of 0.05) would make it harder to reject the null.
</details>

---
## 🔴 Q20 – Quantitative Methods - Parametric and Non-Parametric Tests of Independence
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading9_20
- level: 1
- reading: 9
- topic: Quantitative Methods
- module: 9.1
- los_text: 9.b explain tests of independence based on contingency table data.
- question_type: mcq
- difficulty: hard
- tags: [Independence Test, Chi-Square, Strength of Association]
</details>

An analyst performs a chi-square test of independence between industry sector (Technology, Healthcare, Financials) and ESG rating (Low, Medium, High) for a sample of 200 companies. The calculated chi-square statistic is 15.75. The critical chi-square value at a 5% significance level with (3-1)*(3-1) = 4 degrees of freedom is 9.488. [cite: 4530] What can the analyst conclude?

- A) There is a strong positive linear association between industry sector and ESG rating.
- B) Industry sector and ESG rating are statistically independent at the 5% significance level.
- C) There is a statistically significant association between industry sector and ESG rating at the 5% significance level.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
The calculated chi-square statistic (15.75) is greater than the critical chi-square value (9.488) for the given significance level (5%) and degrees of freedom (4). Therefore, the analyst rejects the null hypothesis of independence. This means there is a statistically significant association between industry sector and ESG rating. [cite: 4530]

- A is incorrect because the chi-square test indicates association (or lack thereof) but does not describe the strength or direction (positive/negative) of a linear association. For that, other measures specific to the type of data would be needed if variables were ordinal in a way that direction made sense.
- B is incorrect because the null hypothesis of independence is rejected.
</details>

## 🟢 Q1 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_1
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.1
- los_text: 10.a Describe a simple linear regression model, how the least squares criterion is used to estimate regression coefficients, and the interpretation of these coefficients.
- question_type: mcq
- difficulty: easy
- tags: [Regression, Dependent Variable, Independent Variable]
</details>

In a simple linear regression model, $Y_i = b_0 + b_1 X_i + \epsilon_i$, the variable $Y_i$ is best described as the:

- A) Independent variable.
- B) Dependent variable.
- C) Residual term.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
In a simple linear regression model, $Y_i$ represents the dependent variable (also known as the explained variable, endogenous variable, or predicted variable). Its variation is what the model attempts to explain using the independent variable $X_i$. [cite: 4550, 4552, 4554]

- A is incorrect. $X_i$ is the independent variable. [cite: 4555]
- C is incorrect. $\epsilon_i$ is the residual term, representing the unexplained variation in $Y_i$. [cite: 4568]
</details>

---
## 🟢 Q2 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_2
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.1
- los_text: 10.a Describe a simple linear regression model, how the least squares criterion is used to estimate regression coefficients, and the interpretation of these coefficients.
- question_type: mcq
- difficulty: easy
- tags: [Regression, Intercept, Coefficient Interpretation]
</details>

In the estimated simple linear regression equation $\hat{Y}_i = \hat{b}_0 + \hat{b}_1 X_i$, the intercept term, $\hat{b}_0$, represents:

- A) The predicted value of the dependent variable when the independent variable is zero.
- B) The change in the predicted value of the dependent variable for a one-unit change in the independent variable.
- C) The correlation between the dependent and independent variables.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: A**

**Explanation:**
The estimated intercept term ($\hat{b}_0$) in a simple linear regression equation represents the predicted value of the dependent variable (Y) when the independent variable (X) is equal to zero. It is the point where the regression line intersects the Y-axis. [cite: 4584]

- B describes the slope coefficient ($\hat{b}_1$). [cite: 4585]
- C describes the correlation coefficient, which is related to $R^2$ but is not the intercept.
</details>

---
## 🟢 Q3 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_3
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.1
- los_text: 10.b Explain the assumptions underlying the simple linear regression model, and describe how residuals and residual plots indicate if these assumptions may have been violated.
- question_type: mcq
- difficulty: easy
- tags: [Regression, Assumptions, Homoskedasticity]
</details>

One of the key assumptions of a simple linear regression model is homoskedasticity. Homoskedasticity refers to the assumption that the:

- A) Residuals are normally distributed.
- B) Variance of the residuals is constant for all observations.
- C) Residuals are independent of each other.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
Homoskedasticity is the assumption that the variance of the residual term (error term) is constant for all observations. [cite: 4600, 4607] If this assumption is violated (i.e., heteroskedasticity is present), the standard errors of the coefficient estimates may be incorrect.

- A refers to the normality assumption of residuals. [cite: 4602]
- C refers to the independence assumption of residuals. [cite: 4601]
</details>

---
## 🟢 Q4 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_4
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.2
- los_text: 10.c Calculate and interpret measures of fit and formulate and evaluate tests of fit and of regression coefficients in a simple linear regression.
- question_type: mcq
- difficulty: easy
- tags: [Regression, R-squared, Goodness of Fit]
</details>

The coefficient of determination ($R^2$) in a simple linear regression model measures the:

- A) Standard deviation of the residuals.
- B) Percentage of the total variation in the independent variable explained by the dependent variable.
- C) Percentage of the total variation in the dependent variable explained by the independent variable.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
The coefficient of determination ($R^2$) is defined as the percentage of the total variation in the dependent variable that is explained by the variation in the independent variable. [cite: 4646] It is a measure of how well the regression line fits the data.

- A describes the standard error of estimate (SEE). [cite: 4645]
- B incorrectly reverses the roles of the dependent and independent variables.
</details>

---
## 🟢 Q5 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_5
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.3
- los_text: 10.f Describe different functional forms of simple linear regressions.
- question_type: mcq
- difficulty: easy
- tags: [Regression, Functional Forms, Log-Lin Model]
</details>

In a log-lin regression model, where the dependent variable is logarithmic ($\ln Y_i$) and the independent variable is linear ($X_i$), the slope coefficient ($b_1$) is interpreted as:

- A) The absolute change in $Y$ for a one-unit change in $X$.
- B) The relative (percentage) change in $Y$ for a one-unit absolute change in $X$.
- C) The absolute change in $Y$ for a one-percent change in $X$.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
In a log-lin model ($\ln Y_i = b_0 + b_1 X_i + \epsilon_i$), the slope coefficient ($b_1$) is interpreted as the relative change (approximately the percentage change for small values of $b_1$) in the dependent variable ($Y$) for a one-unit absolute change in the independent variable ($X$). [cite: 4692, 4696]
</details>

---
## 🟢 Q6 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_6
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.1
- los_text: 10.a Describe a simple linear regression model, how the least squares criterion is used to estimate regression coefficients, and the interpretation of these coefficients.
- question_type: mcq
- difficulty: easy
- tags: [Regression, Least Squares Criterion]
</details>

The least squares criterion used to estimate the coefficients in a simple linear regression model involves minimizing the:

- A) Sum of the absolute differences between actual and predicted Y-values.
- B) Sum of the squared differences between actual and predicted Y-values.
- C) Number of observations that do not fall on the regression line.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
The least squares criterion selects the regression line that minimizes the sum of the squared vertical distances (residuals) between the actual Y-values ($Y_i$) and the Y-values predicted by the regression equation ($\hat{Y}_i$). This sum is referred to as the sum of squared errors (SSE). [cite: 4571, 4572, 4573]
</details>

---
## 🟢 Q7 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_7
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.2
- los_text: 10.d Describe the use of analysis of variance (ANOVA) in regression analysis, interpret ANOVA results, and calculate and interpret the standard error of estimate in a simple linear regression.
- question_type: mcq
- difficulty: easy
- tags: [Regression, ANOVA, SSE]
</details>

In the context of Analysis of Variance (ANOVA) for a simple linear regression, the Sum of Squared Errors (SSE) represents:

- A) The total variation in the dependent variable.
- B) The variation in the dependent variable explained by the regression.
- C) The variation in the dependent variable unexplained by the regression.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
The Sum of Squared Errors (SSE), also known as the sum of squared residuals, measures the unexplained variation in the dependent variable. [cite: 4635] It is the sum of the squared differences between the actual Y-values and the Y-values predicted by the regression line. [cite: 4637]

- A describes the Total Sum of Squares (SST). [cite: 4630]
- B describes the Regression Sum of Squares (SSR). [cite: 4631]
</details>

---
## 🟡 Q8 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_8
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.1
- los_text: 10.a Describe a simple linear regression model, how the least squares criterion is used to estimate regression coefficients, and the interpretation of these coefficients.
- question_type: mcq
- difficulty: medium
- tags: [Regression, Slope Coefficient, Coefficient Interpretation]
</details>

A simple linear regression of a stock's monthly excess returns (Y) on the market's monthly excess returns (X) yields a slope coefficient ($\hat{b}_1$) of 1.2. This *most likely* implies that:

- A) For every 1% increase in the market's excess return, the stock's excess return is predicted to increase by 1.2%.
- B) The stock is 20% less risky than the market.
- C) 120% of the variation in the stock's excess return is explained by the market's excess return.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: A**

**Explanation:**
The slope coefficient ($\hat{b}_1$) in a simple linear regression represents the estimated change in the dependent variable (stock's excess return) for a one-unit change in the independent variable (market's excess return). [cite: 4585] Thus, a slope of 1.2 means that if the market's excess return increases by 1%, the stock's excess return is predicted to increase by 1.2%. This slope is also known as the stock's beta. [cite: 4590]

- B is incorrect. A beta of 1.2 suggests the stock is 20% more volatile (in terms of systematic risk) than the market, not less risky. [cite: 4592]
- C describes the coefficient of determination ($R^2$), which cannot exceed 100%.
</details>

---
## 🟡 Q9 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_9
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.1
- los_text: 10.b Explain the assumptions underlying the simple linear regression model, and describe how residuals and residual plots indicate if these assumptions may have been violated.
- question_type: mcq
- difficulty: medium
- tags: [Regression, Assumptions, Residual Plot, Heteroskedasticity]
</details>

An analyst examining a residual plot from a simple linear regression observes that the residuals are randomly scattered around zero for low values of the independent variable, but the dispersion of residuals increases as the value of the independent variable increases. This pattern *most likely* indicates:

- A) Non-linearity in the relationship.
- B) Positive serial correlation of the residuals.
- C) Heteroskedasticity.

<details>
<summary>✅ Answer & Explanation</summary

**Correct Answer: C**

**Explanation:**
Heteroskedasticity occurs when the variance of the residuals is not constant across all levels of the independent variable. [cite: 4607] A common pattern for heteroskedasticity in a residual plot is a fan or cone shape, where the spread of residuals increases (or decreases) as the independent variable changes, which is what is described. [cite: 4608]

- A (Non-linearity) would typically show a systematic pattern in the residuals themselves (e.g., a U-shape), not just their variance. [cite: 4604, 4605]
- B (Positive serial correlation) would show a pattern where positive residuals tend to be followed by positive residuals, and negative by negative, often looking like a wave if plotted against time or sequence.
</details>

---
## 🟡 Q10 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_10
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.2
- los_text: 10.c Calculate and interpret measures of fit and formulate and evaluate tests of fit and of regression coefficients in a simple linear regression.
- question_type: mcq
- difficulty: medium
- tags: [Regression, R-squared, Correlation]
</details>

If the correlation coefficient between the dependent variable and the independent variable in a simple linear regression is 0.70, the coefficient of determination ($R^2$) is:

- A) 0.30
- B) 0.49
- C) 0.70

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
For a simple linear regression (one independent variable), the coefficient of determination ($R^2$) is equal to the square of the correlation coefficient ($r$). [cite: 4648]
Given $r = 0.70$, $R^2 = (0.70)^2 = 0.49$.
This means that 49% of the variation in the dependent variable is explained by the independent variable.
</details>

---
## 🟡 Q11 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_11
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.2
- los_text: 10.d Describe the use of analysis of variance (ANOVA) in regression analysis, interpret ANOVA results, and calculate and interpret the standard error of estimate in a simple linear regression.
- question_type: mcq
- difficulty: medium
- tags: [Regression, ANOVA, F-statistic, Significance Test]
</details>

In a simple linear regression, an F-statistic is calculated to be 5.60. The critical F-value at a 5% significance level is 4.20. Based on this information, the analyst should conclude that the:

- A) Intercept coefficient is significantly different from zero.
- B) Slope coefficient is significantly different from zero.
- C) Regression model explains more than 50% of the variation in the dependent variable.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
In a simple linear regression, the F-test assesses the overall significance of the regression model, which is equivalent to testing whether the slope coefficient is significantly different from zero. [cite: 4651] If the calculated F-statistic (5.60) is greater than the critical F-value (4.20), the null hypothesis (that the slope coefficient is zero) is rejected. [cite: 4653] Thus, the slope coefficient is significantly different from zero.

- A is incorrect. The F-test in simple linear regression tests the slope, not specifically the intercept (a t-test is used for the intercept).
- C is incorrect. While a significant F-statistic suggests the model has explanatory power, it doesn't directly indicate that $R^2$ is greater than 0.50 without more information.
</details>

---
## 🟡 Q12 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_12
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.3
- los_text: 10.e Calculate and interpret the predicted value for the dependent variable, and a prediction interval for it, given an estimated linear regression model and a value for the independent variable.
- question_type: mcq
- difficulty: medium
- tags: [Regression, Predicted Value]
</details>

An estimated simple linear regression model is given by: $\text{Predicted Sales} = 500 + 2.5 \times (\text{Advertising Spend})$. If the advertising spend for the next period is projected to be $1,000, the predicted sales would be:

- A) $1,500
- B) $2,500
- C) $3,000

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
To find the predicted sales, substitute the value of the independent variable (Advertising Spend = 1,000) into the regression equation: [cite: 4676]
Predicted Sales = $500 + 2.5 \times (1,000)$
Predicted Sales = $500 + 2,500$
Predicted Sales = $3,000
</details>

---
## 🟡 Q13 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_13
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.3
- los_text: 10.f Describe different functional forms of simple linear regressions.
- question_type: mcq
- difficulty: medium
- tags: [Regression, Functional Forms, Lin-Log Model]
</details>

An analyst estimates a lin-log regression model: $Y_i = b_0 + b_1 \ln(X_i) + \epsilon_i$. If $b_1$ is estimated to be 50, this implies that a 1% increase in $X$ is associated with an approximate:

- A) 50-unit increase in $Y$.
- B) 0.50-unit increase in $Y$.
- C) 50% increase in $Y$.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
In a lin-log model ($Y_i = b_0 + b_1 \ln(X_i) + \epsilon_i$), the slope coefficient ($b_1$) is interpreted as the absolute change in the dependent variable ($Y$) for a relative (percentage) change in the independent variable ($X$). Specifically, a 1% increase in $X$ is associated with an approximate $b_1/100$ unit change in $Y$. Therefore, if $b_1 = 50$, a 1% increase in $X$ is associated with approximately a $50/100 = 0.50$ unit increase in $Y$. [cite: 4697]
</details>

---
## 🟡 Q14 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_14
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.2
- los_text: 10.d Describe the use of analysis of variance (ANOVA) in regression analysis, interpret ANOVA results, and calculate and interpret the standard error of estimate in a simple linear regression.
- question_type: mcq
- difficulty: medium
- tags: [Regression, ANOVA, SEE]
</details>

The Standard Error of Estimate (SEE) in a simple linear regression measures the:

- A) Average distance between the actual Y-values and the mean of Y.
- B) Degree of dispersion of the actual Y-values around the regression line.
- C) Standard deviation of the estimated slope coefficient.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
The Standard Error of Estimate (SEE) for a regression is the standard deviation of its residuals. [cite: 4645] It measures the typical distance between the actual values of the dependent variable and the values predicted by the regression line, thus indicating the degree of dispersion of actual Y-values around the estimated regression line. A lower SEE indicates a better model fit.

- A is related to the total sum of squares.
- C describes the standard error of the slope coefficient, which is used to test the significance of the slope.
</details>

---
## 🟡 Q15 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_15
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.1
- los_text: 10.b Explain the assumptions underlying the simple linear regression model, and describe how residuals and residual plots indicate if these assumptions may have been violated.
- question_type: mcq
- difficulty: medium
- tags: [Regression, Assumptions, Serial Correlation]
</details>

If a plot of regression residuals against time shows a clear cyclical pattern (e.g., residuals are positive for a period, then negative, then positive again), this is *most likely* an indication of:

- A) Heteroskedasticity.
- B) Multicollinearity.
- C) Serial correlation (autocorrelation) of residuals.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
Serial correlation (or autocorrelation) of residuals occurs when the residual term for one observation is correlated with that of another observation, often in time-series data. [cite: 4601] A plot of residuals against time that shows a systematic pattern (like a cyclical or wave-like pattern) suggests that the residuals are not independent, violating a key assumption of linear regression. This is consistent with the description. [cite: 4613, 4614, 4615]

- A (Heteroskedasticity) would show a changing variance of residuals (e.g., fanning out). [cite: 4608]
- B (Multicollinearity) refers to high correlation between independent variables, which is not applicable in simple linear regression (one independent variable) and is not directly observed from a plot of residuals against time.
</details>

---
## 🟡 Q16 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_16
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.2
- los_text: 10.c Calculate and interpret measures of fit and formulate and evaluate tests of fit and of regression coefficients in a simple linear regression.
- question_type: mcq
- difficulty: medium
- tags: [Regression, Hypothesis Testing, t-statistic]
</details>

An analyst runs a simple linear regression of company profit on R&D spending. The estimated slope coefficient is 0.15, and its standard error is 0.05. There are 25 observations. To test if R&D spending has a statistically significant positive impact on profit at the 5% significance level, the analyst would compare the calculated t-statistic to a critical t-value with:

- A) 23 degrees of freedom, one-tailed test.
- B) 24 degrees of κάντε το ένα παιχνίδι για παιδιάfreedom, two-tailed test.
- C) 25 degrees of freedom, one-tailed test.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: A**

**Explanation:**
The hypothesis test for a regression coefficient uses a t-statistic with $n-k-1$ degrees of freedom, where $n$ is the number of observations and $k$ is the number of independent variables. In a simple linear regression, $k=1$, so the degrees of freedom are $n-2$. Here, $n=25$, so df = $25-2 = 23$.
The question asks to test if R&D spending has a "statistically significant *positive* impact," which implies a one-tailed test ($H_a: b_1 > 0$).

Calculated t-statistic = (Estimated coefficient - Hypothesized value) / Standard error
$t = (0.15 - 0) / 0.05 = 3.0$.
This would be compared to a one-tailed critical t-value with 23 df at the 5% significance level.
</details>

---
## 🔴 Q17 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_17
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.3
- los_text: 10.f Describe different functional forms of simple linear regressions.
- question_type: mcq
- difficulty: hard
- tags: [Regression, Functional Forms, Log-Log Model, Elasticity]
</details>

In a log-log regression model, $\ln(Y_i) = b_0 + b_1 \ln(X_i) + \epsilon_i$, the slope coefficient $b_1$ is interpreted as the:

- A) Percentage change in Y for a one-unit change in X.
- B) Unit change in Y for a one-percent change in X.
- C) Elasticity of Y with respect to X.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
In a log-log model, both the dependent and independent variables are in logarithmic form. The slope coefficient ($b_1$) directly measures the elasticity of Y with respect to X. [cite: 4698] This means $b_1$ represents the estimated percentage change in Y for a 1% change in X.

- A describes the interpretation of $b_1$ in a log-lin model. [cite: 4696]
- B describes the interpretation of $b_1$ in a lin-log model (approximately $b_1/100$ for a 1% change in X). [cite: 4697]
</details>

---
## 🔴 Q18 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_18
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.2
- los_text: 10.c Calculate and interpret measures of fit and formulate and evaluate tests of fit and of regression coefficients in a simple linear regression.
- question_type: mcq
- difficulty: hard
- tags: [Regression, ANOVA, SST, SSR, SSE]
</details>

Consider the following information from a simple linear regression:
Total Sum of Squares (SST) = 250
Regression Sum of Squares (SSR) = 150
The coefficient of determination ($R^2$) and the Sum of Squared Errors (SSE) are *closest* to:

- A) $R^2 = 0.40$; SSE = 100
- B) $R^2 = 0.60$; SSE = 100
- C) $R^2 = 0.60$; SSE = 400

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
The relationship between SST, SSR, and SSE is: SST = SSR + SSE. [cite: 4639]
Therefore, SSE = SST - SSR = 250 - 150 = 100.

The coefficient of determination ($R^2$) is calculated as SSR / SST. [cite: 4646]
$R^2 = 150 / 250 = 0.60$.

So, $R^2 = 0.60$ (or 60%) and SSE = 100.
</details>

---
## 🔴 Q19 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_19
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.1
- los_text: 10.b Explain the assumptions underlying the simple linear regression model, and describe how residuals and residual plots indicate if these assumptions may have been violated.
- question_type: mcq
- difficulty: hard
- tags: [Regression, Assumptions, Consequences of Violation]
</details>

If the assumption of homoskedasticity is violated in a simple linear regression model (i.e., heteroskedasticity is present), which of the following is the *most likely* consequence?

- A) The estimated regression coefficients ($\hat{b}_0$ and $\hat{b}_1$) will be biased.
- B) The standard errors of the regression coefficients will be unreliable, leading to incorrect conclusions from hypothesis tests.
- C) The coefficient of determination ($R^2$) will be artificially inflated.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
When heteroskedasticity (non-constant variance of residuals) is present, the ordinary least squares (OLS) estimates of the regression coefficients ($\hat{b}_0$ and $\hat{b}_1$) are still unbiased and consistent. However, the OLS estimates of the standard errors of these coefficients become unreliable (typically underestimated if variance increases with X, or overestimated if it decreases). This unreliability of standard errors leads to incorrect t-statistics and F-statistics, making hypothesis tests about the significance of the coefficients invalid. [cite: 4607]

- A is incorrect; the coefficients themselves remain unbiased.
- C is not necessarily true; $R^2$ measures the proportion of explained variance, and while heteroskedasticity affects the reliability of statistical inference, it doesn't systematically inflate $R^2$ in a predictable direction without further context.
</details>

---
## 🔴 Q20 – Quantitative Methods - Simple Linear Regression
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading10_20
- level: 1
- reading: 10
- topic: Quantitative Methods
- module: 10.3
- los_text: 10.e Calculate and interpret the predicted value for the dependent variable, and a prediction interval for it, given an estimated linear regression model and a value for the independent variable.
- question_type: mcq
- difficulty: hard
- tags: [Regression, Prediction Interval, Confidence Interval]
</details>

When predicting the value of the dependent variable using a simple linear regression model, a 95% prediction interval will be:

- A) Narrower than a 95% confidence interval for the mean value of the dependent variable, given a specific value of the independent variable.
- B) Wider than a 95% confidence interval for the mean value of the dependent variable, given a specific value of the independent variable.
- C) The same width as a 95% confidence interval for the mean value of the dependent variable, given a specific value of the independent variable.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
A prediction interval is used to estimate the range for a *single new observation* of the dependent variable, given a specific value of the independent variable. A confidence interval for the mean value of the dependent variable estimates the range for the *average* value of the dependent variable, given a specific value of the independent variable.

The prediction interval must account for two sources of uncertainty:
1. Uncertainty in estimating the true regression line (same as for the confidence interval for the mean).
2. The inherent variability of individual observations around the true regression line (the error term $\epsilon_i$).

Because the prediction interval incorporates this additional source of uncertainty (the random error term for a single observation), it will always be wider than the confidence interval for the mean value of Y at the same level of confidence and for the same value of X. The standard error of the forecast ($s_f$) used for prediction intervals is larger than the standard error used for the confidence interval of the mean. [cite: 4678]
</details>

## 🟢 Q1 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_1
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.a Describe aspects of "fintech" that are directly relevant for the gathering and analyzing of financial data.
- question_type: mcq
- difficulty: easy
- tags: [Fintech, Definition]
</details>

"Fintech" *most accurately* refers to:

- A) Financial theories developed using technological tools.
- B) The regulatory framework governing technology use in finance.
- C) Developments in technology applied to the financial services industry.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
Fintech refers to developments in technology that can be applied to the financial services industry[cite: 4732]. This includes companies that develop these technologies.

- A is too narrow; fintech is broader than just theories.
- B describes a part of the ecosystem but not fintech itself.
</details>

---
## 🟢 Q2 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_2
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.b Describe Big Data, artificial intelligence, and machine learning.
- question_type: mcq
- difficulty: easy
- tags: [Big Data, Characteristics]
</details>

Which of the following are commonly cited characteristics of Big Data?

- A) Accuracy, Brevity, and Clarity.
- B) Volume, Velocity, and Variety.
- C) Structure, Source, and Security.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
The key characteristics of Big Data are often described by the "3 V's": Volume (the vast amounts of data), Velocity (the speed at which data is generated and communicated), and Variety (the different forms data can take, from structured to unstructured)[cite: 4742].
</details>

---
## 🟢 Q3 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_3
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.b Describe Big Data, artificial intelligence, and machine learning.
- question_type: mcq
- difficulty: easy
- tags: [Artificial Intelligence, Definition]
</details>

Artificial intelligence (AI) is *best* described as:

- A) Computer systems programmed to simulate human cognition.
- B) A statistical method for analyzing large datasets.
- C) The network of interconnected physical devices generating data.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: A**

**Explanation:**
Artificial intelligence refers to computer systems that can be programmed to simulate human cognition, enabling them to perform tasks that typically require human intelligence[cite: 4760]. Neural networks are an example of AI[cite: 4761].

- B describes aspects of data science or machine learning more specifically.
- C describes the Internet of Things.
</details>

---
## 🟢 Q4 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_4
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.c Describe applications of Big Data and Data Science to investment management.
- question_type: mcq
- difficulty: easy
- tags: [Text Analytics, Application]
</details>

Analyzing the frequency of specific words and phrases in company regulatory filings to gauge sentiment is an example of:

- A) Algorithmic trading.
- B) Text analytics.
- C) Corporate exhaust.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
Text analytics refers to the analysis of unstructured data in text or voice forms[cite: 4780]. Analyzing the frequency of words and phrases in documents like regulatory filings is a common application of text analytics in finance[cite: 4781, 4782].

- A refers to computerized securities trading.
- C refers to data generated by businesses as a byproduct of their operations.
</details>

---
## 🟢 Q5 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_5
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.b Describe Big Data, artificial intelligence, and machine learning.
- question_type: mcq
- difficulty: easy
- tags: [Machine Learning, Definition]
</details>

Machine learning is a technique where a computer algorithm:

- A) Is explicitly programmed for every possible decision pathway.
- B) Learns to model output data from input data or detect patterns without human assistance.
- C) Relies solely on structured data from traditional financial reports.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
In machine learning, a computer algorithm is given inputs of source data and is designed to learn, without human assistance, how to model output data based on input data, or to learn how to detect and recognize patterns in the input data[cite: 4763, 4764].
</details>

---
## 🟢 Q6 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_6
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.b Describe Big Data, artificial intelligence, and machine learning.
- question_type: mcq
- difficulty: easy
- tags: [Big Data, Data Sources, Corporate Exhaust]
</details>

Data generated from bank records and retail scanner data are examples of what type of alternative data source?

- A) Internet of Things.
- B) Corporate exhaust.
- C) Social media posts.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
Corporate exhaust refers to data generated by businesses as a byproduct of their operations, such as bank records or retail scanner data[cite: 4738, 4739].

- A refers to data from interconnected sensor devices.
- C is data generated by individuals.
</details>

---
## 🟢 Q7 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_7
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.c Describe applications of Big Data and Data Science to investment management.
- question_type: mcq
- difficulty: easy
- tags: [Algorithmic Trading, Definition]
</details>

Computerized securities trading based on a predetermined set of rules is known as:

- A) Natural Language Processing.
- B) Algorithmic trading.
- C) Deep learning.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
Algorithmic trading refers to computerized securities trading based on a predetermined set of rules[cite: 4790].

- A refers to interpreting human language with computers.
- C is a technique within machine learning using layered neural networks.
</details>

---
## 🟡 Q8 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_8
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.b Describe Big Data, artificial intelligence, and machine learning.
- question_type: mcq
- difficulty: medium
- tags: [Big Data, Data Science, Data Processing]
</details>

In the context of data science, the process of ensuring data quality by adjusting for bad or missing data is known as:

- A) Capture.
- B) Curation.
- C) Transfer.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
Curation is a data processing method that involves assuring data quality by adjusting for bad or missing data[cite: 4752].

- A (Capture) is collecting data and transforming it into usable forms[cite: 4751].
- C (Transfer) is moving data from its source or storage to where it is needed[cite: 4754].
</details>

---
## 🟡 Q9 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_9
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.b Describe Big Data, artificial intelligence, and machine learning.
- question_type: mcq
- difficulty: medium
- tags: [Machine Learning, Supervised Learning, Unsupervised Learning]
</details>

In which type of machine learning are input and output data labeled, allowing the machine to learn how to model the outputs from the inputs?

- A) Unsupervised learning.
- B) Deep learning.
- C) Supervised learning.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
In supervised learning, the input and output data are labeled, and the machine learns to model the outputs from the inputs[cite: 4768]. The machine is then given new, unlabeled data to use the model on.

- A (Unsupervised learning) involves unlabeled input data where the machine learns to describe the structure of the data[cite: 4769].
- B (Deep learning) is a technique that can employ either supervised or unsupervised learning[cite: 4771].
</details>

---
## 🟡 Q10 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_10
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.b Describe Big Data, artificial intelligence, and machine learning.
- question_type: mcq
- difficulty: medium
- tags: [Machine Learning, Overfitting]
</details>

When a machine learning model learns the input and output data too exactly, treating noise as true parameters and identifying spurious patterns, this is known as:

- A) Underfitting.
- B) Curation.
- C) Overfitting.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
Overfitting occurs when a machine learning model learns the input and output data too exactly, essentially memorizing the training data including its noise and spurious patterns[cite: 4773]. This results in a model that is too complex and performs poorly on new, unseen data.

- A (Underfitting) occurs when the model fails to identify actual patterns and is not complex enough[cite: 4775].
- B (Curation) is a data processing step to ensure data quality.
</details>

---
## 🟡 Q11 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_11
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.c Describe applications of Big Data and Data Science to investment management.
- question_type: mcq
- difficulty: medium
- tags: [NLP, Application, Investment Management]
</details>

An investment firm uses a computer system to analyze thousands of analyst research reports to detect subtle changes in overall sentiment that are not captured by explicit buy/sell recommendations. This application is *most likely* an example of:

- A) High-frequency trading.
- B) Text analytics.
- C) Natural Language Processing (NLP).

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
Natural Language Processing (NLP) refers to the use of computers and artificial intelligence to interpret human language[cite: 4783]. Evaluating large volumes of research reports to detect subtle changes in sentiment is a potential application of NLP in finance[cite: 4785]. While text analytics is related (analyzing text data)[cite: 4780], NLP often implies a deeper level of language interpretation and understanding.

- A is a type of algorithmic trading focused on speed.
- B (Text analytics) is a broader term; NLP is a more specific application for interpreting language nuances like sentiment.
</details>

---
## 🟡 Q12 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_12
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.b Describe Big Data, artificial intelligence, and machine learning.
- question_type: mcq
- difficulty: medium
- tags: [Big Data, Data Variety, Unstructured Data]
</details>

Which of the following is an example of unstructured data in the context of Big Data?

- A) A company's quarterly earnings reported in a spreadsheet.
- B) Video footage from security cameras in a retail store.
- C) A list of stock ticker symbols and their corresponding exchange codes.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
Unstructured data refers to information that does not have a predefined format or organization[cite: 4748]. Video footage is a classic example of unstructured data[cite: 4749].

- A (spreadsheet data) is an example of structured data.
- C (list of symbols and codes) is also structured data, likely in a table format.
</details>

---
## 🟡 Q13 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_13
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.b Describe Big Data, artificial intelligence, and machine learning.
- question_type: mcq
- difficulty: medium
- tags: [Machine Learning, Deep Learning, Neural Networks]
</details>

Deep learning, a technique within machine learning, is characterized by its use of:

- A) Simple linear regression models on small datasets.
- B) Layers of neural networks to identify patterns from simple to complex.
- C) Explicitly programmed rules for every decision node.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
Deep learning is a machine learning technique that uses layers of neural networks to identify patterns, starting with simple patterns and progressing to more complex ones[cite: 4770]. It can employ supervised or unsupervised learning[cite: 4771].

- A is incorrect; deep learning typically handles complex, non-linear relationships and vast amounts of data.
- C is incorrect; machine learning, including deep learning, involves the algorithm learning from data rather than being explicitly programmed for every rule.
</details>

---
## 🟡 Q14 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_14
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.a Describe aspects of "fintech" that are directly relevant for the gathering and analyzing of financial data.
- question_type: mcq
- difficulty: medium
- tags: [Fintech, Data Analysis, Big Data]
</details>

A primary area where fintech is developing tools directly relevant for financial data analysis is:

- A) Standardizing traditional accounting report formats.
- B) Increasing functionality to handle large, diverse datasets and apply AI.
- C) Reducing the volume of data generated by financial markets.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
Key areas where fintech is developing include increasing functionality to handle large sets of data that may come from many sources and exist in various forms, and developing tools and techniques like artificial intelligence for analyzing these very large datasets[cite: 4734].

- A, while potentially useful, is not a primary development area of fintech itself, though fintech tools might consume such data.
- C is the opposite; fintech often deals with the increasing volume of data.
</details>

---
## 🟡 Q15 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_15
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.b Describe Big Data, artificial intelligence, and machine learning.
- question_type: mcq
- difficulty: medium
- tags: [Big Data, Latency]
</details>

Real-time stock market price feeds are described as having:

- A) High variety.
- B) High latency.
- C) Low latency.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
Velocity, one of the characteristics of Big Data, refers to how quickly data are communicated[cite: 4745]. Real-time data, such as stock market price feeds, are said to have low latency, meaning they are communicated very quickly with minimal delay[cite: 4745]. High latency means data are communicated periodically or with a lag[cite: 4746].
</details>

---
## 🟡 Q16 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_16
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.c Describe applications of Big Data and Data Science to investment management.
- question_type: mcq
- difficulty: medium
- tags: [Risk Governance, Big Data, Application]
</details>

How can Big Data techniques enhance risk governance in investment management?

- A) By solely relying on historical financial statement data for risk assessment.
- B) By enabling real-time monitoring of risk exposures using diverse data sources.
- C) By guaranteeing the elimination of all investment risks.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
Risk governance requires understanding a firm's exposure to various risks[cite: 4786]. Machine learning and other Big Data techniques can be useful in modeling and testing risk, particularly by using real-time data from diverse sources to monitor risk exposures[cite: 4789].

- A is too narrow; Big Data involves many non-traditional data sources beyond historical financial statements.
- C is incorrect; Big Data techniques can help manage and model risk, but not eliminate it entirely.
</details>

---
## 🔴 Q17 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_17
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.b Describe Big Data, artificial intelligence, and machine learning.
- question_type: mcq
- difficulty: hard
- tags: [Machine Learning, Underfitting, Model Complexity]
</details>

An analyst develops a machine learning model to predict stock returns. The model shows poor performance on both the training dataset and a new test dataset. It consistently fails to capture the underlying trends in the data. This scenario *most likely* describes:

- A) Overfitting.
- B) Underfitting.
- C) Successful curation.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
Underfitting occurs when the machine learning model fails to identify actual patterns and relationships in the data, treating true parameters as noise[cite: 4775]. Such a model is not complex enough to describe the data and will perform poorly on both the training data (because it hasn't learned it well) and new test data.

- A (Overfitting) describes a model that learns the training data too well, including noise, and thus performs well on training data but poorly on new test data[cite: 4773].
- C (Successful curation) would imply high-quality data, which doesn't directly explain the model's failure to capture trends.
</details>

---
## 🔴 Q18 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_18
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.b Describe Big Data, artificial intelligence, and machine learning.
- question_type: mcq
- difficulty: hard
- tags: [Big Data, Data Visualization, Unstructured Data]
</details>

Which data visualization technique is *most* suitable for displaying the frequency with which different terms appear in a large collection of unstructured text data, such as analyst reports?

- A) Scatter plots.
- B) Mind maps.
- C) Word clouds.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
Word clouds are a visualization technique used for less structured data, such as text, to illustrate the frequency with which words appear in a sample of text[cite: 4756]. More frequent words are typically displayed in a larger font.

- A (Scatter plots) are used to display the relationship between two continuous variables.
- B (Mind maps) display logical relations among concepts[cite: 4756], not directly word frequencies.
</details>

---
## 🔴 Q19 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_19
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.c Describe applications of Big Data and Data Science to investment management.
- question_type: mcq
- difficulty: hard
- tags: [Algorithmic Trading, HFT, Market Impact]
</details>

High-frequency trading (HFT) systems primarily aim to profit from:

- A) Long-term economic trends identified through fundamental analysis.
- B) Intraday securities mispricings by executing a large volume of orders rapidly.
- C) Thematic investment opportunities based on ESG factors.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: B**

**Explanation:**
High-frequency trading (HFT) is an application of algorithmic trading that identifies and takes advantage of intraday securities mispricings[cite: 4793]. It involves executing a high volume of orders at very high speeds.

- A describes traditional investment strategies, not HFT.
- C describes a specific investment approach not directly related to the mechanism of HFT.
</details>

---
## 🔴 Q20 – Quantitative Methods - Introduction to Big Data Techniques
<details>
<summary>Meta Data</summary>

- id: QUANT_L1_W6_Reading11_20
- level: 1
- reading: 11
- topic: Quantitative Methods
- module: 11.1
- los_text: 11.b Describe Big Data, artificial intelligence, and machine learning.
- question_type: mcq
- difficulty: hard
- tags: [Machine Learning, Black Box, Explainability]
</details>

A significant challenge associated with some advanced machine learning models, particularly deep learning, in financial applications is their:

- A) Inability to process non-numeric data.
- B) Tendency to systematically underfit complex data.
- C) "Black box" nature, where the reasoning behind their predictions may not be easily explainable.

<details>
<summary>✅ Answer & Explanation</summary>

**Correct Answer: C**

**Explanation:**
A further challenge with machine learning, especially with complex models like deep learning, is that their results can be a "black box," producing outcomes based on relationships that are not readily explainable or interpretable by humans[cite: 4777]. This lack of transparency can be a concern in financial applications where understanding the drivers of a decision is crucial for risk management and regulatory compliance.

- A is incorrect; many ML techniques, including those using NLP and text analytics, are designed to process non-numeric (unstructured) data.
- B is incorrect; while underfitting can be a problem if a model is too simple[cite: 4775], advanced models are often more prone to overfitting if not properly regularized or validated.
</details>