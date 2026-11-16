import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

RNG_SEED = 2026
INITIAL_PRICE = 105
DAYS = 35
N_PATHS = 10


def load_prices():
    data = pd.read_csv("data/historical_prices.csv")
    return data["day"].to_numpy(), data["price_bells"].to_numpy()


def calculate_daily_parameters(prices):
    weekly = prices.reshape(5, 7)
    buy_prices = np.repeat(weekly[:, 0], 6)
    sell_prices = weekly[:, 1:].reshape(-1)

    returns = sell_prices / buy_prices - 1
    mu = returns.mean()
    sigma = returns.std(ddof=1)
    return mu, sigma


def simulate_gbm(s0, mu, sigma, days, paths, seed):
    rng = np.random.default_rng(seed)
    z = rng.standard_normal((days, paths))
    increments = (
        (mu - 0.5 * sigma**2)
        + sigma * z
    )
    log_prices = np.vstack(
        [np.zeros(paths), np.cumsum(increments, axis=0)]
    )
    return s0 * np.exp(log_prices)


def main():
    historical_days, prices = load_prices()
    mu, sigma = calculate_daily_parameters(prices)

    simulated = simulate_gbm(
        INITIAL_PRICE, mu, sigma, DAYS, N_PATHS, RNG_SEED
    )

    future_days = np.arange(
        historical_days[-1] + 1,
        historical_days[-1] + DAYS + 2
    )

    plt.figure(figsize=(12, 6))
    plt.plot(
        historical_days,
        prices,
        linewidth=2,
        label="Historical prices"
    )

    for i in range(N_PATHS):
        plt.plot(future_days, simulated[:, i], alpha=0.65)

    plt.axvline(
        historical_days[-1] + 1,
        linestyle="--",
        linewidth=1.2,
        label="Start of simulation"
    )
    plt.xlabel("Day")
    plt.ylabel("Price (Bells)")
    plt.title("Historical Turnip Prices + GBM Simulations")
    plt.grid(True, alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.show()

    print(f"Daily drift: {mu:.4f} ({mu:.2%})")
    print(f"Daily volatility: {sigma:.4f} ({sigma:.2%})")


if __name__ == "__main__":
    main()
