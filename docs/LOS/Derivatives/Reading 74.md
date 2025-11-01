## Reading 74: Option Replication Using Put–Call Parity

### 🎯 Introduction

Welcome to one of the most elegant concepts in finance! Think of financial assets like LEGO® bricks. You can build the exact same model in different ways using different combinations of bricks. **Put-Call Parity** shows us how we can build the exact same financial payoff using two different sets of "bricks": one combination using a call option, and another using a put option. Because they build the same thing, they must cost the same. If they don't, there's a risk-free profit opportunity, and in finance, those don't last long! This reading unlocks the magic of how options, stocks, and bonds are all mathematically linked.

-----

### <span style="color: #1565C0;">Part 1: The Master Equation: What is Put-Call Parity? ⚖️ (LOS 74.a)</span>

**Put-Call Parity** is a fundamental relationship that links the prices of European call options, put options, the underlying stock, and a risk-free bond. It's built on the principle of **no-arbitrage**—meaning no risk-free lunch! 🥪

To understand it, let's create two special portfolios that have the *exact same payoff* at expiration.

* **Portfolio A: The Fiduciary Call** 📞+ 🏦  
  * **What it is:** A long **call option** combined with a long position in a **risk-free zero-coupon bond** that pays the exercise price (X) at expiration.  
  * **Analogy:** You have the *right to buy* a stock at price X, and you also have the *cash (X)* ready from the bond to make the purchase if you decide to.

* **Portfolio B: The Protective Put** 🛡️+ 📈  
  * **What it is:** A long **put option** combined with a long position in one share of the **underlying stock**.  
  * **Analogy:** You *own the stock*, but you also have an *insurance policy* (the put) that lets you sell it for at least price X, protecting you from any downside.

#### <span style="color: #6A1B9A;">1.1 Why They Are Equal: The Payoff Showdown</span>

Since these two portfolios have identical payoffs no matter what happens to the stock price, their initial costs must be the same.

-----

##### <span style="color: #E65100;">1.1.1 Payoff at Expiration</span>

Let's see what each portfolio is worth at expiration (Time T), where **S<sub>T</sub>** is the stock price at expiration and **X** is the exercise price.

| Scenario | Payoff of Fiduciary Call (Call + Bond) | Payoff of Protective Put (Stock + Put) | Result |
| :--- | :--- | :--- | :--- |
| **Stock price is high (S<sub>T</sub> ≥ X)** | (S<sub>T</sub> - X) + X = **S<sub>T</sub>** | S<sub>T</sub> + 0 = **S<sub>T</sub>** | Identical! ✅ |
| **Stock price is low (S<sub>T</sub> < X)** | 0 + X = **X** | S<sub>T</sub> + (X - S<sub>T</sub>) = **X** | Identical! ✅ |

-----

Because their payoffs are always the same, the Law of One Price says their values today must be equal. This gives us the famous **Put-Call Parity equation**:

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$c_0 + X(1+R_f)^{-T} = S_0 + p_0$$

</div>

Where:

* **c<sub>0</sub>** = Price of the European call option today  
* **X(1+R<sub>f</sub>)<sup>-T</sup>** = Price of the risk-free bond today (PV of X)  
* **S<sub>0</sub>** = Price of the underlying stock today  
* **p<sub>0</sub>** = Price of the European put option today  

#### <span style="color: #6A1B9A;">1.2 Building Synthetic Assets 🤖</span>

The real power of this equation is that if you know the prices of any three of these assets, you can solve for the fourth. You can create a **synthetic** version of any asset using the other three.

```mermaid
graph TD
    subgraph Synthetic Stock
        A[Long Call] --> S;
        B[Short Put] --> S;
        C[Long Bond] --> S;
    end
    subgraph Synthetic Call
        D[Long Stock] --> Ca;
        E[Long Put] --> Ca;
        F[Short Bond] --> Ca;
    end
    S[= Long Stock Position]
    Ca[= Long Call Position]
```

**Synthetic Stock:** `Long Call + Short Put + Long Bond` = `A share of stock`

<div style="background-color: #E3F2FD; border-left: 5px solid #1976D2; padding: 12px; margin: 15px 0;">
<div style="color: #000000; font-weight: 500;">

💡 CFA Exam Tip ✍️:Memorize the core put-call parity formula: **c + PV(X) = S + p**. A simple mnemonic is "cops," but with the stock and put together: **c + bond = Stock + p**. You will be tested on your ability to rearrange this formula to solve for any of the four components or to identify arbitrage opportunities if the equation doesn't hold.

</div>
</div>

-----

### <span style="color: #1565C0;">Part 2: The Forward Twist: What is Put-Call-Forward Parity? ⏩ (LOS 74.b)</span>

This is a neat variation of the main formula. What if instead of dealing with the actual stock, we use a **forward contract** on the stock?

Remember, a long position in a stock (**S<sub>0</sub>**) can be replicated by:

* Entering a **long forward contract** (which costs nothing today).
* Buying a **risk-free bond** that will be worth the forward price (**F<sub>0</sub>(T)**) at expiration. The cost of this bond today is the present value of the forward price.

So, we can replace the stock (**S<sub>0</sub>**) in our original parity formula with the cost of its synthetic equivalent: **F<sub>0</sub>(T)(1 + R<sub>f</sub>)<sup>-T</sup>**.

This gives us the **Put-Call-Forward Parity equation**:

<div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin: 10px 0;">

$$F_0(T)(1+R_f)^{-T} + p_0 = c_0 + X(1+R_f)^{-T}$$

</div>

This relationship links the prices of puts, calls, and risk-free bonds to the **forward price** of the underlying, rather than its spot price. It's incredibly useful for pricing options on assets that primarily trade in the forward or futures markets, like commodities or currencies.

-----

### 🧪 Formula Summary

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Put-Call Parity:** 

$$c_0 + X(1+R_f)^{-T} = S_0 + p_0$$

</div>

<div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin: 10px 0;">

**Put-Call-Forward Parity:** 

$$F_0(T)(1+R_f)^{-T} + p_0 = c_0 + X(1+R_f)^{-T}$$

</div>

-----

<div style="background-color: #FFF9E6; border-left: 5px solid #F57C00; padding: 15px; margin: 20px 0;">

### 🎯 Quick Exam-Day Pointers

<div style="color: #000000; font-weight: 500;">

* **European Options Only:**  
  * This parity relationship **only** holds for **European options** because they can only be exercised at expiration.  
  * **American options** (with early exercise) ❌ break this equivalence.

* **It's All About No-Arbitrage:**  
  * Two portfolios with identical future payoffs must have the same price today.  
  * If not, you can buy the cheap one, sell the expensive one, and lock in a risk-free profit. ✅

* **Know Your Synthetics:**  
  * Be ready to identify the combination of assets needed to replicate a stock, a bond, a call, or a put.  
  * Rearranging the main formula is a key exam skill. ➡️

* **Same X, Same T:**  
  * For parity to hold, the call and put must have the **same exercise price (X)** and the **same expiration date (T)**.

</div>
</div>