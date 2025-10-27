-----
### <span style="color: #1565C0;">Reading 9: Parametric and Non-Parametric Tests of Independence</span>

### <span style="color: #6A1B9A;">🎯 Introduction</span>

Welcome, future charterholder! Imagine you notice that every time ice cream sales go up, so do the number of shark attacks. 🍦🦈 Are these two related? Does one cause the other? A <b>correlation</b> exists, but it's likely a coincidence driven by a third factor: <b>summer</b>! This reading gives you the statistical tools to be a mythbuster. You'll learn how to test whether a relationship you see in your data is statistically real or just random noise. We'll cover how to test <b>correlations</b> for significance and how to use a <b>contingency table</b> to see if two categories, like "high growth" and "high dividend," are truly independent of each other. Let's start separating <b>fact</b> from <b>fiction</b>!

-----

### <span style="color: #1565C0;">Part 1: Are We Related? Testing for Correlation 🔗</span>

When we calculate a <b>correlation coefficient</b> from a sample of data, we get a number like +0.4 or -0.6. But that's just for our sample. The big question is: is the true correlation for the <b>entire population</b> actually zero? We need a formal hypothesis test to find out.

* <b>Null Hypothesis ($H_0$):</b> The true population correlation is zero ($H_0: \rho = 0$).
* <b>Alternative Hypothesis ($H_a$):</b> The true population correlation is not zero ($H_a: \rho \neq 0$).

#### <span style="color: #6A1B9A;">1.1 Parametric Test (The t-Test)</span>

This is the standard test for correlation, but it comes with a key assumption: both variables must be <b>normally distributed</b>.

The test statistic follows a <b>t-distribution</b> with <b>n-2 degrees of freedom</b>:

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
$$t = \frac{r\sqrt{n-2}}{\sqrt{1-r^2}}$$
</div>

Where:
* $r$ = sample correlation coefficient
* $n$ = sample size

<b>Intuition:</b> The t-statistic gets larger (and more significant) if the sample correlation (<b>r</b>) is far from zero, or if the sample size (<b>n</b>) is large. A large sample gives us more confidence that the correlation we're seeing isn't just a fluke.

#### <span style="color: #6A1B9A;">1.2 Nonparametric Test (Spearman Rank Correlation)</span>

What if your data isn't normally distributed, or what if you're dealing with ranks instead of actual values (e.g., ranking fund performance from 1st to 10th)? The <b>Spearman rank correlation test</b> comes to the rescue!

It works by converting the data for each variable into ranks and then testing if those ranks are correlated. The formula looks complex, but the idea is simple: it measures the consistency of the rankings between two variables. For large samples (n > 30), you can use a t-test to check if the Spearman correlation is statistically significant.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
💡 CFA Exam Tip ✍️:The key takeaway is knowing <b>when</b> to use each test. See normally distributed data? Use the standard <b>t-test for correlation</b>. See data that is ranked or does not meet the normality assumption? Think <b>Spearman rank correlation</b>. And remember, the degrees of freedom for the standard correlation t-test is <b>n-2</b>.
</div>
</div>

-----

### <span style="color: #1565C0;">Part 2: Sorting Data into Bins: The Chi-Square Test for Independence 📊</span>

Sometimes, our data isn't numerical but <b>categorical</b> (e.g., "Low," "Medium," "High"). The <b>Chi-square ($\chi^2$) test</b> helps us determine if there's a relationship between two categorical variables. We want to know: is being in one category independent of being in another?

The tool for this test is a <b>contingency table</b>, which shows the number of observations that fall into each combination of categories.

<b>The Logic:</b> The test works by comparing the actual frequencies we <b>observe</b> in our sample with the <b>expected</b> frequencies we would see if the two variables were perfectly independent.

* <b>Null Hypothesis ($H_0$):</b> The two variables are independent.
* <b>Alternative Hypothesis ($H_a$):</b> The two variables are dependent.

#### <span style="color: #6A1B9A;">2.1 Theory & Calculation 🧮</span>

Let's use an example of 324 firms categorized by Earnings Growth and Dividend Yield.

<b>Observed Frequencies Table</b>

