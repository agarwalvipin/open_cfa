## Reading 75: Valuing a Derivative Using a One-Period Binomial Model 🌳

🎯 **Introduction**

Imagine you're at a fork in the road where a path splits into two—one goes up a hill, the other goes down. You know exactly where each path leads. The **one-period binomial model** is a lot like that! It's a powerful tool that simplifies a complex world by assuming an asset's price can only move to one of two possible values in the next period: up or down. By knowing these two potential outcomes, we can perfectly calculate what an option is worth today. This reading will show you two ways to do this: by building a risk-free portfolio and by using a clever shortcut called risk-neutral pricing.

---

### Part 1: How Do We Value an Option with Two Possible Futures? 🤔

The core idea here is **replication** and **no-arbitrage**. We can create a portfolio of the underlying stock and a loan that perfectly mimics the option's payoffs. Since the portfolio and the option have identical future payoffs, they must have the same price today. Otherwise, a risk-free profit opportunity (arbitrage) would exist.

To do this, we need to build a risk-free (perfectly hedged) portfolio. The key ingredient is the **hedge ratio (h)**, which tells us how many shares of the underlying asset we need to hold for each option we write to make our portfolio's value immune to the stock's movement.

#### **Valuing a Call Option**

Let's say we want to find the value of a European call option. We'll create a portfolio by buying `h` shares of the stock and selling one call option.

* **Goal:** Make the portfolio's value the same whether the stock price goes up or down.
* **Portfolio Value at Expiration:**
    * If price goes up: $V^+ = hS^+ - c^+$
    * If price goes down: $V^- = hS^- - c^-$
* **Hedge Ratio Formula:** To make $V^+ = V^-$, the hedge ratio must be:
    $h = \frac{c^+ - c^-}{S^+ - S^-}$

Since this portfolio is now risk-free, its return must be the **risk-free rate ($R_f$)**.

> **Example Time! 🧮**
>
> An HDFC Bank stock is currently trading at **$S_0 = \$50$**. In one period, it can either go up to **$S^+ = \$60$** or down to **$S^- = \$42$**. We want to value a call option with an exercise price of **$X = \$55$**. The risk-free rate is **3%**, 3303].
>
> 1.  **Find Option Payoffs:**
>     * If stock goes up to $60: c^+ = \text{Max}(0, 60 - 55) = \$5$.
>     * If stock goes down to $42: c^- = \text{Max}(0, 42 - 55) = \$0$.
>
> 2.  **Calculate Hedge Ratio (h):**
>     $h = \frac{5 - 0}{60 - 42} = \frac{5}{18} = 0.278$.
>     This means we buy 0.278 shares for every 1 call option we sell.
>
> 3.  **Find the Portfolio's Future Value:**
>     The portfolio will be worth the same amount in either scenario. Let's use the "up" state:
>     $V^+ = (0.278 \times \$60) - \$5 = \$16.68 - \$5 = \$11.68$.
>
> 4.  **Discount to Find Today's Value:**
>     The portfolio's value today must be the future value discounted at the risk-free rate:
>     $V_0 = \frac{\$11.68}{1.03} = \$11.34$.
>
> 5.  **Solve for the Call Price ($c_0$):**
>     The initial cost of setting up the portfolio was $V_0 = hS_0 - c_0$.
>     $\$11.34 = (0.278 \times \$50) - c_0$
>     $\$11.34 = \$13.90 - c_0 \implies c_0 = \$2.56$.
>
> The fair price of the call option today is **$2.56**.

#### **Valuing a Put Option**

The process for a put option is almost identical, but our hedged portfolio consists of buying `h` shares and **buying** one put option.

* **Hedge Ratio Formula:** The formula for `h` is the same:
    $h = \frac{p^+ - p^-}{S^+ - S^-}$

> [!TIP]
> **CFA Exam Tip ✍️:** Notice the hedge ratio for a put will be negative. This means you should *short* `h` shares for every put option you buy to create the risk-free hedge. For the exam, focus on understanding the *process* of creating a risk-free portfolio and discounting its value.

---

