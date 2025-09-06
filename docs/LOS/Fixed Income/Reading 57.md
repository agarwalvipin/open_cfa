## Reading 57: Yield-Based Bond Duration Measures and Properties 📏

🎯 **Introduction**

In the last reading, Macaulay duration gave us the "balancing point" or "seesaw fulcrum" for a bond's interest rate risk. Now, we're going to upgrade that concept into a practical, powerful tool. This reading introduces **Modified Duration**, a direct measure of a bond's price sensitivity. Think of it as a speedometer for your bond's price—it tells you, in percentage terms, how much the price is likely to change if its yield moves by 1%. It's one of the most important metrics in all of fixed income, and we'll learn exactly how to calculate it and use it to manage risk.

---

### Part 1: Modified Duration: The Price Sensitivity Super-Tool ⚡

While Macaulay duration is measured in years, **Modified Duration (ModDur)** gives us a direct, intuitive measure of interest rate risk.

**Modified Duration** is an estimate of the percentage change in a bond's price for a 1% (100 basis point) change in its yield to maturity (YTM).

It's easily calculated from Macaulay duration:

**Formula: Modified Duration**
$\text{Modified Duration} = \frac{\text{Macaulay Duration}}{1 + \frac{\text{YTM}}{\text{Periodicity}}}$

#### **Putting Modified Duration to Work**
The real power of ModDur is in estimating price changes. The formula is simple but essential:

**Formula: Approximate % Price Change**
$\%\Delta \text{Price} \approx -\text{ModDur} \times \Delta\text{YTM}$

The negative sign is crucial! It captures the inverse relationship between price and yield. If yields go up, the price change is negative (it falls).

> **Example Time! 🧮**
> A bond has a **Modified Duration** of **3.50**. If its YTM suddenly *increases* by 0.50% (50 basis points), what is the estimated percentage change in its price?
>
> $\% \Delta \text{Price} \approx -3.50 \times (+0.005) = -0.0175 = -1.75\%$
>
> The bond's price is expected to fall by approximately 1.75%.

```text
Example Time! 🧮

A bond has a Modified Duration of 3.50. If its YTM suddenly increases by 0.50% (50 basis points), what is the estimated percentage change in its price?

%ΔPrice ≈ -3.50 × (+0.005) = -0.0175 = -1.75%

The bond's price is expected to fall by approximately 1.75%.

Don't Know Macaulay? No Problem!
We can also estimate ModDur directly by "shocking" the bond's price. Calculate the bond's price for a small yield increase (V+) and a small yield decrease (V-) and plug them into this formula:

Formula: Approximate Modified Duration
Approx. ModDur = (V_- - V_+) / (2 × V_0 × ΔYTM)
where V_0 is the initial price.
```

---

### Part 2: Putting Duration into Dollar (or Rupee) Terms 💵

Modified duration gives us a percentage change, but traders often want to know the actual cash impact.

* **Money Duration (or Dollar Duration):** This converts the percentage change into a currency amount for the entire bond position.
    $\text{Money Duration} = \text{Annual ModDur} \times \text{Full Price of Bond Position}$
    The estimated price change in money terms is then: `−Money Duration × ΔYTM`.

* **Price Value of a Basis Point (PVBP):** This is a very popular metric on trading desks. It measures the change in the full price of a bond, in currency, for a tiny **one basis point (0.01%)** change in its YTM. It provides a simple, absolute measure of risk. For a $1 million bond position, the PVBP tells you how many dollars you'll make or lose if the yield moves by just 0.01%.

---

### Part 3: What Makes a Bond More Sensitive? The Drivers of Duration 🚗

A bond's duration (i.e., its interest rate risk) is not random. It is directly influenced by three key characteristics. Understanding these relationships is critical.

| Factor | Relationship with Duration | Why? (The Simple Intuition) |
| :--- | :--- | :--- |
| **Maturity** | **Longer Maturity** → **Higher Duration** ⬆️ | Cash flows received further in the future are much more sensitive to changes in discount rates. A 30-year bond's price will move much more than a 2-year bond's price for the same change in rates. |
| **Coupon Rate** | **Higher Coupon** → **Lower Duration** ⬇️ | A higher coupon means you get more of your total return back sooner in cash. This shortens the bond's weighted-average time to receive cash flows, making it less sensitive to rate changes. A **zero-coupon bond**, which pays everything at the end, has the highest duration for a given maturity. |
| **Yield to Maturity**| **Higher YTM** → **Lower Duration** ⬇️ | This is a mathematical property of convexity. At higher yields, the price-yield curve is flatter, meaning price is less sensitive to a given change in yield. At very low yields, the curve is steep, and duration is high. |

> [!TIP]
> **CFA Exam Tip ✍️:** The three drivers of duration are one of the most frequently tested concepts in Fixed Income. You MUST know that duration (interest rate risk) is higher for bonds with **longer maturity, lower coupons, and lower yields**.

---

### 🧪 Formula Summary

* **Modified Duration from Macaulay:**
    $\text{ModDur} = \frac{\text{MacDur}}{1 + \text{Periodic YTM}}$
* **Approximate Percentage Price Change:**
    $\%\Delta \text{Price} \approx -\text{ModDur} \times \Delta\text{YTM}$
* **Approximate Modified Duration:**
    $\text{Approx. ModDur} = \frac{V_- - V_+}{2 \times V_0 \times \Delta\text{YTM}}$
* **Money Duration:**
    $\text{MoneyDur} = \text{ModDur} \times \text{Full Price}$
* **PVBP:**
    $\text{PVBP} \approx \frac{(V_-) - (V_+)}{2} \times \text{Par Value} \times 0.01$

---

> [!IMPORTANT]
> ### 🎯 Quick Exam-Day Pointers
>
> * **Modified Duration = Price Sensitivity:** It's the approximate percentage price change for a 1% change in YTM.
> * **The Golden Formula:** **%ΔPrice ≈ -ModDur × ΔYTM**. The negative sign is not optional! It represents the inverse relationship between price and yield.
> * **The 3 Levers of Duration:** Remember what increases interest rate risk:
>     1.  **Longer** Maturity
>     2.  **Lower** Coupon Rate
>     3.  **Lower** initial YTM
> * **PVBP** is the actual money change for a tiny 1 basis point move in yield—a trader's favorite risk metric.