## Reading 77: Alternative Investments – Performance & Valuation

### 🎯 Introduction

Measuring the return on a stock like HDFC Bank is like checking a live cricket score—the numbers are public, updated constantly, and easy to understand.

But measuring the performance of an alternative investment? That's more like judging a complex, multi-year science experiment 🧪. The results come in phases, the inputs are unique, and you need special tools to figure out if it was a success. This reading gives us those tools, focusing on the unique challenges and calculations for alternatives.

-----

### <span style="color: #1565C0;">Part 1: Why Is Measuring Performance So Tricky? (LOS 77.a)</span>

Appraising the performance of alternative investments is a different ball game for several key reasons:

* 🔄 **Unique Life Cycles & Cash Flows**  
  * Investments in private equity involve capital being invested (**capital calls**) and returned (**distributions**) at different, unpredictable times over many years. This leads to the famous **J-Curve Effect**.
* ⚖️ **Use of Leverage**  
  * Hedge funds and private equity often borrow money to magnify returns. This also magnifies losses, making risk assessment more complex.
* ❓ **Difficult Valuations**  
  * Many alternative assets don't have public market prices, so they must be valued using estimates. This can lead to **smoothed returns**, where performance appears less volatile than it really is.
* 💸 **Complex Fee Structures**  
  * Fees aren't simple percentages; they can vary by investor and over time, affecting the final return.

#### <span style="color: #6A1B9A;">1.1 The J-Curve Effect</span>

For illiquid funds like private equity, returns are typically negative in the early years before turning positive, creating a "J" shape on a graph.

```mermaid
graph LR
    subgraph "Investment Life Cycle & The J-Curve"
        direction LR
        A(Start) --> B["Phase 1: Capital Commitment
        Initial Negative Returns
        Fees & setup costs are paid"]
        B --> C["Phase 2: Capital Deployment
        Returns still negative/flat
        Capital is invested in companies"]
        C --> D["Phase 3: Capital Distribution
        Sharp Positive Returns
        Successful investments are sold for a profit"]
    end
    style B fill:#f8d7da
    style C fill:#fff3cd
    style D fill:#d4edda
```

#### <span style="color: #6A1B9A;">1.2 Valuation: The Fair Value Hierarchy</span>

Because many alternative assets don't trade on an open market, we use a framework to estimate their value:

* **Level 1** 🟢: Quoted prices for **identical** assets in active markets. This is the most reliable.  
  * *Example*: The share price of Reliance Industries on the NSE.
* **Level 2** 🟡: Observable inputs for **similar** assets.  
  * *Example*: Valuing a corporate bond that doesn't trade often by looking at the yields of similar bonds.
* **Level 3** 🔴: Unobservable inputs; valuation is based on a manager's own models and assumptions. This is the most subjective.  
  * *Example*: Valuing a private Indian startup. This reliance on "mark-to-model" accounting can lead to **smoothed returns** and understated volatility.

#### <span style="color: #6A1B9A;">1.3 Key Performance Metrics: IRR vs. MOIC</span>

Due to the irregular timing of cash flows, we need special metrics.

##### <span style="color: #E65100;">1.3.1 Internal Rate of Return (IRR)</span>

* **What it is**: The discount rate that makes the net present value (NPV) of all cash flows equal to zero.
* **Pros ✅**: The preferred metric for private equity and real estate because it fully **accounts for the timing of cash flows**.
* **Cons ❌**: It's more complicated to calculate and involves assumptions about reinvestment rates.

##### <span style="color: #E65100;">1.3.2 Multiple of Invested Capital (MOIC)</span>

* **What it is**: A simple, intuitive measure also known as the money multiple.
* **Pros ✅**: Very easy to calculate and understand. A 2x MOIC means you doubled your money.
* **Cons ❌**: Its biggest flaw is that it **completely ignores the time value of money**. A 2x return over 2 years is fantastic; a 2x return over 15 years is not.

#### <span style="color: #00838F;">1.4 Global & Local Context 🌍</span>

* **Global Example:** U.S. private equity funds often show a pronounced J-curve, with early losses due to fees and slow capital deployment, followed by strong gains as investments mature.
* **Indian Example:** Indian venture capital funds also experience the J-curve, but the timing and magnitude may differ due to local market dynamics and regulatory factors.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️: 
Master the logic for IRR and MOIC. IRR is superior for timing, MOIC is intuitive but ignores time value. Know the J-curve phases and why Level 3 assets can distort reported returns.

</div>
</div>

-----

### <span style="color: #1565C0;">Part 2: The Investor's Bottom Line – Calculating Returns After Fees (LOS 77.b)</span>

This is where the rubber meets the road. Calculating the final return an investor receives requires navigating complex fee arrangements and fund rules.

#### <span style="color: #6A1B9A;">2.1 Liquidity Provisions: Getting Your Money Out</span>

