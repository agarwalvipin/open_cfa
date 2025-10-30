## Reading 57: Yield-Based Bond Duration Measures and Properties 📏

### 🎯 Introduction

In the last reading, **Macaulay duration** gave us the "balancing point" or "seesaw fulcrum" for a bond's interest rate risk. Now, we're going to upgrade that concept into a practical, powerful tool. This reading introduces **Modified Duration**, a direct measure of a bond's price sensitivity. Think of it as a speedometer for your bond's price—it tells you, in percentage terms, how much the price is likely to change if its yield moves by 1%. It's one of the most important metrics in all of fixed income, and we'll learn exactly how to calculate it and use it to manage risk.

-----

### <span style="color: #1565C0;">Part 1: Modified Duration—The Price Sensitivity Super-Tool ⚡ (LOS 57.a)</span>

While **Macaulay duration** is measured in years, **Modified Duration (ModDur)** gives us a direct, intuitive measure of interest rate risk.

#### <span style="color: #6A1B9A;">1.1 What is Modified Duration?</span>

* **Modified Duration** estimates the **percentage change** in a bond's price for a 1% (100 basis point) change in its yield to maturity (**YTM**).
* It's calculated from Macaulay duration:

  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
  
  $$\text{Modified Duration} = \frac{\text{Macaulay Duration}}{1 + \frac{\text{YTM}}{\text{Periodicity}}}$$
  
  </div>

#### <span style="color: #6A1B9A;">1.2 Estimating Price Changes</span>

* The real power of ModDur is in estimating price changes. The formula is simple but essential:

$$\text{% } \Delta \text{Price} \approx -\text{ModDur} \times \Delta\text{YTM}$$

* The **negative sign** is crucial! It captures the inverse relationship between price and yield. If yields go up, the price change is negative (it falls).
<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️: Modified Duration is your go-to metric for price sensitivity. Always remember the negative sign—price and yield move in opposite directions! ✅

</div>
</div>

#### <span style="color: #6A1B9A;">1.3 Example Calculation</span>

* A bond has a **Modified Duration** of **3.50**. If its YTM increases by 0.50% (50 basis points), what is the estimated percentage change in its price?

$$\text{% } \Delta \text{Price} \approx -3.50 \times (+0.005) = -0.0175 = -1.75\%$$

* The bond's price is expected to fall by approximately **1.75%**. ⬇️

#### <span style="color: #6A1B9A;">1.4 Estimating ModDur Directly</span>

* If you don't know Macaulay duration, you can estimate ModDur by "shocking" the bond's price:

  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
  
  $$\text{Approx. ModDur} = \frac{V_- - V_+}{2 \times V_0 \times \Delta\text{YTM}}$$
  
  </div>
  where $V_0$ is the initial price.

-----

### <span style="color: #1565C0;">Part 2: Putting Duration into Dollar (or Rupee) Terms 💵 (LOS 57.b)</span>

Modified duration gives us a percentage change, but traders often want to know the actual cash impact.

#### <span style="color: #6A1B9A;">2.1 Money Duration (Dollar Duration)</span>

* **Money Duration (or Dollar Duration):** Converts the percentage change into a currency amount for the entire bond position.

  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
  
  $$\text{Money Duration} = \text{Annual ModDur} \times \text{Full Price of Bond Position}$$
  
  </div>

* The estimated price change in money terms is then: $-\text{Money Duration} \times \Delta\text{YTM}$.

#### <span style="color: #6A1B9A;">2.2 Price Value of a Basis Point (PVBP)</span>

* **Price Value of a Basis Point (PVBP):** Measures the change in the full price of a bond, in currency, for a tiny **one basis point (0.01%)** change in its YTM.

  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
  
  $$\text{PVBP} \approx \frac{(V_-) - (V_+)}{2} \times \text{Par Value} \times 0.01$$
  
  </div>

* For a $1 million bond position, the PVBP tells you how many dollars you'll make or lose if the yield moves by just 0.01%. ✅

-----

### <span style="color: #1565C0;">Part 3: What Makes a Bond More Sensitive? The Drivers of Duration 🚗 (LOS 57.c)</span>

A bond's duration (i.e., its interest rate risk) is not random. It is directly influenced by three key characteristics. Understanding these relationships is critical.

#### <span style="color: #6A1B9A;">3.1 Key Drivers of Duration</span>

| **Factor** | **Relationship with Duration** | **Why? (The Simple Intuition)** |
| :--- | :--- | :--- |
| **Maturity** | **Longer Maturity** → **Higher Duration** ⬆️ | Cash flows received further in the future are much more sensitive to changes in discount rates. A 30-year bond's price will move much more than a 2-year bond's price for the same change in rates. |
| **Coupon Rate** | **Higher Coupon** → **Lower Duration** ⬇️ | A higher coupon means you get more of your total return back sooner in cash. This shortens the bond's weighted-average time to receive cash flows, making it less sensitive to rate changes. A **zero-coupon bond**, which pays everything at the end, has the highest duration for a given maturity. |
| **Yield to Maturity** | **Higher YTM** → **Lower Duration** ⬇️ | At higher yields, the price-yield curve is flatter, meaning price is less sensitive to a given change in yield. At very low yields, the curve is steep, and duration is high. |

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️: The three drivers of duration are frequently tested. Duration (**interest rate risk**) is higher for bonds with **longer maturity**, **lower coupons**, and **lower yields**. ✅

</div>
</div>

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Macaulay Duration of a Perpetuity:**

$$\text{MacDur}_{\text{Perpetuity}} = \frac{1 + r}{r}$$

where $r$ is the yield per period.

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Modified Duration from Macaulay:**

$$\text{ModDur} = \frac{\text{MacDur}}{1 + \text{Periodic YTM}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Approximate Percentage Price Change:**

$$\text{% } \Delta \text{Price} \approx -\text{ModDur} \times \Delta\text{YTM}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Approximate Modified Duration:**

$$\text{Approx. ModDur} = \frac{V_- - V_+}{2 \times V_0 \times \Delta\text{YTM}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Money Duration:**

$$\text{MoneyDur} = \text{ModDur} \times \text{Full Price}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**PVBP:**

$$\text{PVBP} \approx \frac{(V_-) - (V_+)}{2} \times \text{Par Value} \times 0.01$$

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* **Modified Duration = Price Sensitivity:** It's the approximate percentage price change for a 1% change in YTM.
* **The Golden Formula:** **%ΔPrice ≈ -ModDur × ΔYTM**. The negative sign is not optional! It represents the inverse relationship between price and yield. ✅
* **The 3 Levers of Duration:** Remember what increases interest rate risk:
  * **Longer** Maturity ⬆️
  * **Lower** Coupon Rate ⬆️
  * **Lower** initial YTM ⬆️
* **PVBP** is the actual money change for a tiny 1 basis point move in yield—a trader's favorite risk metric.

</div>
</div>