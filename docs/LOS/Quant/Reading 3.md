## Reading 3: Statistical Measures of Asset Returns

### 🎯 Introduction

Welcome, future charterholder! Think of analyzing an investment's returns like getting a detailed weather report. 🌦️ A simple "average temperature" (the **mean**) doesn't tell the whole story. You also need to know the range of possible temperatures (the **dispersion** or risk), whether extreme weather is likely (the **kurtosis**), and if the temperature is usually higher on sunny days versus rainy days (the **correlation**). This reading gives you the complete toolkit to be a financial meteorologist, allowing you to dissect and truly understand the nature of investment returns beyond just the average. Let's get started!

***

### Part 1: Finding the Center and Measuring the Spread 📍

First, we need to find the "typical" return (**central tendency**) and then measure how spread out the returns are around that center (**dispersion**).

#### **Measures of Central Tendency: The "Average" Return**

* **Arithmetic Mean**: This is the simple average you're used to. It's the sum of all returns divided by the number of observations. 
* **Median**: The middle value. If you line up all the returns from smallest to largest, the median is the one smack in the middle. The big advantage of the median is that it's **not affected by outliers** (extremely high or low values). 
* **Mode**: The value that occurs most frequently in the data. 

**Why does this matter?** Outliers can seriously distort the mean. If a fund had nine years of 5% returns and one year of a 100% return, the mean would be very high, but the median (5%) would give a much better sense of the fund's typical performance.

#### **Measures of Location: Slicing the Data 🍰**

**Quantiles** are points that divide a distribution into equal-sized, continuous parts.
* **Quartiles**: Divide the data into four quarters. The **interquartile range** (difference between the third and first quartiles) shows the spread of the middle 50% of the data. 
* **Quintiles**: Five equal parts.
* **Deciles**: Ten equal parts.
* **Percentiles**: One hundred equal parts.

#### **Measures of Dispersion: How Risky Is It? 🎢**

Dispersion measures the variability of returns. In finance, this is our primary measure of **risk**.

* **Range**: The simplest measure: Maximum Value - Minimum Value. 
* **Mean Absolute Deviation (MAD)**: The average of the absolute differences between each observation and the mean. It tells you, on average, how far a single return is from the mean. 
* **Variance and Standard Deviation**: These are the most important measures of risk.
    * **Variance ($s^2$)** is the average of the *squared* deviations from the mean.
    * **Standard Deviation ($s$)** is the square root of the variance. It's more intuitive because it's in the same units as the mean (e.g., if the mean return is 10%, the standard deviation might be 15%). 
    * For a **sample** of data, we divide by **n-1** to get an unbiased estimate of the population variance. 

#### **Relative Dispersion: The Coefficient of Variation (CV)**

What if you want to compare the risk of two very different assets, like a high-growth Indian tech stock and a stable US utility company? Their standard deviations aren't directly comparable because their expected returns are so different.

The **Coefficient of Variation (CV)** solves this. It measures the amount of risk (standard deviation) *per unit of return* (mean). A lower CV is better—it means you're getting more return for the risk you're taking. 

$$CV = \frac{Standard~Deviation~of~X}{Average~Value~of~X}$$

> [\!TIP]
> **CFA Exam Tip ✍️:** The **standard deviation** is the single most important measure of risk in the Level 1 curriculum. You must be able to calculate it and understand what it represents. The **CV** is the go-to tool for comparing risk between two investments on an "apples-to-apples" basis.

***

### Part 2: Beyond the Basics: Shape, Tails, and Teamwork 🐘

Real-world returns are rarely perfect bell curves. We need tools to describe their shape and how they interact.

#### **Skewness: Is the Distribution Lopsided?**

**Skewness** measures the asymmetry of a distribution.



* **Positively Skewed (Skewed Right)**: Characterized by a long right tail. This means there are frequent small losses and a few extreme gains. Think of venture capital or a lottery ticket. For a positively skewed distribution: **Mean > Median > Mode**. 
* **Negatively Skewed (Skewed Left)**: Characterized by a long left tail. This means frequent small gains and a few extreme losses. Think of selling options—you collect small premiums most of the time, but face the risk of a huge payout. For a negatively skewed distribution: **Mean < Median < Mode**. 

