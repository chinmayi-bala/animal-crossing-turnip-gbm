import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


RNG_SEED = 2026
INITIAL_PRICE = 105
DAYS = 35
N_SIMULATIONS = 10_000


def get_parameters(prices):
    weekly = prices.reshape(5, 7)
    buy_prices = np.repeat(weekly[:, 0], 6)
    sell_prices = weekly[:, 1:].reshape(-1)

    returns = sell_prices / buy_prices - 1
    mu = returns.mean()
    sigma = returns.std(ddof=1)
    return mu, sigma


def simulate_final_prices(s0, mu, sigma, days, simulations, seed):
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(simulations)

    return s0 * np.exp(
        (mu - 0.5 * sigma**2) * days
        + sigma * np.sqrt(days) * z
    )


def main():
    prices = pd.read_csv(
        "data/historical_prices.csv"
    )["price_bells"].to_numpy()

    mu, sigma = get_parameters(prices)

    final_prices = simulate_final_prices(
        INITIAL_PRICE,
        mu,
        sigma,
        DAYS,
        N_SIMULATIONS,
        RNG_SEED
    )

    mean_price = final_prices.mean()
    median_price = np.median(final_prices)

    plt.figure(figsize=(10, 6))
    plt.hist(
        final_prices,
        bins=50,
        density=True,
        alpha=0.65
    )
    plt.axvline(
        mean_price,
        linestyle="--",
        linewidth=1.8,
        label=f"Mean = {mean_price:.1f}"
    )
    plt.axvline(
        median_price,
        linestyle="--",
        linewidth=1.8,
        label=f"Median = {median_price:.1f}"
    )
    plt.xlabel("Simulated final price (Bells)")
    plt.ylabel("Density")
    plt.title("Simulated Turnip Price After 35 Days")
    plt.grid(True, alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.show()

    print(f"Mean final price: {mean_price:.2f} Bells")
    print(f"Median final price: {median_price:.2f} Bells")
    print(f"Minimum simulated price: {final_prices.min():.2f}")
    print(f"Maximum simulated price: {final_prices.max():.2f}")


if __name__ == "__main__":
    main()
