Here is a detailed summary of Reading 67, crafted in the style you requested.

## Reading 67: Forward Commitment and Contingent Claim Features and Instruments 📜

### 🎯 Introduction

Welcome, aspiring charterholder\! This reading is your dojo for mastering the fundamental weapons of finance: **derivatives**. These instruments don't have value on their own; they *derive* their value from an underlying asset (like a stock, bond, or interest rate).

In this session, we'll learn to distinguish between the two great families: **Forward Commitments** (the *obligations*) and **Contingent Claims** (the *rights*). Understanding this core division is the first step to becoming a true derivatives master. You must know what these instruments are and, for options, how to calculate their profit or loss.

Let's begin\!

-----

### <span style="color: \#1565C0;">Part 1: The Two Great Derivative Families (LOS 67.a & 67.c)</span>

Every derivative falls into one of two categories. This is the most critical distinction to learn.

  * **Forward Commitments (LOS 67.c):** A binding agreement where two parties **obligate** themselves to transact in the future at a pre-agreed price. Both sides are locked in. This family includes forwards, futures, and swaps.
  * **Contingent Claims (LOS 67.c):** An "if-then" derivative. The payoff **depends** (is contingent) on a future event. One party (the buyer) has a **right**, while the other party (the seller) has an **obligation**. This family includes options and credit derivatives.

#### <span style="color: \#6A1B9A;">1.1 Family 1: Forward Commitments (The Obligations)</span>

  * **Forward Contracts:**

      * **What it is:** A private, custom agreement between two parties to buy or sell an asset at a specified price (the **forward price**) on a future date (the **settlement date**).
      * **Buyer (Long):** *Obligated* to buy the asset. Profits if the asset's market price is *above* the contract price at expiration.
      * **Seller (Short):** *Obligated* to sell the asset. Profits if the asset's market price is *below* the contract price at expiration.
      * **Key Features:** Traded "Over-the-Counter" (OTC), completely customizable, and has high **counterparty risk** (the risk that the other side fails to perform).

  * **Futures Contracts:**

      * **What it is:** A **standardized** forward contract that trades on a formal exchange.
      * **Standardized:** The exchange dictates the asset, quantity, and expiration dates.
      * **Exchange-Traded:** This is the key difference\! An exchange **clearinghouse** acts as the counterparty to *every* trade.
      * **Result:** Counterparty risk is virtually eliminated.
      * **Key Features:**
        1.  **Daily Mark-to-Market (MTM):** Gains and losses are settled in cash *every single day*.
        2.  **Margin:** Participants must post a deposit called **initial margin**. Your account balance must stay above a **maintenance margin**. If it falls below, you get a "margin call" and must add funds to bring the balance *back up to the initial margin amount*.

  * **Swaps:**

      * **What it is:** An agreement to exchange a *series* of cash flows (payments) on *multiple* settlement dates over a specified time.
      * **Analogy:** Think of a swap as a bundle of forward contracts strung together.
      * **Most Common Type:** An **interest rate swap**, where one party pays a fixed interest rate and the other pays a floating (variable) interest rate.
      * **Key Feature:** The payments are typically **netted**. At each payment date, only one party—the one who owes more—makes a net payment to the other.

#### <span style="color: \#6A1B9A;">1.2 Family 2: Contingent Claims (The Rights)</span>

  * **Options:**

      * **What it is:** A contract giving the **buyer** the **right**, *but not the obligation*, to buy or sell an underlying asset at a specified price (the **exercise** or **strike price**).
      * The buyer pays a price, the **option premium**, for this right.
      * The **seller (writer)** receives the premium and is *obligated* to perform if the buyer exercises their right.
      * **Call Option:** The **right to buy**. (Mnemonic: You "call" the asset *to* you). You're bullish.
      * **Put Option:** The **right to sell**. (Mnemonic: You "put" the asset *onto* someone). You're bearish.

  * **Credit Derivatives:**

      * **What it is:** A derivative where the payoff is contingent on a specific **credit event**, such as a company defaulting on its bonds.
      * **Example: Credit Default Swap (CDS).** This is essentially insurance on a bond. The CDS "buyer" pays a regular premium. The CDS "seller" receives the premium and agrees to pay the "buyer" if the bond defaults.

-----

### <span style="color: \#1565C0;">Part 2: Option Payoffs & Profits at Expiration (LOS 67.b)</span>

This is a guaranteed exam-level concept. You *must* know how to calculate the profit and loss for all four option positions.

**Key Terms:**

  * $S_T$ = Spot Price of the underlying asset at expiration
  * $X$ = Exercise (Strike) Price
  * $c_0$ = Call Premium (the price the call buyer *pays*)
  * $p_0$ = Put Premium (the price the put buyer *pays*)

**The Two-Step Process:**

1.  **Find the Value at Expiration:** What is the option worth on its last day? It's $\max(0, \dots)$ because you would never exercise an option to lose money.
2.  **Find the Profit:** $\text{Profit} = \text{Value at Expiration} - \text{Initial Cost (Premium)}$.

