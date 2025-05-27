## 🎯 CFA Level 1 Quant Exam Tips Sheet 🎯

Here’s a breakdown of tips for each Quantitative Methods reading, designed to help you calculate quickly and accurately, separating the pros from the beginners.

---

### Reading 1: Rates and Returns

* **Pro Tip 🚀:** Understand the **hierarchy of means**: For values that are not all equal, Harmonic Mean < Geometric Mean < Arithmetic Mean[cite: 174]. Knowing this can help you quickly sense-check answers or eliminate options without full calculation.
* **Calculator Efficiency 🧮:**
    * **Geometric Mean**: Instead of manually multiplying and then finding the nth root, use your calculator's `y^x` (or `x^y`) and `1/x` functions for powers and roots[cite: 156]. For example, for $\sqrt[3]{1.21903}$, enter `1.21903 [y^x] 3 [1/x] [=]` on a TI BA II Plus[cite: 156].
    * **Money-Weighted Return (MWR)**: This is an IRR calculation[cite: 192]. Master the CF (Cash Flow) function on your calculator[cite: 195, 211].
        * **TI BA II Plus Keystrokes for MWR example**[cite: 211]:
            * `[CF] [2nd] [CLR WORK]` (Clear prior entries)
            * `100 [ENTER]` ($CF_0$) [cite: 210, 211]
            * `[↓] 118 [ENTER]` ($C01$) (Net flow for period 1: +120 deposit - 2 dividend = +118) [cite: 210, 211]
            * `[↓] [↓] -264 [ENTER]` ($C02$) (Net flow for period 2: -260 sale - 4 dividend = -264) [cite: 210, 211]
            * `[IRR] [CPT]` → Result: 13.86% [cite: 212]
        * **Key Insight**: Remember to treat the initial investment as an inflow to the account (positive if you're looking from the account's perspective) or an outflow from the investor's pocket (negative)[cite: 199, 213]. Subsequent deposits are inflows (positive), and withdrawals/final sale are outflows (negative) if initial investment was positive (or vice-versa)[cite: 199, 200, 213]. Consistency in signs for inflows vs. outflows is crucial[cite: 216].
* **Time-Weighted Return (TWR)**:
    * **Pro Tip 🚀**: TWR is unaffected by the timing of cash flows [cite: 232] and is preferred for manager performance evaluation[cite: 233]. MWR *is* affected by cash flow timing[cite: 235]. If significant cash is added just before a period of good performance, MWR > TWR[cite: 237]. If added before poor performance, MWR < TWR[cite: 236].
    * **Calculation**: Break the period into sub-periods based on cash flows[cite: 220]. Calculate HPR for each sub-period[cite: 221]. Link them geometrically: $(1+TWR)^N = (1+HPR_1)(1+HPR_2)...(1+HPR_n)$[cite: 222].
* **Annualizing Returns**:
    * **Formula**: Annualized Return = $(1 + HPR)^{365/days} - 1$ [cite: 245] (or relevant number of periods in a year if not daily).
    * **Pro Tip 🚀**: For periods less than a year, the annualized return will be higher than the HPR. For periods longer than a year, it will be lower.
* **Continuously Compounded Returns**:
    * **Formula**: $R_{CC} = \ln(1+HPR) = \ln(\frac{\text{Ending Value}}{\text{Beginning Value}})$[cite: 255].
    * **Calculator Efficiency 🧮**: Use the `LN` button[cite: 255]. For example, $P_0 = \$100, P_1 = \$120$. $R_{CC} = \ln(120/100) = \ln(1.2) = 18.232\%$[cite: 259].
    * **Key Insight**: Continuously compounded returns are additive over time[cite: 259].

---

### Reading 2: The Time Value of Money in Finance

* **Calculator Setup ⚙️ (TI BA II Plus)**:
    * **P/Y = 1**: Crucial for CFA exam calculations[cite: 329]. SchweserNotes emphasizes setting Periods Per Year (P/Y) to 1[cite: 331].
        * Keystrokes: `[2nd] [P/Y] "1" [ENTER] [2nd] [QUIT]`[cite: 331].
    * This means `N` becomes the number of compounding periods and `I/Y` is the interest rate *per compounding period*[cite: 335].
