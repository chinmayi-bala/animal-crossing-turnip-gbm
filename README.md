# Animal Crossing Turnip Market: A Geometric Brownian Motion Simulation

Can the Animal Crossing: New Horizons turnip market be modelled using mathematics from real-world financial markets?

This project explores the game's unpredictable "Stalk Market" using Python, probability, statistics, and Geometric Brownian Motion (GBM). Using five weeks of recorded turnip prices, I investigated how a stochastic model could simulate price movements and what its predictions reveal about the risks of applying mathematical financial models to a fictional market.

## Research Question

To what extent would the Animal Crossing "Stalk Market" be successful and profitable in reality?

## Motivation

During the 2020 lockdown, I became interested in the turnip market in Animal Crossing: New Horizons and its unpredictable prices. I wanted to explore whether this in-game market could be studied using the mathematical techniques used to model financial markets.

This project began as a mathematical investigation and became an opportunity to explore programming, statistical analysis, probability distributions, and stochastic modelling.

## What the Project Does

- Organizes historical turnip-price data.
- Calculates returns to investigate price changes.
- Visualizes the distribution of historical log returns.
- Simulates 10,000 possible final prices using GBM.
- Compares mean and median simulated outcomes.


## Mathematical Model

### Geometric Brownian Motion

Geometric Brownian Motion (GBM) is a stochastic process used
to model quantities that evolve over time with random changes.

The continuous-time GBM model is:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
$$

where:

- $S_t$ is the price at time $t$.
- $\mu$ is the drift parameter.
- $\sigma$ is the volatility parameter.
- $W_t$ is a standard Brownian motion.
- $dt$ represents a small time interval.

For simulation, the model can be written in discrete form:

$$
S_{t+\Delta t} =
S_t \exp\left[
\left(\mu-\frac{\sigma^2}{2}\right)\Delta t
+\sigma\sqrt{\Delta t}\,Z
\right]
$$

Here, $Z$ is a random variable drawn from a standard normal
distribution, and $\Delta t$ is the time step.

This equation ensures that simulated prices remain positive
and incorporates random variation into each price change.

### Parameter Estimation

Let $r_t$ be a log return:

$$
r_t = \ln\left(\frac{S_t}{S_{t-1}}\right)
$$

For a time step of $\Delta t = 1$, the parameters are
estimated using:

$$
\hat{\sigma} = s_r
$$

$$
\hat{\mu} = \bar{r} + \frac{1}{2}s_r^2
$$

where $\bar{r}$ is the sample mean of the log returns and
$s_r$ is their sample standard deviation.

These estimates are based on the observed data and are
not guaranteed to describe future price movements accurately.

## Project Structure

```text
animal-crossing-turnip-gbm/
├── README.md
├── requirements.txt
├── data/
│   ├── historical_prices.csv
│   └── daily_returns.csv
├── src/
│   ├── gbm_simulation.py
│   ├── final_price_simulation.py
│   └── LEGACY_NOTES.md
└── results/
    ├── gbm_paths.png
    ├── log_returns.png
    ├── final_price_distribution.png
    └── summary.json
```

## Getting Started

### Requirements

- Python 3
- NumPy
- Matplotlib
- SciPy
- Pandas

### Installation

Clone the repository and navigate into the project directory:

```bash
git clone <your-repository-url>
cd animal-crossing-turnip-gbm
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

### Run the Simulations

Run the GBM price-path simulation:

```bash
python src/gbm_simulation.py
```

Run the final-price distribution simulation:

```bash
python src/final_price_simulation.py
```

The scripts generate visualizations and numerical summaries of the simulations.

## Visualizations

### Simulated Price Paths

![GBM price paths](results/gbm_paths.png)

### Historical Log Returns

![Historical log returns](results/log_returns.png)

### Simulated Final Prices

![Final price distribution](results/final_price_distribution.png)

## Key Findings

The dataset contains 35 recorded prices across five weeks, ranging from 47 to 459 Bells. The unusually high observation of 459 Bells illustrates how a single extreme value can influence statistical analysis.

The simulations demonstrate how randomness and volatility can produce a wide range of possible outcomes. However, simulated prices are model outputs, not predictions of what the game's prices will actually be.

## Limitations

- The dataset covers only five weeks and is too small to represent every possible price pattern.
- Geometric Brownian Motion assumes a particular mathematical structure for price movements that may not reflect the game's actual mechanics.
- The model's results depend on how drift and volatility are estimated.
- The game's turnip prices are governed by game-specific patterns and rules rather than the same mechanisms as real financial markets.
- A simulated price distribution does not, by itself, establish whether a trading strategy is profitable.

## Future Improvements

- Compare simulated prices with the game's actual price patterns.
- Investigate alternative methods of estimating drift and volatility.
- Calculate the probability of finishing with a profit under clearly defined buying and selling assumptions.
- Compare GBM with alternative stochastic models.
- Expand the dataset and evaluate how the additional observations affect the results.

## What I Learned

This project allowed me to connect mathematical theory with programming by translating a stochastic process into a working simulation. It also highlighted the importance of understanding model assumptions, checking calculations, and distinguishing mathematical outputs from real-world conclusions.

## Technologies

Python · NumPy · Pandas · Matplotlib · SciPy
