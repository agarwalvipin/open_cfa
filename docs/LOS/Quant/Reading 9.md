Of course! Here is a detailed summary for Reading 9.

## Reading 9: Parametric and Non-Parametric Tests of Independence

### 🎯 Introduction

Welcome, future charterholder! Imagine you notice that every time ice cream sales go up, so do the number of shark attacks. 🍦🦈 Are these two related? Does one cause the other? A **correlation** exists, but it's likely a coincidence driven by a third factor: summer! This reading gives you the statistical tools to be a mythbuster. You'll learn how to test whether a relationship you see in your data is statistically real or just random noise. We'll cover how to test correlations for significance and how to use a **contingency table** to see if two categories, like "high growth" and "high dividend," are truly independent of each other. Let's start separating fact from fiction!

***

### Part 1: Are We Related? Testing for Correlation 🔗

When we calculate a **correlation coefficient** from a sample of data, we get a number like +0.4 or -0.6. But that's just for our sample. The big question is: is the true correlation for the *entire population* actually zero? We need a formal hypothesis test to find out.

The setup is always:
* **Null Hypothesis ($H_0$)**: The true population correlation is zero ($H_0: \rho = 0$). 
* **Alternative Hypothesis ($H_a$)**: The true population correlation is not zero ($H_a: \rho \neq 0$).

#### **Parametric Test (The t-Test)**

This is the standard test for correlation, but it comes with a key assumption: both variables must be **normally distributed**. 

The test statistic follows a **t-distribution** with **n-2 degrees of freedom**: 
$$t = \frac{r\sqrt{n-2}}{\sqrt{1-r^2}}$$
Where:
* $r$ = sample correlation coefficient
* $n$ = sample size

**Intuition**: The t-statistic gets larger (and more significant) if the sample correlation (`r`) is far from zero, or if the sample size (`n`) is large. A large sample gives us more confidence that the correlation we're seeing isn't just a fluke. 

#### **Nonparametric Test (Spearman Rank Correlation)**

What if your data isn't normally distributed, or what if you're dealing with ranks instead of actual values (e.g., ranking fund performance from 1st to 10th)? The **Spearman rank correlation test** comes to the rescue! 

It works by converting the data for each variable into ranks and then testing if those ranks are correlated.  The formula looks complex, but the idea is simple: it measures the consistency of the rankings between two variables. For large samples (n > 30), you can use a t-test to check if the Spearman correlation is statistically significant. 

> [\!TIP]
> **CFA Exam Tip ✍️:** The key takeaway is knowing *when* to use each test. See normally distributed data? Use the standard **t-test for correlation**. See data that is ranked or does not meet the normality assumption? Think **Spearman rank correlation**. And remember, the degrees of freedom for the standard correlation t-test is **n-2**.

***

### Part 2: Sorting Data into Bins: The Chi-Square Test for Independence 📊

Sometimes, our data isn't numerical but categorical (e.g., "Low," "Medium," "High"). The **Chi-square ($\chi^2$) test** helps us determine if there's a relationship between two categorical variables. We want to know: is being in one category independent of being in another?

The tool for this test is a **contingency table**, which shows the number of observations that fall into each combination of categories. 

**The Logic**: The test works by comparing the actual frequencies we *observe* in our sample with the *expected* frequencies we would see if the two variables were perfectly independent. 

* **Null Hypothesis ($H_0$)**: The two variables are independent.
* **Alternative Hypothesis ($H_a$)**: The two variables are dependent.

#### **Theory & Calculation 🧮**

Let's use an example of 324 firms categorized by Earnings Growth and Dividend Yield. 

**Observed Frequencies Table** 

| Earnings Growth | Dividend Yield (Low) | Dividend Yield (Medium) | Dividend Yield (High) | Row Total |
| :--- | :---: | :---: | :---: | :---: |
| Low | 28 | 53 | 42 | **123** |
| Medium | 42 | 32 | 30 | **104** |
| High | 49 | 25 | 14 | **87** |
| **Column Total**| **119** | **110** | **86** | **324** |

**Step 1: Calculate the Expected Frequency for each cell.**
If the variables were independent, the expected count for any cell would be:
$$E_{ij} = \frac{(\text{Total for Row i}) \times (\text{Total for Column j})}{\text{Total Sample Size}}$$
For example, the expected count for "Medium Growth" and "Medium Yield" is:
$E_{2,2} = \frac{104 \times 110}{324} = 35.3$ 

**Step 2: Calculate the Chi-Square Test Statistic.**
This statistic sums up the differences between observed and expected values for all cells.
$$\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$
A large value means the observed and expected counts are very different, suggesting the variables are *not* independent.

**Step 3: Compare to the Critical Value.**
The test statistic follows a **chi-square distribution** with **(r-1) x (c-1)** degrees of freedom, where 'r' is the number of rows and 'c' is the number of columns.  If your calculated $\chi^2$ statistic is bigger than the critical value from the table, you **reject the null hypothesis** and conclude the variables are dependent.

#### **Global & Local Context 🌍**

An e-commerce giant like Amazon (global) or Flipkart (India) could use a chi-square test to see if a customer's geographic region (North, South, East, West) is independent of the product category they purchase most (Electronics, Fashion, Groceries). If the test shows they are *dependent*, it means buying habits differ by region, and the company can create powerful, targeted marketing campaigns.

> [\!TIP]
> **CFA Exam Tip ✍️:** You probably won't have to calculate a full, large chi-square statistic on the exam. However, you absolutely must know the **logic**: it's a test of **Observed vs. Expected** frequencies for categorical data. A large test statistic implies the variables are **dependent**. Also, remember the formula for degrees of freedom: **(rows - 1) x (columns - 1)**.

***

### 🧪 Formula Summary

* **t-Test for Correlation Coefficient**: $$t = \frac{r\sqrt{n-2}}{\sqrt{1-r^2}}$$ (with df = n-2)
* **Spearman Rank Correlation Coefficient**: $$r_s = 1 - \frac{6\sum d_i^2}{n(n^2 - 1)}$$
* **Chi-Square Test Statistic**: $$\chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$ (with df = (r-1)(c-1))
* **Expected Frequency for a Contingency Table Cell**: $$E_{ij} = \frac{(\text{Row i Total}) \times (\text{Column j Total})}{\text{Grand Total}}$$

***

> [\!IMPORTANT]
>
> ### 🎯 Quick Exam-Day Pointers
>
> * **Purpose of the Tests:** These tests determine if a relationship observed in a *sample* is statistically significant and likely exists in the *population*.
> * **Testing Correlation:** Use the **t-test** for normally distributed data. Use the **Spearman rank test** for ranked (ordinal) data or when normality is not assumed. The null is always that the true correlation is zero.
> * **Testing Categorical Data:** Use the **Chi-Square ($\chi^2$) test** with a **contingency table**. The null is that the variables are independent.
> * **Degrees of Freedom are Key:**
>     * For the correlation t-test: **df = n - 2**.
>     * For the chi-square test: **df = (rows - 1) x (columns - 1)**.
> * **Chi-Square Logic:** A large $\chi^2$ value means `Observed` is far from `Expected`, so you REJECT independence. The variables are likely related.