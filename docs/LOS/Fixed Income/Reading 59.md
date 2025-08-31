## Reading 59: Curve-Based and Empirical Fixed-Income Risk Measures 🧩

🎯 **Introduction**

The duration measures we've learned so far are fantastic, but they have a couple of big assumptions. **Modified Duration**, our trusty speedometer, assumes a bond's cash flows are perfectly predictable. It also assumes that when interest rates change, the entire yield curve shifts up or down in perfect parallel, like a synchronized swimming team. But what happens with a **callable bond**, where the cash flows are uncertain? And what if the yield curve *twists*, with short-term rates rising while long-term rates fall? Our simple tools would fail. This reading introduces the advanced toolkit needed for these messy, real-world scenarios: **Effective Duration** and **Key Rate Duration**.

---

### Part 1: Handling Tricky Bonds: Effective Duration & Convexity 🃏

For a standard, option-free bond, the cash flows are set in stone. But for bonds with **embedded options** (callable, putable, or mortgage-backed securities), the future cash flows are uncertain. We don't know *if* or *when* a callable bond will be redeemed early. This uncertainty means we cannot calculate a single, meaningful Yield to Maturity (YTM). And if we can't calculate YTM, we can't use Modified Duration.

The solution is **Effective Duration (EffDur)**.

**Effective Duration** measures a bond's price sensitivity to a change in the **benchmark yield curve** (e.g., the government spot curve), not its own YTM. It's calculated using a bond pricing model that can handle the option's complex behavior.

The formula looks familiar, but the input is different:
$\text{Effective Duration} = \frac{V_- - V_+}{2 \times V_0 \times \Delta\text{Curve}}$
where ΔCurve is the parallel shift in the benchmark yield curve (e.g., 25 basis points). We do the same for **Effective Convexity (EffCon)**.

#### **How Options Affect Duration & Convexity**

* **Callable Bonds:** 📞
    * At low yields, the issuer is very likely to call the bond. This puts a ceiling on the bond's price.
    * As yields fall, the price stops rising, or rises much more slowly.
    * This causes the bond's duration to decrease at low yields.
    * It can also lead to **negative convexity**, which is very bad for investors! It means you get less upside when rates fall and more downside when rates rise.
* **Putable Bonds:** 🛡️
    * At high yields, the investor is very likely to "put" the bond back to the issuer. This puts a floor on the bond's price.
    * As yields rise, the price falls much less than an option-free bond would.
    * This causes the bond's duration to decrease at high yields.
    * Putable bonds always have **positive convexity**, which is great for investors.

---

### Part 2: The Yield Curve Twist: Key Rate Duration 🔑

Both Modified and Effective Duration measure risk based on a **parallel shift** of the yield curve. But what if the curve changes shape?



**Key Rate Duration** (also called **partial duration**) is the solution. It measures a bond's price sensitivity to a change in a *single specific point* on the benchmark yield curve, holding all other rates constant.

* **Example:** A portfolio's 10-year key rate duration of 4.7 tells you that if *only* the 10-year benchmark yield falls by 1%, the portfolio's value will rise by approximately 4.7%.

**Why is it useful?**
Portfolio managers can analyze the key rate durations of their portfolio to see where their risks are concentrated along the yield curve. They can then build portfolios that are hedged against specific non-parallel shifts, like a "barbell" portfolio that is protected against a flattening of the yield curve. The sum of a bond's key rate durations is approximately equal to its effective duration.

---

### Part 3: Theory vs. Reality: Analytical vs. Empirical Duration 🔬

The duration measures we've discussed so far are all a type of **Analytical Duration**. There's another approach called **Empirical Duration**.

#### **Analytical Duration**

* **What it is:** All the model-based durations we've learned (Macaulay, Modified, Effective, Key Rate).
* **How it's calculated:** Using mathematical formulas and bond pricing models.
* **Key Assumption:** It assumes that when the benchmark government yield changes, the bond's credit spread over the benchmark remains **constant**.

#### **Empirical Duration**

* **What it is:** A duration calculated using historical market data.
* **How it's calculated:** By running a statistical regression of a bond's historical price changes against historical changes in a benchmark yield (e.g., a 10-year Treasury yield).
* **Key Feature:** It reflects what has *actually happened* in the market, including any real-world relationship between benchmark yields and credit spreads.

**Why the Difference Matters:**
In a "flight-to-quality" crisis, investors sell risky corporate bonds and buy safe government bonds. This causes government yields to fall while corporate credit spreads widen (and their yields rise).
* **Analytical duration** would predict the corporate bond's price should *rise* (due to the fall in the benchmark yield).
* **Empirical duration**, based on historical crisis data, would correctly predict the bond's price would *fall*.

---

### 🧪 Formula Summary

* **Effective Duration:** $\text{EffDur} = \frac{V_- - V_+}{2 \times V_0 \times \Delta\text{Curve}}$
* **Effective Convexity:** $\text{EffCon} = \frac{V_- + V_+ - (2V_0)}{(\Delta\text{Curve})^2 \times V_0}$
* **Percentage Price Change (with Effective Measures):**
    $\%\Delta \text{Price} \approx [- \text{EffDur} \times \Delta\text{Curve}] + [ \frac{1}{2} \times \text{EffCon} \times (\Delta\text{Curve})^2 ]$

---

> [!IMPORTANT]
> ### 🎯 Quick Exam-Day Pointers
>
> * **Use Effective Duration for Options:** When a bond has **embedded options**, its cash flows are uncertain. You MUST use **Effective Duration** and **Effective Convexity**, which are based on shifts in the benchmark curve.
> * **Callable Bonds Can Have Negative Convexity:** This is a major risk for investors. At low yields, the price of a callable bond is "compressed" and stops rising, which is an undesirable trait.
> * **Use Key Rate Duration for Curve Twists:** **Key Rate Duration** is the tool to measure a portfolio's sensitivity to **non-parallel** shifts in the yield curve.
> * **Analytical vs. Empirical:** **Analytical** duration is model-based and assumes constant spreads. **Empirical** duration is history-based and reflects how spreads have actually behaved.