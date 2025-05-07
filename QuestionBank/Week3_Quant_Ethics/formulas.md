# 📘 CFA Level 1 - Week 3 Formula Sheet

## 📗 Reading 3: Statistical Measures of Asset Returns

### 🔹 Measures of Central Tendency

**Arithmetic Mean (Sample):**  
```math
x̄ = (Σ xᵢ) / n
```

---

### 🔹 Measures of Dispersion

**Range:**  
```math
Range = Maximum Value – Minimum Value
```

**Mean Absolute Deviation (MAD):**  
```math
MAD = Σ |xᵢ – x̄| / n
```

**Sample Variance (s²):**  
```math
s² = Σ (xᵢ – x̄)² / (n – 1)
```

**Sample Standard Deviation (s):**  
```math
s = √[Σ (xᵢ – x̄)² / (n – 1)]
```

**Coefficient of Variation (CV):**  
```math
CV = s / x̄
```

**Target Downside Deviation (Target Semideviation):**  
```math
s_target = √[Σ (xᵢ – R_T)² / (n – 1)], for all xᵢ ≤ R_T
```
(*R_T = target return*)

---

### 🔹 Skewness and Kurtosis (Approximate for Large Samples)

**Sample Skewness (Sk):**  
```math
Sk ≈ (1/n) × [Σ (xᵢ – x̄)³ / s³]
```

**Sample Kurtosis (K):**  
```math
K ≈ (1/n) × [Σ (xᵢ – x̄)⁴ / s⁴]
```
*Excess Kurtosis = Sample Kurtosis – 3*

---

### 🔹 Covariance and Correlation

**Sample Covariance (Covₓᵧ):**  
```math
Covₓᵧ = Σ (xᵢ – x̄)(yᵢ – ȳ) / (n – 1)
```

**Correlation Coefficient (ρₓᵧ or rₓᵧ):**  
```math
ρₓᵧ = Covₓᵧ / (sₓ × sᵧ)
```

---

## 📗 Reading 4: Probability Trees and Conditional Expectations

**Expected Value of X:**  
```math
E(X) = Σ P(xᵢ) × xᵢ
```

**Variance of X:**  
```math
σ²(X) = Σ P(xᵢ) × [xᵢ – E(X)]²
```

**Bayes’ Formula:**  
```math
P(Event | Info) = [P(Info | Event) × P(Event)] / P(Info)
```
*Used to update prior probabilities given new information.*
