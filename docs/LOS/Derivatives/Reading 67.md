## Reading 67: Forward Commitment and Contingent Claim Features and Instruments

-----

### <span style="color: #1565C0;">Part 1: Introduction & Definitions (LOS 67.a)</span>

This LOS introduces the fundamental building blocks of the derivatives world. We can classify them into two broad categories, which we will explore later in this reading: **Forward Commitments** and **Contingent Claims**.

#### <span style="color: #6A1B9A;">1.1 Forward Contracts</span>

A **forward contract** is a private, customized agreement between two parties to buy or sell an asset at a specified price on a future date.

  * **Customized**: The terms (asset, quantity, date, price) are all negotiated between the two parties.
  * **Private (OTC)**: They don't trade on an exchange.
  * **Counterparty Risk**: Because it's a private agreement, there is a significant risk that one party might default on its obligation.

#### <span style="color: #6A1B9A;">1.2 Futures Contracts</span>

A **futures contract** is a standardized forward contract that trades on an organized exchange (like the NSE in India).

  * **Standardized**: The exchange sets all terms, so all contracts for a given asset and month are identical.
  * **Exchange-Traded**: Traded publicly, providing transparency.
  * **No Counterparty Risk**: The exchange's clearinghouse guarantees every trade.
  * **Marked-to-Market**: Gains and losses are settled in cash every single day. This daily settlement process, along with margin requirements, is how the exchange prevents defaults.

Here's a key comparison for the exam:

| Feature | Forward Contract | Futures Contract |
| :--- | :--- | :--- |
| **Trading Venue** | Private (Over-the-Counter) | Public Exchange (e.g., NSE) |
| **Standardization** | Customized | Standardized |
| **Counterparty Risk**| High | Virtually None (due to clearinghouse) |
| **Liquidity** | Low | High |
| **Settlement** | Single payment at expiration | Daily cash settlement (Mark-to-Market) |

#### <span style="color: #6A1B9A;">1.3 Swaps</span>

A **swap** is an agreement between two parties to exchange a series of cash flows over a period of time. Think of it as a series of forward contracts bundled together. The most common type is an "interest rate swap," where one party pays a fixed interest rate and receives a floating rate from the other party, based on a notional principal amount.

#### <span style="color: #6A1B9A;">1.4 Options (Calls and Puts)</span>

An **option** gives the **buyer** the **right, but not the obligation**, to buy or sell an underlying asset at a predetermined price on or before a specified date. This is the critical difference from forwards and futures, which are obligations.

  * **Call Option**: The right to **buy** the underlying asset. You would want the asset's price to go **up**.
  * **Put Option**: The right to **sell** the underlying asset. You would want the asset's price to go **down**.
  * **Premium**: The buyer pays a price to the seller (writer) for this right, called the option premium.

#### <span style="color: #6A1B9A;">1.5 Credit Derivatives</span>

A **credit derivative** is a contract that transfers credit risk from one party to another. The most common example is a **Credit Default Swap (CDS)**, which acts like an insurance policy on a bond. The buyer pays regular premiums, and the seller agrees to pay out if the bond's issuer defaults.

##### <span style="color: #00838F;">1.6 Global & Local Context 🌍</span>

Examples:
  * **Global**: Credit Default Swaps are widely used in US and European bond markets.
  * **Local (India)**: Interest rate swaps are common among Indian banks for managing rate risk.

-----

### <span style="color: #1565C0;">Part 2: Option Profit & Value Calculations (LOS 67.b)</span>

This is a very practical and frequently tested area. The key is to distinguish between an option's **value at expiration** (its intrinsic worth) and the **profit** from the trade, which must account for the initial premium paid or received.

Let's use an example: a stock option on **Tata Consultancy Services (TCS)**.

  * Current TCS Stock Price (S): Let's assume various prices at expiration.
  * Exercise Price (X): **₹3,500**
  * Call Premium (c): **₹100**
  * Put Premium (p): **₹80**

#### <span style="color: #6A1B9A;">2.1 Call Options</span>

A call option gives the buyer the right to buy TCS at ₹3,500.

  * **Long Call (Buyer)**
    * You buy the call, hoping the price of TCS goes up. Your maximum loss is the ₹100 premium you paid.
    * <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
      $$\text{Value at Expiration} = \max(0, S - X)$$
      $$\text{Profit} = \text{Value at Expiration} - \text{Call Premium}$$
      $$\text{Breakeven} = X + \text{Premium} = ₹3,500 + ₹100 = ₹3,600$$
      </div>
  * **Short Call (Seller/Writer)**
    * You sell the call, hoping the price of TCS stays below ₹3,500. Your maximum gain is the ₹100 premium you received. Your potential loss is unlimited.
    * <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
      $$\text{Profit} = \text{Call Premium} - \text{Value at Expiration}$$
      </div>

