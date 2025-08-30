### Module 74.1: Put-Call Parity

This module explains how the prices of calls, puts, the underlying stock, and risk-free bonds are all mathematically linked.

#### Put-Call Parity for European Options (LOS 74.a)

Put-call parity is a no-arbitrage equation that shows the precise relationship between the prices of European calls and puts with the same underlying asset, exercise price (X), and expiration date (T).

It's based on the payoffs of two specially constructed portfolios:

1.  **Fiduciary Call 📞+ 🏦:** This portfolio consists of a **long call option** and a **long position in a risk-free, zero-coupon bond** that pays the exercise price X at expiration.
    * If at expiration $S_T > X$, the call is exercised. Payoff = $(S_T - X) + X = S_T$.
    * If at expiration $S_T \le X$, the call expires worthless. Payoff = $0 + X = X$.
    * **Overall Payoff:** **Max($S_T$, X)**.

2.  **Protective Put 🛡️+ 📈:** This portfolio consists of a **long put option** and a **long position in one share of the underlying stock**.
    * If at expiration $S_T > X$, the put expires worthless. Payoff = $0 + S_T = S_T$.
    * If at expiration $S_T \le X$, the put is exercised. Payoff = $(X - S_T) + S_T = X$.
    * **Overall Payoff:** **Max($S_T$, X)**.

Since both portfolios have the **exact same payoff** at expiration regardless of what happens to the stock price, the law of one price dictates they must have the **exact same value** today. This gives us the put-call parity equation:

**Value of Fiduciary Call = Value of Protective Put**
$$c_0 + X(1+R_f)^{-T} = p_0 + S_0$$
Where:
* $c_0$ = Price of the call option today
* $p_0$ = Price of the put option today
* $S_0$ = Price of the underlying stock today
* $X(1+R_f)^{-T}$ = Present value of the risk-free bond (PV of X)

**Synthetic Positions**
The power of this formula is that it can be rearranged to replicate any of the four assets using a combination of the other three. For example, to create a **synthetic share of stock**:
$$S_0 = c_0 - p_0 + X(1+R_f)^{-T}$$
This means buying a call, selling a put, and investing the present value of the exercise price in a risk-free bond perfectly replicates the payoffs of owning the stock.

> **CFA Exam Tip:** Put-call parity is a major topic. You **must** memorize the formula. The most common exam question gives you the price of three of the assets and asks you to calculate the no-arbitrage price of the fourth.

---

#### Put-Call-Forward Parity (LOS 74.b)

This is a simple extension of the main parity relationship. It applies when you are dealing with options on forward or futures contracts.

Instead of using the underlying stock (which costs $S_0$ today), we use a **forward contract** on the stock. The cost of replicating the stock's payoff using a forward contract is the **present value of the forward price ($F_0(T)$)**.

So, we simply replace $S_0$ in the original equation with the present value of the forward price:
$$c_0 + X(1+R_f)^{-T} = p_0 + F_0(T)(1+R_f)^{-T}$$

This version links the prices of puts and calls to the price of a forward contract instead of the spot price of the underlying asset -3281].

***

### Summary of Formulas for Reading 74

This reading is centered on one of the most important no-arbitrage relationships in finance. You must know these formulas.

* **Put-Call Parity:**
    This equation links the prices of European puts and calls with the underlying stock and a risk-free bond.
    $$c_0 + X(1+R_f)^{-T} = p_0 + S_0$$

* **Synthetic Stock:**
    An example of rearranging the parity equation to replicate an asset.
    $$S_0 = c_0 - p_0 + X(1+R_f)^{-T}$$

* **Put-Call-Forward Parity:**
    This version replaces the spot price of the stock with the present value of the forward price.
    $$c_0 + X(1+R_f)^{-T} = p_0 + F_0(T)(1+R_f)^{-T}$$

***

### ⚡ Quick Exam-Day Pointers

For Reading 74, expect calculation-heavy questions. Speed and accuracy with the main formula are essential.

* **It's All About No-Arbitrage:** Put-call parity exists because two special portfolios, the **Fiduciary Call** (Call + Bond) and the **Protective Put** (Put + Stock), have the exact same payoffs at expiration. Because their payoffs are identical, their prices today *must* be identical.

* **Memorize the Formula!** 🧠 This is non-negotiable. Use a mnemonic if it helps, like "**S**ome **P**eople **C**are about **B**onds" (Stock + Put = Call + Bond [PV of X]). A very common exam question will give you three of the four inputs and ask you to solve for the missing one.

* **Watch Your PV Calculation:** Remember that the "Bond" part of the equation is the **present value** of the exercise price, discounted at the risk-free rate: $X(1+R_f)^{-T}$. Don't forget to discount!

* **Think Synthetically:** Understand that the formula can be algebraically rearranged to create a "synthetic" version of any of the four assets. For example, a synthetic long call = long put + long stock - long bond.

* **Forward Parity is Just a Substitution:** Don't be intimidated by put-call-forward parity. It's the same exact formula as the original, but you simply replace the spot price of the stock ($S_0$) with the **present value of the forward price** ($F_0(T)(1+R_f)^{-T}$).