#### <span style="color: \#6A1B9A;">2.1 Call Options (You're Bullish\!) 🐂</span>

  * **Long Call (Buyer):** You *bought* the right to *buy* at $X$.

      * **Value at Expiration:** $$\text{Value} = \max(0, S_T - X)$$
      * **Profit:** $$\text{Profit} = \max(0, S_T - X) - c_0$$
      * **Max Loss:** The premium you paid ($-c_0$).
      * **Max Profit:** Unlimited (as $S_T$ can rise forever).
      * **Breakeven:** $$S_T = X + c_0$$

  * **Short Call (Seller/Writer):** You *sold* the right to *buy* at $X$.

      * **Profit:** $$\text{Profit} = c_0 - \max(0, S_T - X)$$
      * **Max Profit:** The premium you received ($+c_0$).
      * **Max Loss:** Unlimited (a *very* risky position\!).
      * **Breakeven:** $$S_T = X + c_0$$

#### <span style="color: \#6A1B9A;">2.2 Put Options (You're Bearish\!) 🐻</span>

  * **Long Put (Buyer):** You *bought* the right to *sell* at $X$.

      * **Value at Expiration:** $$\text{Value} = \max(0, X - S_T)$$
      * **Profit:** $$\text{Profit} = \max(0, X - S_T) - p_0$$
      * **Max Loss:** The premium you paid ($-p_0$).
      * **Max Profit:** $X - p_0$ (if $S_T$ falls to 0).
      * **Breakeven:** $$S_T = X - p_0$$

  * **Short Put (Seller/Writer):** You *sold* the right to *sell* at $X$.

      * **Profit:** $$\text{Profit} = p_0 - \max(0, X - S_T)$$
      * **Max Profit:** The premium you received ($+p_0$).
      * **Max Loss:** $X - p_0$ (if $S_T$ falls to 0).
      * **Breakeven:** $$S_T = X - p_0$$

<div style="background-color: \#E3F2FD; border-left: 5px solid \#1976D2; padding: 12px; margin: 15px 0;">
<div style="color: \#000000; font-weight: 500;">

**💡 Samurai's Dojo: Option Profit Example**

Let's use the text's example:

  * **Call Option:** $X = \$40$, Premium $c_0 = \$3$.
  * **Put Option:** $X = \$35$, Premium $p_0 = \$0.75$.

**Scenario 1: Stock Price at Expiration $S_T = \$30$**

  * **Long Call Profit:** $\max(0, 30 - 40) - 3 = 0 - 3 = -\$3.00$ (Max Loss).
  * **Short Call Profit:** $+3 - \max(0, 30 - 40) = +3 - 0 = +\$3.00$ (Max Profit).
  * **Long Put Profit:** $\max(0, 35 - 30) - 0.75 = 5 - 0.75 = +\$4.25$.
  * **Short Put Profit:** $+0.75 - \max(0, 35 - 30) = +0.75 - 5 = -\$4.25$.

**Scenario 2: Stock Price at Expiration $S_T = \$43$**

  * **Long Call Profit:** $\max(0, 43 - 40) - 3 = 3 - 3 = \$0.00$ (Breakeven).
  * **Short Call Profit:** $+3 - \max(0, 43 - 40) = +3 - 3 = \$0.00$ (Breakeven).
  * **Long Put Profit:** $\max(0, 35 - 43) - 0.75 = 0 - 0.75 = -\$0.75$ (Max Loss).
  * **Short Put Profit:** $+0.75 - \max(0, 35 - 43) = +0.75 - 0 = +\$0.75$ (Max Profit).

</div>
</div>

-----

### 🧪 Formula Summary

<div style="background-color: \#F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

  * **Call Value at Expiration:** $$\text{Value} = \max(0, S_T - X)$$
  * **Put Value at Expiration:** $$\text{Value} = \max(0, X - S_T)$$
  * **Long Call Profit:** $$\text{Profit} = \max(0, S_T - X) - c_0$$
  * **Short Call Profit:** $$\text{Profit} = c_0 - \max(0, S_T - X)$$
  * **Long Put Profit:** $$\text{Profit} = \max(0, X - S_T) - p_0$$
  * **Short Put Profit:** $$\text{Profit} = p_0 - \max(0, X - S_T)$$
  * **Call Breakeven:** $$S_T = X + c_0$$
  * **Put Breakeven:** $$S_T = X - p_0$$

</div>

-----

<div style="background-color: \#FFF9E6; border-left: 5px solid \#F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: \#000000; font-weight: 500;">

  * **Commitment vs. Claim:** This is the \#1 concept. **Commitments (Forwards, Futures, Swaps)** are *obligations* for both sides. **Claims (Options, CDS)** are a *right* for the buyer and an *obligation* for the seller.
  * **Futures vs. Forwards:** Know the differences\!
      * **Futures:** Standardized, Exchange-Traded, Daily MTM, No Counterparty Risk (due to clearinghouse).
      * **Forwards:** Custom, OTC, Settle at Expiration, High Counterparty Risk.
  * **Option Profit Formulas:** Don't just memorize them, *understand* them.
      * $\text{Value} = \max(0, \dots)$
      * $\text{Profit} = \text{Value} - \text{Premium}$
  * **Breakeven Points (Mnemonics):**
      * **"Call Up":** Call Breakeven = $X + c_0$ (You must "call up" to cover the cost).
      * **"Put Down":** Put Breakeven = $X - p_0$ (The price must "put down" to cover the cost).
  * **Risk Profiles:**
      * **Unlimited Profit:** Long Call.
      * **Unlimited Loss:** Short Call.
      * **Limited Loss:** Long Call/Put (Loss limited to the premium paid).
      * **Limited Profit:** Short Call/Put (Profit limited to the premium received).

</div>
</div>