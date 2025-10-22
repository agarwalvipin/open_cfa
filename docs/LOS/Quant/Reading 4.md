## Reading 4: Probability Trees and Conditional Expectations

### 🎯 Introduction

Welcome, future charterholder\! Imagine you're a detective trying to solve a case. 🕵️‍♂️ You start with some initial beliefs about what might have happened (**prior probabilities**). As new clues and evidence come in (**new information**), you don't just guess; you systematically update your beliefs to get closer to the truth. This reading teaches you how to be that financial detective. We'll learn how to map out all possible future scenarios using **probability trees**, calculate the most likely outcome (**expected value**), and most importantly, use **Bayes' formula** to intelligently update our forecasts as new market information arrives. Let's start gathering the clues\!

-----

### Part 1: What's the Most Likely Outcome? Expected Value & Volatility 🎲

Instead of just one possible future, we often face several potential outcomes, each with a different probability. The **expected value** is the probability-weighted average of all these possible outcomes. It's your best guess for the future, balancing the likelihood of each scenario.

  * **Expected Value, E(X)**: The long-run average value if you could repeat the "experiment" many times.
    $$E(X) = \sum P(x_i)x_i = P(x_1)x_1 + P(x_2)x_2 + ... + P(x_n)x_n$$
  * **Variance ($\sigma^2$) and Standard Deviation ($\sigma$)**: These measure the dispersion, or **volatility**, of the outcomes around the expected value. A high variance means the potential outcomes are very spread out (more risk), while a low variance means they are tightly clustered around the average (less risk).

#### **Theory 🧠**

Unlike calculating variance for a *historical sample* where you divide by `n-1`, when you have a *forward-looking probability model*, you don't use `n-1`. Instead, you use the probabilities themselves as weights.

**Variance from a Probability Model**:
$$\sigma^2 = \sum P(x_i)[x_i - E(X)]^2$$

This is the probability-weighted sum of the squared deviations from the expected value.

#### **Example 🧮**

Let's forecast the returns for a tech stock like Tata Consultancy Services (TCS) based on the state of the economy.

| Economic Scenario | Probability | Return (R_A) |
| :--- | :---: | :---: |
| Boom | 30% | 20% |
| Normal | 50% | 12% |
| Slow | 20% | 5% |

1.  **Calculate Expected Return E(R)**:
  E(R) = (0.30 × 20%) + (0.50 × 12%) + (0.20 × 5%) = 6% + 6% + 1% = **13%**

2.  **Calculate Variance (σ²)**:

    * Boom: 0.30 × (20% − 13%)² = 0.30 × (7%)² = 0.00147
    * Normal: 0.50 × (12% − 13%)² = 0.50 × (−1%)² = 0.00005
    * Slow: 0.20 × (5% − 13%)² = 0.20 × (−8%)² = 0.00128
    * **Variance** = 0.00147 + 0.00005 + 0.00128 = **0.00280**

3.  **Calculate Standard Deviation (σ)**:
  σ = √0.00280 = **5.29%**


### Part 2: Mapping the Future: Probability Trees & Conditional Expectations 🌳

A **probability tree** is a fantastic visual tool for mapping out sequential events and their probabilities. It helps you see all possible paths the future might take and calculate the probability of each final outcome.

```mermaid
graph TD
  subgraph "Probability Tree for EPS"
    direction LR
    A(Start) -->|Prob. of Good Economy = 60\%| B(Good Econ)
    A -->|Prob. of Poor Economy = 40\%| C(Poor Econ)

    B -->|Prob. of Good Results = 30\%| D[EPS = \$1.80<br/>Joint Prob = 18\%]
    B -->|Prob. of Poor Results = 70\%| E[EPS = \$1.70<br/>Joint Prob = 42\%]

    C -->|Prob. of Good Results = 60\%| F[EPS = \$1.30<br/>Joint Prob = 24\%]
    C -->|Prob. of Poor Results = 40\%| G[EPS = \$1.00<br/>Joint Prob = 16\%]
  end
```

To find the **joint probability** of any final outcome, you just multiply the probabilities along its path. For example, the probability of a good economy *and* good company results is $60\% \times 30\% = 18\%$.

The overall **expected value** is the sum of each outcome multiplied by its joint probability:
$$E(\mathrm{EPS}) = (0.18 \times 1.80) + (0.42 \times 1.70) + (0.24 \times 1.30) + (0.16 \times 1.00) = 1.51$$
(So EPS = \$1.51.)

