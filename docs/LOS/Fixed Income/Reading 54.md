## Reading 54: Yield and Yield Spread Measures for Floating-Rate Instruments 🌊

### 🎯 Introduction

If a regular fixed-rate bond is like a salaried job with a predictable, steady income, then a **floating-rate note (FRN)** is like being a freelance consultant whose pay adjusts based on current market rates. Because their income adjusts, their value stays remarkably stable. This reading dives into these "freelancers" of the bond world. We'll learn why their prices don't fluctuate much and how to measure the extra **margin** they pay above a benchmark rate. We will also step into the fast-paced world of the **money market**, decoding the unique language and calculations used for ultra-short-term debt.

-----

### <span style="color: #1565C0;">Part 1: Understanding Floating-Rate Note (FRN) Yields ⛵</span>

The magic of an FRN is its stability. Unlike a fixed-rate bond whose value gets hammered when interest rates rise, an FRN's coupon payment adjusts upward, keeping its price close to **par value**.

The coupon of an FRN is made of two parts:

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
$$\text{Coupon Rate} = \text{Market Reference Rate (MRR)} + \text{Quoted Margin (QM)}$$
</div>

There are two key **margins** you must know:

* **Quoted Margin (QM):** This is the **fixed spread** the FRN pays over the MRR. It is set when the bond is issued and **does not change**.
* **Required Margin (or Discount Margin, DM):** This is the spread that investors **demand today** to compensate for the issuer's current credit risk. This **can change** based on the market's perception of the issuer's health.

The relationship between these two margins determines whether the FRN trades at a premium, par, or discount on its coupon reset dates.

* If **DM > QM** 😟: The market demands more spread than the bond is paying. This means the issuer's credit has worsened. The FRN will trade at a **discount** (Price < Par).
* If **DM < QM** 😊: The market demands less spread than the bond is paying. This means the issuer's credit has improved. The FRN will trade at a **premium** (Price > Par).
* If **DM = QM** 😐: The market's required spread matches the bond's paid spread. The FRN will trade at **par** (Price = Par).

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">
💡 CFA Exam Tip ✍️:This is a crucial concept. Think of it just like a fixed-rate bond. If the required yield (YTM) is greater than the coupon rate, the bond trades at a discount. For an FRN, the **Discount Margin (DM)** is the "required" part and the **Quoted Margin (QM)** is the "coupon" part. The logic is identical!
</div>
</div>

-----

### <span style="color: #1565C0;">Part 2: Decoding the Money Market Dialect 🗣️</span>

**Money market securities** are debt instruments that mature in one year or less. They have their own peculiar set of yield conventions that you must be able to translate for comparison purposes.

#### <span style="color: #6A1B9A;">2.1 Discount Yields</span>

This method quotes the yield as an annualized percentage discount from the bond's face value.

* **Who uses it?** U.S. Treasury Bills (T-bills) and Commercial Paper.
* **Key Features:**
  * It's based on the **face value**, not the price paid.
  * It's typically annualized using a **360-day year**.
* **Bottom Line:** A discount yield is *not* a true measure of an investor's return. It **understates** the actual yield. ❌

#### <span style="color: #6A1B9A;">2.2 Add-on Yields</span>

This method quotes the yield as an annualized interest rate that is added on to the amount invested.

* **Who uses it?** Bank Certificates of Deposit (CDs) and Repos.
* **Key Features:**
  * It's based on the **principal invested**, not the face value.
  * It can be annualized using a 360-day or 365-day year.
* **Bottom Line:** An add-on yield is a more accurate representation of an investor's return. ✅

#### <span style="color: #6A1B9A;">2.3 The Universal Translator: Bond Equivalent Yield</span>

To compare these different money market instruments fairly, we must convert their yields to a single standard: the **bond equivalent yield**.

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
$$\text{Bond Equivalent Yield (BEY)} = \text{Add-on Yield (365-day year)}$$
</div>

-----

#### <span style="color: #E65100;">2.4 Example: From Discount to BEY 🧮</span>

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">
**Example:**  
A 90-day U.S. T-bill with a $1,000 face value is quoted at a discount yield of 1.2%. What is its bond equivalent yield?

1. **Calculate the Dollar Discount:**  
   $$\text{Discount} = \$1,000 \times 1.2\% \times \frac{90}{360} = \$3.00$$

2. **Calculate the Price of the T-bill:**  
   $$\text{Price} = \$1,000 - \$3.00 = \$997.00$$

3. **Calculate the Holding Period Yield (HPY):**  
   $$\text{HPY} = \frac{\$3.00}{\$997.00} = 0.3009\%$$

4. **Convert to Bond Equivalent Yield (annualize for 365 days):**  
   $$\text{BEY} = 0.3009\% \times \frac{365}{90} = 1.2203\%$$

Notice that the BEY (1.22%) is higher than the initial discount yield (1.2%), because it's based on the actual price paid and a 365-day year.
</div>

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**FRN Price Rule:**  
If **Discount Margin > Quoted Margin**, then **Price < Par**.
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**Holding Period Yield (HPY):**  
$$\text{HPY} = \frac{\text{Ending Value} - \text{Beginning Value}}{\text{Beginning Value}}$$
</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">
**Bond Equivalent Yield from HPY:**  
$$\text{BEY} = \text{HPY} \times \frac{365}{\text{Days to Maturity}}$$
</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">
### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">
* **FRN Pricing is about Margins:** The price of a floating-rate note on its reset date is determined by the relationship between the market's **Required/Discount Margin (DM)** and the bond's fixed **Quoted Margin (QM)**.
* **Money Market Language:** Know the difference between **discount yields** (based on face value, 360 days) and **add-on yields** (based on price, 360 or 365 days).
* **BEY is the Standard:** To compare any two money market instruments, always convert their yields to the **bond equivalent yield**, which is an **add-on yield** based on a **365-day year**.
* **Discount yields will always understate the true return (the BEY).** ❌
</div>
</div>