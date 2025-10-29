### <span style="color: #1565C0;">Reading 53: Yield and Yield Spread Measures for Fixed-Rate Bonds 📏</span>

### <span style="color: #1565C0;">🎯 Introduction</span>

Welcome back, future charterholder\! You know how to price a bond using a yield (YTM), but what exactly *is* that yield? And how does it compare to other ways of measuring return, especially when bonds pay coupons at different frequencies? 🤔 This reading dives deep into the world of bond yields. We'll learn how to compare yields apples-to-apples, even with different compounding periods, and explore various yield measures like current yield, yield-to-call, and yield-to-worst. We'll also tackle **yield spreads** – the extra return you get for taking on more risk than Uncle Sam's bonds. Think of this as getting your toolkit ready to truly compare bond returns and understand risk premiums. Let's get yielding\!

-----

### <span style="color: #1565C0;">Part 1: Comparing Apples and Oranges - Yields & Compounding 🍎🍊 (LOS 53.a)</span>

-----
#### <span style="color: #1565C0;">Part 1.1 Yield-to-Maturity (YTM) Review</span>

Remember, YTM is the **Internal Rate of Return (IRR)** that equates the present value of a bond's promised future cash flows (coupons + principal) to its current market price. It's the total return you anticipate if you hold the bond to maturity, all payments are made, and you reinvest coupons at that same YTM.

  * **Calculation:** You typically use a financial calculator:
      * Enter $N$ (number of periods), $PV$ (current price, as negative), $PMT$ (coupon payment per period), $FV$ (face value, usually 100 or 1000).
      * Compute $I/Y$ (yield per period).
  * **Annualizing:** By convention, the quoted YTM is the periodic yield multiplied by the number of periods per year.
      * *Annual-pay bond:* Periodic yield = Annual YTM.
      * *Semiannual-pay bond:* Periodic yield = Annual YTM / 2. The quoted YTM is $2 \times$ (semiannual yield).
      * *Quarterly-pay bond:* Periodic yield = Annual YTM / 4. Quoted YTM is $4 \times$ (quarterly yield).

#### <span style="color: #1565C0;">Part 1.2 Periodicity and Effective Annual Yield (EAY)</span>

The number of coupon payments per year is the bond's **periodicity**. A semiannual bond has periodicity = 2.

The problem? A 6% YTM on a semiannual bond isn't directly comparable to a 6% YTM on an annual bond because of different compounding frequencies. The semiannual bond actually gives you a slightly better return due to compounding within the year.

To compare yields properly, we calculate the **Effective Annual Yield (EAY)**:

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$EAY = \left(1 + \frac{YTM}{\text{Periodicity}}\right)^{\text{Periodicity}} - 1$$

</div>

*Example:* A bond with a stated YTM of 10%.

  * *Semiannual (Periodicity = 2):* $EAY = (1 + 0.10/2)^2 - 1 = 1.05^2 - 1 = 10.25\%$.
  * *Quarterly (Periodicity = 4):* $EAY = (1 + 0.10/4)^4 - 1 = 1.025^4 - 1 = 10.38\%$.

**Converting Yields:** You can convert a quoted YTM from one periodicity to another by first finding the EAY, and then solving for the equivalent YTM for the desired periodicity.

*Example:* Convert a 4% YTM (semiannual basis) to an equivalent annual-pay yield and quarterly-pay yield.

1.  *Periodic Rate:* 4% / 2 = 2% per 6 months.
2.  *EAY:* $(1.02)^2 - 1 = 4.04\%$. This *is* the equivalent annual-pay yield.
3.  *Equivalent Quarterly Rate:* Find the quarterly rate $r$ such that $(1+r)^4 = 1.0404$. So, $1+r = (1.0404)^{1/4} = 1.00995$. Quarterly rate $r = 0.995\%$.
4.  *Equivalent Quarterly Quoted YTM:* $0.995\% \times 4 = 3.98\%$.

