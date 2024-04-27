from e1inv import*
#from functions_of_kernel import*
import numpy as np

def gamma_process_with_inverse_levy(shape, scale, M, g, limX, limY):
    """
    scale --> already 1/beta
    M = number of points of the gamma process (truncation) 
    a,b,c,d = limits of my square"""
    # step 1 

    a = limX[0]
    b = limY[1]

    c = limY[0]
    d = limY[1]

    #expected sium of the weights: E(T(S)) = 1/beta*a(S) 

    ## step 2
    x = np.random.uniform(a,b,M)
    y = np.random.uniform(c,d,M)

    ##step 3
    tau=[np.random.exponential(1)]
    for i in range(M-1):
        tau.append(tau[-1] + np.random.exponential(1))

    
    ##step 4
    w = []

    for m in range(M): 
        w_m = E1_inverse(tau[m]/shape)* scale
        w.append(float(w_m))

    return w, x, y

"""shape = 3
scale = 2
M = 10
g = 5
limX = [0,1]
limY = [0,1]
w, x, y = gamma_process_with_inverse_levy(shape, scale, M, g, limX, limY)

print(w)"""


"""
def gamma_process_with_inverse_levy_for_posterior(alpha, beta, c_, M, g, limX, limY, sigma, limXin, limYin, sch):
    scale --> already 1/beta
    M = numberof points of the gamma process (truncation) 
    a,b,c,d = limits of my square
    # step 1 

    a = limX[0]
    b = limY[1]

    c = limY[0]
    d = limY[1]

    #expected sium of the weights: E(T(S)) = 1/beta*a(S) 

    ## step 2
    x = np.random.uniform(a,b,M)
    y = np.random.uniform(c,d,M)

    means = [[i, j] for i, j in zip(x, y)]

    integral = np.array(kernel_integral_over_X(means, sigma, sch, limXin, limYin))

    beta_star_inv= (beta +  1/c_)*np.ones(np.size(integral)) + integral
    beta_star = [1/a for a in beta_star_inv]

    ##step 3
    tau=np.cumsum(np.random.exponential(1,M))
    
    ##step 4
    w = np.zeros(M)

    for m in range(M): 
        w[m] = E1_inverse(tau[m]/alpha)* beta_star[m]

    w[np.isnan(w)] = 0

    return w, x, y

shape = 3
g = 51
limX = [0,100]
limY = [0,100]

w, x, y = gamma_process_with_inverse_levy(shape, scale, M, g, limX, limY)

print(sum(w))


M = 100
alpha = 3
beta = 2
c = 1
scale = 2
sigma = 0.1
g = 50

limXin = [0,1]
limX = [0,1]
limYin = [0,1]
limY = [0,1]

w, x, y = gamma_process_with_inverse_levy_for_posterior(alpha, beta, c, M, g, limX, limY, sigma, limXin, limYin, scale)

print(w[:5])"""