Of course. Reading 75 introduces the binomial model, a foundational tool for option pricing. It demonstrates how no-arbitrage principles can be used to find the precise value of an option.

Here is a detailed summary of Module 75.1.

***

### Module 75.1: Binomial Model for Option Values

This module presents two related methods for valuing an option in a simplified, one-period world where the underlying asset's price can only move to one of two possible future values.

#### The No-Arbitrage (Hedge Ratio) Method (LOS 75.a)

This approach values an option by creating a perfectly hedged, risk-free portfolio. Because the portfolio is risk-free, its return must be the risk-free rate.

**The Process:**

1.  **Define the Future:** Start with the two possible future prices of the underlying asset (up-state and down-state) and the corresponding option payoffs at expiration ($c^+$ and $c^-$).

2.  **Build a Riskless Portfolio:** Create a portfolio by being **short one call option** and **long *h* shares** of the underlying stock. The variable ***h*** is the **hedge ratio**.

3.  **Find the Hedge Ratio (h):** Calculate the number of shares needed to ensure the portfolio has the exact same value whether the stock goes up or down.
    $$h = \frac{\text{Up-state Option Payoff} - \text{Down-state Option Payoff}}{\text{Up-state Stock Price} - \text{Down-state Stock Price}} = \frac{c^+ - c^-}{S^+ - S^-}$$

4.  **Value the Future Portfolio:** Since the portfolio's future value is now certain (it's the same in both states), calculate this guaranteed future value: $V_T = hS^+ - c^+$.

5.  **Discount to Today:** Find the present value of this riskless portfolio by discounting its certain future value at the **risk-free rate ($R_f$)**: $V_0 = \frac{V_T}{1+R_f}$.

6.  **Solve for the Option Price:** The value of the portfolio today ($V_0$) is also equal to its initial construction cost ($hS_0 - c_0$). Since you know everything else, you can solve for the call price ($c_0$).
    $$c_0 = hS_0 - V_0$$

> **CFA Exam Tip:** Understand the logic of this process. The goal is to create a portfolio with a certain future payoff. Because the payoff is certain, you are justified in discounting it at the risk-free rate.

---

#### The Risk-Neutral Probability Method (LOS 75.b)

This second method is a mathematical shortcut that yields the exact same result as the hedge ratio method. It uses a hypothetical "risk-neutral" world to value the option.

**What is Risk Neutrality?**
It's an imaginary world where investors are indifferent to risk. In this world, the expected return on *all* assets (even risky stocks) is simply the **risk-free rate**. We use this assumption to calculate "risk-neutral probabilities," which are not real-world probabilities but are useful for pricing.

**The Process:**

1.  **Define the Future:** Same as before, identify the up-state and down-state prices and option payoffs ($c^+$ and $c^-$).

2.  **Calculate Risk-Neutral Probabilities ($\pi$):** Calculate the probability of an up-move ($\pi_{up}$) that would make the stock's expected return equal the risk-free rate.
    $$\pi_{up} = \frac{(1+R_f) - \text{Down-move Factor}}{\text{Up-move Factor} - \text{Down-move Factor}}$$
    And $\pi_{down} = 1 - \pi_{up}$
    *(Note: You are more likely to be given these probabilities on the exam than asked to calculate them from scratch).*

3.  **Calculate Expected Option Payoff:** Use these risk-neutral probabilities to find the weighted-average expected payoff of the option at expiration.
    Expected Payoff = $(\pi_{up} \times c^+) + (\pi_{down} \times c^-)$

4.  **Discount to Today:** Discount this single expected payoff back to today using the **risk-free rate ($R_f$)**.
    $$c_0 = \frac{\text{Expected Payoff}}{1+R_f}$$

> **CFA Exam Tip:** Both methods lead to the same no-arbitrage price. The key takeaway from both is that in a no-arbitrage framework, the **risk-free rate is the appropriate discount rate** for valuing options.

***

### Summary of Formulas for Reading 75

This reading introduces the binomial model, which requires understanding both the process and the formulas.

* **Hedge Ratio (for a call option):**
    This tells you how many shares of the underlying you need to hold for each option you write to create a riskless portfolio.
    $$h = \frac{c^+ - c^-}{S^+ - S^-}$$

* **Risk-Neutral Probability of an Up-Move ($\pi_{up}$):**
    This is the "pseudo-probability" that makes the expected return of the underlying asset equal the risk-free rate.
    $$\pi_{up} = \frac{(1+R_f) - d}{u-d}$$
    *(where 'u' is the up-move factor, e.g., 1.20 for a 20% up-move, and 'd' is the down-move factor, e.g., 0.80 for a 20% down-move)*

* **Option Value Using Risk-Neutrality:**
    This is the core valuation formula for the risk-neutral method.
    $$c_0 = \frac{[\pi_{up} \times c^+] + [(1-\pi_{up}) \times c^-]}{1+R_f}$$

***

### ⚡ Quick Exam-Day Pointers

For Reading 75, the exam will test your understanding of the no-arbitrage process. The key is to remember *why* the models work.

* **Two Paths, One Destination:** Both methods presented—the **Hedge Ratio** method and the **Risk-Neutral Probability** method—are just different ways to arrive at the same **no-arbitrage option price**.

* **The Golden Rule: Discount at $R_f$!** 🪙 The entire point of both binomial methods is to create a situation where the future payoff is effectively riskless. Because of this, the correct discount rate to use is **always the risk-free rate ($R_f$)**. If you see an option pricing question with multiple interest rates, you'll almost certainly use the risk-free rate.

* **Hedge Ratio Logic:** The goal is to build a *physically riskless portfolio* (long stock, short option). Since its future value is certain, you can discount it by $R_f$.

* **Risk-Neutral Logic:** The goal is to calculate a *risk-adjusted expected payoff*. The special "risk-neutral" probabilities are designed to remove the need for a risk premium. This allows you to discount the probability-weighted payoff by $R_f$.

* **Focus on the Process:** For Level 1, it's more important to understand the steps and logic of the valuation process than to perform complex multi-step calculations. Be prepared to calculate the final option value if you are given the option payoffs and the risk-neutral probabilities.