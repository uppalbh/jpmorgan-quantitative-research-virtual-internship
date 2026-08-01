## Task 4: Optimal FICO Score Bucketing

### Objective
Convert continuous FICO scores into optimal categorical credit ratings.

### Method
Implemented Dynamic Programming to maximize bucket log-likelihood.

The algorithm computes:
- Prefix sums
- Bucket likelihood
- DP optimization
- Boundary reconstruction

This approach is more statistically rigorous than using arbitrary bucket intervals.
