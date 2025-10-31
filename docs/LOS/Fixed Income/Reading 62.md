## Reading 62: Credit Analysis for Corporate Issuers 🏢

### 🎯 Introduction

Welcome to the heart of credit analysis: **corporations**. This is where your financial statement analysis skills truly come to life. Unlike sovereigns, companies can't print money or (usually) collect taxes. Their ability to pay debt comes from one place: **generating cash flow**.

In this reading, we'll learn how to perform a full credit check-up. We'll start with the qualitative "feel" of a company—its business model and management—and then move to the quantitative "facts" by calculating key leverage and coverage ratios. Finally, we'll master the "pecking order" of debt, learning why **not all debt is created equal** in a bankruptcy.

-----

### <span style="color: #1565C0;">Part 1: The Corporate Credit Check-Up (LOS 62.a & 62.b)</span>

Evaluating a company's creditworthiness involves blending qualitative art with quantitative science.

#### <span style="color: #6A1B9A;">1.1 Qualitative Factors (The "Art" 🎨)</span>

We start by assessing the company's fundamental character and operating environment:

  * **Business Model:** Does the company have stable, predictable cash flows?  A utility company is (usually) more stable than a trendy fashion brand.
  * **Industry Competition:** Less competition is better for credit quality. We analyze the company's competitive advantages.
  * **Business Risk:** This is the company's inherent operational and financial risk (e.g., operating leverage, cyclicality).
  * **Corporate Governance:** This is a huge factor, showing management's "character."
      * **Covenants:** High-yield issuers are likely to have *negative covenants* (restricting actions like paying big dividends), while investment-grade issuers have fewer.
      * **Management's Past Actions:** Has management favored shareholders over debtholders (e.g., by issuing debt to buy back stock)? This is a major red flag for bondholders.
      * **Accounting Policies:** Aggressive revenue recognition, heavy use of off-balance-sheet financing, or frequent auditor changes are all warning signs.

#### <span style="color: #6A1B9A;">1.2 Quantitative Factors (The "Science" 🔬)</span>

This is all about the numbers. We need to know a company's true cash-generating ability. Analysts use several key cash flow metrics:

  * **EBITDA:** Earnings Before Interest, Taxes, Depreciation, and Amortization. A common proxy for operating cash flow.
  * **CFO (Cash Flow from Operating Activities):** The cash generated from the firm's core business, found on the cash flow statement. It *includes* changes in working capital.
  * **FFO (Funds From Operations):** A key metric! `FFO = CFO + (Net Interest Paid) - (Change in Working Capital)`. It's similar to CFO but *excludes* the impact of working capital swings, which can make it a more stable measure of long-term cash generation.
  * **RCF (Retained Cash Flow):** `RCF = CFO - Dividends`. This shows how much cash is left after paying out dividends.

#### <span style="color: #6A1B9A;">1.3 The Key Credit Ratios (LOS 62.b)</span>

We use those cash flow measures to build ratios that tell us about a company's profitability, coverage, and leverage.

| Ratio Type | Ratio Name | Calculation | Indication of Higher Credit Quality |
| :--- | :--- | :--- | :--- |
| **Profitability** | EBIT margin | `EBIT / Revenue` | Higher ratio |
| **Coverage** | EBIT coverage | `EBIT / Interest Expense` | Higher ratio |
| **Leverage** | Debt to EBITDA | `Debt / EBITDA` | Lower ratio |
| **Leverage** | RCF to Net Debt | `RCF / (Debt - Cash)` | Higher ratio |

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 Ratios Explained**

  * **Profitability Ratios (EBIT margin):** Show how efficiently the company turns sales into pre-tax, pre-interest profit.
  * **Coverage Ratios (EBIT coverage):** This is critical. It asks: "How many times over can the company's earnings cover its interest payments?"  A ratio of 13.8x means it earned 13.8 times what it needs for interest.
  * **Leverage Ratios (Debt/EBITDA, RCF/Net Debt):** These measure the size of the debt burden relative to cash flow. `Debt/EBITDA` shows how many years of cash flow it would take to pay off all debt. `RCF/Net Debt` shows what percentage of the net debt could be paid off with one year's retained cash flow.

