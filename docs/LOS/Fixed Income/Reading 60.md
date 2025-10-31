## Reading 60: Credit Risk 📉

### 🎯 Introduction

Welcome to one of the most critical readings in Fixed Income. While interest rate risk is a well-known opponent, **credit risk** is the hidden adversary that can lead to a portfolio's downfall.

This reading is all about mastering the art of analyzing that risk. We're moving beyond the "risk-free" world of government bonds and into the corporate world, where a company's promise to pay isn't always a guarantee.

We will learn how to measure this risk using its core components: the **Probability of Default (POD)** and the **Loss Given Default (LGD)**. We'll also decipher the language of credit rating agencies (what does BBB- *really* mean?) and, most importantly, understand what makes credit spreads—the extra yield you demand for taking this risk—widen and narrow.

-----

### <span style="color: #1565C0;">Part 1: Deconstructing Credit Risk (LOS 60.a)</span>

**Credit risk** is the risk of loss if a borrower (issuer) fails to make a promised interest or principal payment on time. This failure is called a **default**.

#### <span style="color: #6A1B9A;">1.1 The "Cs" of Credit Analysis 🕵️‍♀️</span>

To assess credit risk, analysts use a framework often called the "Cs of credit analysis". These are split into bottom-up (issuer-specific) and top-down (macro) factors:

  * **Bottom-Up Factors (Issuer-Specific):**
      * **Capacity:** The borrower's ability to generate cash flow to make their debt payments. This is the *most important* C.
      * **Capital:** The borrower's other resources (e.g., assets) that reduce reliance on debt.
      * **Collateral:** The value of assets pledged as security for the debt. (e.g., Secured vs. Unsecured bonds ).
      * **Covenants:** The legal terms and conditions of the bond that protect lenders (e.g., restrictions on issuing more debt).
      * **Character:** Management's integrity, strategy, and willingness to repay debt.
  * **Top-Down Factors (Macro):**
      * **Country:** The political and legal stability of the issuer's home country.
      * **Conditions:** The macroeconomic environment (e.g., business cycle, inflation).
      * **Currency:** The risk of exchange rate changes, especially for issuers with debt in a foreign currency.

#### <span style="color: #6A1B9A;">1.2 The Core Components of Credit Loss</span>

Credit risk is ultimately quantified by two key components:

1.  **Probability of Default (POD):** The *likelihood* that a borrower will default on their obligation in a given year.
2.  **Loss Given Default (LGD):** The *amount* of loss if a default occurs. This is expressed as a percentage of the bond's value.
      * This is the opposite of the **Recovery Rate (RR)**, which is the percentage investors get back after a default.
      * `LGD = 1 - Recovery Rate` 

<div style="background-color: #F3E5F5; border-left: 5px solid #7B1FA2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 The Big Formulas**

  * **Expected Loss (EL):** This is the average loss you can expect over a period.
    `Expected Loss (EL) = Probability of Default (POD) × Loss Given Default (LGD)` 

  * **The Price of Risk:** The market doesn't give you yield for free. The **credit spread** (the extra yield a bond pays over a risk-free bond) is the compensation you receive for taking on this expected loss.
    `Credit Spread ≈ POD × LGD%` 

</div>
</div>

#### <span style="color: #6A1B9A;">1.3 Investment Grade (IG) vs. High Yield (HY) Risk</span>

How you apply these concepts depends heavily on the bond's quality:

  * **Investment Grade (IG):** For high-quality bonds (e.g., 'A' rated), the *actual* probability of default is very low. The main risk for an IG investor is **credit spread risk**—the risk that the bond's credit quality deteriorates (e.g., gets downgraded), causing its spread to widen and its price to fall.
  * **High Yield (HY) / "Junk" Bonds:** For low-quality bonds, default is a very real possibility. Therefore, the **Loss Given Default (LGD)** and **Recovery Rate** are critical drivers of value. Interestingly, HY bonds are often secured by collateral (to make them sellable), which can *lower* the LGD compared to an unsecured IG bond.

-----

### <span style="color: #1565C0;">Part 2: The Rating Agencies' Report Card (LOS 60.b)</span>