##### <span style="color: #00838F;">2.2 Global & Local Context 🌍</span>

Examples:
  * **Global**: US equity options are highly liquid and standardized.
  * **Local (India)**: NSE options on stocks like TCS are popular among retail traders.

#### <span style="color: #6A1B9A;">2.3 Put Options</span>

A put option gives the buyer the right to sell TCS at ₹3,500.

  * **Long Put (Buyer)**
    * You buy the put, hoping the price of TCS goes down. Your maximum loss is the ₹80 premium you paid.
    * <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
      $$\text{Value at Expiration} = \max(0, X - S)$$
      $$\text{Profit} = \text{Value at Expiration} - \text{Put Premium}$$
      $$\text{Breakeven} = X - \text{Premium} = ₹3,500 - ₹80 = ₹3,420$$
      </div>
  * **Short Put (Seller/Writer)**
    * You sell the put, hoping the price of TCS stays above ₹3,500. Your maximum gain is the ₹80 premium you received. Your loss is substantial if the stock price falls.
    * <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
      $$\text{Profit} = \text{Put Premium} - \text{Value at Expiration}$$
      </div>

-----

### <span style="color: #1565C0;">Part 3: Forward Commitments vs. Contingent Claims (LOS 67.c)</span>

This is a fundamental concept in derivatives. All the instruments we've discussed fall into one of these two categories.

#### <span style="color: #6A1B9A;">3.1 Forward Commitments</span>

A **forward commitment** is a contract that creates an **obligation** for both parties to transact in the future. It's a "we *will* do this" agreement. The value of the contract at initiation is zero for both parties.

  * **Key Feature**: Both parties are locked into the transaction. There is no choice.
  * **Examples**:
    * **Forward Contracts**
    * **Futures Contracts**
    * **Swaps**

#### <span style="color: #6A1B9A;">3.2 Contingent Claims</span>

A **contingent claim** is a contract where the payoff is *contingent* on a future event. It gives one party the **right**, not the obligation, to transact. The other party has the obligation if the right is exercised. The buyer of this right pays a premium at the start.

  * **Key Feature**: One party has a choice to make, depending on whether the outcome is favorable.
  * **Examples**:
    * **Options** (Calls and Puts)
    * **Credit Derivatives** (like a CDS, which only pays out *if* a default event occurs)

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
💡 CFA Exam Tip ✍️:The easiest way to distinguish them is to ask: <b>Does a party have a choice to act?</b> If yes, it's a contingent claim. If no (both are obligated), it's a forward commitment.
</div>
</div>

##### <span style="color: #00838F;">3.3 Global & Local Context 🌍</span>

Examples:
  * **Global**: Options and CDS are used for hedging and speculation worldwide.
  * **Local (India)**: Forward contracts are common in commodity trading.

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**Call Option Value at Expiration:**  
$$\text{Value} = \max(0, \text{Spot Price at Expiration} - \text{Exercise Price})$$
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**Put Option Value at Expiration:**  
$$\text{Value} = \max(0, \text{Exercise Price} - \text{Spot Price at Expiration})$$
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**Profit for Long Position (Buyer):**  
$$\text{Profit} = \text{Value at Expiration} - \text{Premium Paid}$$
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**Profit for Short Position (Seller):**  
$$\text{Profit} = \text{Premium Received} - \text{Value at Expiration}$$
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**Breakeven for Call Option:**  
$$\text{Breakeven} = \text{Exercise Price} + \text{Premium}$$
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**Breakeven for Put Option:**  
$$\text{Breakeven} = \text{Exercise Price} - \text{Premium}$$
</div>

-----

### <span style="color: #1565C0;">Final Summary for Reading 67</span>

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">
### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">
* **Forwards vs. Futures:**  
  * Futures are standardized, exchange-traded, and have no counterparty risk due to daily marking-to-market and a central clearinghouse.  
  * Forwards are customized, private (OTC), and have significant counterparty risk.
* **Obligation vs. Right:**  
  * Forward commitments (forwards, futures, swaps) are <b>obligations</b>.  
  * Contingent claims (options, CDS) provide a <b>right</b> to one party.
* **Option Profit/Loss:**  
  * Don't forget to subtract the premium when calculating profit for a buyer, and to add it when calculating profit for a seller.  
  * The maximum loss for an option <b>buyer</b> is always the premium they paid.  
  * The maximum profit for an option <b>seller</b> is the premium they received.
* **Call vs. Put:**  
  * A <b>Call</b> is a bet on the price <b>going up</b>.  
  * A <b>Put</b> is a bet on the price <b>going down</b>.
</div>
</div>