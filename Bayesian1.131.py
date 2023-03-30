import math

# Define a prior probability distribution
def prior(x):
    return 1 / (1 + math.exp(-x))

# Define a likelihood function
def likelihood(x, mu, sigma):
    return 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Define a posterior function
def posterior(x, mu, sigma):
    return likelihood(x, mu, sigma) * prior(mu)

# Define the data
data = [1, 2, 3, 4, 5]

# Compute the posterior distribution
mu_range = [-5, 5]
sigma_range = [0.1, 5]
step = 0.1
posteriors = {}
for mu in range(int((mu_range[1] - mu_range[0]) / step)):
    mu_val = mu_range[0] + mu * step
    for sigma in range(int((sigma_range[1] - sigma_range[0]) / step)):
        sigma_val = sigma_range[0] + sigma * step
        posterior_val = sum([math.log(posterior(x, mu_val, sigma_val)) for x in data])
        posteriors[(mu_val, sigma_val)] = posterior_val

# Find the maximum posterior
max_mu, max_sigma = max(posteriors, key=posteriors.get)

print("The maximum posterior is at mu =", max_mu, "and sigma =", max_sigma)
