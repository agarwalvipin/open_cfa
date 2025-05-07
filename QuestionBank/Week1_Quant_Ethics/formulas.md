# CFA Level 1 - Week 1 Formula Sheet

## Reading 1: Rates and Returns

### Interest Rate Components

* **Nominal Risk-Free Rate (Approximate Relation):**
    $$
    \text{Nominal Risk-Free Rate} \approx \text{Real Risk-Free Rate} + \text{Expected Inflation Rate}
    $$
    

* **Required Interest Rate on a Security (Conceptual Breakdown):**
    $$
    \begin{aligned} \text{Required Rate} \approx \quad & \text{Nominal Risk-Free Rate} \\ & + \text{ Default Risk Premium} \\ & + \text{ Liquidity Premium} \\ & + \text{ Maturity Risk Premium} \end{aligned}
    $$
    

### Return Measures

* **Holding Period Return (HPR):**
    $$
    HPR = \frac{\text{Ending Value} - \text{Beginning Value} + \text{Income}}{\text{Beginning Value}} = \frac{P_1 - P_0 + D_1}{P_0}
    $$
    

* **Multiperiod Holding Period Return:**
    $$
    (1 + HPR_{\text{Total}}) = (1 + HPR_1) \times (1 + HPR_2) \times \dots \times (1 + HPR_n)
    $$
    *The total return is found by subtracting 1 after compounding.*
    

* **Arithmetic Mean Return ($\bar{R}$):**
    $$
    \bar{R} = \frac{\sum_{t=1}^T R_t}{T}
    $$
    *Simple average of periodic returns.*
    

* **Geometric Mean Return ($R_G$):**
    $$
    R_G = \left[ \prod_{t=1}^T (1+R_t) \right]^{1/T} - 1
    $$
    *Compound annual rate.*
    

* **Harmonic Mean ($\bar{X}_H$):**
    $$
    \bar{X}_H = \frac{N}{\sum_{i=1}^N \frac{1}{X_i}}
    $$
    *Used for averaging ratios, like cost per share in dollar-cost averaging.*
    

* **Annualized Return from HPR:**
    $$
    R_{\text{Annual}} = (1 + HPR)^{\frac{365}{\text{Days}}} - 1
    $$
    *Adjusts HPR for a period of 'Days' to an annual equivalent.*
    

* **Continuously Compounded Return ($R_{CC}$):**
    $$
    R_{CC} = \ln(1 + HPR) = \ln\left(\frac{\text{Ending Value}}{\text{Beginning Value}}\right)
    $$
    *Where 'ln' is the natural logarithm.*
    

* **Nominal vs. Real Return (Exact Relation):**
    $$
    (1 + \text{Real Return}) = \frac{(1 + \text{Nominal Return})}{(1 + \text{Inflation Rate})}
    $$
    *So, Real Return = $\frac{(1 + \text{Nominal Return})}{(1 + \text{Inflation Rate})} - 1$*
    

* **Nominal vs. Real Return (Approximate Relation):**
    $$
    \text{Real Return} \approx \text{Nominal Return} - \text{Inflation Rate}
    $$
    

### Other Return Concepts

* **Leveraged Return Rate ($R_L$):**
    $$
    R_L = \frac{\text{Return on Total Investment} - \text{Borrowing Cost}}{\text{Equity Investment}} = \frac{r(V_0 + V_B) - r_B V_B}{V_0}
    $$
    *Where $r$ = return on total assets, $V_0$ = initial equity, $V_B$ = borrowed amount, $r_B$ = borrowing rate.*