import numpy as np

spot = 100      # Spot Price
T = 1           # Option time
r = 0.05        # Discount Rate
sigma = 0.2     # Volatility (Standard Deviation)
nSimulation = 2
nSteps = 3      # Number of days is actually 252
strike = 100    # Strike Price  
dt = T/nSteps   # Every day


drift = (r - (sigma*sigma)/2)*dt
a = sigma * np.sqrt(dt)



# Let's make the random variable that follow the normal distribution

rv = np.random.normal(0,1,(nSimulation,nSteps))

matrix = np.zeros((nSimulation,nSteps))

matrix[:,0] = spot
#**print(matrix)



# Let's apply the formula of S(t+1)

for i in range(1,nSteps):
    matrix[:,i] = matrix[:,i-1]*np.exp(drift + a*rv[:,i])

#**print(matrix)

# Let's calculate the payoff of call for every simulation

c = matrix[:,-1] - strike

#**print(c)

# We can not take the negative one

for i in range(0,nSimulation):
    if(c[i]<0):
        c[i] = 0


#**print(c)
        
# Let's calculate the payoff of put for every simulation

p = strike - matrix[:,-1]

#**print(p)

# We can not take the negative one

for i in range(0,nSimulation):
    if(p[i]<0):
        p[i] = 0


        
# Let's calculate the payoff of the call
call_payoff = np.mean(c)




# Let's calculate the payoff of the put
put_payoff = np.mean(p)




# Discounting back to today's price (provide the present value of a future value)
call_price = call_payoff * np.exp(-r*T)

put_price = put_payoff * np.exp(-r*T)

print("The call price is: ", call_price)
print("The put price is: ", put_price)