#### <span style="color: #1565C0;">Part 1.3 Other Yield Measures</span>

  * **Street Convention vs. True Yield:** Most YTM calculations use scheduled coupon dates (**street convention**). **True yield** accounts for delays if payment dates fall on weekends/holidays, making it slightly lower.

  * **Current Yield (Income/Running Yield):** Simple measure focusing only on coupon income relative to price. Ignores capital gains/losses and reinvestment income.

    <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
    
    $$\text{Current Yield} = \frac{\text{Annual Cash Coupon Payment}}{\text{Bond Price (Flat Price)}}$$
    
    </div>
    *Example:* A 20-year, \$1,000 par, 6% semiannual bond priced at \$802.07.
    *Annual Coupon:* \$0.06 × \$1000 = \$60.
    *Current Yield:* \$60 / \$802.07 = 7.48%.

  * **Simple Yield:** Adjusts current yield by adding a straight-line amortization of the discount (or subtracting amortization of the premium) over the remaining life.

    <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
    
    $$\text{Simple Yield} \approx \frac{\text{Annual Coupon} \pm \frac{\text{Par Value} - \text{Price}}{\text{Years to Maturity}}}{\text{Price}}$$
    
    </div>
    *Example:* 3-year, 8% semiannual bond priced at 90.165.
    *Discount:* $100 - 90.165 = 9.835$.
    *Annual Amortization:* $9.835 / 3 = 3.278$.
    *Simple Yield:* $(\$8 + 3.278) / 90.165 = 12.51\%$.

  * **Yield to Call (YTC):** Calculates the yield assuming the bond is called by the issuer at a specific call date and call price. Use the call date as $N$, call price as $FV$.

  * **Yield to Worst (YTW):** For a callable bond, this is the **lowest** yield among the YTM and all the possible YTCs. Banks/regulators often require bonds to be reported at YTW.

    *Example:* 5-yr, 6% semi bond at 102. Call @102 in 3 yrs (N=6), Call @101 in 4 yrs (N=8).
    *YTM (N=10, FV=100, PV=-102, PMT=3):* I/Y = 2.768%, YTM = 5.54%.
    *YTC (1st call, N=6, FV=102, PV=-102, PMT=3):* I/Y = 2.941%, YTC1 = 5.88%.
    *YTC (2nd call, N=8, FV=101, PV=-102, PMT=3):* I/Y = 2.830%, YTC2 = 5.66%.
    *YTW:* Lowest is 5.54% (the YTM in this case).

  * **Option-Adjusted Yield:** For bonds with embedded options, the yield can be conceptually adjusted to what it *would be* if the bond were option-free. This involves adding the value of the embedded call option (if callable) back to the price before calculating yield. The option-adjusted yield will be *lower* than the callable bond's YTM. This helps compare bonds with different options on a consistent basis. Think "option removed".

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️: Be comfortable converting between YTMs of different periodicities using EAY. Know the definitions and simple calculations for Current Yield and Simple Yield. Understand that YTW is the minimum of YTM and all YTCs for a callable bond. Remember that Option-Adjusted Yield < YTM for a callable bond.

</div>
</div>

-----

### <span style="color: #1565C0;">Part 2: Measuring the Premium - Yield Spreads 💰➖💰 (LOS 53.b)</span>

Bond yields reflect a risk-free rate plus premiums for various risks (credit, liquidity, etc.). A **yield spread** measures this extra return compared to a benchmark, usually a government bond of similar maturity.

-----
#### <span style="color: #1565C0;">Part 2.1 Benchmark Spreads</span>

  * **G-Spread (Government Spread):** The difference (in basis points) between a bond's YTM and the YTM of a government bond with the same (or interpolated) maturity. Used for bonds priced off government yield curves.
      * *Calculation:* Bond YTM - Benchmark Govt Bond YTM.
      * If no exact maturity benchmark exists, interpolate between the closest shorter and longer maturity government bonds.
        *Example:* A 3-yr, 8% semi bond priced at 103.165. 1-yr T-yield=3%, 4-yr T-yield=5%.
        *Bond YTM (N=6, PV=-103.165, PMT=4, FV=100):* I/Y = 3.408%, YTM = 6.82%.
        *Interpolated 3-yr T-yield:* $3\% + \frac{3-1}{4-1} \times (5\% - 3\%) = 4.33\%$.
        *G-Spread:* $6.82\% - 4.33\% = 2.49\%$ or 249 bps.
  * **I-Spread (Interpolated Spread):** The difference between a bond's YTM and standard **swap rates** (fixed rates in interest rate swaps) of the same maturity. Often used for Eurobonds. Swap rates represent interbank risk levels.

**Why Use Spreads?** Changes in a bond's yield can come from:

