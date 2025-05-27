# 🧾 Formula Sheet: Week 1 - Rates and Returns (Reading 1)

## LOS 1.a: Interpret interest rates as required rates of return, discount rates, or opportunity costs and explain an interest rate as the sum of a real risk-free rate and premiums that compensate investors for bearing distinct types of risk.

* **Nominal Risk-Free Rate (Exact Formula)** [cite: 141]
    ```math
    (1 + \text{Nominal Risk-Free Rate}) = (1 + \text{Real Risk-Free Rate}) \times (1 + \text{Expected Inflation Rate})
    ```

* **Nominal Risk-Free Rate (Approximation)** [cite: 141]
    ```math
    \text{Nominal Risk-Free Rate} \approx \text{Real Risk-Free Rate} + \text{Expected Inflation Rate}
    ```

* **Components of a Nominal Interest Rate** [cite: 148]
    ```math
    \text{Nominal Interest Rate} = \text{Real Risk-Free Rate} + \text{Inflation Premium} + \text{Default Risk Premium} + \text{Liquidity Premium} + \text{Maturity Premium}
    ```

---

## LOS 1.b: Calculate and interpret different approaches to return measurement over time and describe their appropriate uses.

* **Holding Period Return (HPR) - General** [cite: 149]
    ```math
    HPR = \frac{\text{End-of-Period Value}}{\text{Beginning-of-Period Value}} - 1
    ```

* **Holding Period Return (HPR) - For a Stock with Dividends** [cite: 149]
    ```math
    HPR = \frac{P_t + Div_t}{P_0} - 1
    ```
    or
    ```math
    HPR = \frac{P_t - P_0 + Div_t}{P_0}
    ```
    Where:
    * $P_t$ = Price at the end of the period
    * $P_0$ = Price at the beginning of the period
    * $Div_t$ = Dividend paid during the period

* **Holding Period Return (HPR) - Over Multiple Periods** [cite: 150]
    (Example for 3 periods)
    ```math
    HPR_{\text{Total}} = (1 + HPR_{\text{Period 1}}) \times (1 + HPR_{\text{Period 2}}) \times (1 + HPR_{\text{Period 3}}) - 1
    ```

* **Arithmetic Mean Return** [cite: 152]
    ```math
    \bar{R}_{\text{Arithmetic}} = \frac{\sum_{i=1}^{n} R_i}{n} = \frac{R_1 + R_2 + \dots + R_n}{n}
    ```
    Where:
    * $R_i$ = Return for period $i$
    * $n$ = Number of periods

* **Geometric Mean Return** [cite: 153]
    ```math
    \bar{R}_{\text{Geometric}} = \left[ \prod_{i=1}^{n} (1 + R_i) \right]^{\frac{1}{n}} - 1 = \sqrt[n]{(1+R_1)(1+R_2)\dots(1+R_n)} - 1
    ```

* **Harmonic Mean** [cite: 166]
    ```math
    \bar{X}_{\text{Harmonic}} = \frac{N}{\sum_{i=1}^{N}\frac{1}{X_i}}
    ```
    Where:
    * $N$ = Number of observations
    * $X_i$ = Value of observation $i$

---

## LOS 1.c: Compare the money-weighted and time-weighted rates of return and evaluate the performance of portfolios based on these measures.

