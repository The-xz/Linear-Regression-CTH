import sys # sys.argv[1] takes the argument after the file name: "python .\native_regression.py hej", "hej" == sys.argv[1]
import matplotlib.pylab as plt
from matrix import *

def native_plot():
    X = []
    Y = []
    Y2 =[]

    file_info = loadtxt(sys.argv[1])


    for x_value in file_info:
        X.append(x_value[0])
        
    for y_value in file_info:
        Y.append(y_value[1])

    Xp = powers(X,0,1)
    Yp = powers(Y,1,1)
    Xpt = transpose(Xp)

    [[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    
    for x in X:
        Y2.append(b + m * x)

    plt.plot(X,Y,"ro")
    plt.plot(X,Y2) 
    plt.show()
    
if __name__ == "__main__":
    native_plot()