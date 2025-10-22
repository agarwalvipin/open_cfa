Of course! Here is a detailed summary for Reading 7.

## Reading 7: Estimation and Inference

### 🎯 Introduction

Welcome, future charterholder! Imagine you're a food critic trying to rate a massive restaurant chain. 👨‍🍳 You can't possibly eat every dish at every location, right? So, you strategically select a **sample** of dishes to taste. How you choose that sample is crucial. Did you pick dishes randomly? Did you make sure to try appetizers, main courses, and desserts in the right proportions? **Estimation and Inference** is the science of tasting that sample and making an educated guess (an **inference**) about the quality of the entire chain. This reading teaches you how to pick a good sample and the statistical magic that allows you to be confident in your final review!

***

### Part 1: How Do We Pick a Good Sample?  M

When we analyze a population (like all the stocks in an index), we almost always use a sample. The goal is to get a sample that represents the whole population, and the method we use to pick it determines how reliable our conclusions will be.

There are two main families of sampling:
* **Probability Sampling**: Each member of the population has a known chance of being selected. This is the gold standard.
* **Non-probability Sampling**: The selection is not random and is based on convenience or judgment. This is easier but riskier.

#### **Probability Sampling Methods (The Good Stuff) ✅**

#### **Theory 🧠**

* **Simple Random Sampling**: Every member has an equal chance of being picked. It's like drawing names out of a hat.
* **Systematic Sampling**: You select every nth member from a list (e.g., picking every 50th company from the S&P 500 list). It's simple and can be close to random.
* **Stratified Random Sampling**: This is a more advanced, high-quality method.
    1.  First, divide the population into subgroups (**strata**) based on important characteristics (e.g., industry sector, company size).
    2.  Then, draw a simple random sample from *each* subgroup in proportion to its size.
    This guarantees your sample will have the same mix of characteristics as the whole population.
* **Cluster Sampling**: The population is divided into subgroups (**clusters**), often by geography.
    1.  You randomly select a few of the clusters.
    2.  You then sample *all* or a random selection of members from within those chosen clusters.
    This is cheaper and faster than stratified sampling but can have more **sampling error** if the clusters aren't truly representative of the whole population.

#### **Global & Local Context 🌍**

A fund manager wants to create a portfolio of 100 bonds that tracks a global bond index of 1,000 bonds. Using **simple random sampling** might accidentally give her too many long-term bonds. Instead, she would use **stratified random sampling**. She would group the index bonds by maturity, credit rating, and country. Then, she would randomly select bonds from each of these "strata" to ensure her 100-bond portfolio perfectly mirrors the risk characteristics of the entire 1,000-bond index.

#### **Non-Probability Sampling Methods (Use with Caution) ⚠️**

* **Convenience Sampling**: Selecting data that is easy to get. For example, surveying only the companies in your city. It's fast and cheap but often highly biased.
* **Judgmental Sampling**: The researcher uses their own judgment to select a sample they believe is representative. If the researcher is a true expert, this can work well. If not, it can be very biased.

> [\!TIP]
> **CFA Exam Tip ✍️:** The exam loves to test the difference between **stratified** and **cluster** sampling. In **stratified**, you take a sample from *every* group. In **cluster**, you take a sample of the *groups* themselves. Stratified sampling generally has a lower sampling error because it's more representative.

***

### Part 2: The Magic of Large Numbers: The Central Limit Theorem ✨

The **Central Limit Theorem (CLT)** is one of the most powerful and magical ideas in statistics. It says that if you take a large enough number of random samples from *any* population (even a weird, non-symmetrical one) and you plot the *means* of those samples, the distribution of those means will be approximately normal (a perfect bell curve).

For the CLT to apply, the sample size (`n`) should be **30 or more**.

Here are the three key properties of the CLT:
1.  The sampling distribution of the sample means will be approximately normal.
2.  The mean of this distribution of sample means will be equal to the true population mean, $\mu$.
3.  The variance of this distribution will be the population variance divided by the sample size, $\frac{\sigma^2}{n}$.

#### **The Standard Error of the Sample Mean**

This leads to a crucial concept: the **standard error of the sample mean**. This is NOT the standard deviation of your data; it's the standard deviation of all the *sample means*. It tells you how precise your estimate of the population mean is.

* If population standard deviation ($\sigma$) is known: $$\sigma\_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$
* If population standard deviation is unknown (which is almost always the case), we use the sample standard deviation ($s$): $$s\_{\bar{x}} = \frac{s}{\sqrt{n}}$$

Notice the $\sqrt{n}$ in the denominator. This is huge! It means that as your **sample size (n) increases, the standard error decreases**. A larger sample size gives you a more precise estimate of the true population mean.

> [\!TIP]
> **CFA Exam Tip ✍️:** Do not confuse the **standard deviation of the sample (s)** with the **standard error of the sample mean ($s_{\bar{x}}$)**. The standard deviation measures the dispersion of the data points in your sample. The standard error measures how much the sample *mean* is likely to vary from the true population mean.

***

### Part 3: Pulling Yourself Up by Your Bootstraps: Resampling Methods 🥾

What if your sample size is small (less than 30) or you have doubts about the data's distribution? **Resampling** methods can help by creating many new samples from your original one to estimate the sampling distribution.

* **Jackknife**: You create multiple samples by taking your original sample and leaving out one observation at a time. It's a handy, computationally simple tool that can help reduce bias in your estimates.
* **Bootstrap**: This is a more modern and computationally intensive method. You create new samples by drawing observations from your original sample **with replacement**. This means after you pick an observation, you put it back in the "hat," so it could be picked again. By doing this thousands of times, you can build a very accurate picture of the sampling distribution for almost any statistic (like the mean, median, etc.).

> [\!TIP]
> **CFA Exam Tip ✍️:** The key difference to remember is the method. **Jackknife** = "leave one out." **Bootstrap** = "sample with replacement." Bootstrap is generally considered more powerful and versatile.

***

### 🧪 Formula Summary

* **Standard Error of the Sample Mean (Population $\sigma$ known)**: $$\sigma\_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$
* **Standard Error of the Sample Mean (Population $\sigma$ unknown)**: $$s\_{\bar{x}} = \frac{s}{\sqrt{n}}$$

***

> [\!IMPORTANT]
>
> ### 🎯 Quick Exam-Day Pointers
>
> * **CLT is your best friend.** If sample size `n ≥ 30`, you can assume the distribution of sample *means* is normal. This unlocks many statistical tests.
> * **Bigger is Better.** Increasing your sample size `n` makes your estimates more precise by *decreasing* the standard error of the sample mean.
> * **Stratified vs. Cluster.** Know the difference! Stratified samples from *every* group; Cluster randomly selects *the groups*. Stratified is generally more precise.
> * **Don't Confuse Standard Deviation and Standard Error.** Standard deviation measures the volatility of the data points. Standard error measures the precision of your *sample mean*.
> * **Resampling Methods.** Remember the key phrases: **Jackknife** is "leave one out." **Bootstrap** is "sample with replacement."