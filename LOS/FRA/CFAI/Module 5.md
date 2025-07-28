### **Reading 5: Analyzing Statements of Cash Flows II**

This reading builds on the previous one, focusing on how to use the information in the Statement of Cash Flows to evaluate a company's performance, calculate important valuation metrics like free cash flow, and assess liquidity and solvency.

#### **1. Evaluating Sources and Uses of Cash**

**Detailed Explanation:**
A thorough analysis involves looking at the patterns of cash flow over several years. The combination of positive or negative cash flows from operating, investing, and financing activities tells a story about the company's life cycle and health.

| CFO | CFI | CFF | Interpretation & Company Stage |
| :-- | :-- | :-- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| **+** | **−** | **−** | **Healthy, Mature Company:** Generating more cash than it needs from operations. Using it to invest for the future (CFI −) and pay back capital providers (CFF −, e.g., dividends, debt repayment). This is the ideal pattern. |
| **+** | **−** | **+** | **Growing Company:** Operations are profitable, but the company needs more cash for expansion than it generates internally. So, it's investing heavily (CFI −) and raising capital to fund this growth (CFF +). |
| **−** | **+** | **+** | **Struggling Company / Early Startup:** Not generating cash from operations. It's raising external capital (CFF +) and possibly selling off assets (CFI +) just to stay afloat. This is not sustainable. |
| **+** | **+** | **−** | **Mature/Restructuring Company:** Generating cash from operations and selling off assets (CFI +). Using this cash to pay down debt or return cash to shareholders (CFF −). This could signal a lack of growth opportunities. |

**Indian Context Example:**
* **Hindustan Unilever (HUL)** typically shows a healthy, mature pattern (**CFO +, CFI −, CFF −**). It generates strong cash from selling its consumer goods, invests some in its factories, and pays substantial dividends to shareholders.
* A fast-growing tech company like **Nykaa** in its early public years might show a pattern of (**CFO +, CFI −, CFF +**). It generates cash from operations but invests heavily in technology and marketing, funding it with proceeds from its IPO.

> **CFA Exam Tip:**
> Be prepared to look at a summary of a company's cash flows over a few years (e.g., CFO was positive, CFI was negative, CFF was positive) and identify the most likely stage of its life cycle.

---

#### **2. Free Cash Flow (FCF) Measures**

**Detailed Explanation:**
Free cash flow represents the cash that a company generates after accounting for the cash outlays to support its operations and maintain its capital assets. It's a crucial metric for valuation because it represents the cash available to be distributed to the company's capital providers (debt and equity holders).

There are two main types:
1.  **Free Cash Flow to the Firm (FCFF):** This is the cash flow available to **all** capital providers (both debt and equity holders) *before* any debt payments are made.
2.  **Free Cash Flow to Equity (FCFE):** This is the cash flow available to **only** the equity holders *after* all debt-related payments (interest and principal) have been made.

**Calculations:**
The formulas can be started from either Net Income or CFO. Starting from CFO is often easier.
* **FCInv (Fixed Capital Investment):** This is simply the capital expenditures (capex). `FCInv = Capex - Proceeds from sale of long-term assets`.
* **Net Borrowing:** `Debt Issued - Debt Repaid`.

**Indian Context Example:**
An analyst valuing **Tata Steel** would calculate its FCFF to determine the total value of the company (its enterprise value). They would start with Tata Steel's CFO, add back the after-tax interest paid on its large debt load, and then subtract its heavy capital expenditures on its steel plants. The resulting FCFF could then be discounted to find the company's value. To find the value of just the equity, they would calculate FCFE.

> **CFA Exam Tip:**
> You **must know the formulas for FCFF and FCFE**, especially the versions starting from CFO. These are highly likely to be tested. A common question provides the components (CFO, Interest Paid, Tax Rate, Capex, Net Borrowing) and asks you to calculate either FCFF or FCFE.

---

#### **3. Cash Flow Ratios**

**Detailed Explanation:**
These ratios use cash flow data, which is often seen as less subject to manipulation than accrual-based earnings data.

* **Performance/Profitability Ratios:** These measure a company's ability to generate cash from its operations.
    * **Cash Flow to Revenue:** (CFO / Revenue) - Shows how much cash is generated from every rupee of sales.
    * **Cash Return on Assets:** (CFO / Average Total Assets) - Shows how well the company uses its asset base to generate operating cash.
* **Coverage Ratios:** These measure a company's ability to meet its debt obligations. They are crucial for credit analysis.
    * **Debt Coverage:** (CFO / Total Debt) - Measures the ability to pay back total debt from operating cash flow.
    * **Interest Coverage:** ((CFO + Interest Paid + Taxes Paid) / Interest Paid) - This is a cash-based version of the times interest earned ratio. It shows the ability to make interest payments from operating cash.
    * **Reinvestment:** (CFO / Capex) - Shows the ability to fund capital expenditures from internally generated cash. A ratio > 1.0 is desirable.

**Indian Context Example:**
A lender at the State Bank of India (SBI) evaluating a loan application from a manufacturing company would heavily rely on cash flow coverage ratios. They would look at the **Debt Coverage Ratio** to see how many years of operating cash flow it would take to pay back all its debt. A low ratio would be a major concern.

> **CFA Exam Tip:**
> Be familiar with the purpose of the main cash flow ratios. You might be asked which ratio is best for assessing a specific aspect of performance (e.g., "Which ratio best measures a company's ability to fund its capital spending from internal cash?"). The answer would be the Reinvestment ratio. Calculation questions are also possible.

***

### **Reading 5: Summary**

#### **List of Formulas Used**
1.  **Free Cash Flow to the Firm (FCFF):**
    * From Net Income:
        $$\text{FCFF} = \text{NI} + \text{NCC} + \text{Int}(1 - \text{Tax Rate}) - \text{FCInv} - \text{WCInv}$$
    * From CFO:
        $$\text{FCFF} = \text{CFO} + \text{Int}(1 - \text{Tax Rate}) - \text{FCInv}$$
        *Where: NI = Net Income, NCC = Non-cash Charges, Int = Interest Expense, FCInv = Fixed Capital Investment, WCInv = Working Capital Investment, CFO = Cash Flow from Operations*

2.  **Free Cash Flow to Equity (FCFE):**
    * From FCFF:
        $$\text{FCFE} = \text{FCFF} - \text{Int}(1 - \text{Tax Rate}) + \text{Net Borrowing}$$
    * From CFO:
        $$\text{FCFE} = \text{CFO} - \text{FCInv} + \text{Net Borrowing}$$

3.  **Key Cash Flow Ratios:**
    * **Debt Coverage:** `CFO / Total Debt`
    * **Interest Coverage:** `(CFO + Interest Paid + Taxes Paid) / Interest Paid`
    * **Reinvestment:** `CFO / Cash paid for long-term assets (Capex)`

#### **Quick Exam-Day Pointer**
* The pattern of signs (+ or −) for CFO, CFI, and CFF can indicate a company's life-cycle stage. The **healthy, mature profile is CFO+, CFI-, CFF-**.
* **FCFF is the cash available to ALL capital providers (debt and equity).**
* **FCFE is the cash available to ONLY equity holders.**
* Master the FCFF and FCFE formulas starting from CFO, as they are simpler and more frequently tested.
* Cash-based coverage ratios (like Debt Coverage) are important tools for credit analysis.
