# 💰 Fixed Income Formulas

## 🏦 Reading 47: Fixed-Income Instrument Features

- 🎫 **Coupon Payment:** The periodic interest payment made to bondholders.
  >
  $$
  \text{Coupon Payment} = \text{Face Value} \times \frac{\text{Stated Coupon Rate}}{\text{Payments per Year}}
  $$

- 📊 **Credit Spread:** The additional yield for holding a risky bond over a risk-free benchmark.
  >
  $$
  \text{Spread} = \text{Corporate Bond Yield} - \text{Government Bond Yield}
  $$

---

## 💸 Reading 48: Fixed-Income Cash Flows and Types

- 📈 **FRN Periodic Coupon Payment:** For floating-rate notes.
  >
  $$
  \text{Periodic Coupon Payment} = \frac{\text{Annualized MRR} + \text{Annualized Margin}}{\text{Number of Periods per Year}} \times \text{Face Value}
  $$

- 📈 **Capital-Indexed Bond Calculations:**
  1. 📊 **Inflation-Adjusted Principal:**
     >
     $$
     \text{Adjusted Principal} = \text{Principal} \times (1 + \text{Inflation Rate})
     $$
  2. 🎫 **Coupon Payment on Adjusted Principal:**
     >
     $$
     \text{Coupon Payment} = \frac{\text{Coupon Rate}}{\text{Periods per Year}} \times \text{Adjusted Principal}
     $$

- 🔄 **Convertible Bond Formulas:**
  1. ⚖️ **Conversion Ratio:**
     >
     $$
     \text{Conversion Ratio} = \frac{\text{Par Value of Bond}}{\text{Conversion Price}}
     $$
  2. 💰 **Conversion Value:**
     >
     $$
     \text{Conversion Value} = \text{Conversion Ratio} \times \text{Market Price of Common Share}
     $$

---

## 🏢 Reading 50: Fixed-Income Markets for Corporate Issuers

- 🔄 **Repurchase Agreement (Repo) Formulas:**
  1. 💰 **Purchase Price (Loan Amount):**
     >
     $$
     \text{Purchase Price} = \frac{\text{Market Value of Securities}}{\text{Initial Margin}}
     $$
  2. 📈 **Repurchase Price:**
     >
     $$
     \text{Repurchase Price} = \text{Purchase Price} \times \left(1 + \text{Repo Rate} \times \frac{\text{Days}}{360 \text{ or } 365}\right)
     $$
  3. ✂️ **Haircut:**
     >
     $$
     \text{Haircut} = \frac{\text{Market Value} - \text{Purchase Price}}{\text{Market Value}}
     $$
     or
     >
     $$
     \text{Haircut} = 1 - \frac{1}{\text{Initial Margin}}
     $$
  4. 📊 **Variation Margin:**
     >
     $$
     \text{Variation Margin} = (\text{Initial Margin} \times \text{Adjusted Purchase Price}) - \text{Market Value of Collateral}
     $$

---

## 💰 Reading 52: Fixed-Income Bond Valuation: Prices and Yields

- 📊 **Bond Price (Value):** Present value of all future cash flows, discounted at YTM.
  - 📅 **Annual Coupon Bond:**
    >
    $$
    \text{Price} = \sum_{t=1}^{N} \frac{\text{Coupon}}{(1 + \text{YTM})^t} + \frac{\text{Principal}}{(1 + \text{YTM})^N}
    $$
  - 📆 **Semiannual Coupon Bond:**
    >
    $$
    \text{Price} = \sum_{t=1}^{2N} \frac{\text{Coupon}/2}{(1 + \text{YTM}/2)^t} + \frac{\text{Principal}}{(1 + \text{YTM}/2)^{2N}}
    $$

- 🕐 **Accrued Interest:**
  >
  $$
  \text{Accrued Interest} = \text{Coupon Payment} \times \left(\frac{\text{Days from Last Coupon to Settlement}}{\text{Days in Coupon Period}}\right)
  $$

- 💲 **Full Price (Dirty Price):**
  >
  $$
  \text{Full Price} = \text{Flat Price} + \text{Accrued Interest}
  $$

- 📈 **Full Price Calculation Between Coupon Dates:**
  >
  $$
  \text{Full Price} = \text{PV at Last Coupon Date} \times (1 + \text{Periodic YTM})^{\frac{\text{Days since last coupon}}{\text{Days in coupon period}}}
  $$

