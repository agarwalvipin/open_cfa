## Reading 19: Currency Exchange Rates and Currency Forward Markets

### 🎯 Introduction

Welcome, future charterholder! Imagine you're at a giant, chaotic airport currency exchange. You have Indian Rupees (INR) and want to buy Thai Baht (THB), but the booth only has prices for INR to USD and USD to THB. What do you do? You do a two-step trade! This is the essence of a **cross rate**.

Now, what if you need that Baht in 90 days, not today? You'd want to lock in a price now for a future exchange. That's a **forward rate**. This reading is your calculator and your rulebook for that currency exchange. You'll master the math of cross rates and learn the "no free lunch" principle that governs how forward rates are set, ensuring you can navigate the global currency markets like a pro.

-----

### <span style="color: #1565C0;">Part 1: The Two-Step Trade - Calculating Cross Rates 💱 (LOS 19.a)</span>

#### <span style="color: #6A1B9A;">1.1 Cross Rate Theory 🧠</span>

* A **cross rate** is an exchange rate between two currencies that is derived from their individual exchange rates with a common third currency (usually the US dollar). It's how we price less common currency pairs.
* The key is to set up the calculation so that the common currency "cancels out."

##### <span style="color: #E65100;">1.1.1 Formula</span>

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\left( \frac{A}{B} \right) \times \left( \frac{B}{C} \right) = \frac{A}{C}$$

</div>
The 'B' term cancels out!

##### <span style="color: #E65100;">1.1.2 Example 🧮</span>

You are given the following quotes:

  * `MXN/USD` = 10.70 (10.70 Mexican pesos per US dollar)
  * `USD/AUD` = 0.60 (0.60 US dollars per Australian dollar)

What is the `MXN/AUD` cross rate?

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\left( \frac{MXN}{USD} \right) \times \left( \frac{USD}{AUD} \right) = \frac{10.70 \text{ MXN}}{1 \text{ USD}} \times \frac{0.60 \text{ USD}}{1 \text{ AUD}} = 6.42 \frac{MXN}{AUD}$$

</div>

