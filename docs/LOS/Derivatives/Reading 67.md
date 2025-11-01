## <span style="color: #1565C0;">Reading 67: Forward Commitment and Contingent Claim Features and Instruments 📜</span>

### <span style="color: #1565C0;">🎯 Introduction</span>

Welcome, aspiring charterholder! This reading is your dojo for mastering the fundamental weapons of finance: **derivatives**. These instruments derive their value from an underlying asset (stock, bond, or interest rate).

In this session we'll distinguish between the two families: **Forward Commitments** (obligations) and **Contingent Claims** (rights). Understand definitions and option profit/loss calculations.

Let's begin!

-----

### <span style="color: #1565C0;">Part 1: The Two Great Derivative Families (LOS 67.a & 67.c)</span>

Every derivative falls into one of two categories. This is the most critical distinction to learn.

#### <span style="color: #6A1B9A;">1.1 Family 1: Forward Commitments (The Obligations)</span>

* **Forward Commitments (LOS 67.c):** A binding agreement where two parties **obligate** themselves to transact in the future at a pre-agreed price. Includes forwards, futures, and swaps.

* **Forward Contracts:**
  * **What it is:** A private, customizable agreement to buy/sell an asset at the **forward price** on a specified settlement date.
  * **Buyer (Long):** Obligated to buy; profits if market price > contract price at expiration.
  * **Seller (Short):** Obligated to sell; profits if market price < contract price at expiration.
  * **Key Features:** OTC, customizable, higher **counterparty risk**.

* **Futures Contracts:**
  * **What it is:** A **standardized** forward contract traded on an exchange.
  * **Exchange-Clearinghouse:** Clearinghouse becomes the counterparty, reducing counterparty risk.
  * **Key Features:**
    * **Daily Mark-to-Market (MTM):** Gains/losses settled daily.
    * **Margin Requirements:** Initial and maintenance margins; margin calls if balance falls below maintenance.

* **Swaps:**
  * **What it is:** Exchange of a *series* of cash flows over time (e.g., interest rate swap: fixed vs floating).
  * **Analogy:** A bundle of forward contracts.
  * **Key Feature:** Payments are typically **netted** on each payment date.

#### <span style="color: #6A1B9A;">1.2 Family 2: Contingent Claims (The Rights)</span>

* **Contingent Claims (LOS 67.c):** Payoff depends on a future event. Buyer has a **right**, seller an **obligation**.

* **Options:**
  * **What it is:** Buyer has the right, but not the obligation, to buy or sell at the **strike (X)** by expiration.
  * **Premium:** Buyer pays the option premium; seller (writer) receives it and is obligated if exercised.
  * **Call:** Right to buy (bullish). Call buyer bullish.
  * **Put:** Right to sell (bearish).

* **Credit Derivatives:**
  * **What it is:** Payoff contingent on a **credit event** (e.g., default).
  * **Example:** Credit Default Swap (CDS) — buyer pays premium; seller compensates if default occurs.

-----

### <span style="color: #1565C0;">Part 2: Option Payoffs & Profits at Expiration (LOS 67.b)</span>

This is an exam-core concept: calculate profit/loss for the four basic option positions.

**Key Terms:**

* $S_T$ = Spot price at expiration
* $X$ = Exercise (strike) price
* $c_0$ = Call premium
* $p_0$ = Put premium

**The Two-Step Process:**

1. **Find the Value at Expiration:** Option value = $\max(0, \dots)$.
2. **Find the Profit:** $\text{Profit} = \text{Value at Expiration} - \text{Premium}$.

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\text{Call value at expiration} = \max(0, S_T - X)$$

$$\text{Put value at expiration} = \max(0, X - S_T)$$

$$\text{Profit} = \text{Value at Expiration} - \text{Premium}$$

</div>

#### <span style="color: #6A1B9A;">2.1 Call Options (You're Bullish!) 🐂</span>

