## Reading 48: Fixed-Income Cash Flows and Types 💸

### 🎯 Introduction

Imagine you lend money to a friend. How do they pay you back? Do they give you a little bit of interest every month and then the full amount at the very end? That's a **bullet** payment. Or do they pay you back in equal installments that include both interest and a piece of the original loan, so by the end, it's all paid off? That's an **amortizing** loan. Bonds work in similar ways! This reading explores the different cash flow structures a bond can have, from simple to complex. We'll also look at special features like options that can be embedded within a bond, giving either the borrower or the lender a unique advantage.

-----

### <span style="color: #1565C0;">Part 1: How Do Bonds Repay the Money? Cash Flow Structures 🌊</span>

Not all bonds pay back their principal at the end. The structure of cash flows can vary significantly, which affects the bond's risk and return profile.

#### <span style="color: #6A1B9A;">1.1 Bullet Structure 🎯</span>
* **Bullet Structure:**  
  The issuer makes regular interest-only payments (**coupons**) throughout the bond's life. Then, at maturity, the entire **principal** (the face value) is repaid in one single "bullet" payment.

#### <span style="color: #6A1B9A;">1.2 Amortizing Structure 🏡</span>
* **Amortizing Structure:**  
  Each payment consists of both interest and a portion of the principal.
  * **Fully Amortizing:** The loan is completely paid off with the final periodic payment. There is no lump-sum principal payment at the end.
  * **Partially Amortizing with a Balloon Payment:** Each payment includes some principal, but not enough to pay it off entirely. A large lump-sum of the remaining principal, called a **balloon payment**, is due at maturity.

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

**Example: Fully vs. Partially Amortizing 🧮**

A 5-year, $1,000 bond with a 5% interest rate.  
* **Fully Amortizing:** The issuer would make 5 equal annual payments of $230.97. After the last payment, the loan is fully paid off.  
  (Calculator: N=5, I/Y=5, PV=1000, FV=0, CPT PMT)
* **Partially Amortizing (with $200 balloon):** The issuer would make 5 smaller annual payments of $194.78$, and the final payment would also include the $200$ balloon payment.

(Calculator: $N=5$, $I/Y=5$, $PV=1000$, $FV=-200$, CPT $PMT$)

</div>

#### <span style="color: #6A1B9A;">1.3 Sinking Fund Provisions 📉</span>
* **Sinking Fund Provisions:**  
  To reduce the risk of not being able to make a huge principal payment at maturity, an issuer might use a **sinking fund**. This provision requires the issuer to set aside money and periodically retire a portion of the bond issue before maturity.
  * **✅ Good for Investors:** Lowers credit risk because the final principal payment is smaller.
  * **❌ Bad for Investors:** Creates **reinvestment risk**. If your bond is called and redeemed when interest rates are low, you have to reinvest your money at a lower return.

-----

### <span style="color: #1565C0;">Part 2: Not All Coupons Are Created Equal: Different Coupon Structures 🎨</span>

Beyond the standard fixed coupon, bonds can have a variety of interesting coupon structures.

#### <span style="color: #6A1B9A;">2.1 Floating-Rate Notes (FRNs)</span>
* The coupon rate is not fixed. It resets periodically based on a market reference rate (MRR) plus a fixed margin.  
  **⬆️ Great for investors in a rising-rate environment!**

#### <span style="color: #6A1B9A;">2.2 Step-Up Coupon Bonds</span>
* The coupon rate increases over time according to a predetermined schedule (e.g., 2% for the first 3 years, then 4% for the next 3).

#### <span style="color: #6A1B9A;">2.3 Credit-Linked Notes</span>
* The coupon rate is linked to the issuer's credit rating. If the issuer's rating gets downgraded, the coupon rate increases to compensate investors for the higher risk.

#### <span style="color: #6A1B9A;">2.4 Payment-in-Kind (PIK) Bonds</span>
* A risky feature where the issuer can choose to pay interest with more bonds rather than cash.  
  **❌ Usually done by highly leveraged companies.**

#### <span style="color: #6A1B9A;">2.5 Inflation-Linked Bonds (Linkers)</span>
* These bonds protect investors from inflation. The most common type is the **capital-indexed bond** (like U.S. **Treasury Inflation-Protected Securities or TIPS**).  
  Here, the principal amount is adjusted for inflation, and the fixed coupon rate is applied to this new, higher principal.  
  **✅ Protects both the coupon payments and the final principal from losing purchasing power.**

-----

### <span style="color: #1565C0;">Part 3: Special Features: Embedded Options 🃏</span>

Some bonds come with special features called **embedded options** that give either the issuer or the investor the right to take a certain action. A bond with no such features is called a **straight** or **option-free bond**.