| Earnings Growth | Dividend Yield (Low) | Dividend Yield (Medium) | Dividend Yield (High) | Row Total |
| :--- | :---: | :---: | :---: | :---: |
| Low | 28 | 53 | 42 | <b>123</b> |
| Medium | 42 | 32 | 30 | <b>104</b> |
| High | 49 | 25 | 14 | <b>87</b> |
| <b>Column Total</b>| <b>119</b> | <b>110</b> | <b>86</b> | <b>324</b> |

<b>Step 1: Calculate the Expected Frequency for each cell.</b>
If the variables were independent, the expected count for any cell would be:

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
$$E_{ij} = \frac{(\text{Total for Row i}) \times (\text{Total for Column j})}{\text{Total Sample Size}}$$
</div>

For example, the expected count for "Medium Growth" and "Medium Yield" is:

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
$E_{2,2} = \frac{104 \times 110}{324} = 35.3$
</div>

<b>Step 2: Calculate the Chi-Square Test Statistic.</b>
This statistic sums up the differences between observed and expected values for all cells.

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
$$\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$
</div>

A large value means the observed and expected counts are very different, suggesting the variables are <b>not</b> independent.

<b>Step 3: Compare to the Critical Value.</b>
The test statistic follows a <b>chi-square distribution</b> with <b>(r-1) x (c-1)</b> degrees of freedom, where 'r' is the number of rows and 'c' is the number of columns. If your calculated $\chi^2$ statistic is bigger than the critical value from the table, you <b>reject the null hypothesis</b> and conclude the variables are dependent.

#### <span style="color: #00838F;">2.2 Global & Local Context 🌍</span>

An e-commerce giant like Amazon (global) or Flipkart (India) could use a chi-square test to see if a customer's geographic region (North, South, East, West) is independent of the product category they purchase most (Electronics, Fashion, Groceries). If the test shows they are <b>dependent</b>, it means buying habits differ by region, and the company can create powerful, targeted marketing campaigns.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
💡 CFA Exam Tip ✍️:You probably won't have to calculate a full, large chi-square statistic on the exam. However, you absolutely must know the <b>logic</b>: it's a test of <b>Observed vs. Expected</b> frequencies for categorical data. A large test statistic implies the variables are <b>dependent</b>. Also, remember the formula for degrees of freedom: <b>(rows - 1) x (columns - 1)</b>.
</div>
</div>

-----

### <span style="color: #6A1B9A;">🧪 Formula Summary</span>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
<b>t-Test for Correlation Coefficient:</b>
$$t = \frac{r\sqrt{n-2}}{\sqrt{1-r^2}}$$
<small>(with df = n-2)</small>
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
<b>Spearman Rank Correlation Coefficient:</b>
$$r_s = 1 - \frac{6\sum d_i^2}{n(n^2 - 1)}$$
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
<b>Chi-Square Test Statistic:</b>
$$\chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$
<small>(with df = (r-1)(c-1))</small>
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
<b>Expected Frequency for a Contingency Table Cell:</b>
$$E_{ij} = \frac{(\text{Row i Total}) \times (\text{Column j Total})}{\text{Grand Total}}$$
</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* <b>Purpose of the Tests.</b> These tests determine if a relationship observed in a <b>sample</b> is statistically significant and likely exists in the <b>population</b>.
* <b>Testing Correlation.</b> Use the <b>t-test</b> for normally distributed data. Use the <b>Spearman rank test</b> for ranked (ordinal) data or when normality is not assumed. The null is always that the true correlation is zero.
* <b>Testing Categorical Data.</b> Use the <b>Chi-Square ($\chi^2$) test</b> with a <b>contingency table</b>. The null is that the variables are independent.
* <b>Degrees of Freedom are Key.</b>
  * For the correlation t-test: <b>df = n - 2</b>.
  * For the chi-square test: <b>df = (rows - 1) x (columns - 1)</b>.
* <b>Chi-Square Logic.</b> A large $\chi^2$ value means <b>Observed</b> is far from <b>Expected</b>, so you <b>REJECT</b> independence. The variables are likely related.

</div>
</div>