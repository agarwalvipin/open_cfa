## Reading 54: Yield and Yield Spread Measures for Floating-Rate Instruments 🚀

### 🎯 Introduction

Alright, future CFA charterholder, let's switch gears! We've tackled fixed-rate bonds, but the debt world isn't always static. Welcome to **Floating-Rate Notes (FRNs)** – bonds whose coupon payments move with market rates – and the unique realm of **Money Market Instruments**, the short-term sprinters of the fixed-income world 🏃💨.

Think of FRNs as bonds that adapt to changing interest rate weather 🌦️. Their yields reset periodically. Money market instruments, on the other hand, mature in less than a year, but figuring out their *true* yield can feel like navigating a maze due to different quoting conventions 🧭. This reading equips you to understand how FRNs are priced relative to their risk and how to accurately compare yields on various short-term debt instruments. Let's decode these dynamic yields!

-----

### <span style="color: #1565C0;">Part 1: Floating-Rate Notes (FRNs) - Riding the Rate Wave 🌊 (LOS 54.a)</span>

FRNs are bonds whose coupon payments aren't fixed forever. Instead, they adjust based on a market benchmark plus a little extra.

#### <span style="color: #6A1B9A;">1.1 FRN Basics</span>

* **Coupon Structure:** The coupon rate on an FRN typically resets periodically (e.g., quarterly or semi-annually) based on a specified **Market Reference Rate (MRR)**, like SOFR or EURIBOR, plus a fixed **spread** or **margin**. 
    * Formula: `Coupon Rate = MRR + Quoted Margin (QM)`
* **Why FRNs?** They offer investors protection against rising interest rates (coupons go up) and issuers often use them when they prefer floating-rate funding.
* **Price Stability:** Because the coupon resets to current market rates (plus the margin), the price of an FRN tends to stay much closer to par value compared to fixed-rate bonds of similar maturity, especially around reset dates. 

#### <span style="color: #6A1B9A;">1.2 Quoted Margin vs. Discount Margin - The Spread Showdown!</span>

This is crucial for understanding FRN pricing *between* reset dates or if the issuer's creditworthiness changes.

* **Quoted Margin (QM):** The fixed spread *specified in the bond indenture* that is added to the MRR to calculate the coupon payment. 
* **Required Margin / Discount Margin (DM):** The spread *required by the market* to compensate for the issuer's current credit risk (and liquidity, etc.). This is the spread that would make the FRN trade at par *today*. 

**The Relationship Dictates Price:** 

<div style="background-color: #F3E5F5; border-left: 5px solid #7B1FA2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 MNEMONIC: "QM vs DM = Coupon vs Yield"**
  - Think of QM like the bond's stated coupon spread and DM like the market's required yield spread.
  - If **QM = DM**: Market requires what the bond offers -> **Price = Par** (Happy equilibrium!) 😊
  - If **QM < DM**: Market requires *more* spread than the bond offers (coupon spread is deficient) -> **Price < Par** (Discount) 😟
  - If **QM > DM**: Market requires *less* spread than the bond offers (coupon spread is generous) -> **Price > Par** (Premium) 😎

</div>
</div>

* **Why does the price change?** If an issuer's credit quality worsens after issuance, investors will demand a higher spread (DM increases). Since the QM is fixed, the bond must trade at a discount to offer the higher required yield. The opposite happens if credit quality improves. 

#### <span style="color: #6A1B9A;">1.3 Valuing an FRN (Simplified Method on Reset Date)</span>

While complex models exist, a common way to *estimate* an FRN's value involves using the current MRR + QM for future coupons and discounting them back at the current MRR + DM. 

*Example: FRN Valuation*
A $100,000 face value FRN pays semi-annually: 180-day MRR + 1.20% (QM).
Today is a reset date, 5 years (10 periods) left.
Current 180-day MRR = 3.0% (annualized).
Current Discount Margin (DM) = 1.5% (annualized).

1.  **Calculate the next coupon payment (per $100 par):**
    * Annualized Coupon Rate = MRR + QM = 3.0% + 1.2% = 4.2% 
    * Semi-annual Coupon Payment (PMT) = (4.2% / 2) * $100 = $2.10 