1.  **Macroeconomic factors:** Affecting the benchmark yield (e.g., changes in inflation expectations, central bank policy).
2.  **Microeconomic factors:** Affecting the spread (e.g., changes in the issuer's creditworthiness, issue liquidity).
      * If yield increases but spread is constant $\implies$ Macro factors drove benchmark yields up.
      * If yield spread increases $\implies$ Micro factors specific to the bond/issuer occurred.

#### <span style="color: #1565C0;">Part 2.2 Spreads Over the Spot Curve</span>

YTM is a single average rate, but reality is more complex – different cash flows should arguably be discounted at different rates based on their timing (**spot rates**). Spreads calculated using the entire benchmark *spot curve* are more precise.

  * **Z-Spread (Zero-Volatility Spread):** The **constant spread** (in basis points) that must be added to *each* spot rate on the benchmark (e.g., Treasury) spot curve to make the present value of the bond's cash flows equal its current market price. It accounts for the shape of the spot curve.

    <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
    
    $$\text{Price} = \frac{CF_1}{(1+S_1+Z)} + \frac{CF_2}{(1+S_2+Z)^2} + ... + \frac{CF_N+Par}{(1+S_N+Z)^N}$$
    (Where $S_i$ are benchmark spot rates, $Z$ is the Z-spread)
    
    </div>

      * Calculated via iteration (trial-and-error).
        *Example:* 3-yr, 9% annual bond at 89.464. Treasury spot rates: S1=4%, S2=8.167%, S3=12.377%. 3-yr T-YTM = 12%.
        *G-Spread:* Bond YTM (13.50%) - T-YTM (12%) = 1.50% or 150 bps.
        *Z-Spread:* Find ZS such that $89.464 = \frac{9}{(1.04+ZS)^1} + \frac{9}{(1.08167+ZS)^2} + \frac{109}{(1.12377+ZS)^3}$.
        *Solution (via iteration):* ZS = 1.67% or 167 bps. Notice Z-Spread > G-Spread because the spot curve is upward sloping.

  * **Option-Adjusted Spread (OAS):** Used for bonds with **embedded options**. It's the Z-spread *after* the value of the embedded option has been removed. Think of it as the spread for credit and liquidity risk *only*, excluding the spread component related to the option.

      * Uses complex option pricing models to value the embedded option.
      * **For a callable bond:** Option value is positive (benefits issuer). OAS = Z-Spread - Option Value (in bps). Therefore, **OAS < Z-Spread**. The difference represents compensation to the investor for the call risk.
      * **For a putable bond:** Option value is positive (benefits investor). Z-Spread = OAS - Option Value. Therefore, **OAS > Z-Spread**. (Though the calculation is more complex in practice).

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️: Know the difference between G-Spread (vs. govt bond YTM) and I-Spread (vs. swap rate). Understand Z-Spread as the constant spread over the benchmark *spot curve*. For OAS, remember the key relationship for callable bonds: **OAS = Z-Spread - Option Value**, meaning OAS < Z-Spread. OAS isolates credit and liquidity spread from the option component.

</div>
</div>

-----

### <span style="color: #1565C0;">🧪 Formula Summary</span>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Effective Annual Yield (EAY):**
$$EAY = \left(1 + \frac{YTM}{\text{Periodicity}}\right)^{\text{Periodicity}} - 1$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Current Yield:**
$$\text{Current Yield} = \frac{\text{Annual Cash Coupon Payment}}{\text{Bond Price}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Simple Yield (Approximate):**
$$\text{Simple Yield} \approx \frac{\text{Annual Coupon} \pm \text{Straight-Line Amortization}}{\text{Price}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**G-Spread:**
$$\text{G-Spread} = \text{Bond YTM} - \text{Government Bond YTM (interpolated if needed)}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**I-Spread:**
$$\text{I-Spread} = \text{Bond YTM} - \text{Swap Rate (interpolated if needed)}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Z-Spread (Conceptual):** Find Z such that
$$\text{Price} = \sum_{i=1}^{N} \frac{CF_i}{(1+S_i+Z)^i}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**OAS for Callable Bond:**
$$\text{OAS} = \text{Z-Spread} - \text{Option Value (bps)}$$

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### <span style="color: #1565C0;">🎯 Quick Exam-Day Pointers</span>

<div style="color: #000000; font-weight: 500;">

  * **EAY is King:** Always convert yields to EAY to compare bonds with different coupon frequencies. Know the formula!
  * **Yield Hierarchy:** For a discount bond (Price < Par), Coupon Rate < Current Yield < YTM. For a premium bond (Price > Par), Coupon Rate > Current Yield > YTM.
  * **Callable Bonds:** Remember YTW is the minimum of YTM and all YTCs.
  * **Spreads Measure Risk:** G-Spread and I-Spread compare YTM to benchmarks (govt bonds or swaps).
  * **Z-Spread vs. Spot Curve:** Z-Spread is the constant spread added to the *entire* benchmark spot curve to match the bond's price.
  * **OAS Removes Option:** OAS adjusts the Z-spread for embedded options, reflecting only credit/liquidity risk. For callable bonds, **OAS < Z-Spread**.

</div>
</div>