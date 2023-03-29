import numpy as np
import matplotlib.pyplot
# Define the parameters of the stock price model
S0 = 100 # initial stock price
mu = 0.05 # drift rate
sigma = 0.2 # volatility
T = 1 # time horizon
N = 252 # number of time steps
dt = T/N # time step size

# Simulate the stock price using geometric Brownian motion
t = np.linspace(0, T, N+1)
W = np.append(0, np.random.normal(size=N)*np.sqrt(dt))
S = S0*np.exp(np.cumsum((mu - 0.5*sigma**2)*dt + sigma*W))

# Calculate the log return of the stock price over time
log_returns = np.log(S[1:]) - np.log(S[:-1])

# Simulate the log return using Ito's Lemma
log_returns_ito = (mu - 0.5*sigma**2)*dt + sigma*np.random.normal(size=N)*np.sqrt(dt)

# Plot the results
fig, ax = plt.subplots(2, 1, figsize=(10,8))
ax[0].plot(t, S)
ax[0].set_ylabel('Stock price')
ax[1].plot(t[1:], log_returns)
ax[1].plot(t[1:], log_returns_ito, linestyle='--')
ax[1].set_ylabel('Log return')
ax[1].set_xlabel('Time')
ax[1].legend(['Actual', 'Ito'], loc='upper left')
plt.show()
