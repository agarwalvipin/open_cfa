## Reading 56: Interest Rate Risk and Return 🎢

🎯 **Introduction**

Owning a fixed-rate bond is like being on a seesaw with market interest rates. When rates in the market go up, the price of your existing, lower-coupon bond goes down. When market rates fall, your bond suddenly looks more attractive, and its price goes up. This reading is all about this thrilling but risky ride. We'll break down the three sources of a bond's return and explore the two opposing forces of **price risk** and **reinvestment risk**. Most importantly, we'll introduce a crucial concept called **Macaulay duration**—a single number that tells you the exact balancing point of this interest rate seesaw.

---

### Part 1: Where Does a Bond's Return *Really* Come From? 💰

An investor's total return from a bond, known as the **horizon yield**, comes from three places:
1.  **Coupon & Principal Payments:** The promised cash flows you receive from the issuer.
2.  **Reinvestment Income:** The interest you earn by reinvesting the coupon payments you receive over time.
3.  **Capital Gain or Loss:** The profit or loss you make if you sell the bond before maturity at a price different from your purchase price.

When interest rates change, they pull an investor's return in two opposite directions, creating two key risks.

#### **Price Risk 📉**

This is the risk that if market interest rates **rise**, the market price (**carrying value**) of your bond will **fall**.

* **Who it affects most:** Investors with a **short investment horizon** who plan to sell the bond before it matures.
* **The logic:** If new bonds are being issued with a 7% coupon, no one will pay full price for your old 5% coupon bond. You'll have to sell it at a discount (a capital loss) to attract a buyer.
* **Conclusion:** For a short-term investor, a rise in interest rates is **bad news**.

#### **Reinvestment Risk 📉**

This is the risk that if market interest rates **fall**, you will have to reinvest your coupon payments at a lower rate, earning less interest-on-interest than you initially expected.

* **Who it affects most:** Investors with a **long investment horizon** who plan to hold the bond to maturity.
* **The logic:** If you bought a bond yielding 5%, you expected to reinvest all your coupons at 5%. If rates drop to 3%, your total return will be dragged down because your reinvestment income will be much lower than planned.
* **Conclusion:** For a long-term investor, a fall in interest rates is **bad news**.

---

### Part 2: Macaulay Duration: The Seesaw's Fulcrum ⚖️

So, if rising rates hurt short-term investors (price risk) and falling rates hurt long-term investors (reinvestment risk), is there a magical investment horizon where these two risks perfectly cancel each other out?

Yes! This horizon is the bond's **Macaulay duration**.

**Macaulay duration** is the weighted-average time (in years) until a bond's cash flows are received. The "weights" are the present value of each cash flow as a percentage of the bond's full price.

**The Golden Interpretation:**
Macaulay duration is the investment horizon at which a bond investor is **immunized** from interest rate risk. If your investment horizon is equal to the bond's Macaulay duration, the gain/loss from reinvestment income will perfectly offset the loss/gain from the bond's market price. Your realized return will be the original YTM you locked in at purchase, *no matter what interest rates do*.

> **Calculating Macaulay Duration: A 3-Step Process**
> 1.  **Find the PV of Each Cash Flow:** Discount every single coupon and the final principal payment back to today using the bond's YTM. Sum them up to get the bond's price.
> 2.  **Calculate the Weight of Each Cash Flow:** Divide the PV of each cash flow by the total price of the bond.
> 3.  **Calculate the Weighted-Average Time:** Multiply the weight of each cash flow by the time (in years) it is received. Sum up these values. The result is the Macaulay duration in years.

#### **The Duration Gap**

The **duration gap** measures the mismatch between your investment horizon and the bond's Macaulay duration. It tells you which risk you're more exposed to.

**Duration Gap = Macaulay Duration – Investment Horizon**

* **Positive Duration Gap (MacDur > Horizon):** Your horizon is shorter than the bond's balancing point. You are more exposed to **price risk**. A rise in interest rates will hurt your return.
* **Negative Duration Gap (MacDur < Horizon):** Your horizon is longer than the bond's balancing point. You are more exposed to **reinvestment risk**. A fall in interest rates will hurt your return.

> [!TIP]
> **CFA Exam Tip ✍️:** You must understand the interpretation of Macaulay duration. The exam will test your understanding of it as the investment horizon that eliminates interest rate risk. Being able to calculate it is important, but knowing what it *means* is critical.

---

### 🧪 Formula Summary

* **Macaulay Duration:**
    $\text{MacDur} = \sum_{t=1}^{N} \left[ \frac{\frac{\text{CF}_t}{(1+y)^t}}{\text{Price}} \times t \right]$
    (Conceptually: The weighted-average time to receipt of cash flows)
* **Duration Gap:**
    $\text{Duration Gap} = \text{Macaulay Duration} - \text{Investment Horizon}$

---

> [!IMPORTANT]
> ### 🎯 Quick Exam-Day Pointers
>
> * **Two Opposing Risks:** Interest rate changes create **price risk** (bad for short horizons if rates rise) and **reinvestment risk** (bad for long horizons if rates fall).
> * **Macaulay Duration is the Sweet Spot:** Macaulay duration is the investment horizon where price risk and reinvestment risk perfectly offset. If you hold a bond for a period equal to its Macaulay duration, your return is locked in.
> * **What the Duration Gap Tells You:**
>     * **Positive Gap (Horizon is short):** You're exposed to **price risk**.
>     * **Negative Gap (Horizon is long):** You're exposed to **reinvestment risk**.
> * A zero-coupon bond has no reinvestment risk, and its Macaulay duration is equal to its maturity.