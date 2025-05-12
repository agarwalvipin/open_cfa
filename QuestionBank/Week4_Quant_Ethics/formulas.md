## Week 4 Formula Sheet

### Reading 5: Portfolio Mathematics

1.  **Expected Return of a Portfolio (n assets):**
    $$E(R_p) = \sum_{i=1}^{n} w_i E(R_i)$$
    Where:
    * \(E(R_p)\) = Expected return of the portfolio
    * \(w_i\) = Weight of asset \(i\) in the portfolio
    * \(E(R_i)\) = Expected return of asset \(i\)

2.  **Covariance of Returns (Probability Model for two assets A and B):**
    $$Cov(R_A, R_B) = \sum_{k=1}^{m} P(S_k) [R_{A,k} - E(R_A)] [R_{B,k} - E(R_B)]$$
    Where:
    * \(P(S_k)\) = Probability of economic state \(k\)
    * \(R_{A,k}\) = Return of asset A in state \(k\)
    * \(R_{B,k}\) = Return of asset B in state \(k\)
    * \(E(R_A)\) = Expected return of asset A
    * \(E(R_B)\) = Expected return of asset B

3.  **Correlation Coefficient:**
    $$\rho(R_A, R_B) = \frac{Cov(R_A, R_B)}{\sigma_A \sigma_B}$$
    Where:
    * \(\rho(R_A, R_B)\) = Correlation coefficient between asset A and asset B
    * \(Cov(R_A, R_B)\) = Covariance between asset A and asset B
    * \(\sigma_A\) = Standard deviation of asset A
    * \(\sigma_B\) = Standard deviation of asset B

4.  **Variance of a Two-Asset Portfolio:**
    Using Covariance:
    $$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B Cov(R_A, R_B)$$
    Using Correlation:
    $$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \sigma_A \sigma_B \rho(R_A, R_B)$$
    Where:
    * \(\sigma_p^2\) = Portfolio variance
    * \(w_A, w_B\) = Weights of asset A and asset B
    * \(\sigma_A^2, \sigma_B^2\) = Variances of asset A and asset B
    * \(\sigma_A, \sigma_B\) = Standard deviations of asset A and asset B

5.  **Variance of a Three-Asset Portfolio (A, B, C):**
    $$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + w_C^2 \sigma_C^2 + 2 w_A w_B Cov(R_A, R_B) + 2 w_A w_C Cov(R_A, R_C) + 2 w_B w_C Cov(R_B, R_C)$$
    Or using correlation:
    $$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + w_C^2 \sigma_C^2 + 2 w_A w_B \sigma_A \sigma_B \rho_{AB} + 2 w_A w_C \sigma_A \sigma_C \rho_{AC} + 2 w_B w_C \sigma_B \sigma_C \rho_{BC}$$

6.  **Roy's Safety-First Ratio (SFR):**
    $$SFR = \frac{E(R_p) - R_L}{\sigma_p}$$
    Where:
    * \(E(R_p)\) = Expected portfolio return
    * \(R_L\) = Threshold level return (minimum acceptable return)
    * \(\sigma_p\) = Portfolio standard deviation

### Reading 6: Simulation Methods

1.  **Continuously Compounded Return (from HPR or Price Relative):**
    $$r_{CC} = \ln(1 + HPR)$$
    or
    $$r_{CC} = \ln\left(\frac{P_T}{P_0}\right)$$
    Where:
    * \(r_{CC}\) = Continuously compounded return
    * \(HPR\) = Holding Period Return
    * \(P_T\) = Price at time T
    * \(P_0\) = Price at time 0
    * \(\ln\) = Natural logarithm

2.  **Future Asset Price with Continuous Compounding:**
    $$P_T = P_0 e^{r_{0,T}}$$
    Where:
    * \(P_T\) = Asset price at time T
    * \(P_0\) = Asset price at time 0 (initial price)
    * \(r_{0,T}\) = Continuously compounded rate of return from time 0 to T
    * \(e\) = Base of the natural logarithm (approx. 2.71828)

*(Note: Ethics Reading 91 – Standards IV to VII does not involve quantitative formulas.)*