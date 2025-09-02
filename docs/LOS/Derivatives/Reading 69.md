## Module 69.1: Arbitrage, Replication, and Carrying Costs

This module introduces the core concepts that form the bedrock of derivative pricing: the idea that you can't get risk-free money for nothing (no-arbitrage) and that you can perfectly mimic a derivative's payoff using other assets (replication).

### Arbitrage and Replication in Pricing Derivatives (LOS 69.a)

The pricing of derivatives isn't based on guessing what the price of an asset will be in the future. Instead, it's based on a powerful concept called the **law of one price**, which states that two assets (or portfolios of assets) with the exact same future cash flows, regardless of what happens in the future, must sell for the same price today.

If they don't, an opportunity for **arbitrage** exists. Arbitrage is a set of transactions that generates a **risk-free profit** without any net investment of your own money. In efficient markets, these opportunities are rare and disappear almost instantly because traders exploit them. Derivative pricing models assume no arbitrage is possible.

**How does this work in practice? Through Replication.**

**Replication** means creating a portfolio of other assets (like the underlying stock and a risk-free bond) that has the exact same payoffs as the derivative you're trying to price. Since the replicating portfolio and the derivative have identical future payoffs, they must have the same price today.

**A Real-World Example (Indian Context):**

Let's price a 1-year forward contract on a share of Reliance Industries (RIL).
* Current Spot Price of RIL ($S_0$): ₹3,000
* 1-year risk-free interest rate ($R_f$): 7% (e.g., from a government T-bill)

What should the 1-year forward price, $F_0(T)$, be?

We can use replication to figure this out. Consider two portfolios:

1.  **Portfolio A (The Derivative Path):** A long forward contract on one RIL share and a risk-free bond that will be worth the forward price, $F_0(T)$, in one year.
    * **Cost today:** The forward contract costs nothing to enter. The bond costs the present value of the forward price, which is $\frac{F_0(T)}{(1 + 0.07)^1}$.
    * **Payoff in 1 year:** The bond matures to $F_0(T)$, which you use to buy the RIL share as per the forward contract. Your net payoff is the RIL share, worth $S_T$.

2.  **Portfolio B (The Cash Market Path):** Buy one RIL share today.
    * **Cost today:** ₹3,000 ($S_0$).
    * **Payoff in 1 year:** You are holding the RIL share, which will be worth $S_T$.

Since both portfolios have the exact same payoff in one year (one RIL share), their costs today must be equal to prevent arbitrage.

$$\frac{F_0(T)}{1.07} = S_0 = 3000$$

Solving for the no-arbitrage forward price:
$$F_0(T) = 3000 \times (1.07) = 3210$$

> **<mark>EXAM TIP:</mark>:** This is a cornerstone formula. For an underlying asset with no costs or benefits of holding, the no-arbitrage forward price is simply the spot price compounded at the risk-free rate.
> $$F_0(T) = S_0(1 + R_f)^T$$
> **Memorize this relationship.** It's built on the idea that you should be indifferent between buying the asset today and holding it, or agreeing to buy it in the future and investing the money risk-free in the meantime.

***

### Spot vs. Expected Future Price and the Cost of Carry (LOS 69.b)

A common mistake is to think the forward price is the market's "best guess" of the future spot price. **This is incorrect.**
* **Forward Price, $F_0(T)$:** A price determined by the no-arbitrage relationship. It's a calculated value based on the current spot price and the costs/benefits of holding the asset.
* **Expected Future Spot Price, $E(S_T)$:** The market's consensus forecast of what the asset's price will be at time T. This is based on fundamentals, supply/demand, and risk appetite.

These two prices are rarely equal. The difference is explained by the **Cost of Carry**.

The **Cost of Carry** (or carrying costs) is the net cost of holding an asset for a period. It includes:
* **Financing Costs (+):** The interest cost on the funds used to purchase the asset. This *increases* the forward price.
* **Storage Costs (+):** Costs to store and insure a physical asset (e.g., warehousing charges for wheat in a Punjab mandi or vault charges for gold in Mumbai). This also *increases* the forward price.
* **Benefits (-):** Any income or non-monetary benefit received from holding the asset. This *decreases* the forward price.
    * **Income:** Dividends from a stock (e.g., Infosys dividend) or coupon payments from a bond.
    * **Convenience Yield:** A non-monetary benefit of physically holding an asset, which isn't available to someone just holding a forward contract. For example, a jewellery manufacturer in Surat might hold a physical inventory of diamonds to avoid production shutdowns, even if it's costly. This benefit of having the physical asset on hand is the convenience yield. It's most relevant for commodities.

The general formula for the forward price incorporating the cost of carry is:

$$F_0(T) = [S_0 + PV_0(\text{Costs}) - PV_0(\text{Benefits})](1 + R_f)^T$$

**A Real-World Example with Dividends:**

Let's go back to our RIL example. Suppose RIL is expected to pay a dividend of ₹30 in six months.
* $S_0$ = ₹3,000
* $R_f$ = 7% per year
* Present Value of Dividend ($PV_0(\text{Benefit})$) = $\frac{30}{(1.07)^{0.5}} \approx 28.99$

Now, the no-arbitrage forward price is calculated on the spot price *minus* the present value of the dividend. Why? Because if you buy the share today to replicate the forward, you'll receive that dividend, which offsets part of your initial cost.

$$F_0(T) = (S_0 - PV_0(\text{Benefit})) \times (1 + R_f)^T$$
$$F_0(T) = (3000 - 28.99) \times (1.07)^1 = 2971.01 \times 1.07 \approx 3179$$

Notice the forward price is lower than the 3,210 we calculated earlier because the benefit of the dividend makes it cheaper to carry the asset.

> **<mark>EXAM TIP:</mark>:** Understand the intuition behind the cost of carry model. Don't just memorize the formula. **Costs of holding the asset increase the forward price, while benefits of holding it decrease the forward price.** This is a very testable concept. The exam might ask you to identify which factor would increase or decrease a forward price.

Excellent. Here are the final takeaways for Reading 69.

***

### Summary of Formulas for Reading 69

Here are the key formulas presented in this reading, which are essential for your exam preparation.

* **No-Arbitrage Forward Price (No Costs or Benefits):**
    This is the foundational formula for an underlying asset that has no dividends, storage costs, or other benefits.
    $$F_0(T) = S_0(1 + R_f)^T$$
    where:
    * $F_0(T)$ = Forward price at time 0 for a contract expiring at time T
    * $S_0$ = Spot price of the underlying asset at time 0
    * $R_f$ = Risk-free rate of interest
    * $T$ = Time to expiration of the contract

* **Cost of Carry Model (General Formula):**
    This formula adjusts the spot price for all costs and benefits associated with holding the underlying asset until the forward contract expires.
    $$F_0(T) = [S_0 + PV_0(\text{Costs}) - PV_0(\text{Benefits})](1 + R_f)^T$$
    where:
    * $PV_0(\text{Costs})$ = Present value of any costs (e.g., storage, insurance) at time 0
    * $PV_0(\text{Benefits})$ = Present value of any benefits (e.g., dividends, convenience yield) at time 0

* **Forward Price for a Dividend-Paying Stock:**
    A common application of the general model where the benefit is a dividend.
    $$F_0(T) = (S_0 - PV_0(\text{Dividends}))(1 + R_f)^T$$

* **Currency Forward Price (Interest Rate Parity):**
    This formula establishes the no-arbitrage relationship between spot and forward exchange rates based on the interest rates of the two currencies.
    $$F_{p/b} = S_{p/b} \times \frac{(1+i_p)^T}{(1+i_b)^T}$$
    where:
    * $F_{p/b}$ = Forward exchange rate (price currency per base currency)
    * $S_{p/b}$ = Spot exchange rate (price currency per base currency)
    * $i_p$ = Interest rate of the price currency (e.g., INR)
    * $i_b$ = Interest rate of the base currency (e.g., USD)

***

### ⚡ Quick Exam-Day Pointers

On exam day, keep these high-level concepts in mind for Reading 69.

* **No-Arbitrage is King:** All derivative pricing is built on the foundation of no-arbitrage. The correct price is the one that prevents a risk-free profit. For this reason, the **risk-free rate ($R_f$)** is the appropriate rate to use in pricing models, not an investor's required return.
* **Price vs. Value:** Do not confuse these! The **price** of a forward contract (the agreed-upon transaction price, $F_0(T)$) is set at the beginning. The **value** of the contract is what it's worth at any point in time. At initiation, the forward price is set so that the contract's **value is zero** to both parties.
* **Cost of Carry Intuition:** Don't just memorize the formula, understand the logic.
    * Anything that makes it **more expensive to hold the physical asset** (like storage costs) will **increase** the forward price.
    * Anything that provides a **benefit to holding the physical asset** (like dividends or convenience yield) will **decrease** the forward price.
* **Replicate to Price:** The core of no-arbitrage pricing is replication. A long forward position can be perfectly replicated by buying the underlying asset today and borrowing the money to do so at the risk-free rate.
* **Forward Price $\neq$ Future Spot Price:** The forward price is not a forecast. It's a mathematically derived price based on today's spot price and the cost of carry. The market's expectation of the future spot price can be higher, lower, or the same as the forward price.