#### <span style="color: #6A1B9A;">3.1 Callable Bonds (Benefit the Issuer)</span>
* A **callable bond** gives the *issuer* the right to redeem (or "call") the bond before its maturity date at a specified **call price**.
  * **Why?** Issuers will call their bonds when interest rates have fallen. This allows them to "refinance" their debt at a cheaper rate.
  * **❌ Investor Impact:** This is a major disadvantage for investors, creating **call risk**. The bond's price appreciation is capped near the call price, and investors are forced to reinvest their money at lower rates.
  * **✅ Compensation:** Because of this risk, callable bonds offer a higher yield than otherwise identical non-callable bonds.

#### <span style="color: #6A1B9A;">3.2 Putable Bonds (Benefit the Investor)</span>
* A **putable bond** gives the *bondholder* the right to sell the bond back to the issuer at a pre-specified price before maturity.
  * **Why?** Investors will "put" the bond back to the issuer when interest rates have risen (making their lower-coupon bond less valuable) or if the issuer's credit quality has deteriorated.
  * **✅ Investor Impact:** This is a valuable feature for investors, as it protects them from downside risk.
  * **❌ Compensation:** Because this option benefits the investor, putable bonds offer a lower yield than otherwise identical straight bonds.

#### <span style="color: #6A1B9A;">3.3 Convertible Bonds (Benefit the Investor)</span>
* A **convertible bond** gives the *bondholder* the right to exchange the bond for a specified number of shares of the issuing company's common stock.
  * **Why?** It offers the safety of a bond (regular coupon payments) with the upside potential of equity.
  * **Key Terms:**
    * **Conversion Price:** The price per share at which the bond can be converted.
    * **Conversion Ratio:** The number of shares received upon conversion (`Par Value / Conversion Price`).
    * **Conversion Value:** The market value of the shares received (`Conversion Ratio × Current Share Price`).
  * **❌ Compensation:** Because this is a valuable feature, convertible bonds are issued with lower yields than non-convertible bonds.

-----

### <span style="color: #1565C0;">Part 4: Where Are Bonds Issued and How Are They Taxed? 🌍⚖️</span>

Bonds are categorized based on the currency they're denominated in and where they are issued and traded.

#### <span style="color: #6A1B9A;">4.1 Types of Bonds by Issuance</span>
* **Domestic Bonds:** Issued by a local issuer in the local market and currency. (e.g., HDFC Bank issuing a Rupee-denominated bond in India).
* **Foreign Bonds:** Issued by a foreign entity in a domestic market's currency. (e.g., Toyota issuing a US-dollar bond in the United States).
* **Eurobonds:** Issued outside the jurisdiction of any single country and denominated in a currency different from the country where they are issued. This is the largest and least regulated market. (e.g., a US company issuing a US-dollar bond in London).
* **Global Bonds:** Bonds that are issued simultaneously in the Eurobond market and at least one domestic bond market.

#### <span style="color: #6A1B9A;">4.2 Taxation of Bond Income</span>
* **Coupon Interest:** Typically taxed at an investor's ordinary income tax rate.
* **Capital Gains:** When a bond is sold for a price higher than its purchase price, the profit is usually taxed as a **capital gain**, often at a lower rate than ordinary income.
* **Original Issue Discount (OID) Bonds:** For bonds issued at a discount (like zero-coupon bonds), tax authorities often require the investor to report and pay taxes on a portion of the discount as "imputed interest" *each year*, even though no cash is received until maturity.

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**To find the payment for a fully amortizing loan:**

Parameters: $N$ (number of periods), $I/Y$ (interest rate per period), $PV$ (loan amount), $FV = 0$

$$
PMT = \text{Periodic Payment}
$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**To find the payment for a partially amortizing loan:**

Parameters: $N$ (number of periods), $I/Y$ (interest rate per period), $PV$ (loan amount), $FV$ (balloon payment)

(Enter $FV$ as negative if $PV$ is positive.)

$$
PMT = \text{Periodic Payment}
$$

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* **Cash Flow Structures:**  
  * **Bullet** → Principal at maturity  
  * **Fully Amortizing** → Like a mortgage  
  * **Partially Amortizing** → Principal payments + a final balloon payment
* **Embedded Options are Key:** Remember who benefits!
  * **Call Option → Benefits Issuer** → Higher Yield for Investor
  * **Put Option → Benefits Investor** → Lower Yield for Investor
  * **Convertible Option → Benefits Investor** → Lower Yield for Investor
* **International Bonds:**  
  * Understand the difference between Domestic, Foreign, and Eurobonds.  
  * **Eurobonds** are the least regulated.
* **OID Tax Trap:**  
  * For zero-coupon and other OID bonds, remember that taxes may be due on the "phantom" interest income each year, even before any cash is received.

</div>
</div>