# CFA Level 1 - Week 2 Formula Sheet

## Reading 2: The Time Value of Money in Finance

### Basic Concepts

* **Future Value (FV) of a Single Sum:**
    $$
    FV = PV(1+r)^N
    $$
    *Where PV = Present Value, r = periodic interest rate, N = number of periods.*

* **Present Value (PV) of a Single Sum:**
    $$
    PV = \frac{FV}{(1+r)^N}
    $$
   

* **Future Value (FV) with Continuous Compounding:**
    $$
    FV = PV e^{rN}
    $$
    *Where e is the base of the natural logarithm (\(e \approx 2.71828\)).*

* **Present Value (PV) with Continuous Compounding:**
    $$
    PV = FV e^{-rN} \quad \text{or} \quad PV = \frac{FV}{e^{rN}}
    $$
   

### Perpetuities

* **Present Value (PV) of a Perpetuity:**
    $$
    PV_{\text{Perpetuity}} = \frac{PMT}{r}
    $$
    *Where PMT is the constant periodic payment, r is the periodic discount rate.*

### Annuities

* **Present Value (PV) of an Ordinary Annuity:**
    $$
    PV = PMT \left[ \frac{1 - \frac{1}{(1+r)^N}}{r} \right]
    $$
    *(Often solved using calculator functions: N, I/Y, PMT, FV=0, CPT PV)*

* **Future Value (FV) of an Ordinary Annuity:**
    $$
    FV = PMT \left[ \frac{(1+r)^N - 1}{r} \right]
    $$
    *(Often solved using calculator functions: N, I/Y, PMT, PV=0, CPT FV)*

* **Annuity Payment (PMT) based on PV:**
    $$
    PMT = \frac{PV}{\left[ \frac{1 - \frac{1}{(1+r)^N}}{r} \right]}
    $$
    *(Often solved using calculator functions: N, I/Y, PV, FV=0, CPT PMT)*

### Equity Valuation Models

* **Value of Preferred Stock (Perpetuity Model):**
    $$
    V_P = \frac{D_P}{k_P}
    $$
    *Where $D_P$ = Preferred Dividend, $k_P$ = Required Rate of Return on Preferred Stock.*

* **Constant Growth Dividend Discount Model (Gordon Growth Model):**
    $$
    V_0 = \frac{D_1}{k_e - g_c}
    $$
    *Where $V_0$ = Value of stock today, $D_1$ = Expected Dividend next period, $k_e$ = Required Rate of Return on Equity, $g_c$ = Constant Dividend Growth Rate. Requires $k_e > g_c$.*

* **Implied Required Return on Equity (from Gordon Growth Model):**
    $$
    k_e = \frac{D_1}{P_0} + g_c
    $$
    *Where $P_0$ is the current market price.*

* **Implied Constant Growth Rate (from Gordon Growth Model):**
    $$
    g_c = k_e - \frac{D_1}{P_0}
    $$
   

* **Value from Multistage Dividend Discount Model:**
    $$
    V_0 = \sum_{t=1}^{n} \frac{D_t}{(1+k_e)^t} + \frac{P_n}{(1+k_e)^n}
    $$
    *Where $D_t$ are dividends during the initial high-growth stage(s), $n$ is the number of periods in the initial stage(s), and $P_n$ is the terminal value at the start of the constant growth phase, often calculated using the Gordon Growth Model: $P_n = \frac{D_{n+1}}{k_e - g_c}$.*