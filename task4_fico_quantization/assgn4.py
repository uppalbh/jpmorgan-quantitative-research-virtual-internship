import pandas as pd
import numpy as np

df1 = pd.read_csv("./JPMorgan/task34.csv")
df1 = df1[["fico_score", "default"]]
print(df1.head())
df1 = df1.iloc[:1000].copy() #As the alogirthm is O(n^2)
df1 = df1.sort_values("fico_score").reset_index(drop=True)

N =len(df1)
prefix_defaults = np.zeros(len(df1) + 1)
for i in range(N):
    prefix_defaults[i + 1] = prefix_defaults[i] + df1.iloc[i]["default"]


def bucket_score(i, j):
    no_val = j-i
    no_k = prefix_defaults[j] - prefix_defaults[i]
    pi = no_k / no_val
    eps = 1e-12
    pi = np.clip(pi, eps, 1 - eps) #Values of pi less that eps bumps up to eps
    #and values more than 1-eps gets scaled down to 1-eps
    loss = no_k*np.log(pi) + (no_val-no_k)*np.log(1-pi)
    return loss

sum_costs = 0
def quantization(n, df):
    N = len(df)
    score = np.full((N, N), -np.inf)
    for i in range(N):
        for j in range(i, N):
            score[i][j] = bucket_score(df, i, j+1)
    
    dp = np.full((n, N), -np.inf)
    parent = np.full((n, N), -1, dtype=int)
    for i in range(N): dp[0][i] = score[0][i]

    for i in range(1, n):
        for j in range(i, N):
            for k in range(i-1, j):
                cand = dp[i-1][k] + score[k+1][j]
                if (cand > dp[i][j]):
                    dp[i][j] =  cand
                    parent[i][j] = k

    boundaries = []
    end = N - 1    
    for b in range(n - 1, 0, -1):
        split = parent[b][end]
        boundaries.append(split + 1)
        end = split

    boundaries.reverse()
    print("Maximum Log-Likelihood:", dp[n - 1][N - 1])
    print("\nBucket boundaries (indices):")
    print(boundaries)
    print("\nFICO ranges:")
    start = 0
    rating = n
    for boundary in boundaries + [N]:
        left = df.iloc[start]["fico_score"]
        right = df.iloc[boundary - 1]["fico_score"]
        print(f"Rating {rating}: {left} - {right}")
        rating -= 1
        start = boundary

quantization(6, df1)



