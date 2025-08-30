### Module 71.1: Futures Valuation

This module focuses on how the daily settlement process of futures contracts makes their valuation different from forward contracts and why their prices can diverge.

#### Value and Price of Forwards vs. Futures (LOS 71.a)

The daily **mark-to-market (MTM)** process is the defining feature of futures contracts and the source of all the major differences compared to forwards.

* **Forward Contract:**
    * The **price** ($F_0(T)$) is **fixed** for the life of the contract.
    * The **value** starts at zero and then **fluctuates** daily as the underlying spot price changes. The total profit or loss is only realized in one lump sum at settlement.

* **Futures Contract:**
    * The **value** is **reset to zero at the end of every trading day** because the day's profit or loss is settled in cash immediately through the MTM process.
    * The futures **price** is **updated daily** to the new settlement price. Each day, it's as if you are entering a new futures contract at the new price.

**Example of Daily MTM:**

Imagine you go long one Nifty 50 futures contract at a price of 24,000.
* **Day 1:** The settlement price at the end of the day is 24,050.
    * Your contract has a MTM profit of 50 points. This profit is immediately added to your margin account in cash.
    * The contract value is reset to zero, and your new contract price is effectively 24,050.
* **Day 2:** The settlement price drops to 24,010.
    * You have a MTM loss of 40 points (from the previous day's price of 24,050). This loss is deducted from your margin account.
    * The contract value is reset to zero, and your new price is now 24,010.

> **CFA Exam Tip:** This is a crucial distinction. For an exam question, remember:
> * **Forward:** Value changes, Price is fixed.
> * **Futures:** Value is reset to 0 daily, Price changes daily.

---

#### Why Forward and Futures Prices Differ (LOS 71.b)

If forwards and futures are so similar, why would they have different prices?

The answer lies in the **interest earned (or lost) on the daily MTM cash flows**. Because futures profits are paid out daily, they can be reinvested and earn interest. The difference between the forward and futures price, therefore, depends on the **correlation between futures prices and interest rates**.

1.  📈 **Positive Correlation (Futures Price > Forward Price)**
    * This is common for assets like **stock indices**. When the economy is strong, both stock prices and interest rates tend to rise together.
    * If you are long a futures contract, you receive MTM profits (which you can reinvest at now **higher** interest rates) when prices go up. You pay out MTM losses when prices go down (and interest rates are **lower**), so your funding cost is less.
    * This timing advantage makes futures more desirable than forwards, so the **futures price will be slightly higher than the forward price**.

2.  📉 **Negative Correlation (Futures Price < Forward Price)**
    * This is common for assets like **long-term government bonds**. When interest rates rise, bond prices fall.
    * If you are long a bond futures contract, you receive MTM profits when bond prices rise, which happens when interest rates are **low** (so your reinvestment opportunity is poor). You pay out MTM losses when bond prices fall, which is when interest rates are **high** (so your funding cost for margin calls is expensive).
    * This timing disadvantage makes futures less desirable, so the **futures price will be slightly lower than the forward price**.

3.  😐 **Zero Correlation**
    * If there is no correlation between the underlying's price and interest rates, then **forward and futures prices will be equal**.

> **CFA Exam Tip:** For Level 1, you will not be asked to calculate the price difference, but you **must** understand the theory. The key takeaway is that the daily settlement of futures creates a pricing difference from forwards when interest rates are correlated with the underlying's price.

***

### Summary of Key Concepts for Reading 71

This reading focuses entirely on the unique features of futures contracts that cause them to be priced differently from otherwise identical forward contracts.

* **Daily Mark-to-Market (MTM):** This is the defining feature of futures. At the end of each trading day, gains and losses are settled in cash. This daily settlement resets the **value** of the futures contract to **zero**.
* **Price vs. Value Distinction:**
    * **Forward:** The forward **price is fixed**, while its **value fluctuates** over its life.
    * **Futures:** The futures **value is reset to zero daily**, while its **price is updated daily** to the settlement price, 3151].
* **Reason for Price Difference:** Futures and forward prices can differ because of the **daily settlement of futures gains and losses**. The ability to earn interest on these daily cash flows (or pay interest to fund them) creates a pricing difference if interest rates are correlated with futures prices -3160].
* **Impact of Correlation:**
    * **Positive Correlation:** (e.g., stock indices & interest rates) makes futures more attractive. **Futures Price > Forward Price**.
    * **Negative Correlation:** (e.g., bonds & interest rates) makes futures less attractive. **Futures Price < Forward Price**.
    * **Zero Correlation:** No timing advantage or disadvantage. **Futures Price = Forward Price**.

***

### ⚡ Quick Exam-Day Pointers

For Reading 71, you won't do heavy calculations, but you must know the core concepts.

* **Remember the Daily Reset:** For **Futures**, think **"Daily Cash & Reset to Zero."** 🔄 For **Forwards**, think **"Lump Sum at the End."** 💰
* **The Golden Rule for Price Differences:** The exam loves to ask *why* futures and forward prices differ. The answer is always related to **daily settlement (MTM) and its correlation with interest rates**.
* **Memorize the Correlation Impact:**
    * 📈 **Positive Correlation** (Stocks): Think "Profits are good!" You get gains when rates are high (good for reinvesting). **Futures Price > Forward Price**.
    * 📉 **Negative Correlation** (Bonds): Think "Painful Payments!" You get losses when rates are high (bad for funding margin calls). **Futures Price < Forward Price**.