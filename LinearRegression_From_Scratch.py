from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")

xs = np.array([1,2,3,4,5,6] , dtype=np.float64)
ys = np.array([1,3,6,6,4,7] , dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):
    m = ((mean(xs) * mean(ys)) - mean(xs*ys))/((mean(xs)*mean(xs)) - (mean(xs*xs)))
    b = mean(ys) - m*mean(xs)
    return m , b

m,b = best_fit_slope_and_intercept(xs,ys)
regression_line = []
for x in xs:
    regression_line.append(((m*x)+b))

plt.scatter(xs,ys)
plt.plot(regression_line)
plt.show()




