import sys # sys.argv[1] takes the argument after the file name: "python .\native_regression.py hej", "hej" == sys.argv[1]
import matplotlib.pylab as plt
from numpy import *

def powers(L1, start_power, end_power): 
    
    if len(L1) == 0:
        return array([])
    
    Placeholder_List = []

    Matrix = []
    
    for list_index in range(0, len(L1)):
        for power in range(start_power, end_power + 1):
            power_element = L1[list_index] ** power
            Placeholder_List.append(power_element)
            
        Matrix.append(Placeholder_List)
        Placeholder_List = []
                    
    return array(Matrix)

def poly(a,x):
    polynomial = 0
    power = 0
   
    # Calculates a polynomial of type: y = a_0 + a_1 * x + a_2 * x ** 2 + ... + a_n * x ** n
    for koefficients in a:
        polynomial = polynomial + koefficients * x ** power
        power = power + 1
    return polynomial
    
def numpy_plot():
        
    X = [] # Temperature values
    Y = []
    Y2 = []

    n = int(sys.argv[2]) # Polynomial degree

    file_info = loadtxt(sys.argv[1])

    for x_value in file_info:
        X.append(x_value[0])
        
    for y_value in file_info:
        Y.append(y_value[1])

    points = (X[-1] - X[0])/0.2

    X2 = linspace(int(X[0]), int(X[-1]), int(points)).tolist()

    Xp  = powers(X,0,n)
    Yp  = powers(Y,1,1)
    Xpt = Xp.transpose()

    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]

    for x in X2:
        Y2.append(poly(a,x))

    plt.plot(X,Y,'ro')
    plt.plot(X2,Y2)
    plt.show()
    
if __name__ == "__main__":
    numpy_plot()