Credit rating agencies (like S&P, Moody's, and Fitch) provide independent assessments of an issuer's creditworthiness.

#### <span style="color: #6A1B9A;">2.1 Understanding the Ratings</span>

Ratings are split into two main universes:

| Category | S&P / Fitch | Moody's | Quality |
| :--- | :--- | :--- | :--- |
| **Investment Grade** | AAA, AA, A, BBB | Aaa, Aa, A, Baa | Highest quality down to adequate capacity to pay.  |
| **High Yield (Junk)** | BB, B, CCC... | Ba, B, Caa... | Speculative; significant default risk.  |

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️: Memorize the dividing line! The "floor" for investment grade is **BBB- (S&P/Fitch)** and **Baa3 (Moody's)**. Anything below that (e.g., BB+ or Ba1) is high yield.

</div>
</div>

#### <span style="color: #6A1B9A;">2.2 Don't Trust Blindly! Limitations of Credit Ratings</span>

While useful, you must *not* rely exclusively on agency ratings. They have significant limitations:

1.  **Ratings Lag the Market:** Bond prices and credit spreads move *much faster* than rating agencies, which can take months to react to new information. The market often prices in a downgrade long before the official announcement.
2.  **Difficult-to-Assess Risks:** Ratings are poor at capturing certain risks, like litigation, environmental disasters, or sudden management decisions (like a huge, debt-funded acquisition).
3.  **Ratings Change:** A rating is not static. The risk that a bond gets downgraded is called **credit migration risk** or **downgrade risk**.

-----

### <span style="color: #1565C0;">Part 3: What Makes Spreads Move? (LOS 60.c)</span>

**Credit spread risk** is the danger that a bond's price will fall because its yield spread widens. This is the *primary* concern for IG investors. Spreads are driven by macro, market, and issuer-specific factors.

#### <span style="color: #6A1B9A;">3.1 Macroeconomic Factors 🌍</span>

  * **The Business Cycle:** This is the big one.
      * **Expansions:** The economy is strong, profits are high, and defaults are rare. Risk appetite is high. ➡️ **Spreads NARROW (contract)**.
      * **Recessions:** The economy is weak, profits fall, and defaults rise. Investors become risk-averse. ➡️ **Spreads WIDEN (increase)**.
  * **Flight to Quality:** During a financial crisis, investors panic and sell *everything* risky (like HY bonds) and pile into the safest assets (like Treasuries). This causes HY spreads to "blow out" (widen dramatically).
  * **HY vs. IG Spreads:** High-yield spreads are *much more volatile* than IG spreads and are more strongly correlated with equity returns.

#### <span style="color: #6A1B9A;">3.2 Market Factors 📊</span>

  * **Liquidity:** The "plumbing" of the market matters. If broker-dealers have less capital, they can't make markets as easily. This reduces liquidity and ➡️ **Widens Spreads**.
  * **Supply and Demand:** A heavy new supply of corporate bonds (lots of new issuance) can overwhelm demand and ➡️ **Widen Spreads**.

#### <span style="color: #6A1B9A;">3.3 Decomposing the Spread</span>

A bond's yield spread isn't just for credit risk. It's for liquidity, too.

`Yield Spread = Credit Spread + Liquidity Spread`

An analyst can estimate the **liquidity spread** by looking at the bond's **bid-ask spread**. A wider bid-ask spread implies lower liquidity, which accounts for a larger portion of the total yield spread.

#### <span style="color: #6A1B9A;">3.4 Spreads and Duration: The Double Whammy 💥</span>

Duration doesn't just measure sensitivity to risk-free rate changes; it *also* measures sensitivity to spread changes.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**🧮 The Spread-Duration Formula**

The formula to estimate a bond's price change from a spread change is the *same* as the one for a yield change:

`%Δ Full Price ≈ -ModDur(ΔSpread) + ½Convexity(ΔSpread)²` 

**This is critical:** A longer-duration bond is *more sensitive* to credit spread widening. An investor holding a 30-year corporate bond faces massive risk not just from rising Treasury yields, but also from its own credit spread widening.

</div>
</div>

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

  * **Expected Loss (EL):**
    `EL = Probability of Default (POD) × Loss Given Default (LGD)` 
  * **Loss Given Default (LGD):**
    `LGD = 1 - Recovery Rate` 
  * **Credit Spread (Approximate):**
    `Credit Spread ≈ POD × LGD%` 
  * **Price Change from Spread:**
    `%Δ Price ≈ -ModDur(ΔSpread) + ½Convexity(ΔSpread)²` 
  * **Yield Spread Decomposition:**
    `Yield Spread = Credit Spread + Liquidity Spread` 

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

  * **Key Formulas:** Know `EL = POD × LGD`  and that `Credit Spread ≈ POD × LGD%`.
  * **IG vs. HY Risk:**
      * **IG:** Primary risk is **credit spread risk** (downgrade/widening).
      * **HY:** Primary risk is **default**, so **LGD** and **Recovery Rates** are crucial.
  * **Spreads & The Cycle:** This is a classic. Spreads **WIDEN (increase)** in recessions. Spreads **NARROW (contract)** in expansions.
  * **Flight to Quality:** In a crisis, investors sell HY and buy Treasuries, causing spreads to widen dramatically.
  * **Rating Agency Limitations:** Their biggest flaw is that they **lag the market**. Spreads move first.
  * **The Magic Rating:** Know the IG/HY dividing line: **BBB- (S&P/Fitch)** and **Baa3 (Moody's)**.
  * **Duration & Spreads:** Duration amplifies *all* yield changes. A longer-duration bond has *more* credit spread risk.

</div>
</div>