* **Money-Weighted Rate of Return (MWRR)**
    * The MWRR is the Internal Rate of Return (IRR) on a portfolio, considering all cash inflows and outflows. It's the discount rate '$r$' that solves:
        ```math
        \sum_{t=0}^{N} \frac{CF_t}{(1+MWRR)^t} = 0
        ```
    * Or, equating the present value of inflows to the present value of outflows[cite: 207]:
        (Example structure)
        ```math
        \text{Initial Investment} + \sum \frac{\text{Additional Deposits}}{(1+r)^t} = \sum \frac{\text{Withdrawals}}{(1+r)^t} + \frac{\text{Ending Value}}{(1+r)^N}
        ```
    * For the example given in the text[cite: 207]:
        ```math
        \$100 + \frac{\$118}{(1+r)} = \frac{\$264}{(1+r)^2}
        ```
        (This is solved for $r$ using a financial calculator's IRR function)

* **Time-Weighted Rate of Return (TWRR)**
    1.  Break the overall evaluation period into subperiods based on the timing of cash flows.
    2.  Calculate the Holding Period Return (HPR) for each subperiod: $HPR_t = \frac{MV_E - MV_B + D - C}{MV_B}$ (where $MV_E$ is ending market value, $MV_B$ is beginning market value, $D$ is deposits, $C$ is withdrawals for the subperiod. The text simplifies to $HPR = \frac{\text{End Value (+Div received)}}{\text{Start Value (-New Investment)} } -1$ before any new cash flow)
        * For subperiod $i$: $HPR_i = \frac{\text{Value before external CF}_i}{\text{Value after external CF}_{i-1}} - 1$
    3.  Link the HPRs to find the TWRR over $N$ years[cite: 222, 231]:
        ```math
        (1 + TWRR)^N = (1 + HPR_1) \times (1 + HPR_2) \times \dots \times (1 + HPR_N)
        ```
        ```math
        TWRR = \left[ (1 + HPR_1) \times (1 + HPR_2) \times \dots \times (1 + HPR_N) \right]^{\frac{1}{N}} - 1
        ```
        If HPRs are for periods shorter than a year, $N$ is the number of years in the total period.

---

## LOS 1.d: Calculate and interpret annualized return measures and continuously compounded returns, and describe their appropriate uses.

* **Annualized Return from HPR** [cite: 245]
    ```math
    \text{Annualized Return} = (1 + HPR)^{\frac{365}{\text{Days in Holding Period}}} - 1
    ```

* **Present Value (PV) with Periodic Compounding (General Formula)** [cite: 250]
    ```math
    PV = FV_N \left(1 + \frac{r_s}{m}\right)^{-mN}
    ```
    Where:
    * $FV_N$ = Future value at the end of N years
    * $r_s$ = Stated annual interest rate
    * $m$ = Number of compounding periods per year
    * $N$ = Number of years

* **Continuously Compounded Return ($R_{CC}$)** [cite: 255]
    ```math
    R_{CC} = \ln(1 + HPR)
    ```
    or
    ```math
    R_{CC} = \ln\left(\frac{\text{Ending Value}}{\text{Beginning Value}}\right)
    ```
    Where $\ln$ is the natural logarithm.

---

## LOS 1.e: Calculate and interpret major return measures and describe their appropriate uses.

* **Real Return (Approximate)** [cite: 269]
    ```math
    \text{Real Return} \approx \text{Nominal Return} - \text{Inflation Rate}
    ```

* **Real Return (Exact)** [cite: 269]
    ```math
    (1 + \text{Real Return}) = \frac{(1 + \text{Nominal Return})}{(1 + \text{Inflation Rate})}
    ```
    ```math
    \text{Real Return} = \frac{(1 + \text{Nominal Return})}{(1 + \text{Inflation Rate})} - 1
    ```

* **Real Return (Components as per curriculum note)** [cite: 269]
    ```math
    (1 + \text{Real Return}) = \frac{(1 + \text{Real Risk-Free Rate})(1 + \text{Risk Premium})}{(1 + \text{Inflation Premium})}
    ```
    (This formulation assumes the risk premium includes inflation risk)

* **Leveraged Return (as a rate of return on initial equity $V_0$)** [cite: 282]
    ```math
    \text{Leveraged Return Rate} = \frac{r(V_0 + V_B) - r_B V_B}{V_0}
    ```
    Where:
    * $r$ = Rate of return on the total investment (assets)
    * $V_0$ = Investor's initial equity investment (cash investment)
    * $V_B$ = Amount borrowed
    * $r_B$ = Cost of borrowing (interest rate on $V_B$)

---