#### **Conditional Expectations 🤔**

**Conditional expectations** are expected values that are contingent on a specific event having already happened. It's an updated forecast.

  * **Global Example**: What is the expected return on Apple stock, *given that* the US Federal Reserve just raised interest rates? This new piece of information changes our forecast.
  * **Indian Example**: What is the expected EPS for a bank like HDFC Bank, *given that* the RBI has just announced a new, stricter lending regulation? The announcement updates our expectation.

-----

### Part 3: The Detective's Formula: Updating Beliefs with Bayes' Formula 💡
This is where you become a true financial detective. Bayes' formula updates your prior belief about an event after observing new evidence.

Symbolic formula:
$$P(\text{Event} \mid \text{New Info}) = \frac{P(\text{New Info} \mid \text{Event}) \times P(\text{Event})}{P(\text{New Info})}$$

Worded formula:
Updated probability of the event given the new information = (likelihood of seeing the new information if the event is true × prior probability of the event) divided by (total probability of seeing the new information under all possible events).

Put another way:
Updated belief = (How consistent the evidence is with the event × how likely the event was originally) ÷ (how likely the evidence is overall).

#### **Theory 🧠**

An analyst believes there's a 60% chance the economy will outperform (Event) and a 40% chance it will underperform.

  * If it outperforms, there's a 70% chance a certain stock will go up (New Info | Event).
  * If it underperforms, there's only a 20% chance the stock will go up (New Info | Event).

**Question**: The stock just went up (New Info)\! What is the new, updated probability that the economy is outperforming?

#### **Example & Calculation 🧮**

**Step 1: Find the Prior Probabilities.**

  * P(Outperform) = 60%
  * P(Underperform) = 40%

**Step 2: Find the Joint Probabilities of the "New Info" happening.**

  * P(Stock Up AND Outperform) = P(Up | Outperform) $\times$ P(Outperform) = $70\% \times 60\% = 42\%$
  * P(Stock Up AND Underperform) = P(Up | Underperform) $\times$ P(Underperform) = $20\% \times 40\% = 8\%$

**Step 3: Find the Unconditional Probability of the "New Info".**
This is the total probability that the stock would go up, regardless of the economy. Just add the joint probabilities from Step 2.

  * P(Stock Up) = P(Up AND Outperform) + P(Up AND Underperform) = $42\% + 8\% = 50\%$

**Step 4: Apply Bayes' Formula.**
We want to find P(Outperform | Stock Up).
$$P(\text{Outperform | Stock Up}) = \frac{P(\text{Up AND Outperform})}{P(\text{Up})} = \frac{0.42}{0.50} = \mathbf{84\%}$$

**Conclusion**: Our initial belief was a 60% chance of an outperforming economy. After seeing the new evidence (the stock went up), we've updated our belief to a much more confident **84%**.

> [\!TIP]
> **CFA Exam Tip ✍️:** Bayes' formula questions on the exam can look intimidating. Don't panic\! The best way to solve them is to draw a quick probability tree. It helps you visualize the paths and easily calculate the joint probabilities needed for the numerator and the total probability for the denominator.

-----

### 🧪 Formula Summary

  * **Expected Value**: $$E(X) = \sum P(x_i)x_i$$
  * **Variance (from a probability model)**: $$\sigma^2(X) = \sum P(x_i)[x_i - E(X)]^2$$
  * **Bayes' Formula (for two events A and B)**: $$P(A|B) = \frac{P(B|A)}{P(B)} \times P(A)$$

-----

> [\!IMPORTANT]
>
> ### 🎯 Quick Exam-Day Pointers
>
>   * **Expected Value is a Weighted Average.** It's your single best guess, calculated by weighting each possible outcome by its probability.
>   * **Probability Trees are Your Friend.** Use them to visually map out scenarios. To get the final probability of any branch, multiply the probabilities along the path.
>   * **Variance is Different for Samples vs. Models.** Remember, for forward-looking probability models, you use the probabilities as weights to calculate variance, you DO NOT divide by `n-1`.
>   * **Bayes' Formula = Updating Your Priors.** It's the formal way to answer the question: "Now that I know *this*, what is the probability of *that*?"
>   * **Solve Bayes' with a Tree\!** The easiest way to handle a Bayes' question is to draw a tree, find the probability of all paths where the "new information" occurs, and then use the formula: `(Probability of your desired path) / (Sum of probabilities of ALL paths where the new info occurs)`.