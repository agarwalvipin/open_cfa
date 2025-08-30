### Module 73.1: Option Valuation

This module breaks down an option's price into its core components and examines the factors that drive its value up or down.

#### Exercise Value, Moneyness, and Time Value (LOS 73.a)

An option's premium (its price) is made up of two distinct parts: exercise value and time value.

**1. Moneyness 🤑**
This term simply describes whether the option would be profitable if you exercised it right now.
* **In-the-Money (ITM):** Has a positive payoff if exercised.
    * Call Option: Spot Price > Exercise Price ($S > X$)
    * Put Option: Exercise Price > Spot Price ($X > S$)
* **Out-of-the-Money (OTM):** Would result in a loss if exercised (so you wouldn't).
    * Call Option: Spot Price < Exercise Price ($S < X$)
    * Put Option: Exercise Price < Spot Price ($X < S$)
* **At-the-Money (ATM):** Spot Price = Exercise Price ($S = X$).

**2. Exercise Value (or Intrinsic Value) 💎**
This is the value of the option if it were exercised today. It's the amount by which an option is in-the-money.
* **Key Rule:** Exercise value **cannot be negative**. If an option is at-the-money or out-of-the-money, its exercise value is **zero**.
* **Call Exercise Value:** $Max(0, S - X)$ 
* **Put Exercise Value:** $Max(0, X - S)$ 

**3. Time Value (or Speculative Value) ⏳**
This is the extra amount you pay for an option above its exercise value. It represents the "hope" or possibility that the option will become more profitable before it expires.
* **Formula:** Option Premium = Exercise Value + Time Value 
* **Key Rule:** At the moment of expiration, there is no time left, so the **time value is zero**. The option's price becomes equal to its exercise value. 

> **CFA Exam Tip:** You will almost certainly be asked to do these simple calculations. Given S, X, and the option premium, you should be able to instantly state the moneyness, the exercise value, and the time value.

---

#### Arbitrage and Replication in Option Pricing (LOS 73.b)

Pricing options is different from pricing forward commitments.
* **Forward Commitments:** Have symmetric payoffs, and we use replication to create a portfolio whose value at initiation is zero.
* **Contingent Claims (Options):** Have asymmetric (one-sided) payoffs. Their value at initiation is the premium, which is not zero. We can't use the simple forward pricing model. Instead, we use arbitrage principles to establish **price boundaries** (upper and lower limits) for what an option can be worth. For example, a call option can never be worth more than the stock itself. -3224]

---

#### Factors That Determine Option Value (LOS 73.c)

This is a critical, highly testable topic. Six factors influence an option's premium.

| Factor | Change in Factor | Impact on Call Value 📈 | Impact on Put Value 📉 | Reason |
| :--- | :--- | :--- | :--- | :--- |
| **1. Spot Price ($S_0$)** | Increase | ⬆️ | ⬇️ | Calls benefit from higher prices; puts benefit from lower prices. |
| **2. Exercise Price (X)** | Increase | ⬇️ | ⬆️ | A higher strike makes a call harder to profit from and a put easier to profit from. |
| **3. Time to Expiration (T)**| Increase | ⬆️ | ⬆️* | More time gives the price more opportunity to move favorably. *(Usually true for puts)* |
| **4. Risk-Free Rate ($R_f$)**| Increase | ⬆️ | ⬇️ | A higher rate lowers the PV of the exercise price you pay (good for calls) or receive (bad for puts). |
| **5. Volatility ($\sigma$)** | Increase | ⬆️ | ⬆️ | **Volatility is good for option buyers!** It increases the chance of a large price move, boosting potential profit while the loss is still capped at the premium. |
| **6. Holding Benefits** | Increase | ⬇️ | ⬆️ | Benefits like dividends cause the stock price to drop, which hurts calls and helps puts. |

> **CFA Exam Tip:** Memorize this table! A common question is, "All else being equal, which of the following will most likely increase the value of a European put option?" You need to be able to identify the correct factor and relationship instantly.

***

### Summary of Formulas & Key Relationships for Reading 73

This reading is about breaking down an option's price. The relationships are more important than complex formulas.

* **The Components of an Option's Price:**
    `Option Premium = Exercise Value + Time Value` 

* **Exercise (Intrinsic) Value Calculations:**
    * **Call Option:** `Exercise Value = Max(0, Spot Price - Exercise Price)` or `Max(0, S - X)` 
    * **Put Option:** `Exercise Value = Max(0, Exercise Price - Spot Price)` or `Max(0, X - S)` 

* **Factors Influencing Option Prices:**

| Factor | Change in Factor | Impact on Call Value 📈 | Impact on Put Value 📉 |
| :--- | :--- | :--- | :--- |
| **Spot Price (S)** | Increase | ⬆️  | ⬇️  |
| **Exercise Price (X)** | Increase | ⬇️  | ⬆️  |
| **Time to Expiration (T)**| Increase | ⬆️  | ⬆️ (Usually)  |
| **Risk-Free Rate (Rf)**| Increase | ⬆️ | ⬇️ |
| **Volatility (σ)** | Increase | ⬆️ | ⬆️ |
| **Holding Benefits** | Increase | ⬇️ | ⬆️ |

***

### ⚡ Quick Exam-Day Pointers

For Reading 73, expect questions that test both simple calculations and your understanding of what drives option prices.

* **Master the Three Values:** Be ready for a question that gives you an option's premium and the spot/exercise prices and asks for the **time value**.
    1.  First, calculate the **exercise value** (`Max(0, S-X)` or `Max(0, X-S)`).
    2.  Then, calculate **time value** = Premium - Exercise Value.

* **Volatility is Good for Buyers!** ❤️‍🔥 This is a huge takeaway. Higher volatility increases the value of **both calls and puts**. Why? It increases the potential for a large profitable move, while the maximum loss for the buyer is still just the premium paid.

* **Time is Money (and it's Decaying):** ⏳ An option's time value erodes as it gets closer to expiration. On expiration day, **time value is zero**. This erosion of value is known as "time decay."

* **Know the 6 Factors:** Be prepared for qualitative questions based on the table above. A classic question is "Which of the following will *decrease* the value of a call option?" You need to know the relationships by heart.
