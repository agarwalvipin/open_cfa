# 📊 Formula Sheet: Week 3 - Statistical Measures & Probability

## Reading 3: Statistical Measures of Asset Returns

### LOS 3.a: Calculate, interpret, and evaluate measures of central tendency and location to address an investment problem.

* **Sample Mean ($\bar{X}$)** [cite: 514]
    ```math
    \bar{X} = \frac{\sum_{i=1}^{n} X_i}{n}
    ```
    Where:
    * $X_i$ = Value of observation $i$
    * $n$ = Number of observations in the sample

* **Median**
    * For an odd number of observations sorted in ascending/descending order, the median is the middle value. [cite: 516, 521]
    * For an even number of observations sorted, the median is the arithmetic mean of the two middle observations. [cite: 524, 525]

* **Mode**
    * The value that occurs most frequently in a dataset. [cite: 526] A dataset can have one mode (unimodal), more than one mode (e.g., bimodal), or no mode. [cite: 528, 529]

---

### LOS 3.b: Calculate, interpret, and evaluate measures of dispersion to address an investment problem.

* **Range** [cite: 555]
    ```math
    \text{Range} = \text{Maximum Value} - \text{Minimum Value}
    ```

* **Mean Absolute Deviation (MAD)** [cite: 556]
    ```math
    MAD = \frac{\sum_{i=1}^{n} |X_i - \bar{X}|}{n}
    ```
    Where:
    * $X_i$ = Value of observation $i$
    * $\bar{X}$ = Sample mean
    * $n$ = Number of observations

* **Sample Variance ($s^2$)** [cite: 560]
    ```math
    s^2 = \frac{\sum_{i=1}^{n} (X_i - \bar{X})^2}{n-1}
    ```

* **Sample Standard Deviation ($s$)** [cite: 574]
    ```math
    s = \sqrt{\frac{\sum_{i=1}^{n} (X_i - \bar{X})^2}{n-1}}
    ```

* **Coefficient of Variation (CV)** [cite: 582]
    ```math
    CV = \frac{s}{\bar{X}}
    ```
    Where:
    * $s$ = Sample standard deviation
    * $\bar{X}$ = Sample mean

* **Target Downside Deviation (Target Semideviation, $s_{target}$)** [cite: 593]
    ```math
    s_{target} = \sqrt{\frac{\sum_{\text{for all } X_i \le B} (X_i - B)^2}{n-1}}
    ```
    Where:
    * $X_i$ = Individual observations below the target
    * $B$ = The target value
    * $n$ = Total number of observations in the sample

---

### LOS 3.c: Interpret and evaluate measures of skewness and kurtosis to address an investment problem.

*(Note: The LOS requires interpretation and evaluation, not primarily calculation for Level I. Formulas are provided for context as they appear in the SchweserNotes™).*

* **Sample Skewness (Approximation for large samples)** [cite: 629]
    ```math
    \text{Sample Skewness} \approx \left(\frac{1}{n}\right) \frac{\sum_{i=1}^{n} (X_i - \bar{X})^3}{s^3}
    ```
    Where:
    * $s$ = Sample standard deviation

* **Sample Kurtosis (Approximation for large samples)** [cite: 652]
    ```math
    \text{Sample Kurtosis} \approx \left(\frac{1}{n}\right) \frac{\sum_{i=1}^{n} (X_i - \bar{X})^4}{s^4}
    ```
    Where:
    * $s$ = Sample standard deviation

* **Excess Kurtosis** [cite: 645]
    ```math
    \text{Excess Kurtosis} = \text{Sample Kurtosis} - 3
    ```
    (A normal distribution has a kurtosis of 3 and excess kurtosis of 0).

---

### LOS 3.d: Interpret correlation between two variables to address an investment problem.

* **Sample Covariance ($s_{XY}$ or $Cov(X,Y)$)** [cite: 661]
    ```math
    s_{XY} = \frac{\sum_{i=1}^{n} \{[X_i - \bar{X}][Y_i - \bar{Y}]\}}{n-1}
    ```
    Where:
    * $X_i, Y_i$ = Paired observations of variables X and Y
    * $\bar{X}, \bar{Y}$ = Sample means of X and Y
    * $n$ = Number of paired observations