- 📐 **Matrix Pricing (Linear Interpolation):**
  >
  $$
  \text{Interpolated YTM} = \text{YTM}_\text{short} + \left(\frac{\text{Maturity}_\text{target} - \text{Maturity}_\text{short}}{\text{Maturity}_\text{long} - \text{Maturity}_\text{short}}\right) \times (\text{YTM}_\text{long} - \text{YTM}_\text{short})
  $$

---

## 📊 Reading 53: Yield and Yield Spread Measures for Fixed-Rate Bonds

- 📈 **Effective Annual Yield (EAY):**
  >
  $$
  \text{EAY} = \left(1 + \frac{\text{YTM}}{n}\right)^n - 1
  $$
  Where $n$ = number of coupon payments per year.

- 💸 **Current Yield:**
  >
  $$
  \text{Current Yield} = \frac{\text{Annual Cash Coupon Payment}}{\text{Bond Price}}
  $$

- 📋 **Simple Yield:**
  >
  $$
  \text{Simple Yield} = \frac{\text{Annual Coupon} + \frac{\text{Face Value} - \text{Price}}{\text{Years to Maturity}}}{\text{Price}}
  $$

- 📞 **Callable Bond Value:**
  >
  $$
  \text{Callable Bond Value} = \text{Straight Bond Value} - \text{Call Option Value}
  $$

- 📈 **Zero-Volatility Spread (Z-Spread):**
  >
  $$
  \text{Price} = \frac{\text{CF}_1}{(1 + S_1 + ZS)^1} + \frac{\text{CF}_2}{(1 + S_2 + ZS)^2} + \dots + \frac{\text{CF}_N}{(1 + S_N + ZS)^N}
  $$

- 🎯 **Option-Adjusted Spread (OAS):**
  >
  $$
  \text{OAS} = \text{Z-Spread} - \text{Option Value (in basis points)}
  $$

---

## 📈 Reading 54: Yield and Yield Spread Measures for Floating-Rate Instruments

- 📊 **Quoted Add-On Yield (AOR):**
  >
  $$
  \text{AOR} = \text{HPY} \times \frac{365}{\text{Days to Maturity}}
  $$

- 📉 **Quoted Discount Yield (DR):**
  >
  $$
  \text{DR} = \frac{\text{Discount}}{\text{Face Value}} \times \frac{360}{\text{Days to Maturity}}
  $$

- 📋 **Bond Equivalent Yield (BEY):**
  >
  $$
  \text{BEY} = \text{HPY} \times \frac{365}{\text{Days to Maturity}}
  $$

- 🔄 **BEY from a 360-Day Add-on Rate:**
  >
  $$
  \text{BEY} = \text{AOR}_{360} \times \frac{365}{360}
  $$

---

## 📈 Reading 55: The Term Structure of Interest Rates: Spot, Par, and Forward Curves

- 🎯 **Bond Price using Spot Rates (No-Arbitrage Price):**
  >
  $$
  \text{Price} = \frac{\text{Coupon}_1}{(1 + S_1)^1} + \frac{\text{Coupon}_2}{(1 + S_2)^2} + \dots + \frac{\text{Coupon}_N + \text{Principal}}{(1 + S_N)^N}
  $$

- 📍 **Spot Rate from Forward Rates:**
  >
  $$
  (1 + S_N)^N = (1 + S_1) \times (1 + 1y1y) \times \dots \times (1 + (N-1)y1y)
  $$

- ⏭️ **Forward Rate from Spot Rates:**
  - 1️⃣ **One-Period Forward Rate:**
    >
    $$
    (1 + (N-1)y1y) = \frac{(1 + S_N)^N}{(1 + S_{N-1})^{N-1}}
    $$
  - 📊 **Multi-Period Forward Rate:**
    >
    $$
    \left(1 + (N-M)yMy\right)^M = \frac{(1 + S_N)^N}{(1 + S_{N-M})^{N-M}}
    $$

- 💰 **Bond Price using Forward Rates:**
  >
  $$
  \text{Price} = \frac{\text{Coupon}}{(1+S_1)} + \frac{\text{Coupon}}{(1+S_1)(1+1y1y)} + \dots + \frac{\text{Coupon} + \text{Principal}}{(1+S_1)(1+1y1y)\dots}
  $$

---

## ⚡ Reading 56: Interest Rate Risk and Return

