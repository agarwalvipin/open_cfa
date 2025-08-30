### Module 67.1: Forwards and Futures

This module introduces two key types of forward commitments: forward contracts and futures contracts. While similar, their differences are crucial.

#### Forward Contracts vs. Futures Contracts (LOS 67.a)

Both are agreements to buy or sell an underlying asset at a predetermined price on a future date. However, they operate in very different ways.

**Forward Contracts 🤝**

* **Definition:** A private, customizable agreement between two parties to transact at a specified price and date in the future.
* **Market:** Traded **Over-The-Counter (OTC)**, meaning they are not on a formal exchange.
* **Customization:** Highly flexible. The parties can agree on any underlying asset, quantity, and settlement date.
* **Key Risk:** **Counterparty Risk**. Since it's a private agreement, there's a risk that the other party might default and not honor the contract.
* **Settlement:** The transaction and any profit or loss typically happens only once, at the very end of the contract's life.

* **Real-World Example (Indian Context):** A cotton farmer in Gujarat could enter into a forward contract with a textile mill in Ahmedabad. They might agree today to sell 100 tonnes of cotton in 3 months at a price of ₹70,000 per tonne. This is a private deal tailored to their specific needs.

---

**Futures Contracts 🏛️**

* **Definition:** A **standardized** forward contract that trades on an organized exchange.
* **Market:** Traded on formal exchanges, like the National Stock Exchange (NSE) in India.
* **Standardization:** The contract size, underlying asset quality, and delivery dates are all fixed by the exchange. You can't customize them.
* **Key Feature 1: The Clearinghouse.** The exchange's clearinghouse becomes the buyer to every seller and the seller to every buyer. This **eliminates counterparty risk**. If one party defaults, the clearinghouse steps in.
* **Key Feature 2: Marking-to-Market.** This is a critical difference. At the end of every trading day, your futures position is settled. Profits are added to your account, and losses are deducted. This prevents large losses from building up.
    * **Margin:** To trade futures, you must deposit a small amount of collateral called the **initial margin**. If daily losses cause your margin account to fall below the **maintenance margin**, you get a "margin call" and must deposit more funds to bring it back up to the initial margin level, 2943].

> **CFA Exam Tip:** The differences between forwards and futures are a classic exam topic. You absolutely must know this table.
> 
> | Feature | Forward Contract | Futures Contract |
> | :--- | :--- | :--- |
> | **Market** | OTC (Private) | Exchange-Traded |
> | **Customization** | High | Low (Standardized) |
> | **Counterparty Risk** | High | Virtually None (Clearinghouse) |
> | **Liquidity** | Low | High |
> | **Settlement** | At the end (usually) | Daily (Mark-to-Market) |
> | **Regulation** | Low | High |

***

### Module 67.2: Swaps and Options

This module introduces derivatives where the payoffs are more complex than simple forwards and futures.

#### Swaps, Options, and Credit Derivatives (LOS 67.a continued)

**Swaps 🔄**

* **Definition:** A swap is an OTC agreement between two parties to exchange a series of cash flows over a period of time. Think of it as a bundle of forward contracts strung together.
* **Most Common Type:** The **interest rate swap**. One party agrees to pay a fixed interest rate on a notional amount, and in return, the other party pays a floating interest rate (linked to a benchmark like MIBOR - Mumbai Interbank Offered Rate) on the same notional amount. Only the net difference is paid at each settlement date.
* **Real-World Example (Indian Context):** A real estate company like DLF might take out a large construction loan from SBI at a floating interest rate. To make their interest costs predictable for budgeting, DLF could enter a swap where they pay a fixed rate to a bank and receive a floating rate. They then use the floating payment they receive to pay their loan interest to SBI, effectively converting their floating-rate loan into a fixed-rate loan -2956].

---

**Options (Calls and Puts) ⚖️**

* **Definition:** An option gives the **buyer** the **right**, but not the obligation, to buy or sell an underlying asset at a specified price (the **exercise price** or **strike price**) on or before a future date, 2966]. The buyer pays a price, called the **option premium**, for this right. This is the key difference from forwards/futures, where both parties are *obligated* to transact.
* **Call Option:** Gives the holder the right to **buy** the underlying asset. You would buy a call if you are **bullish** (expect the price to rise).
* **Put Option:** Gives the holder the right to **sell** the underlying asset. You would buy a put if you are **bearish** (expect the price to fall).

---

**Credit Derivatives 🛡️**

* **Definition:** A derivative whose payoff depends on a "credit event" of an underlying debt security, such as a default.
* **Most Common Type:** A **Credit Default Swap (CDS)**. This works like an insurance policy. The buyer of the CDS makes regular payments (like an insurance premium) to the seller. If the underlying bond or loan defaults (the "credit event"), the seller pays the buyer the loss in value.

#### Option Value and Profit at Expiration (LOS 67.b)

This is a critical, calculation-based skill for the exam. The **value** of an option at expiration (its exercise value) is its payoff if exercised. The **profit** also accounts for the initial premium paid or received.