2.  **Calculate the periodic discount rate (per $100 par):**
    * Annualized Required Rate = MRR + DM = 3.0% + 1.5% = 4.5% 
    * Semi-annual Discount Rate (I/Y) = 4.5% / 2 = 2.25% 
3.  **Calculate the FRN Price (PV using financial calculator):**
    * N = 10 (5 years * 2 periods/year)
    * I/Y = 2.25
    * PMT = 2.10
    * FV = 100
    * CPT PV = -98.67 
    * Estimated Value = $98.67 per $100 par, or $98,670 for the $100k note. 
    * *Interpretation:* Because the required margin (DM = 1.5%) is higher than the quoted margin (QM = 1.2%), the FRN trades at a discount. 

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️: Understand the QM vs. DM relationship and its impact on the FRN's price relative to par. This is a common exam concept! Remember QM is fixed, DM reflects current market requirements.

</div>
</div>

-----

### <span style="color: #1565C0;">Part 2: Money Market Instruments - Short-Term Yield Maze 🧭 (LOS 54.b)</span>

Money market instruments are debt securities maturing in one year or less.  Their yields seem simple, but watch out! They are quoted using different conventions, making direct comparison tricky. 

#### <span style="color: #6A1B9A;">2.1 The Quoting Conventions Chaos</span>

Key differences to watch for: 
* **Basis:** 360-day year vs. 365-day year.
* **Yield Type:** Discount Yield vs. Add-on Yield.

| Convention        | Instruments Typically Using It         | Calculation Basis                                  |
| :---------------- | :------------------------------------- | :------------------------------------------------- |
| **Discount Yield (DR)** | U.S. T-bills, Commercial Paper (CP)  | Annualized % discount from *face value*. Usually uses a *360-day* year.  |
| **Add-on Yield (AOR)** | Bank CDs, Repos, MRRs        | Annualized % interest added to *purchase price*. Can use *360 or 365* days.  |

#### <span style="color: #6A1B9A;">2.2 Key Yield Measures Defined</span>

* **Holding Period Yield (HPY):** The *actual* unannualized return earned over the holding period. The foundation for other calculations.
    * `HPY = (Maturity Value - Purchase Price + Interest Received) / Purchase Price`
    * For discount instruments: `HPY = (Face Value / Purchase Price) - 1`
    * For add-on instruments: `HPY = Interest Received / Purchase Price`
* **Discount Yield (DR):** As defined above. Formula: 
    * `DR = ( (Face Value - Purchase Price) / Face Value ) * (360 / Days to Maturity)`
    * Note: It uses Face Value in the denominator, understating the true return.
* **Add-on Yield (AOR):** As defined above. Formula: 
    * `AOR (365 basis) = HPY * (365 / Days to Maturity)`
    * `AOR (360 basis) = HPY * (360 / Days to Maturity)`
* **Bond Equivalent Yield (BEY):** The standard convention used to make money market yields comparable to semi-annual U.S. Treasury note yields. It's simply an **Add-on Yield based on a 365-day year**. 
    * `BEY = HPY * (365 / Days to Maturity)`

#### <span style="color: #6A1B9A;">2.3 Converting Between Yields - The Rosetta Stone! 💎</span>

You *must* be able to convert between these yields. The key is often to first find the HPY.

*Example: Money Market Conversions*

1.  **T-Bill (Discount Yield -> Price & BEY):** 
    * $1,000 face value, 90-day T-bill, 1.2% discount yield (360-day basis).
    * *Actual Discount* = Face Value * DR * (Days / 360) = $1,000 * 0.012 * (90 / 360) = $3.00 
    * *Purchase Price* = Face Value - Discount = $1,000 - $3.00 = $997.00 
    * *HPY* = (Face Value / Price) - 1 = ($1,000 / $997) - 1 = 0.3009% 
    * *BEY* = HPY * (365 / Days) = 0.003009 * (365 / 90) = 1.2203% 

