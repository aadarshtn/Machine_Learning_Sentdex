from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use("fivethirtyeight")

#xs = np.array([1,2,3,4,5,6] , dtype=np.float64)
#ys = np.array([1,3,6,6,4,7] , dtype=np.float64)

def create_dataset(hm,variance,step,correlation=False):
    val =1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance,variance)
        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step
        ys.append(y)
    xs = [i for i in range(len(ys))]
    
    return np.array(xs,dtype=np.float64),np.array(ys,dtype=np.float64)


def best_fit_slope_and_intercept(xs,ys):
    m = ((mean(xs) * mean(ys)) - mean(xs*ys))/((mean(xs)*mean(xs)) - (mean(xs*xs)))
    b = mean(ys) - m*mean(xs)
    return m , b

def squared_error(ys_orig,ys_line):
    return sum((ys_line-ys_orig)**2)

def coefficient_of_determination(ys_orig,ys_line):
    ys_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regression_line = squared_error(ys_orig,regression_line)
    squared_error_ys_mean_line = squared_error(ys_orig,ys_mean_line)
    return 1 - (squared_error_regression_line / squared_error_ys_mean_line)

xs,ys = create_dataset(50,20,1,correlation = 'pos')

m,b = best_fit_slope_and_intercept(xs,ys)
regression_line = []
for x in xs:
    regression_line.append(((m*x)+b))

r_squared = coefficient_of_determination(ys,regression_line)
print(r_squared)

plt.scatter(xs,ys)
plt.plot(regression_line)
plt.show()




