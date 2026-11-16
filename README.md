# 🌱 Animal Crossing Turnip Market — GBM Simulator

A mathematical modelling project exploring the **Stalk Market** in *Animal Crossing: New Horizons* using **Geometric Brownian Motion (GBM)**.

> An old Python project, originally developed for a mathematics exploration, revisited and rebuilt as I continue studying mathematics and programming.

## Research question

**To what extent would the Animal Crossing “stalk” be successful and profitable in reality?**

The original investigation collected five weeks of turnip prices, calculated rates of return and volatility, and used GBM to simulate possible future prices.

## 📊 Dataset

The historical dataset contains 35 recorded prices across five weeks:

- 5 weekly buy prices
- 30 daily sell prices
- Prices range from **47 to 459 Bells**
- The 459-Bell price is a major high-value outlier

The original report calculated a mean daily simple rate of return of approximately **14.29%** and volatility of approximately **84.46%**.

## 🧮 The mathematics

The project models prices with Geometric Brownian Motion:

$$
S_{t+\Delta t}
=
S_t
\exp\left[
(\mu-\frac12\sigma^2)\Delta t
+
\sigma\sqrt{\Delta t}Z
\right]
$$

where:

- $S_t$ = current turnip price
- $\mu$ = drift
- $\sigma$ = volatility
- $\Delta t$ = time step
- $Z \sim N(0,1)$ = random shock

The exponential form keeps simulated prices positive.

### Returns

For the original data, the simple rate of return is

$$
r = \frac{S_{sell}-S_{buy}}{S_{buy}}
$$

and the logarithmic return is

$$
r_{log}=\ln\left(\frac{S_{sell}}{S_{buy}}\right).
$$

The original investigation used these values to study the distribution and risk of the fictional market.

## 💻 Project structure

```text
animal-crossing-turnip-gbm/
├── README.md
├── requirements.txt
├── data/
│   ├── historical_prices.csv
│   └── daily_returns.csv
├── src/
│   ├── gbm_simulation.py
│   └── final_price_simulation.py
└── results/
    ├── gbm_paths.png
    ├── log_returns.png
    ├── final_price_distribution.png
    └── summary.json
```

## 🚀 Running the project

```bash
git clone <your-repository-url>
cd animal-crossing-turnip-gbm
pip install -r requirements.txt
python src/gbm_simulation.py
python src/final_price_simulation.py
```

## 🔬 Original investigation vs. revised version

The appendix of the original report used hard-coded values `mu = 0.1` and `sigma = 0.8`, while the report's analysis states approximately `mu = 0.14285112984` and `sigma = 0.844594157512`.

The rebuilt version uses the values calculated from the collected daily returns (including the sample standard deviation used in the original analysis) and keeps the time units consistent.

This is intentional: the GitHub version is a **reconstruction and extension**, not a claim that the original code was already structured this way.

## ⚠️ Limitations

GBM is a simplified stochastic model. The original investigation identified several limitations:

- The Animal Crossing market is not governed by the same mechanisms as real financial markets.
- The observed turnip prices contain randomness that does not map cleanly onto human-driven markets.
- The extremely high observed volatility is unrealistic for most real-world stocks.
- GBM assumes constant volatility, while real markets can experience changing volatility and sudden jumps.
- Five weeks of data is a very small dataset.

Therefore, the simulations should be interpreted as **mathematical experiments**, not reliable financial predictions.

## 🌷 Why this project?

This project started from a simple question: *could the turnip market in Animal Crossing be treated like a real financial market?*

It became an opportunity to connect a game I enjoyed with probability, statistics, stochastic processes, and programming. Revisiting it now lets me improve the implementation while understanding the mathematics much more deeply.

## 🔭 Future improvements

- Compare GBM against the actual in-game turnip price mechanics
- Run Monte Carlo simulations for profit probabilities
- Estimate the probability of exceeding a target selling price
- Compare different selling strategies
- Add confidence intervals
- Build an interactive dashboard
- Explore models that allow changing volatility or sudden price jumps

## 🛠️ Technologies

- Python
- NumPy
- pandas
- Matplotlib
- SciPy
- Probability & statistics
- Stochastic modelling
- Monte Carlo simulation