Let:
* $S_T$ = Stock Price at Expiration
* $X$ = Exercise (Strike) Price
* $c_0$ = Call premium
* $p_0$ = Put premium

**Call Option 📈**
* **Value at Expiration:** $V_T = \text{Max}(0, S_T - X)$
* **Profit for Buyer (Long Call):** $\pi = \text{Max}(0, S_T - X) - c_0$
* **Profit for Seller (Short Call):** $\pi = c_0 - \text{Max}(0, S_T - X)$
* **Breakeven Point:** $S_T = X + c_0$
* **Key Insight:** The call buyer has limited loss (the premium) and unlimited potential profit. The call seller has limited profit (the premium) and unlimited potential loss. 

**Put Option 📉**
* **Value at Expiration:** $V_T = \text{Max}(0, X - S_T)$
* **Profit for Buyer (Long Put):** $\pi = \text{Max}(0, X - S_T) - p_0$
* **Profit for Seller (Short Put):** $\pi = p_0 - \text{Max}(0, X - S_T)$
* **Breakeven Point:** $S_T = X - p_0$
* **Key Insight:** The put buyer has limited loss (the premium) and substantial but limited profit (if the stock price goes to zero). The put seller has limited profit (the premium) and substantial but limited loss. 

> **CFA Exam Tip:** You must be able to calculate the profit/loss for any of the four basic option positions (long/short call/put) at expiration. Always remember to factor in the initial premium. A common mistake is to only calculate the exercise value and forget about the initial cost/income.

---

#### Forward Commitments vs. Contingent Claims (LOS 67.c)

This is the most important classification in derivatives. All derivatives fall into one of these two categories.

**Forward Commitments**
* **What is it?** An **obligation** for both parties to transact in the future. There is no "walking away."
* **Value at Start:** The price is set so the initial value of the contract is **zero** to both parties. No money changes hands upfront (excluding margins).
* **Examples:** Forwards, Futures, Swaps, 3009].

**Contingent Claims**
* **What is it?** One party has a **right** and the other has an **obligation**, with the payoff being **contingent** on a future event (e.g., the stock price being above the strike price), 3010].
* **Value at Start:** The buyer of the right pays a **premium** to the seller. Therefore, the contract has a positive value to the buyer and a negative value to the seller at the start.
* **Examples:** Options, Credit Default Swaps, 3011].


***

### Summary of Formulas & Payoffs for Reading 67

This reading focuses on definitions and profit/loss calculations. Mastering these option payoffs is non-negotiable for the exam.

* **Call Option Value at Expiration:**
    $V_T = \text{Max}(0, S_T - X)$

* **Put Option Value at Expiration:**
    $V_T = \text{Max}(0, X - S_T)$

* **Long Call Profit (Buyer):**
    $\pi = \text{Max}(0, S_T - X) - c_0$

* **Short Call Profit (Seller/Writer):**
    $\pi = c_0 - \text{Max}(0, S_T - X)$

* **Long Put Profit (Buyer):**
    $\pi = \text{Max}(0, X - S_T) - p_0$

* **Short Put Profit (Seller/Writer):**
    $\pi = p_0 - \text{Max}(0, X - S_T)$

***

### ⚡ Quick Exam-Day Pointers

On exam day, Reading 67 questions will test your ability to quickly define, compare, and calculate.

* **The Great Divide: Obligation vs. Right**
    This is the most important concept in the reading. Every derivative is either a commitment or a claim.
    * 🤝 **Forward Commitments:** An **OBLIGATION** for both parties.
        * *Types:* Forwards, Futures, Swaps.
        * *Key Feature:* Value at initiation is zero.
    * ⚖️ **Contingent Claims:** A **RIGHT** for the buyer, an **OBLIGATION** for the seller.
        * *Types:* Options, Credit Default Swaps.
        * *Key Feature:* Buyer pays a premium upfront.

* **Forwards vs. Futures: Know the Scorecard**
    This comparison is a favorite for exam questions.
    * **Forwards** = Custom, Private (OTC), High Counterparty Risk.
    * **Futures** = Standardized, Exchange-Traded, No Counterparty Risk (thanks to the clearinghouse), and **Daily Mark-to-Market**.

* **Option Math Must Be Automatic!**
    You should be able to calculate the profit or loss for any basic option position in under 30 seconds.
    * **Step 1:** Calculate the option's value at expiration (Max(0, S-X) or Max(0, X-S)).
    * **Step 2:** Adjust for the premium. **Subtract** it for the buyer, **Add** it for the seller.
    * **Remember Breakeven Points:**
        * Call Breakeven = Strike Price + Premium
        * Put Breakeven = Strike Price - Premium

* **Option Risk Profiles in a Nutshell:**
    * **Buyer (Long):** 🧑‍💻 Your risk is **limited** to the premium you paid. Your potential reward is unlimited (call) or large (put).
    * **Seller (Short):** 🏦 Your reward is **limited** to the premium you received. Your potential risk is unlimited (call) or large (put). You get paid to take on risk.