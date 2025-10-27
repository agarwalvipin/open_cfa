-----
### <span style="color: #1565C0;">Reading 7: Estimation and Inference</span>

### 🎯 Introduction

Welcome, future charterholder! Imagine you're a food critic trying to rate a massive restaurant chain. 👨‍🍳 You can't possibly eat every dish at every location, right? So, you strategically select a **sample** of dishes to taste. How you choose that sample is crucial. Did you pick dishes randomly? Did you make sure to try appetizers, main courses, and desserts in the right proportions? **Estimation and Inference** is the science of tasting that sample and making an educated guess (an **inference**) about the quality of the entire chain. This reading teaches you how to pick a good sample and the statistical magic that allows you to be confident in your final review!

-----

### <span style="color: #1565C0;">Part 1: How Do We Pick a Good Sample?</span>

When we analyze a population (like all the stocks in an index), we almost always use a sample. The goal is to get a sample that represents the whole population, and the method we use to pick it determines how reliable our conclusions will be.

There are two main families of sampling:
* **Probability Sampling**: Each member of the population has a known chance of being selected. This is the gold standard.
* **Non-probability Sampling**: The selection is not random and is based on convenience or judgment. This is easier but riskier.

#### <span style="color: #6A1B9A;">1.1 Probability Sampling Methods (The Good Stuff) ✅</span>

#### <span style="color: #6A1B9A;">1.2 Theory 🧠</span>

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

#### <span style="color: #00838F;">1.3 Global & Local Context 🌍</span>

A fund manager wants to create a portfolio of 100 bonds that tracks a global bond index of 1,000 bonds. Using **simple random sampling** might accidentally give her too many long-term bonds. Instead, she would use **stratified random sampling**. She would group the index bonds by maturity, credit rating, and country. Then, she would randomly select bonds from each of these "strata" to ensure her 100-bond portfolio perfectly mirrors the risk characteristics of the entire 1,000-bond index.

#### <span style="color: #6A1B9A;">1.4 Non-Probability Sampling Methods (Use with Caution) ⚠️</span>

* **Convenience Sampling**: Selecting data that is easy to get. For example, surveying only the companies in your city. It's fast and cheap but often highly biased.
* **Judgmental Sampling**: The researcher uses their own judgment to select a sample they believe is representative. If the researcher is a true expert, this can work well. If not, it can be very biased.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
**💡 CFA Exam Tip ✍️:** The exam loves to test the difference between <b>stratified</b> and <b>cluster</b> sampling. In <b>stratified</b>, you take a sample from <i>every</i> group. In <b>cluster</b>, you take a sample of the <i>groups</i> themselves. Stratified sampling generally has a lower sampling error because it's more representative.
</div>
</div>

-----

### <span style="color: #1565C0;">Part 2: The Magic of Large Numbers: The Central Limit Theorem ✨</span>

The <b>Central Limit Theorem (CLT)</b> is one of the most powerful and magical ideas in statistics. It says that if you take a large enough number of random samples from <i>any</i> population (even a weird, non-symmetrical one) and you plot the <b>means</b> of those samples, the distribution of those means will be approximately normal (a perfect bell curve).

For the CLT to apply, the sample size (<b>n</b>) should be <b>30 or more</b>.

Here are the three key properties of the CLT:
1.  The sampling distribution of the sample means will be approximately normal.
2.  The mean of this distribution of sample means will be equal to the true population mean, <b>$\mu$</b>.
3.  The variance of this distribution will be the population variance divided by the sample size, <b>$\frac{\sigma^2}{n}$</b>.

#### <span style="color: #6A1B9A;">2.1 The Standard Error of the Sample Mean</span>

This leads to a crucial concept: the <b>standard error of the sample mean</b>. This is NOT the standard deviation of your data; it's the standard deviation of all the <i>sample means</i>. It tells you how precise your estimate of the population mean is.

* If population standard deviation (<b>$\sigma$</b>) is known:
  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
  $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$
  </div>
* If population standard deviation is unknown (which is almost always the case), we use the sample standard deviation (<b>$s$</b>):
  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
  $$s_{\bar{x}} = \frac{s}{\sqrt{n}}$$
  </div>

Notice the <b>$\sqrt{n}$</b> in the denominator. This is huge! It means that as your <b>sample size (n) increases, the standard error decreases</b>. A larger sample size gives you a more precise estimate of the true population mean.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
**💡 CFA Exam Tip ✍️:** Do not confuse the <b>standard deviation of the sample (s)</b> with the <b>standard error of the sample mean ($s_{\bar{x}}$)</b>. The standard deviation measures the dispersion of the data points in your sample. The standard error measures how much the sample <i>mean</i> is likely to vary from the true population mean.
</div>
</div>

-----

### <span style="color: #1565C0;">Part 3: Pulling Yourself Up by Your Bootstraps: Resampling Methods 🥾</span>

What if your sample size is small (less than 30) or you have doubts about the data's distribution? <b>Resampling</b> methods can help by creating many new samples from your original one to estimate the sampling distribution.

* <b>Jackknife</b>: You create multiple samples by taking your original sample and leaving out one observation at a time. It's a handy, computationally simple tool that can help reduce bias in your estimates.
* <b>Bootstrap</b>: This is a more modern and computationally intensive method. You create new samples by drawing observations from your original sample <b>with replacement</b>. This means after you pick an observation, you put it back in the "hat," so it could be picked again. By doing this thousands of times, you can build a very accurate picture of the sampling distribution for almost any statistic (like the mean, median, etc.).

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
**💡 CFA Exam Tip ✍️:** The key difference to remember is the method. <b>Jackknife</b> = "leave one out." <b>Bootstrap</b> = "sample with replacement." Bootstrap is generally considered more powerful and versatile.
</div>
</div>

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
<b>Standard Error of the Sample Mean (Population $\sigma$ known):</b>
$$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
<b>Standard Error of the Sample Mean (Population $\sigma$ unknown):</b>
$$s_{\bar{x}} = \frac{s}{\sqrt{n}}$$
</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">
* <b>CLT is your best friend.</b> If sample size <b>n ≥ 30</b>, you can assume the distribution of sample <i>means</i> is normal. This unlocks many statistical tests.
* <b>Bigger is Better.</b> Increasing your sample size <b>n</b> makes your estimates more precise by <b>decreasing</b> the standard error of the sample mean.
* <b>Stratified vs. Cluster.</b> Know the difference! <b>Stratified</b> samples from <i>every</i> group; <b>Cluster</b> randomly selects <i>the groups</i>. Stratified is generally more precise.
* <b>Don't Confuse Standard Deviation and Standard Error.</b> Standard deviation measures the volatility of the data points. Standard error measures the precision of your <i>sample mean</i>.
* <b>Resampling Methods.</b> Remember the key phrases: <b>Jackknife</b> is "leave one out." <b>Bootstrap</b> is "sample with replacement."
</div>
</div>