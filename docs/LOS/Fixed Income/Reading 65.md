## Reading 65: Mortgage-Backed Security (MBS) Instrument and Market Features 🏡

🎯 **Introduction**

Mortgage-Backed Securities (MBS) are the titans of the securitization world. If an auto-loan ABS is a reliable family sedan, an MBS is a high-performance sports car with complex features. The most important and unpredictable of these features is **prepayment risk**—the uncertainty that homeowners will pay back their mortgages faster or slower than expected. This reading is your driver's manual for MBS. We'll get a firm grip on this key risk and explore the clever structures, like **Collateralized Mortgage Obligations (CMOs)**, designed to help investors navigate this challenging road.

---

### Part 1: The #1 Risk in MBS: Prepayment Risk ⏭️

Unlike most other loans, mortgages can be paid back early, at any time, with little to no penalty. This creates huge uncertainty for an MBS investor, known as **prepayment risk**. This risk has two sides, and both are bad for the investor.

#### **Contraction Risk (Risk of Faster Prepayments)**

* **When it happens:** When interest rates **fall** 📉.
* **Why it happens:** Homeowners rush to refinance their existing mortgages to lock in a new, lower interest rate. They take out a new loan and use it to pay off their old one in full.
* **Why it's bad for investors:** Investors get their principal back much sooner than expected, right when market rates are low. They are now forced to reinvest this money at a lower yield. This is a form of **reinvestment risk**.
    * **Example:** You buy an MBS yielding 5%. A year later, mortgage rates fall to 3%. Many homeowners in the pool refinance. You get a large chunk of your principal back, but now you can only reinvest it at the new, lower 3% rate.

#### **Extension Risk (Risk of Slower Prepayments)**

* **When it happens:** When interest rates **rise** 📈.
* **Why it happens:** Homeowners have no financial incentive to refinance their low-rate mortgage, so prepayment speeds slow to a crawl.
* **Why it's bad for investors:** Your principal is now stuck in a lower-yielding MBS for longer than you expected, while new bonds are being issued at much more attractive, higher rates. This is a form of **opportunity cost**.
    * **Example:** Your 5% MBS is now less attractive compared to new MBS being issued at 7%, and your cash is tied up for longer than you anticipated.

To manage these risks, issuers can use **time tranching**, which creates different bond classes that receive principal payments sequentially. The first tranche to be paid off has the most protection against extension risk, while the last tranche has the most protection against contraction risk, 2816].

---

### Part 2: A Tour of the Residential MBS (RMBS) Market 🏘️

**Residential Mortgage-Backed Securities (RMBS)** are backed by pools of home loans. The credit quality of these securities depends heavily on the features of the underlying mortgages.

* **Key Loan Features:**
    * **Recourse vs. Non-Recourse:** In a **recourse loan**, the lender can go after the borrower's other assets if the sale of the foreclosed home doesn't cover the loan balance. In a **non-recourse loan**, the lender can only seize the house.
    * **Loan-to-Value (LTV) Ratio:** The percentage of the property's value that is loaned. A lower LTV means the homeowner has more equity and is less likely to default, 2820].
    * **Debt-to-Income (DTI) Ratio:** The borrower's total monthly debt payments as a percentage of their income. A lower DTI indicates a higher ability to repay, 2824].

#### **Mortgage Pass-Through Securities**
This is the simplest MBS structure. An investor buys a share in a pool of mortgages and receives a pro-rata share of all cash flows (interest and any principal prepayments). All investors in the pool share the prepayment risk equally. Two key metrics describe the pool:

* **Weighted Average Coupon (WAC):** The weighted average of the interest rates of all mortgages in the pool.
* **Weighted Average Maturity (WAM):** The weighted average of the remaining months to maturity of all mortgages in the pool.

> **Example: Calculating WAC and WAM 🧮**
> A pass-through MBS is created from three mortgages:
> 
> | Mortgage | Interest Rate | Current Balance ($000s) | Months to Maturity |
> | :--- | :--- | :--- | :--- |
> | A | 2.67% | 90 | 270 |
> | B | 3.10% | 72 | 190 |
> | C | 5.14% | 247 | 280 |
> 
> * **Total Balance** = 90 + 72 + 247 = $409k
> * **WAM Calculation:**
>     WAM = $270 \times (\frac{90}{409}) + 190 \times (\frac{72}{409}) + 280 \times (\frac{247}{409}) = 59.4 + 33.4 + 169.3 = \textbf{262.1 months}$ 
> * **WAC Calculation:**
>     WAC = $2.67\% \times (\frac{90}{409}) + 3.10\% \times (\frac{72}{409}) + 5.14\% \times (\frac{247}{409}) = 0.588\% + 0.546\% + 3.106\% = \textbf{4.24\%}$ 

#### **Collateralized Mortgage Obligations (CMOs)**
A CMO is a more complex structure created by taking the cash flows from a pool of pass-through securities and redirecting them to different tranches with different risk profiles. The main purpose of a CMO is to reapportion the prepayment risk among different classes of investors to better suit their needs, 2838].

---

### Part 3: Big Buildings, Big Loans: Commercial MBS (CMBS) 🏙️

**Commercial Mortgage-Backed Securities (CMBS)** are backed by mortgages on income-producing commercial properties like office buildings, shopping malls, and hotels. They are fundamentally different from RMBS.

* **Call Protection:** Prepayment risk is much less of a concern in CMBS because the underlying commercial loans have significant **call protection** built in to discourage borrowers from prepaying. This includes:
    * **Prepayment Lockout Periods:** A period where prepayment is strictly forbidden.
    * **Prepayment Penalty Points:** A fee charged if the borrower prepays.
    * **Defeasance:** The borrower must use any prepayment to buy a portfolio of government bonds whose cash flows exactly replicate all remaining loan payments.

* **Balloon Risk:** This is the **main risk** in CMBS. Commercial loans are often partially amortizing, meaning a very large **balloon payment** of principal is due at maturity. **Balloon risk** is the risk that the borrower will be unable to refinance this large sum, leading to a default.

---

### 🧪 Formula Summary

* **Weighted Average Maturity (WAM):**
    $\text{WAM} = \sum_{i=1}^{n} w_i \times M_i$
    (where $w_i$ is the weight of mortgage *i*'s balance, and $M_i$ is its remaining maturity in months)
* **Weighted Average Coupon (WAC):**
    $\text{WAC} = \sum_{i=1}^{n} w_i \times c_i$
    (where $c_i$ is the coupon rate of mortgage *i*)
* **Debt-Service Coverage Ratio (for CMBS):**
    $\text{DSCR} = \frac{\text{Net Operating Income}}{\text{Debt Service}}$ 
* **Loan-to-Value (for CMBS):**
    $\text{LTV} = \frac{\text{Current Mortgage Amount}}{\text{Current Appraised Value}}$ 

---

> [!IMPORTANT]
> ### 🎯 Quick Exam-Day Pointers
>
> * **Prepayment Risk is Two-Sided:** **Contraction risk** (faster prepayments) happens when rates **fall**. **Extension risk** (slower prepayments) happens when rates **rise**. Both are bad for the investor.
> * **Agency vs. Non-Agency RMBS:** **Agency** RMBS are government-guaranteed and very safe. **Non-Agency** are private, not guaranteed, and much riskier.
> * **CMOs Redistribute Risk:** The purpose of a **CMO** is to take a simple pool of mortgages and create different tranches to concentrate or reapportion prepayment risk among different investors.
> * **CMBS Key Risks:** Prepayment risk is low due to strong **call protection** (like defeasance). The main risk is **balloon risk**—the risk of default at maturity because the borrower cannot refinance the large final principal payment.