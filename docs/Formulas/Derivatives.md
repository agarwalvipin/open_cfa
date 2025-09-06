# 📈 Derivatives Formulas

## 📊 Reading 66: Derivative Instrument and Derivative Market Features

This reading is descriptive and does not contain mathematical formulas.

---

## 📝 Reading 67: Forward Commitment and Contingent Claim Features and Instruments

- 🎯 **Option value at expiration (exercise value):**

  - 📈 **Call option:**
    $$V_T = \max(0, S_T - X)$$
  - 📉 **Put option:**
    $$V_T = \max(0, X - S_T)$$

- 💰 **Option profit at expiration (value minus premium paid):**

  - 📈 **Long call profit:**
    $$\text{Profit} = \max(0, S_T - X) - \text{Premium}$$
  - 📈 **Short call profit (loss):**
    $$\text{Profit} = \text{Premium} - \max(0, S_T - X)$$
  - 📉 **Long put profit:**
    $$\text{Profit} = \max(0, X - S_T) - \text{Premium}$$
  - 📉 **Short put profit (loss):**
    $$\text{Profit} = \text{Premium} - \max(0, X - S_T)$$

- ⚖️ **Option breakeven points:**

  - 📈 **Call breakeven:** $$S_T^* = X + \text{Premium}$$
  - 📉 **Put breakeven:**  $$S_T^* = X - \text{Premium}$$

---

## 🛡️ Reading 68: Derivative Benefits, Risks, and Issuer and Investor Uses

This reading is descriptive and does not contain mathematical formulas.

---

## ⚖️ Reading 69: Arbitrage, Replication, and the Cost of Carry in Pricing Derivatives

- 🔄 **No-arbitrage forward price (cost-of-carry):**

  - 💸 **Asset with no costs or benefits:**
    $$F_0(T) = S_0(1 + R_f)^T$$
  - 💰 **Asset with costs and/or benefits:**
    $$F_0(T) = [S_0 + \mathrm{PV}_0(\text{Costs}) - \mathrm{PV}_0(\text{Benefits})] (1 + R_f)^T$$

- 🌍 **No-arbitrage forward exchange rate (interest rate parity):**

  $$\text{Forward}_{\text{p/b}} = \text{Spot}_{\text{p/b}} \times \frac{1 + i_p}{1 + i_b}$$

  where p/b is price currency per base currency, and i_p and i_b are the interest rates for the price and base currencies respectively.

---

## ⏳ Reading 70: Pricing and Valuation of Forward Contracts

- 📋 **Value of a forward contract:**

  - 🆕 **At initiation (t = 0):** by design the value is zero

    $$V_0(T) = S_0 - \frac{F_0(T)}{(1 + R_f)^T} = 0$$

  - ⏱️ **During its life (at time t):**

    $$V_t(T) = S_t - \frac{F_0(T)}{(1 + R_f)^{(T-t)}}$$

  - 🏁 **At expiration (t = T):**

    $$V_T(T) = S_T - F_0(T)$$

- 🔮 **Implied forward rate (relationship between spot and forward rates):**

  $$(1 + Z_B)^B = (1 + Z_A)^A \times (1 + F_{A, B-A})^{(B-A)}$$

  where Z_A and Z_B are spot rates for periods A and B, and F_{A,B-A} is the forward rate for the period from A to B.

---

## 🚀 Reading 71: Pricing and Valuation of Futures Contracts

- 📊 **Interest-rate futures price (quoted convention):**

  $$\text{Futures Price} = 100 - (100 \times \text{Implied Annualized Rate})$$

- 📈 **Basis point value (BPV) of an interest-rate futures contract:**

  $$\text{BPV} = \text{Notional Principal} \times \text{Period} \times 0.0001$$

---

## 🔄 Reading 72: Pricing and Valuation of Interest Rate Swaps

- 💱 **Value of an interest-rate swap (fixed-rate payer):**

  $$V_{\text{swap}} = \mathrm{PV}(\text{Floating payments}) - \mathrm{PV}(\text{Fixed payments})$$

  At initiation the fixed rate is set so the swap value is zero.

---

## 🎯 Reading 73: Pricing and Valuation of Options

- 💎 **Exercise value (intrinsic value):**

  - 📈 **Call:** $$\text{Exercise Value} = \max(0, S - X)$$
  - 📉 **Put:**  $$\text{Exercise Value} = \max(0, X - S)$$

- 💰 **Option premium (price decomposition):**

  $$\text{Option Premium} = \text{Exercise Value} + \text{Time Value}$$

- 🔒 **European option price bounds:**

  - 📈 **Call upper bound:** $$c_0 \le S_0$$
  - 📉 **Put upper bound:**  $$p_0 \le \frac{X}{(1 + R_f)^T}$$
  - 📈 **Call lower bound:** $$c_0 \ge \max\left[0, S_0 - \frac{X}{(1 + R_f)^T}\right]$$
  - 📉 **Put lower bound:**  $$p_0 \ge \max\left[0, \frac{X}{(1 + R_f)^T} - S_0\right]$$

---

## 🔄 Reading 74: Option Replication Using Put-Call Parity

- ⚖️ **Put-call parity (European options):**

  $$c_0 + \frac{X}{(1+R_f)^T} = p_0 + S_0$$

  🧩 **Rearrangements / synthetic assets:**

  - 📈 **Synthetic stock:** $$S_0 = c_0 - p_0 + \frac{X}{(1+R_f)^T}$$
  - 💰 **Synthetic bond:**  $$\frac{X}{(1+R_f)^T} = S_0 + p_0 - c_0$$
  - 📈 **Synthetic call:**  $$c_0 = S_0 + p_0 - \frac{X}{(1+R_f)^T}$$
  - 📉 **Synthetic put:**   $$p_0 = c_0 - S_0 + \frac{X}{(1+R_f)^T}$$

- ⏳ **Put-call-forward parity (when underlying is a forward):**

  $$\frac{F_0(T)}{(1+R_f)^T} + p_0 = c_0 + \frac{X}{(1+R_f)^T}$$

---

## 🌳 Reading 75: Valuing a Derivative Using a One-Period Binomial Model

- 🛡️ **Hedge ratio (h):**

  - 📈 **For a call:** $$h = \frac{c_{\text{up}} - c_{\text{down}}}{S_{\text{up}} - S_{\text{down}}}$$
  - 📉 **For a put:**  $$h = \frac{p_{\text{up}} - p_{\text{down}}}{S_{\text{up}} - S_{\text{down}}}$$

- 🎯 **Option value from binomial model (no-arbitrage method):**

  1. 🔍 Find the hedge ratio (h).
  2. 📊 Calculate the value of the hedged portfolio at expiration: $$V_{\text{up}} = h \cdot S_{\text{up}} - c_{\text{up}}.$$ 
  3. ⏮️ Discount the portfolio value to today: $$V_0 = \frac{V_{\text{up}}}{1 + R_f}.$$ 
  4. 💰 Solve for the option price: $$c_0 = h \cdot S_0 - V_0.$$

- 🎲 **Risk-neutral probability of an up-move (π):**

  $$\pi = \frac{(1 + R_f) - d}{u - d}$$

- 🌳 **Option value from binomial model (risk-neutral method):**

  $$\text{Option Value} = \frac{\pi \times \text{Payoff}_\text{up} + (1-\pi) \times \text{Payoff}_\text{down}}{1 + R_f}$$