The mean is always pulled in the direction of the long tail (the outliers). 

#### **Kurtosis: How Fat Are the Tails?**

**Kurtosis** measures how peaked a distribution is and how thick its tails are compared to a normal distribution.

* **Normal Distribution (Mesokurtic)**: Has a kurtosis of 3. **Excess kurtosis** = 0.
* **Leptokurtic (Positive Excess Kurtosis)**: More peaked than normal, with "fatter tails." This means that extreme events (both positive and negative) are *more likely* than a normal distribution would predict. Financial market returns are almost always leptokurtic! 
* **Platykurtic (Negative Excess Kurtosis)**: Flatter than normal, with "thinner tails." Extreme events are less likely. 



#### **Correlation: How Do Assets Move Together? 🤝**

**Covariance** and **Correlation** measure how two variables move in relation to each other.

* **Covariance**: A positive value means the assets tend to move together; a negative value means they tend to move in opposite directions. The number itself is hard to interpret. 
* **Correlation**: This is a standardized version of covariance, ranging from -1.0 to +1.0. It's much easier to interpret. 
    * **+1.0**: Perfect positive correlation. They move in perfect lockstep.
    * **-1.0**: Perfect negative correlation. They are perfect opposites.
    * **0**: No *linear* relationship.

#### **Global & Local Context 🌍**

An analyst might find that the stock price of Maruti Suzuki (an Indian car company) has a strong **positive correlation** with the overall Nifty 50 index. When the market goes up, Maruti tends to go up too. However, the price of gold might have a **negative correlation** with the S&P 500. During times of market stress in the US, investors often flock to gold, pushing its price up.

#### **Important Caveats ⚠️**

* **Correlation ≠ Causation**: Just because two things move together doesn't mean one causes the other. 
* **Spurious Correlation**: You can find high correlations between completely unrelated things by chance or because they are both related to a third, unseen factor. 

> [\!TIP]
> **CFA Exam Tip ✍️:** The exam will test your understanding of what skewness and kurtosis mean for risk. **Negative skew** and **positive excess kurtosis (fat tails)** are a dangerous combination for investors, indicating a higher-than-normal probability of large losses. This is a key concept in risk management.

***

### 🧪 Formula Summary

* **Sample Mean**: $$\bar{X} = \frac{\sum_{i=1}^{n} X_i}{n}$$
* **Sample Variance**: $$s^2 = \frac{\sum_{i=1}^{n} (X_i - \bar{X})^2}{n-1}$$
* **Sample Standard Deviation**: $$s = \sqrt{\frac{\sum_{i=1}^{n} (X_i - \bar{X})^2}{n-1}}$$
* **Coefficient of Variation (CV)**: $$CV = \frac{s}{\bar{X}}$$
* **Covariance**: $$s_{XY} = \frac{\sum_{i=1}^{n} \{[X_i - \bar{X}][Y_i - \bar{Y}]\}}{n-1}$$
* **Correlation**: $$\rho_{XY} = \frac{s_{XY}}{s_X s_Y}$$

***

> [\!IMPORTANT]
>
> ### 🎯 Quick Exam-Day Pointers
>
> * **Standard Deviation is Risk!** When you see standard deviation or variance, think "risk" or "volatility."
> * **Use CV for Comparisons.** To compare the risk of two different investments (e.g., a stock vs. a bond), always use the **Coefficient of Variation (CV)** for a true risk-per-unit-of-return measure.
> * **Skewness = Asymmetry.** Remember `Mean > Median` for positive skew (right tail) and `Mean < Median` for negative skew (left tail). The mean gets pulled by the outliers.
> * **Kurtosis = Fat Tails.** Financial returns are **leptokurtic** (positive excess kurtosis), meaning crashes and booms happen more often than a perfect normal distribution would suggest. This is a critical risk management concept.
> * **Correlation is about Linear Relationships.** It measures how assets move together, but it does NOT tell you that one causes the other.