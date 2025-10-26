## Reading 64: Asset-Backed Security (ABS) Instrument and Market Features

### 🎯 Introduction

If securitization is the factory that bundles small loans into big, tradable bonds, then this reading is our detailed tour of the factory floor. We'll examine the different products that come off the assembly line—bonds backed by auto loans, credit card debt, and more. Most importantly, we'll look at the clever safety features, known as **credit enhancements**, that are built into these securities. These mechanisms act like financial airbags and seatbelts, designed to protect investors from losses even if some of the underlying borrowers default on their loans.

-----

### <span style="color: #1565C0;">Part 1: Covered Bonds—An ABS Cousin from Europe (LOS 64.a)</span>

A **covered bond** is a type of debt issued by a financial institution (usually a bank) that is backed by a specific pool of assets (the **cover pool**), typically high-quality mortgages. While it sounds like an ABS, there are crucial differences that make it a distinct and often safer instrument.

#### <span style="color: #6A1B9A;">1.1 Asset-Backed Securities (ABS)</span>

* **Structure:** Uses a **Special Purpose Entity (SPE)**. The assets are sold by the originator and are legally **off** its balance sheet.
* **Recourse:** Investors only have a claim on the assets within the SPE. If the collateral defaults and isn't enough to pay everyone back, investors cannot go after the original bank for more money.
* **Risk:** The credit risk depends entirely on the quality of the collateral pool and the built-in credit enhancements.

#### <span style="color: #6A1B9A;">1.2 Covered Bonds</span>

* **Structure:** **No SPE is used**. The cover pool of assets **remains on the issuer's balance sheet**.
* **Recourse:** This is the key difference! Investors have **dual recourse**. They have a primary claim on the cash flows from the cover pool, *but if that's not enough*, they also have a general claim on the issuer itself, ranking equally with other senior unsecured bondholders.
* **Risk:** Because of this dual protection, covered bonds are exceptionally safe—often safer than the senior tranche of an ABS and always safer than the issuer's own regular senior debt.

-----

### <span style="color: #1565C0;">Part 2: Safety First—Credit Enhancements (LOS 64.b)</span>

**Credit enhancements** are the safety mechanisms built into an ABS structure to protect investors from losses and thus achieve higher credit ratings.

#### <span style="color: #6A1B9A;">2.1 Internal Credit Enhancements (Built into the Structure)</span>

These are the most common and important forms of protection.

* **Subordination (or Credit Tranching) 🪜:** This is the most popular method. The ABS is sliced into different bond classes (**tranches**) with a clear hierarchy for absorbing losses, known as a **waterfall structure**. Losses are absorbed from the bottom up.

  ##### <span style="color: #E65100;">2.1.1 Example: Waterfall Structure</span>

  <div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
  <div style="color: #000000; font-weight: 500;">

  **Example:** An SPE issues a \$410 million ABS backed by \$410 million of loans. The ABS is structured into three tranches:
    * Tranche A (Senior): \$300 million
    * Tranche B (Subordinated): \$80 million
    * Tranche C (Subordinated/Junior): \$30 million

  If the loan pool suffers \$40 million in losses:
    * Tranche C, the junior-most tranche, absorbs the first \$30 million of losses and is completely wiped out. ❌
    * Tranche B then absorbs the remaining \$10 million of losses. ⬇️
    * Tranche A, the senior tranche, is completely unharmed because it is protected by the full \$110 million of subordinated bonds below it. ✅

  </div>
  </div>

* **Overcollateralization 💎:** The total principal value of the asset pool is greater than the total par value of the bonds issued.

  <div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
  <div style="color: #000000; font-weight: 500;">

  **Example:** The SPE uses a \$110 million pool of auto loans to issue only \$100 million in ABS. The extra \$10 million in collateral acts as a protective buffer against defaults. ✅

  </div>
  </div>

* **Excess Spread 💰:** The interest rate earned on the underlying loans is higher than the interest rate paid to the ABS investors. This extra cash flow is the first line of defense to cover any losses from defaults before touching any principal.

-----

### <span style="color: #1565C0;">Part 3: A Tour of the ABS Market (LOS 64.c)</span>

Besides mortgages, many other types of debt are securitized.

* **Auto Loan ABS:** Backed by pools of car loans. These are relatively simple because the underlying loans are fully amortizing with predictable cash flows.
* **Credit Card Receivable ABS:** Backed by pools of credit card debt. These have a unique structure with a **lockout period** (or **revolving period**).

  <div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
  <div style="color: #000000; font-weight: 500;">

  **Example: Credit Card Lockout Period**
    * For the first 18 months (the lockout period), investors receive only interest payments.
    * As cardholders pay off their balances (principal), that cash is used by the SPE to purchase new credit card receivables from the originator, keeping the collateral pool at a stable size.
    * After the lockout period ends, the principal payments are then passed through to investors to pay down the ABS. This structure protects investors from early prepayment during the lockout phase. ✅

  </div>
  </div>

* **Collateralized Debt Obligations (CDOs):**
  * A CDO is a special type of ABS where the underlying collateral is itself a portfolio of debt securities. The key difference is that a CDO is **actively managed** by a **collateral manager** who buys and sells securities in the pool to generate returns.
  * **Collateralized Loan Obligations (CLOs):** The most common type of CDO today. They are backed by a portfolio of leveraged bank loans.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 CFA Exam Tip ✍️:** The defining feature of a CDO (especially a CLO) that sets it apart from a standard ABS is that its collateral pool is **actively managed**. A standard auto loan or credit card ABS has a static or semi-static pool.

</div>
</div>

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**This reading is conceptual and does not contain any formulas to memorize.**

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* **Covered Bonds = Dual Recourse:** The single most important feature of a **covered bond** is that investors have recourse to both the collateral pool *and* the issuer. They are not issued from an SPE and the assets remain on the issuer's balance sheet. ✅
* **The Big 3 Internal Enhancements:** Know them cold! **Subordination** (the waterfall structure that protects senior tranches), **Overcollateralization** (more assets than bonds), and **Excess Spread** (assets earn more than bonds pay out). ⬆️
* **Credit Card ABS have a Lockout:** Remember the **lockout/revolving period** where principal payments from borrowers are reinvested in new receivables rather than being paid out to investors. ⬇️
* **CDOs are Actively Managed:** This is the key characteristic that distinguishes a CDO/CLO from other types of ABS. ✅

</div>
</div>