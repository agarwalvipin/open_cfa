## Reading 35: Analysis of Income Taxes 🧾

### 🎯 Introduction

Think of a company navigating two sets of rules: one from the accounting standards board (like IFRS or U.S. GAAP) for reporting to investors 📊, and another from the government's tax authorities (like the Income Tax Department in India or the IRS in the US) for paying taxes 💰. Sometimes these rules align perfectly, but often they don't, especially regarding *when* income or expenses are recognized. This mismatch creates temporary differences that give rise to **Deferred Tax Assets (DTAs)** and **Deferred Tax Liabilities (DTLs)** on the balance sheet. This reading is your guide to understanding why these differences occur, how they impact financial statements, and what they tell us about a company's earnings quality and future cash flows\! 🧐

-----

### Part 1: Why Tax Rules Differ - Accounting vs. Taxable Income 🤔 (LOS 35.a)

The core issue is the difference between profit reported to shareholders and profit reported to the taxman.

* **Accounting Profit (or Pretax Income):** This is the profit a company reports on its income statement *before* subtracting income tax expense, calculated using IFRS or U.S. GAAP. It's designed to give investors a clear view of performance. 📈
* **Taxable Income:** This is the profit calculated according to the tax laws of the country. It determines how much tax the company actually owes the government. 🏛️
* **Taxes Payable:** The actual amount of tax due to the government based on the current period's **taxable income** and the **statutory tax rate**.
* **Income Tax Expense:** The tax reported on the income statement. It includes **taxes payable** *plus* changes in **deferred tax liabilities and assets**. It reflects the tax effects related to the **accounting profit**, not necessarily the cash paid.

Differences arise from two main sources:

1.  **Permanent Differences:** These are items that affect either accounting profit *or* taxable income, but **never both**. They don't reverse over time.
    * *Example (Global):* Interest income from municipal bonds in the US might be included in accounting profit but is often tax-exempt.
    * *Example (Global):* Fines or penalties might reduce accounting profit but are often not tax-deductible.
    * Permanent differences cause the company's **effective tax rate** to differ from the **statutory tax rate**, but they **do not create DTA or DTL**. 🚫
2.  **Temporary Differences:** These are the crucial ones\! They occur when accounting rules and tax rules recognize income or expenses in *different time periods*. These differences *will* reverse in the future. They are the origin of DTAs and DTLs.

#### **Deferred Tax Liabilities (DTLs): Paying Less Tax Now, More Later ⏳**

A **Deferred Tax Liability (DTL)** arises when:
* **Income Tax Expense (Income Statement) > Taxes Payable (Tax Return)**

This typically happens when:
* A company recognizes revenue or gains in the income statement *before* they are taxed. (e.g., installment sales)
* A company deducts expenses for tax purposes *before* they are expensed in the income statement.
    * *Classic Example:* Using accelerated depreciation (like double-declining balance) for tax purposes to get bigger deductions early on, while using straight-line depreciation for financial reporting. This saves cash tax now but creates an obligation (liability) to pay more tax later when the timing difference reverses. 📉➡️📈

> **Think of it like this:** You got a tax break *today* because the tax rules were more generous upfront than the accounting rules. But you know you'll have to "pay it back" in the form of higher taxes *later*. That future obligation is the DTL.

#### **Deferred Tax Assets (DTAs): Paying More Tax Now, Less Later ✅**

A **Deferred Tax Asset (DTA)** arises when:
* **Taxes Payable (Tax Return) > Income Tax Expense (Income Statement)**

This typically happens when:
* A company recognizes revenue or gains for tax purposes *before* they are recognized in the income statement. (e.g., rent received in advance might be taxed immediately but recognized as revenue over the lease term)
* A company expenses costs in the income statement *before* they are tax-deductible.
    * *Classic Example:* Estimating and expensing warranty costs when products are sold (accrual accounting), but only getting the tax deduction later when the actual warranty claims are paid. This means paying more cash tax now, creating a future benefit (asset) – the right to pay less tax later. 📈➡️📉
