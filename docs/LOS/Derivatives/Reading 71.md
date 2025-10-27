-----
### <span style="color: #1565C0;">Part 1: Price vs. Value of Forward and Futures Contracts (LOS 71.a) ⚖️</span>

#### <span style="color: #6A1B9A;">1.1 Introduction</span>

It's crucial to distinguish between the <b>price</b> and the <b>value</b> of a derivative contract. The <b>price</b> is the agreed-upon rate for the transaction at a future date, while the <b>value</b> is what the contract is worth today.

#### <span style="color: #6A1B9A;">1.2 Forward Contracts</span>

* <b>Price:</b> The forward price is <b>fixed</b> at the beginning of the contract and remains unchanged throughout its life 🗓️.
* <b>Value:</b> A forward contract is structured to have a <b>value of zero</b> at initiation. However, as the spot price of the underlying asset changes, the value of the forward contract fluctuates. It becomes positive for one party and negative for the other. The entire gain or loss is settled only at expiration.

#### <span style="color: #00838F;">1.3 Global & Local Context 🌍</span>

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
<b>🇮🇳 Indian Example:</b> Imagine a cotton farmer in Gujarat enters a forward contract to sell 100 bales of cotton in 3 months at a price of ₹50,000 per bale. The forward <b>price</b> is fixed at ₹50,000. If, after one month, the market price for cotton jumps to ₹52,000, the <b>value</b> of the contract becomes positive for the buyer and negative for the farmer. However, no money changes hands until the settlement date.
</div>
</div>

#### <span style="color: #6A1B9A;">1.4 Futures Contracts</span>

Futures contracts operate differently due to the <b>Mark-to-Market (MTM)</b> process 🔄.

* <b>Price and Value:</b> Both the price and value of a futures contract change daily.
* <b>Mark-to-Market:</b> At the end of each trading day, the contract is settled based on the day's <b>settlement price</b>.
  * Gains are added to the winner's <b>margin account</b> 💰.
  * Losses are deducted from the loser's margin account.
* After the daily settlement, the contract is effectively repriced to the new settlement price. This process resets the contract's <b>value back to zero</b> at the end of every day.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
<b>🇮🇳 Indian Example:</b> An investor buys one Nifty 50 futures contract on the National Stock Exchange (NSE) at a price of 19,500. The lot size is 50.
<ul>
  <li><b>Day 1:</b> The Nifty futures settlement price is 19,600. The investor has a gain of 100 points.
    <ul>
      <li><b>Gain:</b> $100 \times 50 = 5000$. This amount is credited to their margin account.</li>
      <li>The contract's value is reset to zero, and the new price for the next day is 19,600.</li>
    </ul>
  </li>
  <li><b>Day 2:</b> The settlement price falls to 19,550. The investor has a loss of 50 points from the new price.
    <ul>
      <li><b>Loss:</b> $50 \times 50 = 2500$. This amount is debited from their margin account.</li>
      <li>The contract's value is again reset to zero, and the new price is 19,550.</li>
    </ul>
  </li>
</ul>
</div>
</div>

#### <span style="color: #6A1B9A;">1.5 Interest Rate Futures</span>

Interest rate futures, like those based on the Mumbai Interbank Offered Rate (MIBOR), are quoted differently.

* <b>Price Quotation:</b> The price is quoted as <code>100 - Annualized Interest Rate (%)</code>. A price of 96.50 implies an interest rate of $100 - 96.50 = 3.50\%$.
* <b>Basis Point Value (BPV):</b> This is a critical concept that measures the change in a contract's value for a one-basis-point (0.01%) change in the interest rate. It quantifies the contract's sensitivity.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
💡 CFA Exam Tip ✍️:Remember the inverse relationship for interest rate futures: as interest rates go <b>up</b> 📈, the futures price goes <b>down</b> 📉, and vice-versa.
</div>
</div>

-----

### <span style="color: #1565C0;">Part 2: Why Futures Prices Differ from Forward Prices (LOS 71.b) 🤔</span>

#### <span style="color: #6A1B9A;">2.1 Introduction</span>

