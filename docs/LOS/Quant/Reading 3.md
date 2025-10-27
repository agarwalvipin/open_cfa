## <span style="color: #1565C0;">Reading 3: Statistical Measures of Asset Returns</span>

### <span style="color: #1565C0;">🎯 Introduction</span>

Welcome, future charterholder! Think of analyzing an investment's returns like getting a detailed weather report. 🌦️ A simple "<b>average temperature</b>" (the <b>mean</b>) doesn't tell the whole story. You also need to know the range of possible temperatures (the <b>dispersion</b> or risk), whether extreme weather is likely (the <b>kurtosis</b>), and if the temperature is usually higher on sunny days versus rainy days (the <b>correlation</b>). This reading gives you the complete toolkit to be a financial meteorologist, allowing you to dissect and truly understand the nature of investment returns beyond just the average. Let's get started!

-----

### <span style="color: #1565C0;">Part 1: Finding the Center and Measuring the Spread 📍</span>

First, we need to find the "typical" return (<b>central tendency</b>) and then measure how spread out the returns are around that center (<b>dispersion</b>).

#### <span style="color: #6A1B9A;">1.1 Measures of Central Tendency: The "Average" Return</span>

* <b>Arithmetic Mean</b>: This is the simple average you're used to. It's the sum of all returns divided by the number of observations. 
* <b>Median</b>: The middle value. If you line up all the returns from smallest to largest, the median is the one smack in the middle. The big advantage of the median is that it's <b>not affected by outliers</b> (extremely high or low values). 
* <b>Mode</b>: The value that occurs most frequently in the data. 

<b>Why does this matter?</b> Outliers can seriously distort the mean. If a fund had nine years of 5% returns and one year of a 100% return, the mean would be very high, but the median (5%) would give a much better sense of the fund's typical performance.

#### <span style="color: #6A1B9A;">1.2 Measures of Location: Slicing the Data 🍰</span>

<b>Quantiles</b> are points that divide a distribution into equal-sized, continuous parts.
* <b>Quartiles</b>: Divide the data into four quarters. The <b>interquartile range</b> (difference between the third and first quartiles) shows the spread of the middle 50% of the data. 
* <b>Quintiles</b>: Five equal parts.
* <b>Deciles</b>: Ten equal parts.
* <b>Percentiles</b>: One hundred equal parts.

#### <span style="color: #6A1B9A;">1.3 Measures of Dispersion: How Risky Is It? 🎢</span>

Dispersion measures the variability of returns. In finance, this is our primary measure of <b>risk</b>.

* <b>Range</b>: The simplest measure: Maximum Value - Minimum Value. 
* <b>Mean Absolute Deviation (MAD)</b>: The average of the absolute differences between each observation and the mean. It tells you, on average, how far a single return is from the mean. 
* <b>Variance and Standard Deviation</b>: These are the most important measures of risk.
  * <b>Variance</b> ($s^2$) is the average of the <i>squared</i> deviations from the mean.
  * <b>Standard Deviation</b> ($s$) is the square root of the variance. It's more intuitive because it's in the same units as the mean (e.g., if the mean return is 10%, the standard deviation might be 15%). 
  * For a <b>sample</b> of data, we divide by <b>n-1</b> to get an unbiased estimate of the population variance. 

#### <span style="color: #6A1B9A;">1.4 Relative Dispersion: The Coefficient of Variation (CV)</span>

What if you want to compare the risk of two very different assets, like a high-growth Indian tech stock and a stable US utility company? Their standard deviations aren't directly comparable because their expected returns are so different.

The <b>Coefficient of Variation (CV)</b> solves this. It measures the amount of risk (standard deviation) <i>per unit of return</i> (mean). A lower CV is better—it means you're getting more return for the risk you're taking. 

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$CV = \frac{\text{Standard Deviation of X}}{\text{Average Value of X}}$$

</div>

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
💡 CFA Exam Tip ✍️: The <b>standard deviation</b> is the single most important measure of risk in the Level 1 curriculum. You must be able to calculate it and understand what it represents. The <b>CV</b> is the go-to tool for comparing risk between two investments on an "apples-to-apples" basis.
</div>
</div>

-----

### <span style="color: #1565C0;">Part 2: Beyond the Basics: Shape, Tails, and Teamwork 🐘</span>

Real-world returns are rarely perfect bell curves. We need tools to describe their shape and how they interact.

#### <span style="color: #6A1B9A;">2.1 Skewness: Is the Distribution Lopsided?</span>

<b>Skewness</b> measures the asymmetry of a distribution.

* <b>Positively Skewed (Skewed Right)</b>: Characterized by a long right tail. This means there are frequent small losses and a few extreme gains. Think of venture capital or a lottery ticket. For a positively skewed distribution: <b>Mean > Median > Mode</b>. 
* <b>Negatively Skewed (Skewed Left)</b>: Characterized by a long left tail. This means frequent small gains and a few extreme losses. Think of selling options—you collect small premiums most of the time, but face the risk of a huge payout. For a negatively skewed distribution: <b>Mean < Median < Mode</b>. 