The cross rate is 6.42 Mexican pesos per Australian dollar.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️:Getting the cross rate right is all about lining up the units. Write out the fractions like in the example above. If one of your quotes is "upside down" (e.g., you need `USD/AUD` but you're given `AUD/USD`), just take the inverse (1 / given rate) to flip it before you multiply.

</div>
</div>

-----

### <span style="color: #1565C0;">Part 2: Pricing the Future - Forward Rates and the No-Arbitrage Rule ⚖️ (LOS 19.b)</span>

#### <span style="color: #6A1B9A;">2.1 Forward Exchange Rate & Interest Rate Parity</span>

* A **forward exchange rate** is a rate agreed upon today for the exchange of two currencies at a specific future date. But how is this future rate determined? It's not a guess; it's set by a powerful force called the **no-arbitrage principle**.
* This principle, also known as **Interest Rate Parity**, says that the forward exchange rate must be at a level that prevents traders from making a risk-free profit. It ensures that the return from investing in two different currencies is the same after accounting for the exchange rate.

##### <span style="color: #E65100;">2.1.1 Forward Rate Formula</span>

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\frac{Forward}{Spot} = \frac{(1 + i_{\text{price currency}})}{(1 + i_{\text{base currency}})}$$

$$Forward = Spot \times \frac{(1 + i_p)}{(1 + i_b)}$$

</div>

**Key takeaway:** The currency with the **higher interest rate** will trade at a **forward discount** (its forward price will be lower than its spot price). The currency with the **lower interest rate** will trade at a **forward premium**.

##### <span style="color: #E65100;">2.1.2 Example 🧮</span>

Given:

  * Spot Rate (`ABE/DUB`) = 4.5671
  * 1-year risk-free rate in ABE (price currency) = 5%
  * 1-year risk-free rate in DUB (base currency) = 3%

What is the 1-year forward rate?

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$Forward = 4.5671 \times \frac{(1 + 0.05)}{(1 + 0.03)} = 4.5671 \times \frac{1.05}{1.03} = 4.6558$$

</div>

Because the ABE interest rate is higher, the DUB (base currency) must trade at a forward premium to prevent arbitrage.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️:The logic is more important than memorizing the formula's p's and b's. Just remember: to prevent a free lunch, the higher interest rate currency *must* lose value in the forward market to offset its higher yield. So it will trade at a discount.

</div>
</div>

-----

### <span style="color: #1565C0;">Part 3: Reading the Quotes - Points, Percentages, Premiums, and Discounts 📊 (LOS 19.c)</span>

#### <span style="color: #6A1B9A;">3.1 Forward Quotes in Points</span>

  * **Points** refer to the last decimal places of a spot quote. If a spot rate is quoted to 4 decimal places, 1 point = 0.0001.
  * The forward points are simply added to or subtracted from the spot rate.

**Example:**

  * `AUD/EUR` spot rate = 0.7313
  * 1-year forward quote = +3.5 points
  * The forward rate = 0.7313 + 0.00035 = **0.73165**

#### <span style="color: #6A1B9A;">3.2 Forward Quotes in Percentage</span>

  * The forward rate is given as a percentage deviation from the spot rate.

**Example:**

  * `AUD/EUR` spot rate = 0.7313
  * 120-day forward quote = –0.062%
  * The forward rate = 0.7313 × (1 - 0.00062) = **0.7308**

#### <span style="color: #6A1B9A;">3.3 Forward Premium vs. Forward Discount</span>

  * This simply describes whether the forward price of a currency is higher or lower than its spot price.
    * If **Forward > Spot**, the base currency is trading at a **forward premium**.
    * If **Forward < Spot**, the base currency is trading at a **forward discount**.

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\% \text{ Premium or Discount} = \left( \frac{Forward}{Spot} \right) - 1$$

</div>

**Example:**

  * Spot `USD/EUR` = 1.312
  * 90-day Forward `USD/EUR` = 1.320

The forward premium on the euro (the base currency) is:

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\left( \frac{1.320}{1.312} \right) - 1 = 0.0061 = \boldsymbol{+0.61\%}$$

</div>

The euro is trading at a 0.61% forward premium for 90 days.

#### <span style="color: #00838F;">3.4 Global & Local Context 🌍</span>

* **Global Example:** Cross rates are essential for multinational corporations hedging currency risk across multiple countries. For example, a European company trading with India and Australia will use cross rates to price contracts.
* **Indian Example:** Indian exporters often use forward contracts to lock in exchange rates for future USD/INR payments, applying interest rate parity to avoid arbitrage.

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Cross Rate:** 

$$\frac{A}{C} = \frac{A}{B} \times \frac{B}{C}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**No-Arbitrage Forward Rate (Interest Rate Parity):** 

$$Forward = Spot \times \frac{(1 + i_{\text{price currency}})}{(1 + i_{\text{base currency}})}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Forward Premium/Discount (%):**

$$\text{Premium/Discount (%)} = \left( \frac{\text{Forward}}{\text{Spot}} \right) - 1$$

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* **Cancel the Currency:** 
  * For cross rates, write out the fractions and make sure the middle currency cancels out. This will save you from making simple mistakes.
* **High Interest = Forward Discount:** 
  * The currency with the higher interest rate *must* depreciate in the forward market to prevent arbitrage. It will always trade at a discount.
* **Points are Decimals:** 
  * Remember that "points" refer to the final decimal places of the spot quote. If the spot is to 4 decimals, `+20` points means you add `0.0020`.
* **Premium/Discount is for the BASE currency:** 
  * When you calculate a percentage premium or discount, the result applies to the currency in the denominator (the base currency) of your `Forward/Spot` calculation.

</div>
</div>