2.  **CD (Add-on Yield -> Maturity Payment & BEY):** 
    * $1 million face value, 120-day CD, 1.4% add-on yield (365-day basis).
    * *HPY* = AOR * (Days / 365) = 0.014 * (120 / 365) = 0.4603% 
    * *Interest* = Face Value * HPY = $1,000,000 * 0.004603 = $4,603
    * *Maturity Payment* = Face Value + Interest = $1,000,000 + $4,603 = $1,004,603 
    * *BEY:* Since the quote was already an add-on yield on a 365-day basis, BEY = 1.4%. 

3.  **Bank Deposit (360-day AOR -> BEY & Semiannual Bond Basis):**
    * 100-day deposit, 1.5% add-on yield (360-day basis).
    * *BEY* = AOR * (365 / 360) = 0.015 * (365 / 360) = 1.5208% 
    * *To compare with a semi-annual bond:*
        * *HPY* = AOR * (Days / 360) = 0.015 * (100 / 360) = 0.4167% 
        * *Effective Annual Yield (EAY)* = (1 + HPY)^(365 / Days) - 1 = (1.004167)^(365 / 100) - 1 = 1.5294% 
        * *Convert EAY to Semiannual Bond Basis:*
            * Periodic Semiannual Rate = (1 + EAY)^0.5 - 1 = (1.015294)^0.5 - 1 = 0.7618% 
            * Yield (Semiannual Bond Basis) = Periodic Rate * 2 = 0.7618% * 2 = 1.5236% 

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️: Practice these conversions! Know that BEY (Bond Equivalent Yield) is the standard for comparison and is an Add-on Yield using 365 days. To convert anything to BEY, first find the HPY, then annualize using `(365 / Days)`. Be careful with discount yields – they use face value in the denominator.

</div>
</div>

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**FRN Coupon:**

$$\text{Coupon Rate} = \text{MRR} + \text{Quoted Margin (QM)}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Holding Period Yield (HPY):**

$$\text{HPY} = \frac{\text{Maturity Value}}{\text{Purchase Price}} - 1 \quad \text{(For discount instruments)}$$

$$\text{HPY} = \frac{\text{Interest} + \text{Price Change}}{\text{Purchase Price}} \quad \text{(General)}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Discount Yield (DR) (usually 360 days):**

$$\text{DR} = \frac{\text{Discount}}{\text{Face Value}} \times \frac{360}{\text{Days}}$$

$$\text{Price} = \text{Face Value} \times \left[1 - \text{DR} \times \frac{\text{Days}}{360}\right]$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Add-on Yield (AOR) (360 or 365 days):**

$$\text{AOR} = \text{HPY} \times \frac{\text{Year Basis}}{\text{Days}}$$

$$\text{Interest} = \text{Face Value} \times \text{AOR} \times \frac{\text{Days}}{\text{Year Basis}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Bond Equivalent Yield (BEY):**

$$\text{BEY} = \text{HPY} \times \frac{365}{\text{Days}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Effective Annual Yield (EAY) from HPY:**

$$\text{EAY} = (1 + \text{HPY})^{\frac{365}{\text{Days}}} - 1$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Convert EAY to Semiannual Bond Basis Yield:**

$$\text{Semiannual Yield} = \left[(1 + \text{EAY})^{0.5} - 1\right] \times 2$$

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* **FRN Pricing:** Remember QM vs. DM. If Market Requires More (DM > QM), Price is Discount (< Par). If Market Requires Less (DM < QM), Price is Premium (> Par).
* **Money Market Maze:** Different instruments use different quote conventions (Discount vs. Add-on, 360 vs. 365 days).
* **HPY is Key:** Calculate the actual Holding Period Yield first before annualizing.
* **BEY is the Standard:** Bond Equivalent Yield = HPY * (365 / Days). It's an Add-on rate using 365 days.
* **Discount Yield Quirks:** Based on Face Value, not price. Usually uses 360 days. DR < HPY < BEY (for discount instruments).
* **Add-on Yield:** Based on Purchase Price. Can use 360 or 365 days. AOR (365) *is* the BEY.
* **Comparisons:** Always convert yields to a common basis (like BEY or EAY) before comparing returns.

</div>
</div>