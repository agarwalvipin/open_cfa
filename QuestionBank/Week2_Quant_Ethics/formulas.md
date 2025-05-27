# 💰 Formula Sheet: Week 2 - The Time Value of Money in Finance (Reading 2)

## LOS 2.a: Calculate and interpret the present value (PV) of fixed-income and equity instruments based on expected future cash flows.

### Basic Time Value of Money Formulas

* **Future Value (FV) with Discrete Compounding**
    ```math
    FV = PV(1+r)^t
    ```
    Where:
    * $PV$ = Present Value
    * $r$ = Interest rate per period
    * $t$ = Number of compounding periods

* **Present Value (PV) with Discrete Compounding**
    ```math
    PV = \frac{FV}{(1+r)^t} = FV(1+r)^{-t}
    ```
    Where:
    * $FV$ = Future Value
    * $r$ = Interest rate per period
    * $t$ = Number of compounding periods

* **Future Value (FV) with Continuous Compounding**
    ```math
    FV = PV \times e^{rt}
    ```
    Where:
    * $e$ = Euler's number (approximately 2.71828)
    * $r$ = Continuously compounded annual interest rate
    * $t$ = Number of years

* **Present Value (PV) with Continuous Compounding**
    ```math
    PV = FV \times e^{-rt}
    ```

---

### Fixed-Income Securities Valuation (LOS 2.a Continued)

* **Present Value (Price) of a Zero-Coupon Bond**
    ```math
    PV = \frac{FV}{(1+r)^N}
    ```
    Where:
    * $FV$ = Face Value of the bond
    * $r$ = Yield to maturity (discount rate) per period
    * $N$ = Number of periods to maturity

* **Present Value (Price) of an Annual Coupon Bond**
    ```math
    PV = \sum_{i=1}^{N} \frac{PMT}{(1+r)^i} + \frac{FV}{(1+r)^N}
    ```
    Alternatively, using financial calculator inputs:
    * $N$ = Number of years
    * $I/Y$ = Yield to maturity (discount rate)
    * $PMT$ = Annual coupon payment
    * $FV$ = Face Value of the bond
    * Then, CPT $PV$

* **Present Value (PV) of a Perpetuity**
    ```math
    PV_{Perpetuity} = \frac{PMT}{r}
    ```
    Where:
    * $PMT$ = Periodic payment
    * $r$ = Discount rate per period

* **Annuity Payment**
    ```math
    PMT = \frac{r \times PV}{1-(1+r)^{-t}}
    ```
    Where:
    * $PV$ = Present Value (principal)
    * $r$ = Interest rate per period
    * $t$ = Number of periods

---

### Equity Securities Valuation (LOS 2.a Continued)

* **Preferred Stock Value (using Perpetuity Formula)**
    ```math
    V_{ps} = \frac{D_p}{k_p}
    ```
    Where:
    * $D_p$ = Dividend per period for preferred stock
    * $k_p$ = Required return on the preferred stock

* **Constant Growth Dividend Discount Model (Gordon Growth Model) for Common Stock**
    ```math
    V_0 = \frac{D_1}{k_e - g_c}
    ```
    Where:
    * $V_0$ = Value of a share today
    * $D_1$ = Dividend expected to be paid next period (calculated as $D_0(1+g_c)$)
    * $k_e$ = Required return on common equity
    * $g_c$ = Constant growth rate of dividends

* **Multistage Dividend Discount Model (Example: Two-Stage Growth)**
    1.  Calculate dividends during the initial high-growth period:
        $D_t = D_{t-1}(1+g_{initial})$
    2.  Calculate the terminal value (price) at the end of the high-growth period ($N$) using the Gordon Growth Model with the long-term constant growth rate ($g_L$):
        ```math
        P_N = \frac{D_{N+1}}{k_e - g_L} = \frac{D_N(1+g_L)}{k_e - g_L}
        ```
    3.  Discount the individual high-growth dividends and the terminal value back to the present:
        ```math
        V_0 = \sum_{t=1}^{N} \frac{D_t}{(1+k_e)^t} + \frac{P_N}{(1+k_e)^N}
        ```

---

## LOS 2.b: Calculate and interpret the implied return of fixed-income instruments and required return and implied growth of equity instruments given the present value (PV) and cash flows.

* **Implied Rate of Return for a Pure Discount Bond (solving for r)**
    ```math
    (1+r)^N = \frac{FV}{PV} \implies r = \left(\frac{FV}{PV}\right)^{\frac{1}{N}} - 1
    ```

* **Implied Required Rate of Return on Equity (from Gordon Growth Model)**
    ```math
    k_e = \frac{D_1}{V_0} + g_c
    ```
    (This is the dividend yield plus the constant growth rate)

* **Implied Growth Rate of Dividends (from Gordon Growth Model)**
    ```math
    g_c = k_e - \frac{D_1}{V_0}
    ```
    (This is the required rate of return minus the dividend yield)

---

## LOS 2.c: Explain the cash flow additivity principle, its importance for the no-arbitrage condition, and its use in calculating implied forward interest rates, forward exchange rates, and option values.

### Forward Interest Rates (based on No-Arbitrage)

* **General Relationship for Spot and Forward Rates (Example for 3 periods)**
    ```math
    (1+S_3)^3 = (1+S_1)(1+{_{1}}f_1)(1+{_{2}}f_1)
    ```
    Where:
    * $S_N$ = N-period spot rate
    * $_{t}f_p$ = p-period forward rate starting at time t

* **Implied One-Period Forward Rate, One Period from Now (1y1y or $_{1}f_1$)**
    ```math
    (1+{_{1}}f_1) = \frac{(1+S_2)^2}{(1+S_1)}
    ```

---

### Forward Currency Exchange Rates (based on No-Arbitrage / Interest Rate Parity) (LOS 2.c Continued)

* **No-Arbitrage Forward Exchange Rate (Price Currency / Base Currency)**
    ```math
    \frac{Forward_{P/B}}{Spot_{P/B}} = \frac{(1+Interest\ Rate_{Price\ Currency})}{(1+Interest\ Rate_{Base\ Currency})}
    ```
    or
    ```math
    Forward_{P/B} = Spot_{P/B} \times \frac{(1+i_{Price\ Currency})}{(1+i_{Base\ Currency})}
    ```
    (Note: Interest rates must match the tenor of the forward contract)

---

### Option Pricing (Binomial Model - Illustrative of No-Arbitrage) (LOS 2.c Continued)

* **Hedge Ratio (h)**
    ```math
    h = \frac{c_u - c_d}{S_u - S_d}
    ```
    Where:
    * $c_u$ = Call option value if price goes up
    * $c_d$ = Call option value if price goes down
    * $S_u$ = Stock price if it goes up
    * $S_d$ = Stock price if it goes down

* **No-Arbitrage Option Value ($c_0$)**
    The value is found by ensuring a risk-free portfolio.
    1.  Value of hedged portfolio at initiation: $V_0 = hS_0 - c_0$
    2.  Value of hedged portfolio at expiration (known with certainty): $V_1 = hS_u - c_u = hS_d - c_d$
    3.  Present value of $V_1$: $V_0 = \frac{V_1}{(1+r_f)}$
    4.  Call option value today: $c_0 = hS_0 - V_0$

---