## Reading 53: Yield and Yield Spread Measures for Fixed-Rate Bonds

### 🎯 Introduction

Imagine you're shopping for fruit and see one sign for "Apples: ₹50 per half-dozen" and another for "Oranges: ₹100 per dozen." Which is a better deal? You can't compare them directly; you first need to get them to a common unit, like price per piece. It's the same with bonds! A bond paying coupons semi-annually isn't directly comparable to one paying annually. This reading teaches us how to convert bond yields into a common language—the **effective annual yield**—so we can make true apples-to-apples comparisons. We'll also dive into **yield spreads**, which measure the extra return a bond offers over an ultra-safe benchmark, telling us how much we're being paid for taking on extra risk.

-----

### <span style="color: #1565C0;">Part 1: Making Yields Comparable: Periodicity & Effective Annual Yield 🍎 vs 🍊</span>

A bond's **periodicity** is the number of coupon payments it makes per year (e.g., 1 for annual, 2 for semi-annual, 4 for quarterly). A bond's quoted **Yield to Maturity (YTM)** is stated based on its periodicity. For a semi-annual bond, the quoted YTM is simply the semi-annual interest rate multiplied by two. This is a simple annual rate, not a true compounded rate.

To accurately compare bonds with different coupon frequencies, we must convert their quoted YTMs into an **effective annual yield**, which accounts for the power of compounding.

#### <span style="color: #6A1B9A;">1.1 Effective Annual Yield Formula</span>

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$\text{Effective Annual Yield} = \left(1 + \frac{\text{Quoted YTM}}{n}\right)^n - 1$$

</div>

where $n$ is the periodicity.

#### <span style="color: #6A1B9A;">1.2 Example Calculation</span>

* **Example:**
  * Quoted YTM = **10%**
    * If semi-annual ($n=2$):
      <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
      $$(1 + 0.10/2)^2 - 1 = (1.05)^2 - 1 = 10.25\%$$
      </div>
    * If quarterly ($n=4$):
      <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
      $$(1 + 0.10/4)^4 - 1 = (1.025)^4 - 1 = 10.38\%$$
      </div>
  * As compounding frequency increases, the true annual return rises. ⬆️

-----

### <span style="color: #1565C0;">Part 2: Quick & Simple Yield Measures 🔢</span>

#### <span style="color: #6A1B9A;">2.1 Current Yield</span>

* **Current Yield (or Income Yield):**
  Only considers the annual coupon interest and ignores capital gain/loss and reinvestment income.

  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
  $$\text{Current Yield} = \frac{\text{Annual Cash Coupon Payment}}{\text{Bond Price}}$$
  </div>

#### <span style="color: #6A1B9A;">2.2 Simple Yield</span>

* **Simple Yield:**
  Adds (for discount bond) or subtracts (for premium bond) a straight-line amortization of the discount/premium for a better approximation of total return than current yield.

-----

### <span style="color: #1565C0;">Part 3: Yield Measures for Callable Bonds 📞</span>

For a callable bond, the future is uncertain. The issuer might redeem the bond early, which changes the investor's realized yield. So, we must calculate a few different yield measures.

#### <span style="color: #6A1B9A;">3.1 Yield to Call (YTC)</span>
* Calculated assuming the bond is called on a specific call date at the specified call price. Multiple call dates mean multiple YTCs.

#### <span style="color: #6A1B9A;">3.2 Yield to Worst (YTW)</span>
* The **lowest** yield among all calculated YTCs and the YTM. For callable bonds, assume you will earn the YTW. ❌

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 CFA Exam Tip ✍️:**
When pricing a callable bond that's trading at a **premium**, the Yield to Worst will often be a Yield to Call, because the issuer is likely to call the bond. When it's trading at a **discount**, the YTW is often the Yield to Maturity, as the issuer has no incentive to call it.

</div>
</div>

#### <span style="color: #6A1B9A;">3.3 Option-Adjusted Yield</span>
* Theoretical yield for comparison. Estimates what the yield on the callable bond *would be* if it didn't have the call feature. Allows fair comparison to non-callable (**straight**) bonds.

-----

### <span style="color: #1565C0;">Part 4: Yield Spreads 📏</span>

A **yield spread** is the difference between a bond's YTM and the yield of a benchmark security (usually a risk-free government bond of the same maturity). It's the extra yield you earn for taking on risks like credit risk and liquidity risk.

#### <span style="color: #6A1B9A;">4.1 Common Spread Measures</span>
* **G-Spread (Government Spread):**
  Yield spread over a government bond yield. If a government bond with the exact same maturity doesn't exist, the benchmark yield is interpolated from the yields of the closest-maturity government bonds.
* **I-Spread (Interpolated Spread):**
  Yield spread over a standard swap rate. Used widely as the benchmark in many markets, especially in Europe, as it reflects the default risk of commercial banks rather than the government.

#### <span style="color: #6A1B9A;">4.2 Advanced Spread Measures</span>
* **Z-Spread (Zero-Volatility Spread):**
  The single, constant spread that must be added to *every spot rate* on the risk-free spot curve to make the present value of the risky bond's cash flows equal to its market price. Correctly accounts for the term structure of interest rates.
* **Option-Adjusted Spread (OAS):**
  The ultimate spread measure for bonds with embedded options. The OAS takes the Z-spread and *removes* the component compensating the investor for the option risk.
  * For a **callable bond** (call option benefits issuer), investor demands extra yield for call risk.
    <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
    $$\text{OAS} = \text{Z-spread} - \text{Option Value}$$
    </div>
  * The OAS represents pure compensation for credit and liquidity risk, allowing true comparison between callable, putable, and straight bonds.

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Effective Annual Yield:**
$$\text{EAY} = \left(1 + \frac{\text{YTM}}{n}\right)^n - 1$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Current Yield:**
$$\text{Current Yield} = \frac{\text{Annual Coupon}}{\text{Price}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Option-Adjusted Spread (for a callable bond):**
$$\text{OAS} = \text{Z-Spread} - \text{Call Option Value (in basis points)}$$

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* **Compare Apples to Apples:**
  Always use the **effective annual yield** to compare bonds with different coupon frequencies. ✅
* **Yield to Worst (YTW) is Key:**
  For callable bonds, the YTW is the most important and conservative yield measure to consider. ❌
* **Z-Spread > G-Spread:**
  The **Z-spread** is a more accurate measure of the spread over the benchmark curve than the G-spread because it accounts for the shape of the spot rate curve. ⬆️
* **OAS = Option Removed:**
  The **Option-Adjusted Spread (OAS)** is the spread for credit and liquidity risk *after* the influence of the embedded option has been stripped away. For a callable bond, **OAS will be lower than the Z-Spread**. ⬇️

</div>
</div>