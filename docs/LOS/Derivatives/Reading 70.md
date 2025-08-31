### Module 70.1: Forward Contract Valuation

This module explains the critical difference between a forward contract's **price** and its **value**, and shows how to calculate its value at any point in time. It also applies these forward concepts to interest rates.

#### Pricing and Valuing a Forward Contract (LOS 70.a)

It's crucial to distinguish between the forward **price** and the forward **value**.
* **Forward Price ($F_0(T)$):** The agreed-upon price for the future transaction. This is determined at the start of the contract and **remains fixed** throughout the contract's life.
* **Forward Value ($V_t(T)$):** The market value of the forward contract itself at any time 't' before expiration. This value **fluctuates** as the spot price of the underlying asset changes.

Here's how the value changes over time:

**1. At Initiation (Time 0)**
The forward price is set such that the contract has a **value of zero** to both the long and short positions. Neither party pays the other to enter the agreement.

**2. During the Life of the Contract (Time t)**
As time passes and the spot price ($S_t$) of the underlying moves, the contract will gain or lose value. To find the value to the long position at any time 't', you simply compare the current spot price to the present value of the locked-in forward price.
$$V_t(T) = S_t - \frac{F_0(T)}{(1+R_f)^{(T-t)}}$$
* **Intuition:** The formula calculates what your position is worth *right now*. It's the gain you'd get from owning the asset today ($S_t$) minus the obligation you have to pay the forward price in the future, discounted back to today.

**3. At Expiration (Time T)**
At the moment of expiration, there is no more time value. The value of the contract is simply the difference between the final spot price and the locked-in forward price.
$$V_T(T) = S_T - F_0(T)$$

* **Real-World Example (Indian Context):**
    * You enter a 6-month forward contract to buy one share of TCS at a forward price ($F_0(T)$) of ₹3,900. At initiation, the value is ₹0.
    * Three months later (t=0.25 years, T-t=0.25 years), the spot price of TCS ($S_t$) has risen to ₹4,000. Let's say the risk-free rate is 6%.
    * The value of your long position is now:
        $V_t(T) = ₹4,000 - \frac{₹3,900}{(1.06)^{(0.25)}} \approx ₹4,000 - ₹3,843 = +₹57$.
    * You have an unrealized gain of ₹57 because the asset is now worth more than your discounted obligation.

> **<mark>EXAM TIP:</mark>:** Calculating the value of a forward contract *during its life* is a very common exam question. Memorize the formula $V_t(T) = S_t - PV(F_0(T))$ and understand its logic.

---

#### Forward Interest Rates & FRAs (LOS 70.b)

**Forward Interest Rates**
A **forward rate** is an interest rate for a future period that is implied by the current spot rates for different maturities, 3122]. The market determines these rates through no-arbitrage.

* **Notation:** The notation `XyYy` means the "Y-year forward rate, X years from now." For example, `2y1y` is the 1-year interest rate that will begin in 2 years -3119].
* **Derivation:** Forward rates are derived from spot rates. The key idea is that investing for 3 years at the 3-year spot rate ($S_3$) should give the same return as investing for 2 years at the 2-year spot rate ($S_2$) and then reinvesting for one more year at the implied forward rate (`2y1y`).
    $$(1+S_3)^3 = (1+S_2)^2 \times (1 + 2y1y)$$

**Forward Rate Agreements (FRAs)**
An FRA is a derivative contract used to lock in a future interest rate. It's a forward contract where the underlying is an interest payment.

* **Use Case:** An FRA is perfect for a corporation that plans to borrow or lend money in the future and wants to hedge against interest rate changes.
* **Example (Indian Context):** Suppose Adani Group plans to take out a large 90-day loan in 30 days. They are worried the RBI might raise interest rates. They can enter into an FRA today to lock in the interest rate on that future loan. If rates rise, the FRA will pay them the difference, offsetting their higher borrowing cost.
* **Settlement:** FRAs are cash-settled based on a notional principal. The payment is the difference between the locked-in forward rate and the actual market rate at settlement.

***

### Summary of Formulas for Reading 70

This reading is all about the mechanics of valuing a forward contract over time and understanding forward interest rates.

* **Value of a Forward Contract at Initiation (Time 0):**
    The price is set so the value is zero.
    $$V_0(T) = 0$$

* **Value of a Forward Contract During its Life (at time 't' to the Long position):**
    This is the most important valuation formula in this reading.
    $$V_t(T) = S_t - \frac{F_0(T)}{(1 + R_f)^{(T-t)}}$$
    where:
    * $V_t(T)$ = Value of the contract at time t
    * $S_t$ = Spot price of the underlying at time t
    * $F_0(T)$ = The original, fixed forward price
    * $R_f$ = Risk-free rate
    * $(T-t)$ = Time remaining until expiration

* **Value of a Forward Contract at Expiration (at time T to the Long position):**
    $$V_T(T) = S_T - F_0(T)$$

* **Implied Forward Interest Rate (from Spot Rates):**
    This formula shows the no-arbitrage relationship. The example below is for the 1-year rate, one year from now (`1y1y`).
    $$(1 + 1y1y) = \frac{(1+S_2)^2}{(1+S_1)}$$

***

### ⚡ Quick Exam-Day Pointers

For Reading 70, expect calculation questions on valuing a forward contract mid-life and deriving forward rates.

* **Price is Fixed, Value Fluctuates!** 📌 This is the single most important concept. The forward **price** ($F_0(T)$) is locked in at the start. The **value** ($V_t(T)$) starts at zero and then changes every day as the spot price of the underlying moves.

* **Mid-Life Valuation is Key:** The most likely calculation question will be: "What is the value of this forward contract X months after initiation?"
    * **Think:** It's what I have **now** ($S_t$) minus what I owe **later** (the PV of $F_0(T)$).
    * Don't forget to use the **time remaining** in the contract for discounting, not the original time to maturity.

* **Forward Rates are Implied, Not Guessed:** 🔍 Forward interest rates aren't forecasts. They are the rates required to prevent arbitrage between different maturity spot rates. Be comfortable calculating a simple implied forward rate like `1y1y` from the 1-year and 2-year spot rates.

* **FRAs = Hedging Interest Rates:** Remember the primary use of a **Forward Rate Agreement (FRA)** is to lock in a future borrowing or lending rate, removing uncertainty about future interest rate movements.