* **Correlation Coefficient ($\rho_{XY}$ or $r_{XY}$)** [cite: 668]
    ```math
    \rho_{XY} = \frac{s_{XY}}{s_X s_Y}
    ```
    Where:
    * $s_{XY}$ = Sample covariance between X and Y
    * $s_X$ = Sample standard deviation of X
    * $s_Y$ = Sample standard deviation of Y

* **Covariance implied from Correlation** [cite: 668]
    ```math
    s_{XY} = \rho_{XY} s_X s_Y
    ```

---
---

## Reading 4: Probability Trees and Conditional Expectations

### LOS 4.a: Calculate expected values, variances, and standard deviations and demonstrate their application to investment problems.

* **Expected Value of a Random Variable X ($E(X)$)** [cite: 731]
    ```math
    E(X) = \sum_{i=1}^{n} P(x_i)x_i = P(x_1)x_1 + P(x_2)x_2 + \dots + P(x_n)x_n
    ```
    Where:
    * $P(x_i)$ = Probability of outcome $x_i$
    * $x_i$ = Value of outcome $i$

* **Variance of a Random Variable X ($\sigma^2(X)$ or $Var(X)$) from a Probability Model**
    (Calculated as the probability-weighted sum of squared deviations from the expected value) [cite: 736]
    ```math
    \sigma^2(X) = \sum_{i=1}^{n} P(x_i) [x_i - E(X)]^2
    ```
    (The example in the text [cite: 740, 743] uses this structure by calculating $Prob \times [R_A - E(R_A)]^2$ for each scenario and summing them.)

* **Standard Deviation of a Random Variable X ($\sigma(X)$)** [cite: 737]
    ```math
    \sigma(X) = \sqrt{\sigma^2(X)}
    ```

---

### LOS 4.b: Formulate an investment problem as a probability tree and explain the use of conditional expectations in investment application.

* **Joint Probability (from a probability tree structure)**
    (e.g., Probability of Event A and subsequent Event B, given A)
    ```math
    P(AB) = P(B|A) \times P(A)
    ```
    (Example: $EPS=\$1.80$ with $Prob = (60\% \text{ good economy} \times 30\% \text{ good results}) = 18\%$ [cite: 751, 753])

* **Total Probability Rule (Implied for calculating overall expected values from tree branches)**
    If an outcome $X$ depends on several mutually exclusive and exhaustive events $S_1, S_2, \dots, S_n$:
    ```math
    E(X) = E(X|S_1)P(S_1) + E(X|S_2)P(S_2) + \dots + E(X|S_n)P(S_n)
    ```
    (This is used for instance in Figure 4.1 for calculating Expected EPS [cite: 752])

---

### LOS 4.c: Calculate and interpret an updated probability in an investment setting using Bayes' formula.

* **Bayes' Formula (General Form)** [cite: 761]
    ```math
    P(\text{Event} | \text{Information}) = \frac{P(\text{Information} | \text{Event}) \times P(\text{Event})}{P(\text{Information})}
    ```
    Where $P(\text{Information})$ is the unconditional probability of the new information, often calculated using the total probability rule:
    $P(\text{Information}) = \sum P(\text{Information} | \text{Event}_i)P(\text{Event}_i)$

* **Bayes' Formula (Alternative representation from text)** [cite: 761]
    If $P(AB) = P(BA)$, then $P(B|A)P(A) = P(A|B)P(B)$. Rearranging for $P(A|B)$:
    ```math
    P(A|B) = \frac{P(B|A)P(A)}{P(B)}
    ```

* **Bayes' Formula (Using Joint Probabilities from a Tree Diagram)**
    (Example: If Event C is the "new information" and we want to update the probability of prior Event A)
    ```math
    P(A|C) = \frac{P(AC)}{P(C)} = \frac{P(AC)}{P(AC) + P(BC) + \dots}
    ```
    (The text example shows $P(A|C) = \frac{P(AC)}{P(AC)+P(A^C C)}$ which simplifies to $\frac{\text{Prob(Outperform and Gains)}}{\text{Prob(Gains)}}$ [cite: 762, 768])

---