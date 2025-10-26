## Reading 58: Yield-Based Bond Convexity and Portfolio Properties

-----

### <span style="color: #1565C0;">Part 1: Convexity—The Curve in Bond Pricing (LOS 58.a)</span>

**Introduction**

Imagine you're trying to predict the path of a gently curving road using only a straight ruler. For a short distance, your ruler gives a pretty good estimate. But the further you go, the more the road curves away from your straight line. In the last reading, **Modified Duration** was our straight ruler—a great linear estimate for small changes in yield. This reading introduces **Convexity**, the tool that measures the actual *curve* in the price-yield relationship. By adding a convexity adjustment, we can make our price predictions dramatically more accurate, especially for large swings in interest rates.

#### <span style="color: #6A1B9A;">1.1 Why Duration Alone Isn't Enough</span>

* **The Problem with Duration:** For any change in yield (up or down), duration *underestimates* the bond's new price.
* **The Solution:** **Convexity** measures this curvature. For an option-free bond, it is always a positive number.

**Why Investors Love Convexity ❤️**
* When yields **fall**, the bond's price **increases by more** than duration predicted. (You get a bigger capital gain! ✅)
* When yields **rise**, the bond's price **decreases by less** than duration predicted. (Your capital loss is smaller! ⬇️)
* This asymmetrical effect means that for two bonds with the same duration, the one with higher convexity is more desirable and will have a higher price.

Like duration, we can estimate convexity by "shocking" the bond's price up and down.

##### <span style="color: #E65100;">1.1.1 Approximate Convexity Formula</span>

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\text{Approximate Convexity} = \frac{V_- + V_+ - (2 \times V_0)}{(\Delta\text{YTM})^2 \times V_0}$$

where:
* $V_-$ = Price if yield falls
* $V_+$ = Price if yield rises
* $V_0$ = Initial price

</div>

-----

### <span style="color: #1565C0;">Part 2: Convexity Adjustment—Better Price Predictions (LOS 58.b)</span>

To get a much more precise estimate of a bond's price change, we combine the linear estimate from duration with a second-order adjustment for convexity.

#### <span style="color: #6A1B9A;">2.1 Full Percentage Price Change Estimate</span>

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\%\Delta \text{Price} \approx [- \text{ModDur} \times \Delta\text{YTM}] + [ \frac{1}{2} \times \text{Convexity} \times (\Delta\text{YTM})^2 ]$$

</div>

**Example Time! 🧮**

A bond has a ModDur of 3.50 and a Convexity of 16.9. Let's estimate the price change for a 50 basis point (0.50%) decrease in its YTM.

* **Duration Effect:**  
  -3.50 × (-0.005) = +0.0175 or **+1.75%**
* **Convexity Adjustment:**  
  0.5 × 16.9 × (-0.005)^2 = +0.000211 or **+0.021%**
* **Total Estimated Change:**  
  +1.75% + 0.021% = **+1.771%**

As you can see, the convexity adjustment adds to the price increase, giving a more accurate (and slightly higher) final price estimate.

Just like with duration, we can also calculate **Money Convexity** to see the impact in currency terms.

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\text{Money Convexity} = \text{Annual Convexity} \times \text{Full Price of Bond Position}$$

</div>

-----

### <span style="color: #1565C0;">Part 3: Portfolio Convexity—Aggregating Across Bonds (LOS 58.c)</span>

How do we measure the duration and convexity of a portfolio containing many different bonds? There are two ways:

* **The Cash Flow Approach:** Treat the entire portfolio as one giant, complex bond. Combine all the individual cash flows from all the bonds and calculate the duration and convexity of this aggregate cash flow stream. This method is theoretically perfect but computationally very difficult.
* **The Weighted-Average Approach:** This is the practical and commonly used method. You simply calculate the weighted average of the modified durations (or convexities) of the individual bonds in the portfolio. The weight for each bond is its market value as a proportion of the total portfolio's market value.

#### <span style="color: #6A1B9A;">3.1 Portfolio Duration & Convexity Formulas</span>

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\text{Portfolio Duration} = (w_1 \times D_1) + (w_2 \times D_2) + \dots + (w_n \times D_n)$$

$$\text{Portfolio Convexity} = (w_1 \times C_1) + (w_2 \times C_2) + \dots + (w_n \times C_n)$$

</div>

**🚨 A CRUCIAL LIMITATION 🚨**

The weighted-average approach has one major weakness: it assumes that when interest rates change, the yield for every single bond in the portfolio changes by the exact same amount. This is called a **parallel shift** in the yield curve. In the real world, short-term and long-term rates often move by different amounts (the curve twists or flattens). Therefore, portfolio duration is only an approximation of the portfolio's true interest rate sensitivity.

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Convexity of a Single Cash Flow:**  
$$\text{Convexity}_t = \frac{t(t+1)}{(1+r)^{2}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Approximate Convexity:**  
$$\text{Convexity} = \frac{V_- + V_+ - (2V_0)}{(\Delta\text{YTM})^2 \times V_0}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Percentage Price Change (with Convexity):**  
$$\%\Delta \text{Price} \approx [- \text{ModDur} \times \Delta\text{YTM}] + [ \frac{1}{2} \times \text{Convexity} \times (\Delta\text{YTM})^2 ]$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Portfolio Duration (Weighted Average):**  
$$D_p = w_1D_1 + w_2D_2 + \dots + w_nD_n$$

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* **Convexity Corrects Duration:** Duration is a linear estimate. **Convexity** measures the curvature of the price-yield curve and makes price estimates more accurate, especially for large yield changes.
* **Convexity is Your Friend:** For an option-free bond, the convexity adjustment is **always positive**. This is good for you as a bondholder! ✅ It means you gain more when rates fall and lose less when rates rise compared to what duration alone predicts.
* **Portfolio Duration's Big Assumption:** Calculating portfolio duration as a weighted average of individual bond durations is common, but it relies on the major assumption of a **parallel shift** in the yield curve. ❌ Be aware of this limitation.

</div>
</div>