# Notes on the original code

The original appendix contained two scripts:

1. `GBM Graph and Log Returns Histogram`
2. `Final Price Histogram`

The original scripts are preserved conceptually, but the GitHub reconstruction changes several implementation details:

- The report states μ = 0.14285112984 and σ = 0.844594157512, while the appendix scripts use 0.1 and 0.8.
- The rebuilt version derives μ and σ from the supplied five-week dataset.
- The rebuilt version uses one consistent daily time unit.
- A fixed random seed is used so the GitHub graphs are reproducible.
- The original first histogram filtered simulated log returns to positive values before fitting a lognormal distribution. The rebuilt project instead visualizes the historical daily log returns directly, because log returns themselves can be negative.
