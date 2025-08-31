## Reading 47: Fixed-Income Instrument Features 📜

🎯 **Introduction**

Think of a bond as a very formal IOU. When a large entity like the Government of India or a company like Apple needs to borrow a lot of money, they can't just ask a single bank. Instead, they issue bonds, which are essentially small slices of a giant loan that many different people can buy. This reading is the "user manual" for these IOUs. We'll break down all the essential parts: who's borrowing the money, how much interest they'll pay, when you'll get your money back, and the special rules they promise to follow. Understanding these features is the first step to becoming a fixed-income expert!

---

### Part 1: What Are the Basic Parts of a Bond? 🧩

Every bond, whether issued by a government or a corporation, has a set of core features that define it. Think of these as the bond's DNA.

* **Issuer:** This is simply who is borrowing the money. Major issuers include:
    * **Sovereign Governments:** National governments like the U.S. government issuing Treasury bonds or the Government of India issuing G-Secs. 
    * **Corporations:** Companies like Tata Motors or Microsoft borrowing for expansion. 
    * **Local Governments:** States or cities (municipalities) borrowing for public projects. 
    * **Supranational Entities:** Organizations like the World Bank or International Monetary Fund. 

* **Maturity (or Tenor):** This is the date when the issuer must repay the principal amount of the loan. 
    * **Money Market Securities:** Bonds with original maturities of one year or less. 
    * **Capital Market Securities:** Bonds with original maturities longer than one year. 
    * **Perpetual Bonds:** These are rare bonds that have no maturity date and theoretically pay interest forever! 

* **Principal (Par Value or Face Value):** This is the amount the issuer agrees to repay the bondholder at the maturity date.  It's the "face value" of the IOU.

* **Coupon Rate & Frequency:** The **coupon rate** is the annual interest rate paid on the bond's par value.  This can be structured in a few ways:
    * **Fixed-Coupon:** Pays a constant interest rate throughout its life. For example, a $1,000 par value bond with a 5% coupon paid semi-annually will pay the investor $25 every six months. 
    * **Floating-Rate Notes (FRNs):** The interest rate isn't fixed; it resets periodically based on a **market reference rate (MRR)** (like SOFR) plus a fixed margin.  This protects investors when interest rates are rising.
    * **Zero-Coupon Bonds:** These bonds pay no interest at all! 🤯 Instead, they are sold at a deep discount to their par value and the investor's return comes from the difference between the purchase price and the par value received at maturity. 

* **Seniority:** This determines the order of repayment if the issuer goes bankrupt. Just like a line at a ticket counter, some bondholders get paid before others.
    * **Senior Debt:** Gets paid first. It's less risky. 
    * **Junior (Subordinated) Debt:** Gets paid only after all senior debtholders are paid. It's riskier and thus offers a higher yield. 

* **Contingency Provisions (Embedded Options):** Some bonds have special clauses that allow either the issuer or the investor to take a specific action in the future. We'll explore these more later, but they include things like an issuer's right to repay a bond early (a call option). 

#### The Golden Rule: Price vs. Yield ⚖️

A bond's **yield** is the total return you'll get if you hold it to maturity. For fixed-coupon bonds, the most crucial concept to remember is the inverse relationship between price and yield:
* If a bond's price goes **UP** ⬆️, its yield goes **DOWN** ⬇️.
* If a bond's price goes **DOWN** ⬇️, its yield goes **UP** ⬆️.

Why? If you can buy a bond that pays a fixed $50 coupon each year for a cheaper price (say, $950 instead of $1,000), your overall return (yield) will be higher.



This relationship is often visualized in a **yield curve**, which plots the yields of bonds from the same issuer against their maturities.  A **normal yield curve** slopes upward, meaning longer-term bonds have higher yields to compensate for higher risk over time. , 368] An **inverted yield curve** slopes downward and can sometimes signal an upcoming economic recession. 

---

### Part 2: What's in the Fine Print? The Bond Indenture ⚖️

The **bond indenture** is the master legal contract that details all the rights of the bondholders and the obligations of the issuer.  It's the rulebook for the loan. A key part of the indenture is defining where the repayment money will come from and what rules the issuer must follow.

#### Sources of Repayment

* **Secured Bonds:** These are backed by specific assets (**collateral**) that can be sold to repay bondholders if the issuer defaults. This is like getting a car loan where the car itself is the collateral. 
* **Unsecured Bonds:** These are backed only by the issuer's general promise and ability to generate cash flow. They are riskier than secured bonds. 

#### Bond Covenants: The Dos and Don'ts

Covenants are rules placed on the issuer to protect the bondholders' interests. They come in two flavors:

#### **Affirmative Covenants ✅**

These are things the issuer *promises to do*. They are like a borrower's checklist of responsibilities. 

* Make timely interest and principal payments.
* Provide audited financial statements to bondholders.
* Maintain their assets and carry insurance on them.
* **Pari Passu Clause:** This clause states that the bond will have the same priority of claims as the issuer's other senior debt issues. 
* **Cross-Default Clause:** A crucial protection! It states that if the issuer defaults on any *other* debt obligation, they are also considered in default on this bond. 

#### **Negative Covenants ❌**

These are things the issuer *is restricted from doing*. They are designed to prevent the issuer from taking actions that would increase the risk for bondholders. 

* **Restrictions on Debt:** Cannot issue new debt that would be senior to existing bonds (this is called a **negative pledge clause**). 
* **Restrictions on Asset Sales:** Cannot sell major assets that generate the cash flow needed to pay back the bonds. 
* **Restrictions on Payments to Shareholders:** Cannot pay excessive dividends or buy back a large amount of stock, which would drain cash that could be used to service debt. 

> [!TIP]
> **CFA Exam Tip ✍️:** The distinction between affirmative (must do) and negative (cannot do) covenants is a classic exam topic. Remember that negative covenants are the primary way bondholders protect themselves from the issuer taking on more risk after the bond has been issued.

---

### 🧪 Formula Summary

This reading is foundational and focuses on concepts. There are no calculation formulas to memorize here! 🎉

---

> [!IMPORTANT]
> ### 🎯 Quick Exam-Day Pointers
>
> * **The Core Features:** Be able to describe the 7 key features of a bond: Issuer, Maturity, Par Value, Coupon, Seniority, Contingency Provisions, and Yield.
> * **Price-Yield Seesaw:** The most important relationship in fixed income is **INVERSE**. When price goes up, yield goes down, and vice versa. This is a guaranteed concept on the exam.
> * **Covenants:** Know the difference between **affirmative covenants** (what the issuer MUST do) and **negative covenants** (what the issuer CANNOT do). Negative covenants are the bondholder's main defense.
> * **Secured vs. Unsecured:** Secured bonds are backed by collateral and are safer than unsecured bonds, which are backed only by the issuer's promise.