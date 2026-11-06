
def transpose(S1):

    Placeholder_List = [] # Used to create lists

    Matrix_Transpose = [] # Transpose of matrix M

    matrix_column_element = 0
    matrix_row_element = 0

    for n in range(0, len(S1) * len(S1[0])): # Iterrate through all combinations of row * colum 
        Placeholder_List.append(S1[matrix_row_element][matrix_column_element])
        matrix_row_element = matrix_row_element + 1
        
        if matrix_row_element == len(S1):
            Matrix_Transpose.append(Placeholder_List)
            Placeholder_List = []
            matrix_column_element = matrix_column_element + 1
            matrix_row_element = 0
        
    return Matrix_Transpose

def inverse(S1):
    determinant_of_Matrix = S1[0][0] * S1[1][1] - S1[0][1] * S1[1][0]
    inverse_Matrix = [[S1[1][1]/determinant_of_Matrix, -1 * S1[1][0]/determinant_of_Matrix], [-1 * S1[0][1]/determinant_of_Matrix, S1[0][0]/determinant_of_Matrix]]
    return inverse_Matrix

def matmul(S1, S2):
    New_Matrix = []
    Placeholder_List = []
    
    if len(S1[0]) == len(S2):
        total_sum = 0
        row = 0
        column = 0
        
        for row in range(0, len(S1)):
            for column in range(0, len(S2[0])):
                for element in range(0, len(S2)):
                    total_sum = total_sum + S1[row][element] * S2[element][column]
            
                Placeholder_List.append(total_sum)
                total_sum = 0
                if len(Placeholder_List) == len(S2[0]):
                    New_Matrix.append(Placeholder_List)
                    Placeholder_List = []
        return New_Matrix
    
    else:
        return "Error"

def powers(L1, start_power, end_power):
    
    Placeholder_List = []

    Matrix = [] # Transpose of matrix M

    for list_index in range(0, len(L1)):
        for power in range(start_power, end_power + 1):
            power_element = L1[list_index] ** power
            Placeholder_List.append(power_element)
        Matrix.append(Placeholder_List)
        Placeholder_List = []
        
    return Matrix

def loadtxt(F1):
    Matrix = []

    Matrix_file = open(F1, "r")

    Lines_of_file = Matrix_file.readlines()

    for element in range(0, len(Lines_of_file)):
        Matrix_row = [float(x) for x in Lines_of_file[element].split()]
        Matrix.append(Matrix_row)
    return Matrix

def main():
    Operator = int(input("Choose 1, 2, 3, 4 For Matrix Operator:\n------------------------------------\n1: Transpose\n2: Inverse, (Only 2x2)\n3: Matrix Multiplication\n4: powers\n5: Load .txt file\n------------------------------------\nOperator: "))
    
    if Operator == 1:
        print(transpose([[float(x) for x in row.split(",")] for row in input("Enter Matrix: ").split(";")]))
                
    elif Operator == 2:
        print(inverse([[float(x) for x in row.split(",")] for row in input("Enter Matrix: ").split(";")]))
    
    elif Operator == 3:
        print(matmul(
            [[float(x) for x in row.split(",")] for row in input("Enter Matrix 1: ").split(";")],
            [[float(x) for x in row.split(",")] for row in input("Enter Matrix 2: ").split(";")]
        )) 
        
    elif Operator == 4:
        print(powers([float(x) for x in input("Enter List: ").split(",")], int(input("Starting power: ")), int(input("Ending power: "))))
        
    elif Operator == 5:
        print(loadtxt(input("Name of file: ")))

if __name__ == "__main__":
    main()
    
    
'''
[[], []]
'''