### Part 2: What is "Risk-Neutral" Pricing? ⚖️

**Risk-neutral pricing** is a powerful and elegant alternative. It's a mathematical shortcut that says, "Since we can build a perfect hedge, we don't need to worry about an investor's risk appetite. We can just pretend everyone is risk-neutral." 

In this pretend world, the expected return on any asset is simply the risk-free rate. We use this idea to calculate **risk-neutral probabilities** (often shown as $\pi$), which are pseudo-probabilities that make this true.

The valuation process becomes simpler:
1.  Calculate the option's payoffs if the price goes up ($c^+$) or down ($c^-$).
2.  Calculate the risk-neutral probabilities for the up-move ($\pi_{up}$) and down-move ($\pi_{down}$).
3.  Calculate the expected value of the option's payoff: $E(\text{Payoff}) = (\pi_{up} \times c^+) + (\pi_{down} \times c^-)$.
4.  Discount this expected value back to today at the risk-free rate.

$c_0 = \frac{(\pi_{up} \times c^+) + (\pi_{down} \times c^-)}{1 + R_f}$

> **Example with Risk-Neutral Probabilities! 🧮**
>
> Let's use a new example. A stock is at **$S_0 = \$30$**. It can go up to **$S^+ = \$34.50$** or down to **$S^- = \$26.10$**. The risk-free rate is **7%**. We want to value a call option with **X = $30**.
>
> 1.  **Find Option Payoffs:**
>     * $c^+ = \text{Max}(0, 34.50 - 30) = \$4.50$.
>     * $c^- = \text{Max}(0, 26.10 - 30) = \$0$.
>
> 2.  **Calculate Risk-Neutral Probabilities:**
>     * $\pi_{up} = \frac{(1+R_f)S_0 - S^-}{S^+ - S^-} = \frac{(1.07 \times 30) - 26.10}{34.50 - 26.10} = \frac{6}{8.4} = 0.715$.
>     * $\pi_{down} = 1 - 0.715 = 0.285$.
>
> 3.  **Find Expected Future Value:**
>     $E(\text{Payoff}) = (0.715 \times \$4.50) + (0.285 \times \$0) = \$3.22$.
>
> 4.  **Discount to Find Today's Value:**
>     $c_0 = \frac{\$3.22}{1.07} = \$3.01$.
>
> The fair price of the call option today is **$3.01**.

---

### 🧪 Formula Summary

* **Hedge Ratio (h):**
    $$h = \frac{\text{Payoff}^+ - \text{Payoff}^-}{\text{Underlying}^+ - \text{Underlying}^-}$$
* **Risk-Neutral Probability (Up-move):**
    $$\pi_{up} = \frac{(1+R_f)S_0 - S^-}{S^+ - S^-}$$
* **Option Value using Risk-Neutral Probabilities:**

$$C_0 = \frac{\pi_u \times C_u + \pi_d \times C_d}{1 + r}$$

Where:
- $C_0$ = Option value today
- $\pi_u$ = Risk-neutral probability of up move
- $\pi_d$ = Risk-neutral probability of down move  
- $C_u$ = Option payoff if price goes up
- $C_d$ = Option payoff if price goes down
- $r$ = Risk-free rate

---

> [!IMPORTANT]
> ### 🎯 Quick Exam-Day Pointers
>
> * The binomial model values an option using **no-arbitrage** principles. It assumes the underlying's price can only go to one of two known values in the next period.
> * **Method 1: Replication.** Create a risk-free portfolio by combining the underlying asset and the option. The key is calculating the **hedge ratio (h)**. The value of this risk-free portfolio, discounted at the risk-free rate, allows you to solve for the option's price.
> * **Method 2: Risk-Neutral Pricing.** This is a mathematical shortcut. You calculate special **risk-neutral probabilities** and use them to find the expected payoff of the option. Then, you discount that expected payoff at the **risk-free rate**.
> * Remember, "risk-neutral" doesn't describe investors; it's a technique that works *because* of the no-arbitrage principle. You're valuing the derivative in a hypothetical world where its expected return is the risk-free rate.