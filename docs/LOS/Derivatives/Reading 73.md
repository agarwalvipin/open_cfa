### <span style="color: #1565C0;">Part 1: Option Valuation (LOS 73.a)</span>

This module dives into the fundamental building blocks of an option's price and the key factors that influence its value.

#### <span style="color: #6A1B9A;">1.1 Exercise Value, Moneyness, and Time Value</span>

An option's price, or **premium**, isn't just a random number; it's composed of two distinct parts: its **exercise value** and its **time value**. To understand these, we first need to grasp the concept of **moneyness**.

##### <span style="color: #E65100;">1.1.1 Moneyness: Is Your Option a Winner Right Now? 🏆</span>

**Moneyness** tells you whether exercising your option *right now* would result in a positive payoff. An option can be in one of three states:

* **In-the-Money (ITM):** Exercising the option would be profitable (ignoring the premium paid).
* **At-the-Money (ATM):** The underlying asset's price is equal to the exercise price. No profit or loss on exercise.
* **Out-of-the-Money (OTM):** Exercising the option would result in a loss. You wouldn't do it!

Here’s a simple breakdown where S = Stock Price and X = Exercise Price:

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

```mermaid
graph TD
    subgraph Call Option -Right to Buy
        A[S > X] --> B(In-the-Money)
        C[S = X] --> D(At-the-Money)
        E[S < X] --> F(Out-of-the-Money)
    end
    subgraph Put Option -Right to Sell
        G[S < X] --> H(In-the-Money)
        I[S = X] --> J(At-the-Money)
        K[S > X] --> L(Out-of-the-Money)
    end
```

</div>

#### <span style="color: #00838F;">1.2 Indian Context Example 🌍</span>

Imagine you have a call option on Reliance Industries (RIL) with an **exercise price (X)** of ₹3,000.

* If RIL is currently trading at **S = ₹3,100**, your call option is **₹100 in-the-money**.
* If RIL is trading at **S = ₹2,950**, your call option is **₹50 out-of-the-money**.
* If RIL is trading at **S = ₹3,000**, your call option is **at-the-money**.

##### <span style="color: #E65100;">1.1.2 Exercise Value (Intrinsic Value)</span>

This is the value an option would have if it were exercised immediately. It's simply the amount by which an option is in-the-money. **Crucially, the exercise value can never be negative**—if an option is OTM, its exercise value is zero because you would simply not exercise it.

* **Call Exercise Value:** 
  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
  $$\text{Call Exercise Value} = \max(0, S - X)$$
  </div>
* **Put Exercise Value:** 
  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
  $$\text{Put Exercise Value} = \max(0, X - S)$$
  </div>

##### <span style="color: #E65100;">1.1.3 Time Value</span>

Why would anyone pay for an OTM option that has an exercise value of zero? The answer is **time value**. This is the portion of the option premium that reflects the possibility that the option's value will increase before it expires. It's essentially the "hope" value.

The formula that ties everything together is:

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
$$\text{Option Premium} = \text{Exercise Value} + \text{Time Value}$$
</div>

At expiration, there is no time left, so the **time value is zero**. The option's price becomes equal to its exercise value.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
💡 CFA Exam Tip ✍️:For the CFA Level 1 exam, you must be able to instantly identify an option's moneyness and calculate its exercise value and time value from its premium. This is a foundational concept that gets tested frequently.
</div>
</div>

-----

### <span style="color: #1565C0;">Part 2: Arbitrage & Replication in Pricing (LOS 73.b)</span>

While both **forward commitments** (like forwards and futures) and **contingent claims** (like options) are priced using **no-arbitrage** principles, the application is different.