</div>
</div>

-----

### <span style="color: #1565C0;">Part 2: The Pecking Order (LOS 62.c)</span>

In a bankruptcy, who gets paid first? This is determined by **seniority ranking** or **priority of claims**.

#### <span style="color: #6A1B9A;">2.1 Secured vs. Unsecured Debt</span>

  * **Secured Debt:** This debt is backed by **collateral**—specific assets (like a factory or inventory) that lenders can seize if the company defaults.
  * **Unsecured Debt:** This is backed only by the company's general promise and its overall cash flows. It has no claim on specific assets.

#### <span style="color: #6A1B9A;">2.2 The Waterfall: Priority of Claims</span>

This is the order in which claimants get paid in a bankruptcy. Money flows from top to bottom, and a lower level gets *nothing* until the level above it is paid in full.

**The General Seniority Rankings:** 

1.  **First Lien / First Mortgage** (Highest priority, secured by best assets)
2.  **Senior Secured (Second Lien)**
3.  **Junior Secured**
4.  **Senior Unsecured** (The typical "corporate bond")
5.  **Senior Subordinated**
6.  **Subordinated**
7.  **Junior Subordinated**

Debt in the same category (e.g., all Senior Unsecured bonds) is said to rank **pari passu**, meaning all holders have equal priority and will be treated alike.

#### <span style="color: #6A1B9A;">2.3 Ratings: Issuer vs. Issue & Notching</span>

  * **Issuer Credit Rating (Corporate Family Rating - CFR):** This is the agency's opinion on the company's *overall* creditworthiness. It typically applies to its **senior unsecured** debt.
  * **Issue Credit Rating:** This is the rating for a *specific bond*.
  * **Notching:** This is the key practice of adjusting the *issue* rating up or down from the *issuer (CFR)* rating based on its seniority.
      * A highly-secured First Lien bond might be notched *up* (e.g., issuer is BB, bond is BB+).
      * A Subordinated bond will be notched *down* (e.g., issuer is BB, bond is B+).
      * Notching is much more common for high-yield issuers, where recovery is a primary concern.

<div style="background-color: #F3E5F5; border-left: 5px solid #7B1FA2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 Key Concept: Structural Subordination**

This is a subtle but critical concept. Imagine a **Parent Holding Company** that owns **Subsidiary Operating Company**.

  * The Subsidiary has its own debt.
  * The Parent company also has its own debt.

**The problem:** The Subsidiary's cash flows must be used to pay the *Subsidiary's debt* first. Only the leftover profit (if any) can be "upstreamed" as a dividend to the Parent. The Parent company then uses this dividend to pay *its* debtholders.

**The result:** The Parent's debtholders are *effectively* subordinated (junior) to the Subsidiary's debtholders. This is **structural subordination**, and it means the Parent's bonds are riskier and will be notched down.

</div>
</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

  * **Cash Flow is King:** Know the key cash flow metrics: **EBITDA**, **CFO**, and **FFO** (FFO = CFO but excludes working capital changes).
  * **Key Ratios:**
      * **Coverage (EBIT/Interest):** Higher is better.
      * **Leverage (Debt/EBITDA):** Lower is better.
  * **Priority of Claims:** Secured > Unsecured. Senior > Subordinated. Remember the waterfall.
  * **Pari Passu:** Means "on equal footing." All bonds in the same class (e.g., all senior unsecured) rank equally.
  * **Notching:** Adjusting an *issue* rating based on its seniority relative to the *issuer's* main rating (the CFR).
  * **Structural Subordination:** This is a guaranteed exam-level concept. Parent company debt is *effectively junior* to subsidiary debt. Remember this!

</div>
</div>