- 📈 **Capital Gain or Loss:**
  >
  $$
  \text{Capital Gain/Loss} = \text{Selling Price} - \text{Carrying Value}
  $$
  Where carrying value is the bond's price based on the original YTM at sale.

- ⏱️ **Macaulay Duration:**
  >
  $$
  \text{MacDur} = \sum_{t=1}^{N} t \times w_t = \sum_{t=1}^{N} t \times \frac{\text{PVCF}_t}{\text{Full Price}}
  $$

- ⚖️ **Duration Gap:**
  >
  $$
  \text{Duration Gap} = \text{Macaulay Duration} - \text{Investment Horizon}
  $$

---

## ⚡ Reading 57: Yield-Based Bond Duration Measures and Properties

- 🔧 **Modified Duration (ModDur):**
  >
  $$
  \text{ModDur} = \frac{\text{Macaulay Duration}}{1 + \frac{\text{YTM}}{\text{Periodicity}}}
  $$

- 📊 **Approximate Percentage Price Change:**
  >
  $$
  \Delta\text{Price} \,(\%) \approx -\text{ModDur} \times \Delta\text{YTM}
  $$

- 📏 **Approximate Modified Duration:**
  >
  $$
  \text{Approx. ModDur} = \frac{V_- - V_+}{2 \times V_0 \times \Delta\text{YTM}}
  $$
  Where $V_0$ is the initial price, $V_-$ and $V_+$ are prices after a yield decrease/increase.

- 💰 **Money Duration (Dollar Duration):**
  >
  $$
  \text{Money Duration} = \text{Annual ModDur} \times \text{Full Price of Position}
  $$

- 🎯 **Price Value of a Basis Point (PVBP):**
  >
  $$
  \text{PVBP} \approx \frac{V_- - V_+}{2}
  $$
  or
  >
  $$
  \text{PVBP} \approx \text{Money Duration} \times 0.0001
  $$

---

## 📈 Reading 58: Yield-Based Bond Convexity and Portfolio Properties

- 🔄 **Convexity of a Single Cash Flow:**
  >
  $$
  \text{Convexity at period } t = \frac{t(t+1)}{(1+r)^2}
  $$
  Where:
  - $t$ = period of cash flow
  - $r$ = periodic yield

- 📅 **Annualizing Convexity:**
  >
  $$
  \text{Annual Convexity} = \frac{\text{Convexity}_{\text{periodic}}}{(\text{Periodicity})^2}
  $$

- 📏 **Approximate Convexity:**
  >
  $$
  \text{Approximate Convexity} = \frac{V_- + V_+ - (2 \times V_0)}{(\Delta\text{YTM})^2 \times V_0}
  $$
  Where:
  - $V_-$ = price if YTM decreases by $\Delta\text{YTM}$
  - $V_+$ = price if YTM increases by $\Delta\text{YTM}$
  - $V_0$ = current price

- 📊 **Percentage Price Change (with Duration and Convexity):**
  >
  $$
  \Delta \text{Price} \,(\%) \approx (-\text{Annual ModDur} \times \Delta\text{YTM}) + \left(\frac{1}{2} \times \text{Annual Convexity} \times (\Delta\text{YTM})^2\right)
  $$

- 💰 **Money Convexity:**
  >
  $$
  \text{Money Convexity} = \text{Annual Convexity} \times \text{Full Price of Bond Position}
  $$

- 📋 **Portfolio Duration (Weighted Average):**
  >
  $$
  \text{Portfolio Duration} = \sum_{i=1}^{N} w_i D_i
  $$
  Where:
  - $w_i$ = full price of bond $i$ / total portfolio value
  - $D_i$ = duration of bond $i$

---

## 📈 Reading 59: Curve-Based and Empirical Fixed-Income Risk Measures

- ⚡ **Effective Duration (EffDur):**
  >
  $$
  \text{Effective Duration} = \frac{V_- - V_+}{2 \times V_0 \times \Delta\text{Curve}}
  $$
  Where:
  - $V_0$ = initial bond price
  - $V_-$, $V_+$ = prices after curve shifts
  - $\Delta\text{Curve}$ = parallel shift

- 🔄 **Effective Convexity (EffCon):**
  >
  $$
  \text{Effective Convexity} = \frac{V_- + V_+ - (2 \times V_0)}{(\Delta\text{Curve})^2 \times V_0}
  $$