* **Tax Loss Carryforwards:** If a company has losses for tax purposes, it might be able to use those losses to reduce taxable income (and thus taxes payable) in *future* profitable years. This future tax benefit is recognized as a DTA.

> **Think of it like this:** You paid *more* tax today than your income statement suggests you should have, perhaps because tax rules made you recognize income early or delayed an expense deduction. This overpayment creates a future benefit – the DTA – representing expected tax savings later.

#### **The Core Equation & Tax Rate Changes 🔄**

The link between these items is captured by:

$$\text{Income Tax Expense} = \text{Taxes Payable} + \Delta \text{DTL} - \Delta \text{DTA}$$

Where $\Delta$ means "change in".

* **Impact of Tax Rate Changes:** Since DTAs and DTLs represent *future* tax effects, they are measured using the *enacted tax rate* expected to apply when the temporary difference reverses. If the government changes the tax rates, the company must adjust the carrying value of its existing DTAs and DTLs.
    * An *increase* in the tax rate will *increase* both DTAs and DTLs.
    * A *decrease* in the tax rate will *decrease* both DTAs and DTLs.
    * This adjustment flows through the **income tax expense** on the income statement in the period the rate change is enacted.

> [\!TIP]
> **CFA Exam Tip ✍️:** Understand the triggers for DTA (Tax > Accrual Income or Accrual Expense > Tax Deduction) and DTL (Accrual Income > Tax or Tax Deduction > Accrual Expense). Remember permanent differences *don't* create deferred taxes, only temporary ones do. The core equation linking tax expense, taxes payable, and changes in DTA/DTL is fundamental.

-----

### Part 2: Building the DTA/DTL Balance Sheet 🏗️ (LOS 35.b)

While the income statement approach helps understand the *change*, the **balance sheet method** is typically used to calculate the actual DTA or DTL amount. This involves comparing the **Carrying Value** (book value) of assets and liabilities on the balance sheet with their **Tax Base**.

