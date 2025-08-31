## Reading 53: Yield and Yield Spread Measures for Fixed-Rate Bonds 📏

🎯 **Introduction**

Imagine you're shopping for fruit and see one sign for "Apples: ₹50 per half-dozen" and another for "Oranges: ₹100 per dozen." Which is a better deal? You can't compare them directly; you first need to get them to a common unit, like price per piece. It's the same with bonds! A bond paying coupons semi-annually isn't directly comparable to one paying annually. This reading teaches us how to convert bond yields into a common language—the **effective annual yield**—so we can make true apples-to-apples comparisons. We'll also dive into **yield spreads**, which measure the extra return a bond offers over an ultra-safe benchmark, telling us how much we're being paid for taking on extra risk.

---

### Part 1: Making Yields Comparable: Periodicity & Effective Annual Yield 🍎 vs 🍊

A bond's **periodicity** is the number of coupon payments it makes per year (e.g., 1 for annual, 2 for semi-annual, 4 for quarterly). A bond's quoted **Yield to Maturity (YTM)** is stated based on its periodicity. For a semi-annual bond, the quoted YTM is simply the semi-annual interest rate multiplied by two. This is a simple annual rate, not a true compounded rate.

To accurately compare bonds with different coupon frequencies, we must convert their quoted YTMs into an **effective annual yield**, which accounts for the power of compounding.

**Formula: Effective Annual Yield**
$\text{Effective Annual Yield} = \left(1 + \frac{\text{Quoted YTM}}{n}\right)^n - 1$
where `n` is the periodicity.

> **Example Time! 🧮**
> A bond has a quoted YTM of 10%.
> * **If it pays semi-annually (n=2):**
>     Effective Annual Yield = $(1 + \frac{0.10}{2})^2 - 1 = (1.05)^2 - 1 = 10.25\%$
> * **If it pays quarterly (n=4):**
>     Effective Annual Yield = $(1 + \frac{0.10}{4})^4 - 1 = (1.025)^4 - 1 = 10.38\%$
>
> As you can see, the more frequent the compounding, the higher the true annual return!

---

### Part 2: Quick & Simple Yield Measures 🔢

While YTM is the most comprehensive measure, analysts sometimes use simpler metrics for a quick assessment.

* **Current Yield (or Income Yield):** This is a very basic measure of a bond's return. It only considers the annual coupon interest and ignores any capital gain or loss from the price pulling to par, as well as reinvestment income.
    $\text{Current Yield} = \frac{\text{Annual Cash Coupon Payment}}{\text{Bond Price}}$

* **Simple Yield:** This is a slightly more sophisticated measure. It takes the annual coupon and adds (for a discount bond) or subtracts (for a premium bond) a straight-line amortization of the discount/premium. This gives a better approximation of the total return than the current yield.

---

### Part 3: What's the Yield for a Callable Bond? 📞

For a callable bond, the future is uncertain. The issuer might redeem the bond early, which changes the investor's realized yield. So, we must calculate a few different yield measures.

* **Yield to Call (YTC):** This is the bond's yield calculated assuming it is called on a specific call date at the specified call price. A bond may have several call dates, so you would calculate a YTC for each one.
* **Yield to Worst (YTW):** This is the most conservative measure. It is simply the **lowest** yield an investor could possibly receive among all the calculated YTCs and the YTM. If you buy a callable bond, you should assume you will earn the YTW.

> [!TIP]
> **CFA Exam Tip ✍️:** When pricing a callable bond that's trading at a premium, the Yield to Worst will often be a Yield to Call, because the issuer is likely to call the bond. When it's trading at a discount, the YTW is often the Yield to Maturity, as the issuer has no incentive to call it.

* **Option-Adjusted Yield:** This is a theoretical yield used for comparison purposes. It estimates what the yield on the callable bond *would be* if it didn't have the call feature. This "option-removed" yield allows for a fair comparison to non-callable (**straight**) bonds.

---

### Part 4: Measuring the Extra Return: Yield Spreads 📏

A **yield spread** is the difference between a bond's YTM and the yield of a benchmark security (usually a risk-free government bond of the same maturity). It's the extra yield you earn for taking on risks like credit risk and liquidity risk.

#### **Common Spread Measures**
* **G-Spread (Government Spread):** The yield spread over a government bond yield. If a government bond with the exact same maturity doesn't exist, the benchmark yield is interpolated from the yields of the closest-maturity government bonds.
* **I-Spread (Interpolated Spread):** The yield spread over a standard swap rate. This is widely used as the benchmark in many markets, especially in Europe, as it reflects the default risk of commercial banks rather than the government.

#### **Advanced Spread Measures**
The G-Spread and I-Spread are simple but have a flaw: they compare a bond's single YTM to a benchmark's single YTM, ignoring the overall shape of the yield curve. More advanced measures fix this.

* **Z-Spread (Zero-Volatility Spread):** A more precise measure. The **Z-spread** is the single, constant spread that must be added to *every spot rate* on the risk-free spot curve to make the present value of the risky bond's cash flows equal to its market price. It correctly accounts for the term structure of interest rates.
* **Option-Adjusted Spread (OAS):** This is the ultimate spread measure for bonds with embedded options. The OAS takes the Z-spread and *removes* the component that is compensating the investor for the option risk.
    * For a **callable bond** (which has a call option that benefits the issuer), the investor demands extra yield for the call risk.
        $\text{OAS} = \text{Z-spread} - \text{Option Value}$
    * The OAS represents the pure compensation for credit and liquidity risk, allowing for a true comparison between callable, putable, and straight bonds.

---

### 🧪 Formula Summary

* **Effective Annual Yield:** $\text{EAY} = \left(1 + \frac{\text{YTM}}{n}\right)^n - 1$
* **Current Yield:** $\text{Current Yield} = \frac{\text{Annual Coupon}}{\text{Price}}$
* **Option-Adjusted Spread (for a callable bond):** $\text{OAS} = \text{Z-Spread} - \text{Call Option Value (in basis points)}$

---

> [!IMPORTANT]
> ### 🎯 Quick Exam-Day Pointers
>
> * **Compare Apples to Apples:** Always use the **effective annual yield** to compare bonds with different coupon frequencies.
> * **Yield to Worst (YTW) is Key:** For callable bonds, the YTW is the most important and conservative yield measure to consider.
> * **Z-Spread > G-Spread:** The **Z-spread** is a more accurate measure of the spread over the benchmark curve than the G-spread because it accounts for the shape of the spot rate curve.
> * **OAS = Option Removed:** The **Option-Adjusted Spread (OAS)** is the spread for credit and liquidity risk *after* the influence of the embedded option has been stripped away. For a callable bond, **OAS will be lower than the Z-Spread**.