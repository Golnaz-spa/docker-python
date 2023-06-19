# Pricing European Call using Binomial Lattice
# Pricing European Call using Binomial Lattice -  Various Strike prices (x-axis) Vs. the option value (y-axis)
import seaborn as sns
import numpy as np

# Pricing European Option using Binomial Lattice
def binomial_tree(K, T, S0, r, N, u, d, opttype="C"):
    # Compute the constants
    dt = T / N
    #q is risk meaturity - probability p
    q = (np.exp(r * dt) - d) / (u - d)
    disc = np.exp(-r * dt)
    # Initialize asset prices at maturity time step N
    S = np.zeros(N + 1)
    S[0] = S0 * d ** N
    for j in range(1, N + 1):
        S[j] = S[j - 1] * u / d
    C = np.zeros(N + 1)
    # Initialize option values at maturity
    for j in range(0, N + 1):
        C[j] = max(0, S[j] - K)
    # Step back through the tree
    for i in np.arange(N, 0, -1):
        for j in range(0, i):
            C[j] = disc * (q * C[j + 1] + (1 - q) * C[j])
    return C[0]

S0 = 25
K = 24
T = 1
r = 0.26
N = 3
t = T / (N - 1)
u = 1.1
d = 0.9
opttype = "C"
#varius strike price in range 20 to 40
sT = range(40,60, 1)
optionprice = []
for i in sT:
    strickeprice_list = binomial_tree(i, T, S0, r, N, u, d, opttype="C")
    optionprice.append(strickeprice_list)

print("option price list is", optionprice)
print("option price of this list is : ", optionprice)