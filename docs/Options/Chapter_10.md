Greetings, Stock Options Samurai\! 🗡️ Your progression through the core strategies is commendable.

Chapter 10 takes the vertical spread concept you mastered in Chapters 7 and 8 and applies it to a more complex, but highly useful, setup: **The Combination Spread**. This strategy is the mark of a truly flexible Samurai, ready to profit from a directional move while completely defining both their risk and reward.

-----

## Chapter 10: Combination Spreads — The Defined Risk Attack 🥋

### 🎯 Introduction: What is a Combination Spread?

A **Combination Spread** (or **Strangle Spread**) is a strategy built on the principle of simultaneously buying and selling two different option types (Calls and Puts) with two different strike prices, but always with the **same expiration date**.

The goal is to bracket the stock price with options that fully define the maximum profit and maximum loss.

#### **The Two Main Types**

The two core combination spreads are the mirror images of each other, defined by your market outlook:

| Strategy Name | Outlook | Structure | Net Result |
| :--- | :--- | :--- | :--- |
| **Long Combination Spread** (or **Long Strangle Spread**) | **Very Volatile/Directional** (Expect a **big** move UP or DOWN) | Buy an OTM Put + Buy an OTM Call | **Net Debit** (You pay upfront) |
| **Short Combination Spread** (or **Short Strangle Spread**) | **Neutral/Quiet** (Expect the stock to **stay put**) | Sell an OTM Put + Sell an OTM Call | **Net Credit** (You are paid upfront) |

-----

### 1\. Long Combination Spread (Long Strangle) — The Volatility Bet 🌪️

This is a bet on the market *moving sharply* in either direction. It is a **net debit** strategy, meaning you pay the premium upfront, and that debit is your maximum loss.

#### **The Structure**

You simultaneously:

1.  **Buy** an Out-of-the-Money (OTM) **Put** ($X_L$).
2.  **Buy** an Out-of-the-Money (OTM) **Call** ($X_H$).

$X_L$ (Lower Strike) is below the stock price, and $X_H$ (Higher Strike) is above the stock price.

#### **Risk, Reward, and Break-Evens**

| Metric | Formula |
| :--- | :--- |
| **Maximum Loss** | **Net Debit** Paid (Premium of Call + Premium of Put) |
| **Maximum Profit** | **Unlimited** on the upside (The long call is unlimited). |
| **Downside Break-Even (DBE)** | $X_L - \text{Net Debit}$ |
| **Upside Break-Even (UBE)** | $X_H + \text{Net Debit}$ |

The stock must move outside of the break-even points for the trade to be profitable.

**Mnemonic: L-V-I-C**

  * **L**ong Strangle loves **V**olatility.
  * **I**nvolves **C**ost (Net Debit).

<div style="text-align: center; margin: 20px 0;">
<p style="font-weight: bold;">Long Strangle Profit Profile (The "U" Shape)</p>
<pre>
<code class="mermaid">
graph TD
subgraph Long Strangle
A[DBE] --> B(Max Loss)
B --> C(UBE)
C --> D(Unlimited Profit)
A --> E(Unlimited Profit)

```
      style B fill:#FADBD8,stroke:#CB4335,stroke-width:2px
      style E,D fill:#E8F8F5,stroke:#2ECC71,stroke-width:2px
  end
  
  classDef hidden stroke-opacity:0
  class A,C hidden
```

</code>
</pre>
*The maximum loss occurs if the stock price finishes between the two strikes ($X_L$ and $X_H$), causing both options to expire worthless.*
</div>

-----

### 2\. Short Combination Spread (Short Strangle) — The Quiet Bet 😴

This is the exact opposite of the Long Strangle. You are betting that the stock price will **stay within a defined range** and expire worthless. This is a favorite income strategy. It is a **net credit** strategy.

#### **The Structure**

You simultaneously:

1.  **Sell** an Out-of-the-Money (OTM) **Put** ($X_L$).
2.  **Sell** an Out-of-the-Money (OTM) **Call** ($X_H$).

#### **Risk, Reward, and Break-Evens**

| Metric | Formula |
| :--- | :--- |
| **Maximum Profit** | **Net Credit** Received (Premium of Call + Premium of Put) |
| **Maximum Loss** | **Unlimited** on both the upside and the downside. |
| **Downside Break-Even (DBE)** | $X_L - \text{Net Credit}$ |
| **Upside Break-Even (UBE)** | $X_H + \text{Net Credit}$ |

The stock must **stay between** the break-even points for the trade to be profitable. The maximum profit is achieved if the stock price finishes between the two strikes.

**Key Distinction: Naked Risk\!** The short strangle is essentially a combination of two **naked options**. Because of the unlimited risk, it generally requires a margin account and significant collateral.

**Mnemonic: S-C-U**

  * **S**hort Strangle wants **C**alm.
  * **U**nlimited Risk.

-----

### 3\. Hedging the Short Strangle: The Iron Condor 🛡️

Because the Short Strangle has unlimited risk, it is often **hedged** by buying protective options further out-of-the-money. This transforms the unlimited-risk Short Strangle into the defined-risk **Iron Condor**.

The Iron Condor is a combination of a **Bull Put Spread** and a **Bear Call Spread**.

#### **Iron Condor Structure** (Four Legs)

1.  **Sell** Put ($X_2$)
2.  **Buy** Put ($X_1$) (Bull Put Spread)
3.  **Sell** Call ($X_3$)
4.  **Buy** Call ($X_4$) (Bear Call Spread)

(Note: $X_1 < X_2 < X_3 < X_4$)

#### **Risk/Reward Profile: Fully Defined**

  * **Max Profit:** The Net Credit received (achieved if the stock finishes between $X_2$ and $X_3$).
  * **Max Loss:** The width of the widest spread minus the net credit (fully defined and limited).

**The Samurai's Advantage:** The Iron Condor provides a very high probability of profit (the stock needs to stay within the range $X_2$ to $X_3$) while eliminating the catastrophic unlimited risk of the un-hedged Short Strangle.

-----

### 4\. Selection Criteria: Choosing the Right Strangle

The core decision for a combination spread revolves around **Implied Volatility (IV)**:

| Strategy | IV Environment | Rationale |
| :--- | :--- | :--- |
| **Long Strangle** | **Low IV** (IV is cheap) | You are **buying** both options. Low IV makes the trade cost less, increasing your potential return if volatility rises. |
| **Short Strangle** / **Iron Condor** | **High IV** (IV is expensive) | You are primarily **selling** options. High IV inflates the premium you receive, giving you a wider break-even range for a given credit. |

**Key Concept: The Volatility Swing**
A profitable long strangle requires two things:

1.  **Movement in the stock price.**
2.  **An increase in Implied Volatility (IV)**, which drives up the price of your long options, increasing the return.

The Combination Spreads offer the sophisticated options Samurai the ability to place bets based on **directional moves** OR **market calmness**, all while using a defined set of Call and Put options.