While similar, futures and forward prices are not always identical, primarily due to the MTM process and its interaction with interest rates.

#### <span style="color: #6A1B9A;">2.2 The Mark-to-Market Effect</span>

The daily cash settlement of futures gains and losses is the key.

* <b>If futures prices are positively correlated with interest rates:</b>
  * When prices rise, you receive a cash gain. You can reinvest this cash at a <b>higher</b> interest rate.
  * When prices fall, you have a cash loss. You can borrow to fund this loss at a <b>lower</b> interest rate.
  * <span style="color: #388E3C;">✅ This is an advantageous situation.</span> Therefore, the <b>futures contract is more valuable, and its price will be higher than the forward price.</b>
* <b>If futures prices are negatively correlated with interest rates:</b>
  * The opposite occurs. Gains are reinvested at lower rates, and losses are funded at higher rates.
  * <span style="color: #D32F2F;">❌ This is disadvantageous.</span> Therefore, the <b>futures price will be lower than the forward price.</b>

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">
### 🎯 Quick Exam-Day Pointers
<div style="color: #000000; font-weight: 500;">
<ul>
  <li><b>Exam Highlight:</b> For the exam, you can generally assume that for most underlying assets (like equities and bonds), there is a <b>positive correlation</b> between their prices and interest rates, so <b>Futures Price > Forward Price</b>.</li>
  <li>For interest rate futures themselves, the correlation is <b>negative</b>, so <b>Futures Price < Forward Price</b>.</li>
</ul>
</div>
</div>

#### <span style="color: #6A1B9A;">2.3 Convexity Bias</span>

This is a specific issue related to <b>interest rate forwards (FRAs) and futures</b>.

* <b>FRAs:</b> The payoff on an FRA is based on the <i>present value</i> of the interest differential. This discounting creates a non-linear (<b>convex</b>) relationship with interest rates, similar to a bond's price-yield curve. This means a long FRA position benefits more from a rate decrease than it loses from an equivalent rate increase.
* <b>Interest Rate Futures:</b> The payoff is <b>linear</b>, calculated simply using the BPV.

This difference in payoff structure is called <b>convexity bias</b>. The attractive convexity feature of an FRA means investors are willing to pay a premium for it.

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">
<div style="color: #000000; font-weight: 500;">
<ul>
  <li><b>Exam Highlight:</b> Due to convexity bias, the interest rate on a <b>forward contract (FRA)</b> will be slightly higher than the rate on an equivalent futures contract. This difference is more pronounced for longer-term contracts.</li>
</ul>
</div>
</div>

-----

### <span style="color: #1565C0;">Part 3: Formulas Used in This Reading 🧮</span>

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

<b>Interest Rate Futures Price:</b>
$$\text{Price} = 100 - \text{Annualized Interest Rate} (\%)$$

</div>

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

<b>Basis Point Value (BPV):</b>
$$\text{BPV} = \text{Notional Principal} \times \text{Period} \times 0.0001$$

<i>Note: The 'Period' is expressed in years (e.g., for a 3-month contract, the period is 3/12 or 0.25).</i>

</div>

-----

### <span style="color: #1565C0;">Part 4: Quick Exam-Day Pointer ✅</span>

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">
### 🎯 Quick Exam-Day Pointers
<div style="color: #000000; font-weight: 500;">
<ul>
  <li><b>Futures = Daily MTM.</b> Forwards = Settle at expiry.</li>
  <li>The MTM process resets the <b>value</b> of a futures contract to zero every day.</li>
  <li><b>Futures Price vs. Forward Price:</b> It's all about the correlation with interest rates.
    <ul>
      <li><b>Positive Correlation (most assets):</b> Futures Price > Forward Price.</li>
      <li><b>Negative Correlation (interest rates):</b> Futures Price < Forward Price.</li>
    </ul>
  </li>
  <li><b>Convexity Bias:</b> Applies only to interest rate derivatives. It makes the <b>Forward Rate > Futures Rate</b>.</li>
</ul>
</div>
</div>