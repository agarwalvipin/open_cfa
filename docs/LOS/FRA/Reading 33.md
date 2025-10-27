## Reading 33: Analysis of Long-Term Assets

### 🎯 Introduction

Imagine a company is like a factory. 🏭 **Long-term assets** are the big, important machines inside – the property, plant, and equipment (**PP&E**) that churn out products, plus the invisible but valuable stuff like patents and brand names (**intangible assets**). This reading is your guide to understanding how companies account for these crucial assets, from buying them to using them up (depreciation/amortization), figuring out if they've lost value (**impairment**), and finally getting rid of them (**derecognition**). Mastering this helps you assess how efficiently a company uses its core operational resources!

-----

### <span style="color: #1565C0;">Part 1: Intangible Long-Lived Assets - The Invisible Value 🤔 (LOS 33.a)</span>

**Intangible assets** are valuable resources you can't touch – think brand names (like Coca-Cola's logo🥤), patents (like Pfizer's drug formulas🧪), copyrights, and **goodwill**. Accounting treats them differently depending on how the company got them.

#### <span style="color: #6A1B9A;">1.1 Purchased Intangibles 🛒</span>

* **What:** Buying a patent, trademark, or license from someone else.
* **Accounting:**
  * Recorded on the balance sheet at **cost** (purchase price + related costs).
  * **Finite Life (e.g., patent with 10 years left):** Amortized (expensed gradually) over its useful life. Tested for impairment if needed.
  * **Indefinite Life (e.g., a renewable broadcast license):** Not amortized. Tested for impairment annually.
* **Models (IFRS vs. U.S. GAAP):**
  * **IFRS:** Can use the **Cost Model** (cost less accumulated amortization/impairment) OR the **Revaluation Model** (fair value, *only if* an active market exists – rare for intangibles). Revaluations upward go to OCI (Equity), downward go to Income Statement.
  * **U.S. GAAP:** Only the **Cost Model** is allowed.

#### <span style="color: #6A1B9A;">1.2 Internally Developed Intangibles 🧑‍🔬</span>

* **What:** Creating a brand name, customer list, or new technology through the company's own efforts (R&D).
* **Accounting (General Rule):** Most costs are **expensed as incurred**, NOT put on the balance sheet. Why? Because the future benefits are often too uncertain. Think of advertising costs to build a brand – expensed immediately.
* **Key Exception: Research & Development (R&D)**
  * **IFRS:**
    * **Research Phase** (searching for new knowledge): Costs are **expensed**. 🧪➡️🗑️
    * **Development Phase** (applying research to create a product/process): Costs *can be* **capitalized** (put on the balance sheet as an intangible asset) IF specific criteria are met (technical feasibility, intent to complete/sell, future benefits probable, resources available, etc.). 💡➡️💰
  * **U.S. GAAP:**
    * Generally, both **Research** AND **Development** costs are **expensed**. 🧪+💡➡️🗑️
    * **Exception:** Software development costs *can be* capitalized after technological feasibility is established (similar to IFRS development). 💻➡️💰
* **Impact:** A company developing its own brands/tech (expensing costs) will show lower assets and lower profits (initially) compared to a company buying them (capitalizing costs).

#### <span style="color: #6A1B9A;">1.3 Acquired in a Business Combination (Merger/Acquisition) 🤝</span>

* **What:** When one company buys another, it acquires all its assets, including intangibles – even ones the acquired company didn't have on *its own* balance sheet (like internally developed brands).
* **Accounting:**
  * All identifiable intangible assets (patents, brands, customer lists, etc.) of the acquired company are recorded on the *acquirer's* balance sheet at their **fair value** at the acquisition date.
  * Any *excess* purchase price paid over the fair value of the acquired company's *net identifiable assets* (Assets - Liabilities) is recorded as **Goodwill**.

    <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

    $$\text{Goodwill} = \text{Purchase Price} - \text{Fair Value of Net Identifiable Assets Acquired}$$

    </div>

  * **Goodwill** is an **unidentifiable intangible asset** with an **indefinite life**. It's not amortized but must be tested for impairment annually.

#### <span style="color: #00838F;">1.4 Global & Local Context 🌍</span>

* **Global Example (R&D):** A European pharmaceutical company (under IFRS) like Roche might capitalize significant costs for a drug in late-stage development, while a U.S. competitor like Merck (under U.S. GAAP) would likely have expensed similar costs earlier.
* **Indian Example (Goodwill):** When Tata Motors acquired Jaguar Land Rover, the excess price paid over the fair value of JLR's identifiable assets (factories, brands like Jaguar and Land Rover, technology patents, etc.) would have been recorded as Goodwill on Tata Motors' consolidated balance sheet.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️:Know the IFRS vs. U.S. GAAP R&D difference cold! IFRS splits R&D (expense Research, capitalize Development if criteria met), while U.S. GAAP generally expenses both (except software). Also, remember Goodwill arises *only* from acquisitions and is the 'plug' figure representing the premium paid over fair value of net identifiable assets.

</div>
</div>

-----

### <span style="color: #1565C0;">Part 2: Impairment and Derecognition - When Assets Lose Value 📉➡️🗑️ (LOS 33.b)</span>

Assets don't always hold their value. Sometimes, their worth drops unexpectedly (**impairment**), or the company gets rid of them (**derecognition**).

#### <span style="color: #6A1B9A;">2.1 Impairment: When Value Plummets 📉</span>

<div style="background-color: #F3E5F5; border-left: 5px solid #7B1FA2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

**💡 MNEMONIC: "IFRS: 1-Step & REVERSES; US GAAP: 2-Steps & NO Reversals"**
- **IFRS**: **O**ne-step test (CV vs Recoverable), **R**eversals allowed (except Goodwill)
- **US GAAP**: **T**wo-step test (Recoverability then FV), **N**o reversals
- Think: "**OR**" for IFRS, "**TN**" for US GAAP (Tennessee = no reversals!)

</div>
</div>

An asset is **impaired** if its carrying value (book value) on the balance sheet is higher than its recoverable amount. Both IFRS and U.S. GAAP require writing down impaired assets, but the process differs slightly.

##### <span style="color: #E65100;">2.1.1 IFRS Impairment</span>

* **When to Test:** Annually for indefinite-life intangibles and goodwill. For others, test if indicators of impairment exist (e.g., damage, obsolescence, market decline).
* **Test:** Compare **Carrying Value** to **Recoverable Amount**.
  * **Recoverable Amount** = HIGHER of:
    * **Value in Use:** Present value (PV) of expected future cash flows from using the asset + disposal.
    * **Fair Value less Costs to Sell:** What you could sell it for, minus transaction costs.
* **Impairment Loss:** If Carrying Value > Recoverable Amount, then:

  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

  $$\text{Impairment Loss} = \text{Carrying Value} - \text{Recoverable Amount}$$

  </div>

  The loss is recognized on the **Income Statement** (reduces profit), and the asset's carrying value on the **Balance Sheet** is reduced.
* **Reversals:** YES! If the recoverable amount increases later, the impairment loss can be reversed (up to the original carrying value before impairment). The reversal increases income. (Reversals NOT allowed for Goodwill).

##### <span style="color: #E65100;">2.1.2 U.S. GAAP Impairment (PP&E & Finite-Life Intangibles)</span>

* **When to Test:** Only when events indicate the carrying value may not be recoverable.
* **Two-Step Test:**
  1. **Recoverability Test:** Is **Carrying Value** > **Undiscounted** Future Cash Flows?
     * If YES, the asset *is* impaired. Proceed to Step 2.
     * If NO, the asset is *not* impaired. Stop.
  2. **Loss Measurement:** If impaired (failed Step 1), calculate the loss:

    <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

    $$\text{Impairment Loss} = \text{Carrying Value} - \text{Fair Value}$$

    </div>

    (Fair value is the market price or PV of future cash flows if market price unavailable).
    The loss hits the **Income Statement**, and the asset is written down to **Fair Value** on the **Balance Sheet**.
* **Reversals:** NO! Once written down, impairment losses cannot be reversed, even if the value recovers.

##### <span style="color: #E65100;">2.1.3 U.S. GAAP Impairment (Indefinite-Life Intangibles)</span>

* **When to Test:** Annually.
* **Test:** Similar to Step 2 above (no recoverability test). Compare **Carrying Value** directly to **Fair Value**.
* **Impairment Loss:** If Carrying Value > Fair Value, then:

  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

  $$\text{Impairment Loss} = \text{Carrying Value} - \text{Fair Value}$$

  </div>

* **Reversals:** NO!

#### <span style="color: #6A1B9A;">2.2 Financial Statement & Ratio Impact of Impairment</span>

* **Income Statement:** Loss recognized → Lower Net Income in the impairment year.
* **Balance Sheet:** Asset carrying value reduced → Lower Total Assets, Lower Equity (via Retained Earnings).
* **Cash Flow Statement:** No immediate cash impact (non-cash charge), but future cash flows might be lower if the asset is less productive.
* **Ratios (Year of Impairment):**
  * **Profitability (ROA, ROE):** Decrease (lower NI, lower Assets/Equity).
  * **Activity (Asset Turnover):** Increase (Sales stay same, Avg Assets decrease).
  * **Solvency (Debt-to-Assets, Debt-to-Equity):** Increase (Assets/Equity decrease).
* **Ratios (Subsequent Years):**
  * **Profitability (ROA, ROE):** Increase (NI is higher due to lower future depreciation/amortization; Assets/Equity are lower).
  * Depreciation/Amortization expense will be lower because it's based on the new, lower carrying value.

#### <span style="color: #6A1B9A;">2.3 Derecognition: Getting Rid of Assets 🗑️</span>

This happens when an asset is sold, abandoned, exchanged, or spun off.

* **Sale:**
  * Cash received = **Investing Cash Inflow (CFI)**.
  * Asset (carrying value) removed from the balance sheet.
  * **Gain or Loss** recognized on Income Statement:

    <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

    $$\text{Gain/Loss} = \text{Sale Proceeds} - \text{Carrying Value}$$

    </div>

* **Abandonment:**
  * No cash received.
  * Asset (carrying value) removed from the balance sheet.
  * **Loss** recognized on Income Statement = Carrying Value.
* **Exchange (for another asset):**
  * Old asset (carrying value) removed.
  * New asset recorded, usually at its **fair value**.
  * **Gain or Loss** recognized on Income Statement = Fair Value of Old Asset - Carrying Value of Old Asset. (If fair values unreliable, new asset recorded at old asset's carrying value, no gain/loss).
* **Spinoff:** A division/subsidiary becomes a separate company. The assets/liabilities are removed from the parent's balance sheet (often classified as 'held for sale'/'distribution' first). No gain/loss typically recognized on the spinoff itself.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️:Focus on the IFRS vs. U.S. GAAP impairment differences: IFRS uses a one-step test (Carrying Value vs. Recoverable Amount) and allows reversals (except goodwill). U.S. GAAP uses a two-step test (Recoverability first, then measure loss vs. Fair Value) and *never* allows reversals for assets held for use. Understand the ratio impacts in *both* the impairment year and subsequent years.

</div>
</div>

-----

### <span style="color: #1565C0;">Part 3: Long-Term Asset Disclosures - Mining the Footnotes 📝 (LOS 33.c)</span>

The footnotes are where the real details about long-term assets hide. Analysts need these disclosures to understand the company's investments, depreciation/amortization policies, and potential future needs.

#### <span style="color: #6A1B9A;">3.1 Key Disclosures (IFRS & U.S. GAAP generally similar)</span>

* **Carrying values** for each major class of asset (Land, Buildings, Machinery, Patents, Goodwill, etc.), often showing Gross Cost and Accumulated Depreciation/Amortization separately.
* **Depreciation/Amortization methods** used (e.g., straight-line, declining balance) and estimated **useful lives** or **amortization periods**.
* **Depreciation/Amortization expense** for the period.
* **Impairment losses** recognized and any reversals (IFRS only).
* Details about assets **pledged as collateral** for debt.
* Information on **capital expenditures** during the period and commitments for future expenditures.
* For **Revaluation Model (IFRS only):** Revaluation date, methods used, carrying amount under the cost model, revaluation surplus details.

#### <span style="color: #6A1B9A;">3.2 How Analysts Use Disclosures</span>

* **Assess Depreciation/Amortization Choices:** Are the methods and useful lives reasonable compared to industry peers? Aggressive choices (long lives, high salvage values) can inflate current profits but lead to problems later.
* **Estimate Average Age & Remaining Life:** Useful for judging asset efficiency and predicting future capital expenditures.

  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

  $$\text{Average Age} \approx \frac{\text{Accumulated Depreciation}}{\text{Annual Depreciation Expense}}$$

  $$\text{Average Depreciable Life (Total Useful Life)} \approx \frac{\text{Ending Gross Investment}}{\text{Annual Depreciation Expense}}$$

  $$\text{Remaining Useful Life} \approx \frac{\text{Ending Net Investment}}{\text{Annual Depreciation Expense}}$$

  </div>

  *(Note: These are rough estimates, best for straight-line depreciation).*
* **Evaluate Capital Expenditures:** Is the company investing enough to maintain its asset base (CapEx relative to depreciation)? Is it investing for growth?
* **Calculate Fixed Asset Turnover:** Measures efficiency in using fixed assets to generate sales.

  <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

  $$\text{Fixed Asset Turnover} = \frac{\text{Revenue}}{\text{Average Net Fixed Assets}}$$

  </div>

* **Identify Impairment Trends:** Recurring impairments might signal poor investment decisions or deteriorating industry conditions.
* **Understand Goodwill:** Large or growing goodwill suggests growth through acquisitions. Subsequent impairments indicate potential overpayment or poor integration.

#### <span style="color: #00838F;">3.3 Global & Local Context 🌍</span>

* **Global Example:** Comparing the average age of the aircraft fleet for airlines like Emirates vs. American Airlines using their footnote disclosures can indicate differences in investment cycles, fuel efficiency, and future CapEx needs.
* **Indian Example:** An analyst looking at Reliance Industries could use disclosures to compare the depreciation methods and useful life assumptions for its petrochemical plants versus those used by global competitors like BASF, assessing if Reliance's accounting choices are conservative or aggressive.

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️:Understand what each disclosure tells you. Be prepared to calculate the approximate age/life ratios and interpret them. Recognize that management choices regarding useful lives and salvage values directly impact reported depreciation expense and net income. High fixed asset turnover suggests efficient use of assets.

</div>
</div>

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Goodwill:** 

$$\text{Goodwill} = \text{Purchase Price} - \text{Fair Value of Net Identifiable Assets Acquired}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Impairment Loss (IFRS):** 

$$\text{Loss} = \text{Carrying Value} - \text{Recoverable Amount}$$ 

*(where Recoverable Amount = Higher of Value in Use or Fair Value less Costs to Sell)*

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Impairment Loss (U.S. GAAP - PP&E/Finite Intangibles):** 

Step 1: Check if Carrying Value > Undiscounted Cash Flows. If yes, then Step 2: 

$$\text{Loss} = \text{Carrying Value} - \text{Fair Value}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Impairment Loss (U.S. GAAP - Indefinite Intangibles):** 

$$\text{Loss} = \text{Carrying Value} - \text{Fair Value}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Gain/Loss on Asset Sale:** 

$$\text{Gain/Loss} = \text{Sale Proceeds} - \text{Carrying Value}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Average Age:** 

$$\text{Average Age} \approx \frac{\text{Accumulated Depreciation}}{\text{Annual Depreciation Expense}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Average Depreciable Life:** 

$$\text{Avg. Depreciable Life} \approx \frac{\text{Ending Gross Investment}}{\text{Annual Depreciation Expense}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Remaining Useful Life:** 

$$\text{Remaining Life} \approx \frac{\text{Ending Net Investment}}{\text{Annual Depreciation Expense}}$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Fixed Asset Turnover:** 

$$\text{Fixed Asset Turnover} = \frac{\text{Revenue}}{\text{Average Net Fixed Assets}}$$

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* **Intangible Origins Matter:** 
  * **Purchased** → **Capitalize** 
  * **Internally Developed** → **Mostly Expense** (except IFRS Development & Software)
  * **Acquired in M&A** → **Capitalize at Fair Value**, excess is **Goodwill**
* **R&D Dichotomy:** 
  * **IFRS:** Expense Research / Capitalize Development (if feasible)
  * **U.S. GAAP:** Expense both (except software post-feasibility)
* **Goodwill:** Only from acquisitions, indefinite life, not amortized, test annually for impairment. Represents premium paid.
* **Impairment Triggers & Tests:** 
  * **IFRS:** Recoverable Amount test
  * **U.S. GAAP:** Undiscounted CF test → then Fair Value
* **Impairment Reversals:** 
  * **IFRS:** ✅ YES (except Goodwill)
  * **U.S. GAAP:** ❌ NO (for held-for-use assets)
* **Impairment Impact:** 
  * **Impairment Year:** ⬇️ Lowers NI, Assets, Equity
  * **Future Years:** ⬆️ Increases ROA/ROE (lower depreciation base), turnover, leverage ratios
* **Derecognition:** Gain/Loss = Proceeds/Fair Value - Carrying Value. Impacts NI and CFI (for sales).
* **Disclosures:** Use them to assess accounting quality (depreciation choices), estimate asset age/life, gauge investment levels (CapEx vs. Dep.), and calculate efficiency (Fixed Asset Turnover).

</div>
</div>