* **Tax Base of an Asset:** The amount that will be tax-deductible in the future as the asset's economic benefits are realized. For PP&E, it's often Cost - Accumulated Tax Depreciation.
* **Tax Base of a Liability:** Usually its carrying value less any amount that will be tax-deductible in the future. (Exception: Revenue received in advance is taxed upfront, so its tax base is Carrying Value - Amount that *won't* be taxed in the future).

The relationship is:

#### **Theory 🧠**

| Balance Sheet Item | Comparison             | Resulting Deferred Tax Item | Why?                                                                                                                              |
| :----------------- | :--------------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| **Asset** | Carrying Value > Tax Base | DTL                         | More economic benefit will be recognized for accounting than will be tax-deductible in the future (-> higher future taxable income). |
| **Asset** | Carrying Value < Tax Base | DTA                         | More tax deductions available in the future than accounting expense (-> lower future taxable income).                               |
| **Liability** | Carrying Value > Tax Base | DTA                         | Settling the liability will require outflows that *are* tax-deductible in the future, but aren't reflected in the tax base now.   |
| **Liability** | Carrying Value < Tax Base | DTL                         | Settling the liability involves amounts that have already provided a tax benefit (or won't provide one).                             |

#### **Example 🧮**

Let's revisit the machine from Part 1 ($30,000 cost).
* **End of Year 1:**
    * Accounting Depreciation = $5,000 ->$ Carrying Value = $25,000
    * Tax Depreciation = $10,000 ->$ Tax Base = $20,000
    * Carrying Value ($25k) > Tax Base ($20k). The difference is $5,000.
    * Result: DTL = $5,000 \times \text{Tax Rate}$. If Tax Rate = 30%, DTL = $1,500.

Let's look at the warranty liability from the PDF example.
* **End of Year 1:**
    * Warranty Provision = $5,000; Actual Expenditure = $2,000 ->$ Carrying Value = $3,000.
    * Tax rules don't allow deduction until paid -> Future deductible amount = $3,000.
    * Tax Base = Carrying Value - Future Deductible Amount = $3,000 - $3,000 = $0.
    * Carrying Value ($3k) > Tax Base ($0). The difference is $3,000.
    * Result: DTA = $3,000 \times \text{Tax Rate}$. If Tax Rate = 30%, DTA = $900.

#### **Realizability of Deferred Tax Assets: Will We Get the Benefit? 🤔**

A DTA represents a *future* tax saving. But what if the company doesn't expect to have enough *taxable income* in the future to actually realize those savings?

* Both IFRS and U.S. GAAP require companies to assess the likelihood of realizing DTA benefits ("more likely than not" threshold).
* **IFRS:** If realization is uncertain, the DTA value is directly reduced.
* **U.S. GAAP:** A separate **Valuation Allowance** (a contra-asset account) is created or increased to reduce the net DTA shown on the balance sheet.
    * *Increasing* the valuation allowance *decreases* net income (by increasing tax expense).
    * *Decreasing* the valuation allowance *increases* net income (by decreasing tax expense).
* **Analyst Alert:** Changes in the valuation allowance can be used to manage earnings\! Look for large or unusual changes. 🧐

#### **Analytical Adjustments: How Should We Treat DTA/DTL? ⚖️**

Analysts often adjust financial statements for deferred taxes:

* **DTLs Expected to Reverse:** If the temporary difference *will* reverse (e.g., depreciation on a single asset), treat the DTL as a **liability**. Some analysts might discount it if reversal is far in the future.
* **DTLs *Not* Expected to Reverse:** If a company consistently grows its capital spending, accelerated tax depreciation might perpetually create *new* temporary differences that offset reversing ones. In this case, the DTL balance might never decrease (or even keep growing). Many analysts treat such stable or growing DTLs as **equity**.
* **DTAs:** Treat as **assets**, but evaluate their realizability. If a significant valuation allowance exists or if the DTA relies on future profitability that seems uncertain, analysts might reduce or eliminate the DTA when calculating ratios.

> [\!TIP]
> **CFA Exam Tip ✍️:** Know the Balance Sheet Method (CV vs. Tax Base) rules for creating DTA/DTL. Understand the purpose and impact of the Valuation Allowance (U.S. GAAP). Be ready to explain when an analyst might treat a DTL as equity (stable/growing balance due to recurring source like capex) versus a liability (expected reversal).

-----

### Part 3: Rates, Reconciliations & Disclosures 📊🔍 (LOS 35.c, 35.d)

Understanding a company's tax situation requires looking beyond just the income tax expense line.

#### **Key Tax Rates**

* **Statutory Tax Rate:** The official corporate tax rate in the company's home country.
* **Effective Tax Rate (ETR):** 
  $$\text{ETR} = \frac{\text{Income Tax Expense}}{\text{Accounting Profit (Pretax Income)}}$$ 
  This represents the *actual* rate of tax paid on accounting profit. It often differs from the statutory rate due to permanent differences, tax credits, different tax rates in foreign jurisdictions, changes in valuation allowances, etc.
* **Cash Tax Rate:** 
  $$\text{Cash Tax Rate} = \frac{\text{Cash Taxes Paid}}{\text{Accounting Profit (Pretax Income)}}$$ 
  This measures the cash taxes paid relative to accounting profit.

#### **The Tax Rate Reconciliation**

Companies are required to show a reconciliation explaining *why* their effective tax rate differs from the statutory rate. This is super useful for analysts\! 🤓

* **Why Reconcile?** It highlights the impact of:
    * Permanent differences (e.g., tax-exempt income lowers ETR).
    * Tax credits (lowers ETR).
    * Different tax rates on foreign income (can raise or lower ETR).
    * Changes in valuation allowances (increasing VA raises ETR).
    * Tax holidays or specific incentives.
* **Analysis:**
    * Identify recurring items (like foreign rate differences) vs. one-off items (like a large asset sale).
    * Track trends in reconciliation items to better forecast future ETR.
    * Assess the sustainability of low tax rates (e.g., reliance on expiring tax holidays).

#### **Required Disclosures & Analyst Use**

Footnotes provide crucial details about deferred taxes:

* **Components of DTA/DTL:** What temporary differences are causing them (e.g., depreciation, warranties, inventory valuation, unrealized gains, pensions, tax loss carryforwards).
* **Valuation Allowance:** (U.S. GAAP) Details on the amount and changes.
* **Tax Loss Carryforwards:** Amounts and expiration dates.
* **Reconciliation:** The statutory vs. effective rate reconciliation described above.
* **Current vs. Noncurrent:** Breakdown of DTA/DTL on the balance sheet.

**Analysts use these disclosures to:**

* **Assess Earnings Quality:** Are DTAs being recognized aggressively? Is the valuation allowance reasonable?
* **Forecast Future Earnings & Cash Flow:** Understand the expected timing of DTA/DTL reversals. Estimate future effective and cash tax rates.
* **Evaluate Financial Position:** Adjust DTA/DTL treatment (liability vs. equity) for ratio analysis based on expected reversal patterns.
* **Compare Companies:** Adjust for differences in tax situations when comparing peers.

> [\!TIP]
> **CFA Exam Tip ✍️:** Understand the difference between statutory, effective, and cash tax rates. Know the common items found in a tax rate reconciliation (permanent diffs, foreign rates, credits, VA changes) and how they affect the ETR relative to the statutory rate. Be aware of the key footnote disclosures related to deferred taxes.

-----

### 🧪 Formula Summary

* **Core Relationship:**
    $$\text{Income Tax Expense} = \text{Taxes Payable} + \Delta \text{DTL} - \Delta \text{DTA}$$
* **Deferred Tax Asset/Liability Amount:**
    $$\text{DTA or DTL} = \text{Temporary Difference} \times \text{Enacted Tax Rate}$$
* **Effective Tax Rate (ETR):**
    $$\text{ETR} = \frac{\text{Income Tax Expense}}{\text{Pretax Income}}$$
* **Cash Tax Rate:**
    $$\text{Cash Tax Rate} = \frac{\text{Cash Taxes Paid}}{\text{Pretax Income}}$$

-----

> [\!IMPORTANT]
>
> ### 🎯 Quick Exam-Day Pointers
>
> * **Temporary vs. Permanent:** Only **temporary** differences (timing mismatches between accounting and tax rules that *will* reverse) create DTAs and DTLs. **Permanent** differences affect the ETR but not deferred taxes.
> * **DTL Trigger:** Accounting Income > Taxable Income (or Tax Deduction > Accounting Expense). Think "Liability" = Pay less tax now, more later.
> * **DTA Trigger:** Taxable Income > Accounting Income (or Accounting Expense > Tax Deduction), or Tax Loss Carryforwards. Think "Asset" = Pay more tax now, less later (or get future benefit).
> * **Balance Sheet Method:** Compare Carrying Value (Book) vs. Tax Base to determine DTA/DTL. Know the rules for assets vs. liabilities.
> * **Valuation Allowance (U.S. GAAP):** Reduces DTA if realization isn't "more likely than not." Increasing VA *reduces* Net Income. Watch for manipulation.
> * **Analyst Adjustments:** Treat DTLs expected to reverse as Liabilities; treat DTLs *not* expected to reverse (stable/growing) as Equity. Scrutinize DTA realizability.
> * **Rates:** Statutory (official), Effective (Tax Exp / Pretax Inc), Cash (Cash Tax / Pretax Inc). Know why ETR differs from Statutory (perm diffs, credits, foreign rates, VA changes). Use the reconciliation\!