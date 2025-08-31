## Reading 19 — Exchange-Rate Calculations

*(Economics Topic Area | CFA Level I)*

Below is a **LOS-by-LOS walkthrough** of Reading 19 with Indian-market illustrations, must-know formulas, exam hacks, and quick-day reminders.

---

### LOS 19.a Calculate **and interpret currency cross-rates** 

| Step                                      | What to do                                                                      | Example with INR                                                                                       |
| ----------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **1 — Align quotes**                      | Put both input rates in *common‐currency/base* form.                            | Suppose we have **USD/INR = 83.00** and **EUR/USD = 1.10**. Convert to **USD/EUR = 0.9091** if needed. |
| **2 — Multiply / divide so units cancel** | Cross rate = *(Price/Base₁) ÷ (Price/Base₂)* (or multiply if algebra dictates). | **INR/EUR = 83.00 × 0.9091 = 75.46 ₹ per €**.                                                          |
| **3 — Check sense**                       | Higher‐inflation currency should usually depreciate in real terms.              | Rupee costs fewer euros over time if India’s CPI > Eurozone.                                           |
| **4 — Quote direction**                   | State whether result is *direct* or *indirect* for your home trader.            | For an Indian candidate, INR/EUR is **direct** (price currency ₹).                                     |

> **Memory hook:** draw a “currency ladder” on scratch: *rupee → dollar → euro*; walk along and cancel the rungs. The Schweser example CHF/NZD = (CHF/USD) ÷ (NZD/USD) ➔ 0.7900 shows the algebra in action .

#### Indian reality check 🔍

Air-India hedges jet-fuel bills priced in USD but receives revenue partly in EUR on EU routes. Treasury calculates INR/EUR cross-rate daily to measure margin squeeze.

**Exam trap:** If one quote is *AUD/USD* and the other *NZD/USD*, you must **invert** one before multiplying so the USD terms cancel.

---

### LOS 19.b Explain the **spot-forward-interest-rate arbitrage link** and compute forward rates from points or percentages 

| Concept                                        | Formula                                                                     | “Say it in Indian”                                                                                     |
| ---------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Covered interest-rate parity (CIRP)**        | $F_{P/B} = S_{P/B}\dfrac{1+i_P}{1+i_B}$                                     | With 1-yr INR depo at **7 %** and USD depo at **4 %**, spot **83 ₹/\$**, the 1-yr **F₍₹/\$₎ ≈ 85.40**. |
| **Forward premium / discount** (base currency) | $\text{Prem}_{B} = \frac{F_{P/B}}{S_{P/B}} - 1$                             | If F > S, base is **at premium** (₹ usually at discount vs \$).                                        |
| **Using forward points**                       | $F = S + \text{Points} × 10^{-n}$ ( *n* = # decimals in quote)              | USD/INR spot 83.0200, 3-month pts +18.5 ➔ F = 83.0385.                                                 |
| **Cross-currency forward**                     | Chain two CIRP relations or build synthetic forward via money-market hedge. | Compute 6-mo EUR/INR forward from USD legs if direct bank quote absent.                                |

> **Why arbitrage binds rates:** If quoted F deviates from CIRP, traders borrow the low-rate currency, swap at spot, invest high-rate currency, lock forward, and pocket risk-free profit—forcing F back to no-arbitrage level .

#### Quick RBI-flavoured example

March 2025: 1-yr MCLR ≈ 9 %, Fed funds ≈ 5 %. Spot 83 ₹/\$ implies theoretical 1-yr forward 86.32 ₹/\$. Banks quoted 86.50. Arbitrage? No—quote within bid-ask cusp (<0.2 ₹) so friction wipes profit.

---

## 📑 Formula Sheet – Reading 19

| Task                                | Formula                                                                          |
| ----------------------------------- | -------------------------------------------------------------------------------- |
| **Cross-rate**                      | $X_{C/A} = \dfrac{X_{C/B}}{X_{A/B}}$ (choose multiply or divide to cancel units) |
| **CIRP forward rate**               | $F = S\bigl(\tfrac{1+i_P}{1+i_B}\bigr)$                                          |
| **Forward points conversion**       | $F = S + \tfrac{\text{Pts}}{10^{n}}$                                             |
| **Forward premium/discount (base)** | $\% = \tfrac{F}{S} - 1$                                                          |

*(All symbols as defined above.)*

---

## 🚀 Quick Exam-Day Pointers

1. **Write “Base at the bottom”** next to scratch space—prevents inversion errors.
2. Use the **ladder method**: set up chain so unwanted currencies cancel; arrow points to desired quote.
3. **Premium vs discount sign:** Forward > Spot ⇒ base currency premium; the price currency shows discount.
4. **Forward points:** plus (+) means add to spot (for price currency quotes); minus (–) subtract.
5. **CIRP plug-n-play:** Spot × (1+high-i)/(1+low-i) — do it once in your mind before touching calculator.
6. Fractions kill time—convert to decimals early (e.g., 25 points = 0.0025 if 4-dec quote).

Stick these on your palm-sized cheat card, Vipin, and Reading 19 becomes free marks before you even touch the tougher sections!
