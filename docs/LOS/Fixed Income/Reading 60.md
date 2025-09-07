## Reading 60: Credit Risk 📉

🎯 **Introduction**

Lending money, at its core, is an act of trust. **Credit risk** is the unfortunate possibility that this trust is broken—the risk that a borrower fails to pay back their loan as promised. For investors who buy corporate or other non-government bonds, this is the single most important risk to manage. This reading transforms us into credit detectives. We'll learn how to measure credit risk by looking at the *likelihood* of a default and the potential *severity* of the loss. We'll also examine the role of professional credit rating agencies and explore the economic forces that can cause a borrower's financial health to change.

---

### Part 1: What is Credit Risk and How Do We Measure It? 🔍

**Credit risk** is the risk of loss from a borrower's **default**, which is the failure to make timely payments of interest or principal. To measure this risk, we break it down into two fundamental components:

1.  **Probability of Default (POD):** What is the *likelihood* that the borrower will fail to meet their obligations? Is there a 1% chance? A 10% chance? This is influenced by factors like the company's financial health and the state of the economy.
2.  **Loss Given Default (LGD):** *If* the borrower defaults, how much of the invested money will be lost? This is the inverse of the **recovery rate**. If we expect to recover 40 cents on the dollar, the LGD is 60%. LGD is heavily influenced by the presence of collateral and the bond's seniority.

Combining these two gives us the **Expected Loss**.

**Formula: Expected Loss**
$$\text{Expected Loss} = \text{Probability of Default} \times \text{Loss Given Default}$$

This Expected Loss serves as a good approximation for the **credit spread** an investor should demand over a risk-free bond. It's the extra yield you need as compensation for taking on the credit risk.

> [!TIP]
> **CFA Exam Tip ✍️:** For the exam, clearly distinguish between the two components. **POD** is about *if* a default will happen. **LGD** is about *how bad* it will be if it does. The greatest risk for an **investment-grade** bond is a rising POD (credit deterioration), while for **high-yield** bonds, both POD and LGD are major concerns.

---

### Part 2: The Role of Credit Rating Agencies 🏅

**Credit rating agencies** like Standard & Poor's (S&P), Moody's, and Fitch provide independent, forward-looking opinions on the creditworthiness of an issuer or a specific bond. They assign letter grades that are understood globally.

The most important distinction is the line between **investment grade** and **non-investment grade**.



* **Investment Grade:** Bonds rated **BBB- (by S&P/Fitch) or Baa3 (by Moody's) and higher**. These are considered to have relatively low risk of default.
* **Non-Investment Grade (High-Yield or "Junk" Bonds):** Bonds rated **BB+ (S&P/Fitch) or Ba1 (Moody's) and lower**. These have a higher risk of default but offer higher yields as compensation.

While incredibly useful, investors should not rely solely on these ratings.

**Limitations of Credit Ratings:**
* **Ratings Lag the Market 🐢:** A bond's market price and its credit spread often react to new information much faster than a rating agency can publish a formal rating change.
* **Ratings Can't Capture All Risks 🎲:** Some risks, like a sudden lawsuit, a natural disaster, or a risky acquisition, are difficult for agencies to predict and incorporate into a rating.
* **Ratings Can Be Wrong:** Agencies are not infallible and can make mistakes or have conflicts of interest that may affect their judgment.

---

### Part 3: What Makes Credit Spreads Widen or Narrow? ↔️

**Credit spread risk** is the risk that a bond's price will fall because its yield spread over the risk-free benchmark widens. This is a primary concern for bond investors, especially in the investment-grade space. Spreads are dynamic and are influenced by several factors:

| Factor | Impact on Credit Spreads | Why? |
| :--- | :--- | :--- |
| **The Credit Cycle (Economy)** | **Widen** in recessions, **Narrow** in expansions | In a strong economy, corporate profits are high and defaults are rare, so investors demand less compensation for risk. The opposite is true in a recession. |
| **Market Conditions** | **Widen** during a "flight to quality" | In times of market fear, investors sell risky assets (like corporate bonds) and buy safe-haven assets (like government bonds), causing spreads to blow out. |
| **Broker-Dealer Capital** | **Widen** when broker-dealers have less capital | If the big banks that act as market makers have less capital, it's harder for them to hold inventory. This reduces market liquidity and investors demand a higher spread. |
| **Supply and Demand** | **Widen** with heavy new issuance | A flood of new corporate bond supply can overwhelm investor demand, forcing issuers to offer higher spreads to attract buyers. |
| **Issuer-Specific Factors** | Depends on the company | A company's own financial performance, industry trends, and management decisions directly impact its individual credit spread. |

---

### 🧪 Formula Summary

* **Loss Given Default (%):** $\text{LGD} = 1 - \text{Recovery Rate}$
* **Expected Loss (%):** $\text{EL} = \text{POD} \times \text{LGD}$
* **Credit Spread Approximation:** $\text{Credit Spread} \approx \text{POD} \times \text{LGD}$

---

> [!IMPORTANT]
> ### 🎯 Quick Exam-Day Pointers
>
> * **Credit Risk = POD x LGD:** The two core components are the **Probability of Default** and the **Loss Given Default**.
> * **The IG/HY Dividing Line:** Know the crucial cutoff: **BBB- / Baa3**. Anything above is **investment grade**; anything below is **high yield**.
> * **Don't Trust Ratings Blindly:** Remember that credit ratings **lag the market**, may not capture all risks, and are ultimately just opinions.
> * **Spreads Widen in Bad Times:** The most fundamental relationship to know is that credit spreads **widen** during economic downturns and periods of market stress.