The mean is always pulled in the direction of the long tail (the outliers). 

#### <span style="color: #6A1B9A;">2.2 Kurtosis: How Fat Are the Tails?</span>

<b>Kurtosis</b> measures how peaked a distribution is and how thick its tails are compared to a normal distribution.

* <b>Normal Distribution (Mesokurtic)</b>: Has a kurtosis of 3. <b>Excess kurtosis</b> = 0.
* <b>Leptokurtic (Positive Excess Kurtosis)</b>: More peaked than normal, with "fatter tails." This means that extreme events (both positive and negative) are <i>more likely</i> than a normal distribution would predict. Financial market returns are almost always leptokurtic! 
* <b>Platykurtic (Negative Excess Kurtosis)</b>: Flatter than normal, with "thinner tails." Extreme events are less likely. 

#### <span style="color: #6A1B9A;">2.3 Correlation: How Do Assets Move Together? 🤝</span>

<b>Covariance</b> and <b>Correlation</b> measure how two variables move in relation to each other.

* <b>Covariance</b>: A positive value means the assets tend to move together; a negative value means they tend to move in opposite directions. The number itself is hard to interpret. 
* <b>Correlation</b>: This is a standardized version of covariance, ranging from -1.0 to +1.0. It's much easier to interpret. 
  * <b>+1.0</b>: Perfect positive correlation. They move in perfect lockstep.
  * <b>-1.0</b>: Perfect negative correlation. They are perfect opposites.
  * <b>0</b>: No <i>linear</i> relationship.

#### <span style="color: #00838F;">2.4 Global & Local Context 🌍</span>

An analyst might find that the stock price of Maruti Suzuki (an Indian car company) has a strong <b>positive correlation</b> with the overall Nifty 50 index. When the market goes up, Maruti tends to go up too. However, the price of gold might have a <b>negative correlation</b> with the S&P 500. During times of market stress in the US, investors often flock to gold, pushing its price up.

#### <span style="color: #E65100;">2.5 Important Caveats ⚠️</span>

* <b>Correlation ≠ Causation</b>: Just because two things move together doesn't mean one causes the other. 
* <b>Spurious Correlation</b>: You can find high correlations between completely unrelated things by chance or because they are both related to a third, unseen factor. 

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
💡 CFA Exam Tip ✍️: The exam will test your understanding of what skewness and kurtosis mean for risk. <b>Negative skew</b> and <b>positive excess kurtosis (fat tails)</b> are a dangerous combination for investors, indicating a higher-than-normal probability of large losses. This is a key concept in risk management.
</div>
</div>

-----

### <span style="color: #1565C0;">🧪 Formula Summary</span>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

<b>Sample Mean:</b> 

$$\bar{X} = \frac{\sum\_{i=1}^{n} X\_i}{n}$$

</div>
<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

<b>Mean Absolute Deviation (MAD):</b>

$$MAD = \frac{\sum_{i=1}^{n} |X_i - \bar{X}|}{n}$$

</div>
<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

<b>Sample Variance:</b>

$$s^2 = \frac{\sum\_{i=1}^{n} (X\_i - \bar{X})^2}{n-1}$$

</div>
<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

<b>Sample Standard Deviation:</b> 

$$s = \sqrt{\frac{\sum\_{i=1}^{n} (X\_i - \bar{X})^2}{n-1}}$$

</div>
<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

<b>Coefficient of Variation (CV):</b> 

$$CV = \frac{s}{\bar{X}}$$

</div>
<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

<b>Covariance:</b> 

$$s\_{XY} = \frac{\sum\_{i=1}^{n} \{[X\_i - \bar{X}][Y\_i - \bar{Y}]\}}{n-1}$$

</div>
<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

<b>Correlation:</b> 

$$\rho\_{XY} = \frac{s\_{XY}}{s\_X s\_Y}$$

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* <b>Standard Deviation is Risk!</b> When you see standard deviation or variance, think "<b>risk</b>" or "<b>volatility</b>."
* <b>Use CV for Comparisons.</b> To compare the risk of two different investments (e.g., a stock vs. a bond), always use the <b>Coefficient of Variation (CV)</b> for a true risk-per-unit-of-return measure.
* <b>Skewness = Asymmetry.</b> Remember <code>Mean > Median</code> for positive skew (right tail) and <code>Mean < Median</code> for negative skew (left tail). The mean gets pulled by the outliers.
* <b>Kurtosis = Fat Tails.</b> Financial returns are <b>leptokurtic</b> (positive excess kurtosis), meaning crashes and booms happen more often than a perfect normal distribution would suggest. This is a critical risk management concept.
* <b>Correlation is about Linear Relationships.</b> It measures how assets move together, but it does NOT tell you that one causes the other.

</div>
</div>