* **PV/FV Calculations 🧮**:
    * **Sign Convention**: Always remember to use opposite signs for PV and FV (and PMT if it's an outflow vs. inflows)[cite: 350]. Typically, PV is an outflow (negative) if FV is an inflow (positive)[cite: 351].
    * **Zero-Coupon Bond Pricing**: $PMT = 0$[cite: 350]. Example: 15-year, \$1,000 face, YTM 4%[cite: 346].
        * $N=15, I/Y=4, FV=1000, PMT=0$. CPT $PV = -555.26$[cite: 348, 350].
    * **Coupon Bond Pricing**: $PMT$ is the annual coupon payment[cite: 355]. Example: 10-year, \$1,000 par, 10% coupon, YTM 8%[cite: 360, 362].
        * $N=10, I/Y=8, PMT=100, FV=1000$. CPT $PV = -1,134.20$[cite: 364].
* **Perpetuity Valuation**:
    * **Formula**: $PV_{Perpetuity} = \frac{\text{Payment}}{r}$[cite: 368].
    * **Preferred Stock**: $V_p = \frac{D_p}{k_p}$ (Dividend / Required Return)[cite: 383].
* **Constant Growth DDM (Gordon Growth Model)**:
    * **Formula**: $V_0 = \frac{D_1}{k_e - g_c}$[cite: 393].
    * **Pro Tip 🚀**: $k_e$ must be greater than $g_c$[cite: 393]. This model values the stock one period *before* the dividend ($D_1$) used in the numerator[cite: 393].
* **Implied Returns/Growth Rates**: Rearrange the valuation formulas.
    * **Implied required return from DDM**: $k_e = \frac{D_1}{V_0} + g_c$ (Dividend Yield + Growth Rate)[cite: 423].
    * **Implied growth rate from DDM**: $g_c = k_e - \frac{D_1}{V_0}$ (Required Return - Dividend Yield)[cite: 424].
* **Cash Flow Additivity Principle**: The PV of a stream of cash flows is the sum of the PVs of the individual cash flows[cite: 426]. This is the basis for no-arbitrage pricing[cite: 435].
* **Forward Interest Rates (Implied)**:
    * **Concept**: $(1+S_2)^2 = (1+S_1)(1 + 1y1y)$ for spot rates $S_1, S_2$ and 1-year forward rate starting 1 year from now ($1y1y$)[cite: 448, 453].
    * **Pro Tip 🚀**: The longer-term spot rate is a geometric average of the shorter-term spot rate and the implied forward rates.
* **Forward Exchange Rates (No-Arbitrage)**:
    * **Formula**: $\frac{\text{Forward}}{\text{Spot}} = \frac{(1 + i_{\text{price currency}})}{(1 + i_{\text{base currency}})}$[cite: 461].
    * Or, Forward = Spot $\times \frac{(1 + i_{\text{price currency}} \times \frac{\text{days}}{360})}{(1 + i_{\text{base currency}} \times \frac{\text{days}}{360})}$ (adjusting for periodicity of interest rates).
    * **Pro Tip 🚀**: The currency with the *higher* interest rate will trade at a *forward discount*[cite: 2838]. The currency with the *lower* interest rate will trade at a *forward premium*. This is to prevent arbitrage[cite: 2830, 2838].

---

### Reading 3: Statistical Measures of Asset Returns

* **Measures of Central Tendency**:
    * **Arithmetic Mean ($\bar{x}$)**: Simple average[cite: 510]. Best estimator for a single period's expected return.
    * **Geometric Mean ($R_G$)**: Use for multi-period returns to find the compound rate[cite: 153, 180]. Always ≤ Arithmetic Mean[cite: 163].
    * **Harmonic Mean**: Use for averaging costs when a fixed amount of money is invested periodically (e.g., dollar-cost averaging)[cite: 165, 181]. For positive values, $H < G < A$[cite: 174].
    * **Median**: Middle value; unaffected by outliers[cite: 514, 518].
    * **Mode**: Most frequent value[cite: 526].
* **Measures of Dispersion**:
    * **Range**: Max value - Min value[cite: 555]. Simple but affected by outliers.
    * **Mean Absolute Deviation (MAD)**: Average of absolute values of deviations from the mean[cite: 556].
    * **Variance ($s^2$ or $\sigma^2$)**: Average of squared deviations. For sample variance, denominator is $n-1$ (unbiased estimator)[cite: 560, 563]. Units are squared[cite: 569].
    * **Standard Deviation ($s$ or $\sigma$)**: Square root of variance[cite: 573]. Units are same as data[cite: 572].
    * **Coefficient of Variation (CV)**: $CV = \frac{s}{\bar{x}}$[cite: 582]. Measures risk per unit of return; lower is better[cite: 585]. Useful for comparing datasets with different means[cite: 583].
    * **Target Downside Deviation (Target Semideviation)**: Measures risk below a specific target B[cite: 591, 592]. Only includes deviations where $X_i < B$[cite: 592]. Denominator is still $n-1$[cite: 593].
* **Skewness & Kurtosis**:
    * **Skewness**: Measures asymmetry[cite: 610].
        * **Positive (Right) Skew**: Mean > Median > Mode[cite: 617]. Longer right tail[cite: 613].
        * **Negative (Left) Skew**: Mode > Median > Mean[cite: 623]. Longer left tail[cite: 615].
        * **Pro Tip 🚀**: Mean is pulled in the direction of the skew[cite: 625]. Values > |0.5| are considered significant[cite: 636].
    * **Kurtosis**: Measures peakedness and tail fatness relative to normal distribution[cite: 637].
        * **Leptokurtic**: More peaked, fatter tails (Excess Kurtosis > 0)[cite: 638, 646]. Higher probability of extreme outcomes[cite: 640, 641].
        * **Platykurtic**: Flatter, thinner tails (Excess Kurtosis < 0)[cite: 638, 646].
        * **Mesokurtic**: Same as normal distribution (Excess Kurtosis = 0)[cite: 639, 646]. Normal distribution has kurtosis of 3[cite: 645].
        * **Pro Tip 🚀**: Higher positive excess kurtosis and more negative skew in returns distributions indicate increased risk[cite: 651].
* **Correlation ($\rho_{XY}$ or $r_{XY}$)**: Measures linear relationship between two variables[cite: 667, 669]. Ranges from -1 to +1[cite: 670, 671].
    * $\rho_{XY} = \frac{Cov_{XY}}{s_X s_Y}$[cite: 668].
    * **Pro Tip 🚀**: Correlation does not imply causation[cite: 678]. Spurious correlation can occur[cite: 684]. Scatter plots can reveal non-linear relationships not captured by correlation[cite: 658].

---

### Reading 4: Probability Trees and Conditional Expectations

* **Expected Value $E(X)$**: Probability-weighted average of outcomes[cite: 730]. $E(X) = \sum P(x_i)x_i$[cite: 731].
* **Variance from a Probability Model $\sigma^2(X)$**: $\sigma^2(X) = \sum P(x_i)[x_i - E(X)]^2$[cite: 736].
    * **Pro Tip 🚀**: This is different from sample variance (which uses $n-1$)[cite: 744]. Here, probabilities sum to 1, so no $n$ in the denominator[cite: 745, 746].
* **Standard Deviation $\sigma(X)$**: $\sqrt{\sigma^2(X)}$[cite: 737].
* **Probability Trees**: Visually represent sequences of events and their probabilities[cite: 749].
    * **Conditional Expectations**: Expected values contingent on the outcome of another event[cite: 755]. Used to revise expectations with new info[cite: 756].
* **Bayes' Formula**: Updates prior probabilities based on new information[cite: 760].
    * $P(\text{Event} | \text{Information}) = \frac{P(\text{Information} | \text{Event})}{P(\text{Information})} \times P(\text{Event})$[cite: 761].
    * **Tree Diagram Approach for $P(A|C)$**: $P(A|C) = \frac{P(AC)}{P(AC) + P(BC)}$, where $P(AC)$ is the joint probability of A and C[cite: 778].
    * **Pro Tip 🚀**: When using a tree, the denominator $P(\text{Information})$ is the sum of all paths that lead to that information[cite: 762]. Example: Given stock had gains, $P(\text{Outperform | Gains}) = \frac{P(\text{Gains and Outperform})}{P(\text{Gains and Outperform}) + P(\text{Gains and Underperform})}$[cite: 768].

---

### Reading 5: Portfolio Mathematics

* **Expected Portfolio Return $E(R_p)$**: $E(R_p) = \sum w_i E(R_i) = w_1 E(R_1) + w_2 E(R_2) + ...$[cite: 781].
* **Portfolio Variance ($Var(R_p)$ or $\sigma_p^2$)**:
    * **Two-Asset Portfolio**: $\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2w_A w_B Cov_{AB}$[cite: 801].
    * Alternatively, using correlation: $\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2w_A w_B \rho_{AB} \sigma_A \sigma_B$[cite: 806, 851].
    * **Pro Tip 🚀**: $Cov(R_A, R_A) = Var(R_A)$[cite: 791]. The diagonal terms in a covariance matrix are variances[cite: 798]. Off-diagonal terms are covariances[cite: 798]. $Cov_{AB} = Cov_{BA}$[cite: 798].
    * Lower covariance (even negative) reduces portfolio variance[cite: 805].
* **Covariance from Joint Probability Function**: $Cov(R_A, R_B) = \sum P(R_{Ai}, R_{Bi})[R_{Ai} - E(R_A)][R_{Bi} - E(R_B)]$[cite: 852].
* **Shortfall Risk**: Probability that portfolio return/value falls below a target $R_L$[cite: 821]. $P(R_p < R_L)$[cite: 823].
* **Roy's Safety-First Criterion**: Optimal portfolio *minimizes* $P(R_p < R_L)$[cite: 822, 854].
    * If returns are normally distributed, this means *maximizing* the Safety-First Ratio (SFR)[cite: 823]:
        * $SFR = \frac{E(R_p) - R_L}{\sigma_p}$[cite: 823, 853].
    * **Pro Tip 🚀**: SFR is the number of standard deviations the target return $R_L$ is *below* the expected portfolio return $E(R_p)$[cite: 828]. A higher SFR means a lower probability of falling below $R_L$[cite: 829, 853].

---

### Reading 6: Simulation Methods

* **Lognormal Distribution**:
    * Generated by $e^x$ where $x$ is normal[cite: 858].
    * If returns are continuously compounded and assumed normal (or their sum is normal by CLT), then asset prices $P_T = P_0 e^{r_{0,T}}$ will be lognormally distributed[cite: 862, 863, 867, 911].
    * **Key Properties**: Positively skewed, bounded below by zero (prices can't be negative)[cite: 860, 919].
* **Monte Carlo Simulation**:
    * Process: Specify distributions for risk factors, generate random values, value security, repeat many times, use distribution of outcomes.
    * **Uses**: Valuing complex securities, VaR calculation, simulating strategies/pension liabilities.
    * **Pro Tip 🚀**: Strength is ability to model complex scenarios and use non-historical inputs[cite: 887]. Weakness is complexity and "garbage in, garbage out" – results depend on quality of assumptions/model[cite: 889, 915].
* **Bootstrap Resampling**: Draws repeated samples *with replacement* from the observed dataset to estimate a statistic's sampling distribution (e.g., standard error of the mean)[cite: 897, 916].
    * **Pro Tip 🚀**: Unlike Monte Carlo, inputs are limited by the historical data distribution[cite: 901].

---

### Reading 7: Estimation and Inference

* **Sampling Methods**:
    * **Simple Random Sampling**: Each item has equal chance of selection[cite: 931, 1006].
    * **Systematic Sampling**: Select every nth item[cite: 938]. Approx. random.
    * **Stratified Random Sampling**: Divide population into strata (subgroups based on characteristics); take random samples from each stratum proportionally[cite: 939, 941, 1011]. Reduces sampling error for specific characteristics.
    * **Cluster Sampling**: Divide population into clusters (subgroups, each representative of population)[cite: 954]. Randomly select clusters; sample all (one-stage) or some (two-stage) items from selected clusters[cite: 956, 957, 1013, 1014]. Cheaper, but potentially more error if clusters aren't truly representative[cite: 959].
    * **Non-Probability Sampling (Convenience, Judgmental)**: Based on ease or researcher judgment[cite: 929, 962, 965, 1017]. Higher sampling error likely[cite: 930, 963].
* **Central Limit Theorem (CLT)**:
    * For simple random samples of size $n \ge 30$ from a population with mean $\mu$ and finite variance $\sigma^2$, the sampling distribution of the sample mean $\bar{x}$ will be approximately normal with mean $\mu$ and variance $\frac{\sigma^2}{n}$[cite: 974, 1017].
    * **Standard Error of the Sample Mean ($\sigma_{\bar{x}}$ or $s_{\bar{x}}$)**:
        * Known $\sigma$: $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$[cite: 983].
        * Unknown $\sigma$: $s_{\bar{x}} = \frac{s}{\sqrt{n}}$ (use sample std. dev. $s$)[cite: 984, 1017].
    * **Pro Tip 🚀**: CLT is powerful because it allows us to make inferences about the population mean using the normal distribution, even if the underlying population isn't normal, provided $n$ is large enough[cite: 975, 976]. Increasing sample size $n$ decreases the standard error $s_{\bar{x}}$[cite: 991, 992].
* **Resampling (for Standard Error)**:
    * **Jackknife**: Calculate multiple sample means, each with one observation removed[cite: 997]. Std. dev. of these means estimates $s_{\bar{x}}$[cite: 998, 1020]. Good for small samples, can remove bias[cite: 999, 1000, 1021].
    * **Bootstrap**: Draw many samples of size $n$ *with replacement* from the dataset[cite: 1002]. Calculate std. dev. of these sample means for $s_{\bar{x}}$[cite: 1003, 1022]. More computationally intensive but can be more accurate for complex statistics[cite: 1001, 1004, 1023].

---

### Reading 8: Hypothesis Testing

* **Hypothesis Testing Steps**[cite: 1035]:
    1.  State hypothesis ($H_0, H_a$)[cite: 1036].
    2.  Select test statistic[cite: 1036].
    3.  Specify significance level ($\alpha$)[cite: 1036].
    4.  State decision rule[cite: 1036].
    5.  Collect sample, calculate statistic[cite: 1036].
    6.  Make decision regarding $H_0$[cite: 1036].
    7.  Make decision based on test results[cite: 1036].
* **Null ($H_0$) vs. Alternative ($H_a$)**: $H_0$ is what the researcher wants to reject[cite: 1036, 1235]; it always includes equality ($=, \le, \ge$)[cite: 1040]. $H_a$ is what is concluded if $H_0$ is rejected[cite: 1041, 1236]. They are mutually exclusive and exhaustive[cite: 1044, 1045].
* **Test Statistic General Form**: $\frac{\text{Sample Statistic} - \text{Hypothesized Value}}{\text{Standard Error of Sample Statistic}}$[cite: 1058].
* **Errors**:
    * **Type I Error**: Reject true $H_0$[cite: 1068, 1237]. Probability = $\alpha$ (significance level)[cite: 1070, 1238].
    * **Type II Error**: Fail to reject false $H_0$[cite: 1069, 1237]. Probability = $\beta$.
    * **Power of a Test**: Correctly reject false $H_0$[cite: 1073, 1240]. Power = $1 - \beta$[cite: 1074, 1241].
    * **Pro Tip 🚀**: Decreasing $\alpha$ (e.g., from 5% to 1%) increases $\beta$ (reduces power) for a given sample size[cite: 1083]. Increasing sample size increases power for a given $\alpha$[cite: 1085].
* **Decision Rule**: Reject $H_0$ if test statistic falls in rejection region (beyond critical value(s))[cite: 1049, 1088].
* **p-value**: Smallest significance level at which $H_0$ can be rejected[cite: 1093, 1242]. If p-value < $\alpha$, reject $H_0$[cite: 1094].
* **Common Tests & Test Statistics**:
    * **Population Mean (Large Sample or Known Variance)**: z-test[cite: 1101]. Test stat: $z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$ or $\frac{\bar{x} - \mu_0}{s/\sqrt{n}}$ for large $n$[cite: 1059]. Example in text: Daily option returns test stat = 6.33[cite: 1113], critical z $\pm1.96$ (using z for large sample $n=250$) [cite: 1110, 1113] $\implies$ Reject $H_0$[cite: 1113].
    * **Population Mean (Small Sample, Unknown Variance, Normal Pop.)**: t-test[cite: 1101]. Test stat: $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$ with $df = n-1$[cite: 1059, 1109].
    * **Difference Between Means (Independent Samples, Normal Pops., Equal Unknown Variances)**: t-test with pooled variance[cite: 1117]. $df = n_1 + n_2 - 2$[cite: 1119].
    * **Paired Comparisons (Dependent Samples, Normal Pop. of Differences)**: t-test on mean difference $\bar{d}$[cite: 1135]. Test stat: $t = \frac{\bar{d} - \mu_{dz}}{s_{\bar{d}}}$ with $df = n-1$ (n = # of pairs)[cite: 1144].
    * **Population Variance (Normal Pop.)**: Chi-square ($\chi^2$) test[cite: 1104, 1167]. Test stat: $\chi^2 = \frac{(n-1)s^2}{\sigma_0^2}$ with $df = n-1$[cite: 1178]. $\chi^2$ distribution is asymmetrical, non-negative[cite: 1169, 1179].
    * **Equality of Two Population Variances (Normal Pops., Independent Samples)**: F-test[cite: 1105, 1194]. Test stat: $F = \frac{s_1^2}{s_2^2}$ (larger variance in numerator) [cite: 1197, 1198] with $df_1 = n_1-1$ (num.) and $df_2 = n_2-1$ (den.)[cite: 1197]. F-distribution is right-skewed, non-negative[cite: 1200, 1201].
* **Parametric vs. Nonparametric Tests**:
    * **Parametric**: Rely on assumptions about population distribution (e.g., normality) and parameters (e.g., mean, variance)[cite: 1217, 1243]. z-test, t-test, $\chi^2$-test, F-test[cite: 1243].
    * **Nonparametric**: Fewer assumptions[cite: 1220], used when parametric assumptions aren't met[cite: 1221], data are ranks[cite: 1222], or hypothesis doesn't involve parameters[cite: 1221, 1227, 1245].

---

### Reading 9: Parametric and Non-Parametric Tests of Independence

* **Test of Correlation Coefficient = 0 (Parametric)**:
    * $H_0: \rho = 0$[cite: 1256].
    * Test statistic: $t = \frac{r\sqrt{n-2}}{\sqrt{1-r^2}}$ with $df = n-2$ (assuming variables are normally distributed)[cite: 1257, 1285].
    * **Pro Tip 🚀**: Test statistic increases with sample correlation $r$ and sample size $n$[cite: 1258].
* **Spearman Rank Correlation Test (Nonparametric)**:
    * Used for ranks or when parametric assumptions (like normality) for Pearson correlation are not met[cite: 1264, 1286].
    * Calculates correlation based on ranks of data[cite: 1265].
    * Significance test for Spearman $r_s$: use same t-statistic formula as above if $n > 30$ (using $r_s$ instead of $r$)[cite: 1266, 1289].
* **Test of Independence (Contingency Table Data)**:
    * Uses a chi-square ($\chi^2$) test[cite: 1274, 1291].
    * $H_0$: The two categorical characteristics are independent[cite: 1270].
    * Test statistic: $\chi^2 = \sum \frac{(\text{Observed}_{ij} - \text{Expected}_{ij})^2}{\text{Expected}_{ij}}$[cite: 1274, 1291].
    * Degrees of freedom $df = (\text{rows} - 1) \times (\text{columns} - 1)$[cite: 1274, 1291].
    * Expected frequency $E_{ij} = \frac{(\text{Total Row } i) \times (\text{Total Column } j)}{\text{Grand Total}}$[cite: 1275].
    * **Pro Tip 🚀**: Reject $H_0$ (conclude characteristics are dependent) if calculated $\chi^2 >$ critical $\chi^2$[cite: 1292].

---

### Reading 10: Simple Linear Regression

* **Simple Linear Regression Model**: $Y_i = b_0 + b_1 X_i + \epsilon_i$[cite: 1317, 1453].
    * Estimated line: $\hat{Y}_i = \hat{b}_0 + \hat{b}_1 X_i$[cite: 1318].
    * $\hat{b}_1$ (slope): $\frac{Cov(X,Y)}{Var(X)}$[cite: 1325]. Change in Y for a one-unit change in X[cite: 1324, 1454].
    * $\hat{b}_0$ (intercept): $\bar{Y} - \hat{b}_1 \bar{X}$[cite: 1326]. Value of Y when X = 0[cite: 1325, 1333, 1453].
    * **Least Squares Criterion**: Minimizes Sum of Squared Errors (SSE) or $\sum (Y_i - \hat{Y}_i)^2$[cite: 1320, 1321, 1453].
* **Assumptions of Linear Regression**:
    1.  Linear relationship between X and Y[cite: 1348, 1455].
    2.  Homoskedasticity (constant variance of residuals $\epsilon_i$)[cite: 1349, 1456].
    3.  Independence of residuals (residuals not correlated with each other)[cite: 1349, 1456].
    4.  Normality of residuals[cite: 1351, 1457].
    * **Pro Tip 🚀**: Residual plots help detect violations (e.g., pattern for nonlinearity[cite: 1353, 1354], fanning out for heteroskedasticity[cite: 1357], pattern over time for non-independence [cite: 1362, 1363]).
* **Analysis of Variance (ANOVA)**:
    * **SST (Total Sum of Squares)** = $\sum (Y_i - \bar{Y})^2$[cite: 1380, 1457]. Total variation in Y.
    * **SSR (Regression Sum of Squares)** = $\sum (\hat{Y}_i - \bar{Y})^2$[cite: 1381, 1458]. Explained variation.
    * **SSE (Sum of Squared Errors)** = $\sum (Y_i - \hat{Y}_i)^2$[cite: 1386, 1460]. Unexplained variation.
    * SST = SSR + SSE[cite: 1388].
    * **MSR (Mean Square Regression)** = SSR / k (k= # indep. variables; k=1 for simple linear regression, so MSR=SSR)[cite: 1382, 1459].
    * **MSE (Mean Squared Error)** = SSE / (n-k-1) (for simple linear regression, $df = n-2$)[cite: 1387, 1461].
* **Measures of Fit**:
    * **Coefficient of Determination ($R^2$)**: $R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}$[cite: 1395, 1462]. Percentage of variation in Y explained by X[cite: 1395]. For simple linear regression, $R^2 = (\text{correlation coefficient } r)^2$[cite: 1397].
    * **Standard Error of Estimate (SEE or $s_e$)**: $\sqrt{MSE} = \sqrt{\frac{SSE}{n-2}}$[cite: 1394, 1463]. Standard deviation of residuals[cite: 1393]. Lower SEE = better fit[cite: 1394].
    * **F-Statistic (for overall model significance)**: $F = \frac{MSR}{MSE} = \frac{SSR/k}{SSE/(n-k-1)}$[cite: 1400, 1463]. For simple linear regression (k=1), $F = \frac{SSR}{SSE/(n-2)}$[cite: 1400]. Tests $H_0: b_1 = 0$[cite: 1400, 1463].
        * **Pro Tip 🚀**: For simple linear regression, F-statistic = $(t \text{-statistic for slope coefficient})^2$.
* **Hypothesis Test for Slope Coefficient ($b_1$)**:
    * $H_0: b_1 = \text{hypothesized value (often 0)}$[cite: 1409].
    * Test statistic: $t = \frac{\hat{b}_1 - b_1}{s_{\hat{b}_1}}$ with $df = n-2$[cite: 1408]. $s_{\hat{b}_1}$ is standard error of slope coefficient.
* **Prediction Interval for $\hat{Y}$**: $\hat{Y} \pm t_c \times s_f$, where $s_f$ is standard error of the forecast and $t_c$ is critical t-value with $df = n-2$[cite: 1426, 1463].
    * Variance of forecast: $s_f^2 = s_e^2 [1 + \frac{1}{n} + \frac{(X_p - \bar{X})^2}{(n-1)s_X^2}]$ [cite: 1429] (unlikely to calculate $s_f$ on exam, but know it widens as $X_p$ moves from $\bar{X}$).
* **Functional Forms**: If $Y = f(X)$ is not linear, transform variables[cite: 1438, 1439].
    * **Log-lin**: $\ln(Y) = b_0 + b_1 X$[cite: 1441, 1444]. Slope $b_1 \approx$ relative change in Y for absolute change in X[cite: 1444].
    * **Lin-log**: $Y = b_0 + b_1 \ln(X)$[cite: 1442, 1446]. Slope $b_1 \approx$ absolute change in Y for relative change in X[cite: 1446].
    * **Log-log**: $\ln(Y) = b_0 + b_1 \ln(X)$[cite: 1443, 1447]. Slope $b_1$ is elasticity: relative change in Y for relative change in X[cite: 1447].

---

### Reading 11: Introduction to Big Data Techniques

* **Fintech**: Technology applied to the financial services industry[cite: 1481, 1546]. Key areas: handling large datasets, AI for analysis[cite: 1483].
* **Big Data**: Characterized by Volume, Velocity, and Variety (structured, semi-structured, unstructured)[cite: 1491, 1549].
    * **Data Science**: Methods for processing (capture, curation, storage, search, transfer) and visualizing data[cite: 1498, 1499].
* **Artificial Intelligence (AI)**: Systems simulating human cognition[cite: 1509, 1549].
    * **Machine Learning (ML)**: Algorithms learn from data to model outputs or detect patterns without explicit programming[cite: 1513, 1550].
        * **Supervised Learning**: Labeled input and output data; machine learns mapping[cite: 1517].
        * **Unsupervised Learning**: Unlabeled input data; machine learns structure/patterns[cite: 1518].
        * **Deep Learning**: Uses layers of neural networks for complex pattern recognition[cite: 1519].
        * **Pro Tip 🚀**: Watch for **overfitting** (model too complex, learns noise) [cite: 1522] and **underfitting** (model too simple, misses patterns)[cite: 1524].
* **Applications in Investment Management**[cite: 1528, 1551]:
    * **Text Analytics**: Analyzing unstructured text/voice data (e.g., company filings, sentiment)[cite: 1529, 1552].
    * **Natural Language Processing (NLP)**: AI to interpret human language (e.g., compliance checks, evaluating research reports)[cite: 1532, 1553].
    * **Algorithmic Trading**: Computerized trading based on rules (e.g., optimal execution, high-frequency trading)[cite: 1539, 1554].

---

**General Pro Tips for Quant 🚀:**

1.  **Calculator Mastery**: Know your calculator inside out, especially CF, NPV, IRR, LN, $e^x$, $y^x$, $1/x$, and statistical functions. Time saved here is crucial.
2.  **Formula Understanding**: Don't just memorize; understand what each part of a formula represents. This helps in adapting to slightly different question phrasings.
3.  **Sign Conventions**: Be meticulous with signs in TVM and cash flow analysis.
4.  **Assumptions**: Know the key assumptions behind statistical tests and models (e.g., normality for t-tests, assumptions of linear regression). Violations can change the validity of results.
5.  **Distributions**: Understand the basic shapes and properties of Normal, Lognormal, t, Chi-square, and F-distributions.
6.  **Read Carefully**: Quant questions are often precise. Misreading a "less than" for a "greater than," or a "sample" for a "population," can lead to the wrong answer.