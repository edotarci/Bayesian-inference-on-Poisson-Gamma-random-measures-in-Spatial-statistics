from e1inv import*
from inv_levy import*
import matplotlib.pyplot as plt
from scipy.stats import norm



def evaluation_of_Delta_X(v, sigma_x, sigma_y, M, limXin, limYin, sd, sch):
    """ integration od Delta over X: computed as the integration of each guassian (withe mean sigma_x, sigma_y)
    over the square (as product of the cdf) multiplied by its corrspondent weight v"""

    a = limXin[0]
    b = limXin[1]
    c = limYin[0]
    d = limYin[1]

    P_m = [(norm.cdf(b, sigma_x[m], sd) - norm.cdf(a, sigma_x[m], sd))*(norm.cdf(d, sigma_y[m], sd) - norm.cdf(c, sigma_y[m], sd))*sch for m in range(M)]

    #print(P_m)

    Weights = [v[m] * P_m[m] for m in range(M)]

    #print("weights", Weights)

    Poisson_mean = sum(Weights)

    #print("numero di punti attesi:", Poisson_mean)

    return Poisson_mean, Weights

def point_of_Cox_process(Poisson_mean, Weights, M, sd, limXin, limYin, sigma_x, sigma_y):
    """ Given the measure of the poisson process over the square (Delta(X)) we fist sample the number of points from 
    a Poisson Rv with mean Delta(X) and then we assign the points on the square with probability Delta(dx)/Delta(X).
    To assign the points, we first sample which a gaussian will generate the point (with probability v*N(X)/Delta(X))
    and then we sample the point form that gaussian while it it is inside the square"""

    a = limXin[0]
    b = limXin[1]
    c = limYin[0]
    d = limYin[1]

    Nx = np.random.poisson(Poisson_mean)
    #print("number of points:", Nx)

    x = []
    y = []

    for i in range(Nx):
        I = np.random.choice(M, p = Weights/Poisson_mean)
        check = True
        while check:
            x_i = np.random.normal(sigma_x[I], sd)
            y_i = np.random.normal(sigma_y[I], sd)
            if x_i<b and x_i>a and  y_i<d and  y_i>c:
                x.append(x_i)
                y.append(y_i)
                check = False
            #print(check)

    return x,y


def Cox_process(M,shape,scale,sd, limXin, limYin, limX, limY, sch):
    """simulation of the entire cox process"""
    Lmes = (limX[1] - limX[0])*(limY[1] - limY[0])
    g = 0
    v, sigma_x, sigma_y = gamma_process_with_inverse_levy(shape*Lmes, scale, M, g, limX, limY)
    Poisson_mean, Weights = evaluation_of_Delta_X(v, sigma_x, sigma_y, M, limXin, limYin, sd, sch)
    x,y = point_of_Cox_process(Poisson_mean, Weights, M, sd, limXin, limYin, sigma_x, sigma_y)
    return x,y,v,sigma_x, sigma_y


"""M = 500
scale = 1.5*(10**4)
shape = 70/scale
sd = 2
sch = 10**(-4)

limX   = [0,140]
limY   = [0,140]
limXin = [10,130]
limYin = [10,130]
x,y,v,sigma_x, sigma_y = Cox_process(M,shape,scale,sd, limXin, limYin, limX, limY, sch)
print(len(x))


# Creazione del grafico 3D
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111, projection='3d')

# Tracciamento dei dati
ax.scatter(sigma_x, sigma_y, v, c='r', marker='x')

for i in range(len(sigma_x)):
    ax.plot([sigma_x[i], sigma_x[i]], [sigma_y[i], sigma_y[i]], [0, v[i]], color='blue', linestyle='--')

plt.title("Gamma process")
#print("v", v)
#print("sigma", sigma_x, sigma_y)

plt.show()

plt.plot(x,y,"x")
plt.show()"""