* **Forward Commitments:** These are priced so that their **value at initiation is zero** for both parties. The pricing is based on replicating the payoff by buying the underlying asset and financing it at the risk-free rate (the cost of carry).
* **Contingent Claims (Options):** Options have a **positive value at initiation**, which is the premium paid by the buyer. Their payoffs are one-sided (e.g., a call option buyer can't lose more than the premium). Because of this asymmetry, simple cost-of-carry replication doesn't work. Instead, we use no-arbitrage rules to establish **price boundaries** (upper and lower limits) for option values.

#### <span style="color: #6A1B9A;">2.1 Option Price Boundaries</span>

These boundaries define the "rules" for option prices. If an option's price falls outside these boundaries, a risk-free arbitrage profit is possible.

| Option Type | Lower Bound (Minimum Value) | Upper Bound (Maximum Value) |
| :--- | :--- | :--- |
| **European Call** | <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">$$c_0 \ge \max[0, S_0 - X(1 + R_f)^{-T}]$$</div> | <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">$$c_0 \le S_0$$</div> |
| **European Put** | <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">$$p_0 \ge \max[0, X(1 + R_f)^{-T} - S_0]$$</div> | <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">$$p_0 \le X(1 + R_f)^{-T}$$</div> |

* **Key Intuition:**
  * A call option gives you the right to buy the stock, so its value can **never exceed the stock's price itself**.
  * A put option gives you the right to sell a stock for price X. Even if the stock price drops to zero, the most you can get is X, and you only get it at expiration. So, its value can **never exceed the present value of the exercise price**.
  * The lower bounds ensure that the option is worth at least its exercise value, after accounting for the time value of money on the exercise price.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
💡 CFA Exam Tip ✍️:You are unlikely to be asked to derive these bounds on the exam. However, you should **memorize the formulas for the bounds** and understand the logic behind them. A common question might test whether you can identify if an option is mispriced based on these rules.
</div>
</div>

-----

### <span style="color: #1565C0;">Part 3: Factors Affecting Option Value (LOS 73.c)</span>

Six primary factors influence the price of an option. Understanding their impact is absolutely critical.

| Factor | Change | Impact on Call Value | Impact on Put Value | Why? |
| :--- | :--- | :--- | :--- | :--- |
| **Underlying Price ($S_0$)** | ⬆️ | ⬆️ Increase | ⬇️ Decrease | A higher stock price makes the right to **buy** (call) more valuable and the right to **sell** (put) less valuable. |
| **Exercise Price ($X$)** | ⬆️ | ⬇️ Decrease | ⬆️ Increase | A higher exercise price makes it harder for a call to be ITM (less valuable) but easier for a put to be ITM (more valuable). |
| **Time to Expiration ($T$)** | ⬆️ | ⬆️ Increase | ⬆️ Increase\* | More time provides more opportunity for favorable price moves. (\*There's a rare exception for deep ITM European puts). |
| **Volatility ($\sigma$)** | ⬆️ | ⬆️ Increase | ⬆️ Increase | **Crucial!** Higher volatility increases the chance of extreme price moves. This is good for both calls and puts because payoffs are unlimited/large on one side and losses are capped at the premium. |
| **Risk-Free Rate ($R_f$)** | ⬆️ | ⬆️ Increase | ⬇️ Decrease | A higher risk-free rate lowers the present value of the future exercise price. This is good for a call (you pay less in today's money) and bad for a put (you receive less in today's money). |
| **Carrying Costs/Benefits** (e.g., Dividends) | ⬆️ (e.g., higher dividend) | ⬇️ Decrease | ⬆️ Increase | A stock's price is expected to drop by the dividend amount, which hurts the call's value but helps the put's value. |

#### <span style="color: #00838F;">3.1 Indian Context Example (Volatility) 🌍</span>

Think about options on Infosys (INFY) versus options on Adani Enterprises (ADANIENT). Historically, Adani stocks have shown higher volatility. Therefore, all else being equal, an option on ADANIENT would be more expensive than a similar option on INFY because there's a greater perceived chance of a large price swing.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
💡 CFA Exam Tip ✍️:This table is pure gold for the exam. Questions asking "what happens to a call/put value if X increases?" are extremely common. Memorize this table and the logic behind each relationship. The effect of volatility is a particularly important and frequently tested concept.
</div>
</div>

-----

### <span style="color: #1565C0;">🧪 Formula Summary (LOS 73)</span>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Call Exercise Value:**

$$\max(0, S - X)$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Put Exercise Value:**

$$\max(0, X - S)$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Option Premium:**

$$\text{Option Premium} = \text{Exercise Value} + \text{Time Value}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Lower Bound (European Call):**

$$c_0 \ge \max[0, S_0 - X(1 + R_f)^{-T}]$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Upper Bound (European Call):**

$$c_0 \le S_0$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Lower Bound (European Put):**

$$p_0 \ge \max[0, X(1 + R_f)^{-T} - S_0]$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Upper Bound (European Put):**

$$p_0 \le X(1 + R_f)^{-T}$$

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">
### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* **Moneyness is from the buyer's perspective.**
  * ✅ A call is ITM if $S > X$
  * ✅ A put is ITM if $S < X$
* **Option's premium = intrinsic value (exercise value) + time value.**
  * At expiration, time value is **ZERO**.
* **Volatility is good for options!**
  * Higher volatility increases the value of *both* calls and puts because it increases the probability of a large payoff.
  * Your loss is always capped at the premium.
* **Interest rates and calls move together.**
  * ⬆️ Higher $R_f$ → ⬆️ higher call value.
* **Interest rates and puts move opposite.**
  * ⬆️ Higher $R_f$ → ⬇️ lower put value.
* **Remember the price bounds.**
  * An option's price can't be just anything; it must live within its no-arbitrage boundaries.

</div>
</div>