* **Long Call (Buyer):**

  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

  **Value at Expiration:**

  $$\text{Value} = \max(0, S_T - X)$$

  **Profit:**

  $$\text{Profit} = \max(0, S_T - X) - c_0$$

  **Breakeven:**

  $$S_T = X + c_0$$

  </div>

  * **Max Loss:** Limited to premium paid ($-c_0$).
  * **Max Profit:** Unlimited (as $S_T$ can rise).

* **Short Call (Seller/Writer):**

  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

  **Profit:**

  $$\text{Profit} = c_0 - \max(0, S_T - X)$$

  **Breakeven:**

  $$S_T = X + c_0$$

  </div>

  * **Max Profit:** Premium received ($+c_0$).
  * **Max Loss:** Unlimited.

#### <span style="color: #6A1B9A;">2.2 Put Options (You're Bearish!) 🐻</span>

* **Long Put (Buyer):**

  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

  **Value at Expiration:**

  $$\text{Value} = \max(0, X - S_T)$$

  **Profit:**

  $$\text{Profit} = \max(0, X - S_T) - p_0$$

  **Breakeven:**

  $$S_T = X - p_0$$

  </div>

  * **Max Loss:** Limited to premium paid ($-p_0$).
  * **Max Profit:** $X - p_0$ (if $S_T$ falls to 0).

* **Short Put (Seller/Writer):**

  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

  **Profit:**

  $$\text{Profit} = p_0 - \max(0, X - S_T)$$

  **Breakeven:**

  $$S_T = X - p_0$$

  </div>

  * **Max Profit:** Premium received ($+p_0$).
  * **Max Loss:** $X - p_0$ (if $S_T$ falls to 0).

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 Samurai's Dojo: Option Profit Example**

Let's use the text's example:

* **Call Option:** $X = \$40$, Premium $c_0 = \$3$.
* **Put Option:** $X = \$35$, Premium $p_0 = \$0.75$.

**Scenario 1: $S_T = \$30$**

* **Long Call Profit:** $\max(0,30-40)-3 = -\$3.00$.
* **Short Call Profit:** $+3 - \max(0,30-40) = +\$3.00$.
* **Long Put Profit:** $\max(0,35-30)-0.75 = +\$4.25$.
* **Short Put Profit:** $+0.75 - \max(0,35-30) = -\$4.25$.

**Scenario 2: $S_T = \$43$**

* **Long Call Profit:** $\max(0,43-40)-3 = \$0.00$ (breakeven).
* **Short Call Profit:** $+3 - \max(0,43-40) = \$0.00$ (breakeven).
* **Long Put Profit:** $\max(0,35-43)-0.75 = -\$0.75$.
* **Short Put Profit:** $+0.75 - \max(0,35-43) = +\$0.75$.

</div>
</div>

-----

### <span style="color: #1565C0;">🧪 Formula Summary</span>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Call Value at Expiration:**

$$\text{Value} = \max(0, S_T - X)$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Put Value at Expiration:**

$$\text{Value} = \max(0, X - S_T)$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Long Call Profit:**

$$\text{Profit} = \max(0, S_T - X) - c_0$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Short Call Profit:**

$$\text{Profit} = c_0 - \max(0, S_T - X)$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Long Put Profit:**

$$\text{Profit} = \max(0, X - S_T) - p_0$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Short Put Profit:**

$$\text{Profit} = p_0 - \max(0, X - S_T)$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Breakevens:**

$$\text{Call breakeven: } S_T = X + c_0$$

$$\text{Put breakeven: } S_T = X - p_0$$

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* **Commitment vs. Claim:** Commitments (Forwards, Futures, Swaps) = *obligations*; Claims (Options, CDS) = *rights* for buyers and *obligations* for sellers.
* **Futures vs. Forwards:** Futures = standardized, exchange-traded, daily MTM, clearinghouse; Forwards = OTC, settle at expiration, counterparty risk.
* **Option Profit Formula:** Value = $\max(0,\dots)$; Profit = Value - Premium.
* **Breakeven Mnemonics:** "Call Up": $X + c_0$; "Put Down": $X - p_0$.
* **Risk Profiles:** Long Call = unlimited profit; Short Call = unlimited loss; Long options = loss limited to premium; Short options = profit limited to premium.

</div>
</div>