Unlike mutual funds, you can't just redeem your money from a hedge fund or PE fund overnight:

* 🔐 **Lockup Period**: The minimum time you must hold your investment before you can request a withdrawal.
* ⏰ **Notice Period**: The amount of time (e.g., 30-90 days) you must give the manager *before* you can redeem your funds.
* 🚪 **Gate**: A provision allowing the fund manager to limit redemptions during periods of market stress to avoid a fire sale of assets.

#### <span style="color: #6A1B9A;">2.2 Custom Fee Arrangements</span>

Not all investors pay the same fees:

* 👑 **Founders Class Shares**: Early investors in a new fund are often offered a lower fee structure (e.g., "1.5 and 10" instead of "2 and 20") to entice them to invest.
* ⚖️ **"Either/or" Fees**: A structure where the manager receives either a lower management fee OR a higher performance fee, whichever is greater in a given year.

#### <span style="color: #6A1B9A;">2.3 The Waterfall: How Profits Are Distributed</span>

In private equity, a **waterfall** dictates the order in which profits are distributed.

##### <span style="color: #E65100;">2.3.1 American Waterfall (Deal-by-Deal)</span>

* The GP can collect carried interest after **each individual deal** is profitably exited.
  * **Favors**: The **GP** 👨‍💼, as they get paid sooner.
  * **Risk for LP**: Makes the **clawback provision** extremely important, as the GP might get paid for early wins even if the total fund ends up losing money.

##### <span style="color: #E65100;">2.3.2 European Waterfall (Whole-of-Fund)</span>

* The GP gets paid only after **all LPs have received their entire initial capital back plus their preferred return** from the entire fund's pool of investments.
  * **Favors**: The **LPs** investors, as it's much safer and aligns interests with the fund's overall success.

#### <span style="color: #6A1B9A;">2.4 Index Biases: Is the Data Too Good to Be True?</span>

Hedge fund index performance often looks better than reality due to two key biases:

* 💀 **Survivorship Bias**: When a fund performs poorly and shuts down, it's removed from the index. The index is left with only the "survivors," making the average performance look artificially high.
* 📈 **Backfill Bias**: A manager starts a new fund. If it does well, they begin reporting its performance to an index and "backfill" its amazing (but selectively chosen) history. The index's historical data gets inflated with these pre-selected winners.

#### <span style="color: #00838F;">2.5 Global & Local Context 🌍</span>

* **Global Example:** European PE funds often use the whole-of-fund waterfall, protecting LPs, while U.S. funds may use deal-by-deal, favoring GPs.
* **Indian Example:** Indian hedge funds may have longer lockup periods and stricter gates due to local regulations.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️: 
Fee calculations involving a **High-Water Mark (HWM)** and **hurdle rates** are very common on the exam. Practice the step-by-step logic. The order of operations matters! Also, be able to define and differentiate **Survivorship Bias** from **Backfill Bias**.

</div>
</div>

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Leveraged Return ($r_L$):**  
$$r_L = r + \frac{V_b}{V_c}(r - r_b)$$

Where:  
- $r_L$ = Leveraged rate of return  
- $r$ = Return on the unleveraged assets  
- $V_b$ = Amount of borrowed funds  
- $V_c$ = Amount of cash (equity) capital invested  
- $r_b$ = Borrowing rate

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Multiple of Invested Capital (MOIC):**  
$$\text{MOIC} = \frac{\text{Realized Value} + \text{Unrealized Value}}{\text{Total Invested Capital}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**GP Fee with High-Water Mark ($R_{GP}$):**  
$$R_{GP} = (P_t \times r_m) + \max[0, (P_t - P_{HWM}) \times p]$$

Where:  
- $P_t$ = Fund value at the end of period *t*  
- $r_m$ = Management fee rate  
- $P_{HWM}$ = The fund's peak value at the end of any previous period, net of fees  
- $p$ = Performance fee rate

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* **J-Curve:**  
  * Early costs/fees → ⬇️ Negative returns → Later gains → ⬆️ Positive returns
* **Valuation:**  
  * 🔴 **Level 3** assets are "Mark-to-Model," which can lead to artificially **smoothed returns** and understated risk
* **IRR vs. MOIC:**  
  * ⏰ **IRR** is superior because it accounts for the *timing* of cash flows; **MOIC** does not
* **Fee Calculation Logic:**  
  * 💰 Master the order of operations for calculating net return, especially how the **High-Water Mark (HWM)** works. A fund must exceed its prior peak value before performance fees are paid on new profits
* **Waterfalls:**  
  * 🌊 **American** (deal-by-deal) favors the **GP**; **European** (whole-of-fund) favors the **LP**
* **Index Biases:**  
  * 📊 Remember that **Survivorship** and **Backfill** biases make hedge fund index returns look better than they really are

</div>
</div>