- 📊 **Percentage Price Change (with Effective Duration and Convexity):**
  >
  $$
  \Delta \text{Price} \,(\%) \approx (-\text{EffDur} \times \Delta\text{Curve}) + \left(\frac{1}{2} \times \text{EffCon} \times (\Delta\text{Curve})^2\right)
  $$

- 🎯 **Total Price Change from Key Rate Durations:**
  >
  $$
  \Delta \text{Portfolio Value} \,(\%) \approx \sum_{i=1}^{k} (-\text{Key Rate Duration}_i \times \Delta\text{Yield}_i)
  $$

---

## ⚠️ Reading 60: Credit Risk

- ❗ **Expected Loss (EL):**
  >
  $$
  \text{Expected Loss} = \text{Probability of Default} \times \text{Loss Given Default}
  $$

- 📉 **Loss Given Default (LGD%):**
  >
  $$
  \text{LGD} = 1 - \text{Recovery Rate}
  $$

- 📊 **Credit Spread Approximation:**
  >
  $$
  \text{Credit Spread} \approx \text{Probability of Default} \times \text{LGD}\%
  $$

- 🔍 **Decomposition of Yield Spread:**
  1. 📈 **Total Yield Spread:**
     >
     $$
     \text{Yield Spread} = \text{Bond Yield at Mid-Price} - \text{Benchmark Yield}
     $$
  2. 💧 **Liquidity Spread:**
     >
     $$
     \text{Liquidity Spread} = \text{Yield at Bid Price} - \text{Yield at Offer Price}
     $$
  3. ⚠️ **Credit Spread:**
     >
     $$
     \text{Credit Spread} = \text{Total Yield Spread} - \text{Liquidity Spread}
     $$

- 📊 **Percentage Price Change from Spread Change:**
  >
  $$
  \Delta \text{Price} \,(\%) \approx (-\text{ModDur} \times \Delta\text{Spread}) + \left(\frac{1}{2} \times \text{Convexity} \times (\Delta\text{Spread})^2\right)
  $$

---

## 🏛️ Reading 61: Credit Analysis for Government Issuers

- 🏦 **Debt-Service Coverage Ratio (DSCR):**
  >
  $$
  \text{DSCR} = \frac{\text{Revenue After Operating Costs}}{\text{Interest and Principal Repayments}}
  $$

---

## 🏢 Reading 62: Credit Analysis for Corporate Issuers

- 📊 **Profitability, Coverage, and Leverage Ratios:**
  - 💼 **EBIT Margin:**
    >
    $$
    \frac{\text{EBIT}}{\text{Revenue}}
    $$
  - 🛡️ **Interest Coverage:**
    >
    $$
    \frac{\text{EBIT}}{\text{Interest Expense}}
    $$
  - ⚖️ **Leverage (Debt-to-EBITDA):**
    >
    $$
    \frac{\text{Debt}}{\text{EBITDA}}
    $$
  - 💸 **Leverage (Cash Flow-to-Debt):**
    >
    $$
    \frac{\text{Retained Cash Flow}}{\text{Net Debt}}
    $$
    Where Net Debt = Debt – Cash and marketable securities

---

## 🏠 Reading 65: Mortgage-Backed Security (MBS) Instrument and Market Features

- ⏱️ **Weighted Average Maturity (WAM):**
  >
  $$
  \text{WAM} = \sum_{i=1}^{n} w_i M_i
  $$
  Where:
  - $w_i$ = Current principal balance of mortgage $i$ / Total principal balance of pool
  - $M_i$ = Remaining months to maturity of mortgage $i$

- 🎫 **Weighted Average Coupon (WAC):**
  >
  $$
  \text{WAC} = \sum_{i=1}^{n} w_i C_i
  $$
  Where:
  - $w_i$ = Current principal balance of mortgage $i$ / Total principal balance of pool
  - $C_i$ = Coupon rate of mortgage $i$

- 🏢 **Commercial MBS Credit Analysis Ratios:**
  - 🏦 **Debt-Service Coverage Ratio (DSCR):**
    >
    $$
    \text{DSCR} = \frac{\text{Net Operating Income}}{\text{Debt Service}}
    $$
  - 🏠 **Loan-to-Value (LTV) Ratio:**
    >
    $$
    \text{LTV} = \frac{\text{Current Mortgage Amount}}{\text{Current Appraised Value}}
    $$
