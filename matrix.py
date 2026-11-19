def transpose(S1): #Preforms the transpose operation of a matrix of any type

    if matrix_problem_cheacker(S1) == True:
        return []
    
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


def invert(S1): #Preforms the inverse operation on a matrix, (only takes type 2x2 matrices)
    
    if matrix_problem_cheacker(S1) == True:
        return []
    
    determinant_of_Matrix = (S1[0][0] * S1[1][1]) - (S1[0][1] * S1[1][0])
    if determinant_of_Matrix == 0:
        return "Could not preform inverse operation, determinant = 0"
    inverse_Matrix = [
        [S1[1][1]/determinant_of_Matrix, -(S1[0][1]/determinant_of_Matrix)], 
        [-(S1[1][0]/determinant_of_Matrix), S1[0][0]/determinant_of_Matrix]
    ]
    return inverse_Matrix


def matmul(S1, S2): #Preforms the matrix multiplication operation for acceptable types of matrices

    if matrix_problem_cheacker(S1) == True or matrix_problem_cheacker(S2) == True:
        return []

    New_Matrix = []
    Placeholder_List = []
        

    total_sum = 0
            
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

        
#Takes each element of a list to the power of each number in the range(start_power end_power)
def powers(L1, start_power, end_power): 
    
    if list_problem_cheacker(L1) == True:
        return []
    
    Placeholder_List = []

    Matrix = [] 
    
    for list_index in range(0, len(L1)):
        for power in range(start_power, end_power + 1):
            power_element = L1[list_index] ** power
            Placeholder_List.append(power_element)
            
        Matrix.append(Placeholder_List)
        Placeholder_List = []
                    
    return Matrix
        
#Creats a Matrix from data in an .txt file.
def loadtxt(F1):
    # Try-Except helps us raise errors without the code crashing.
    try:
        Matrix = []

        Matrix_file = open(F1, "r")

        Lines_of_file = Matrix_file.readlines()
        
        Matrix_file.close()
        
        print()

        for element in range(0, len(Lines_of_file)):
            Matrix_row = [float(x) for x in Lines_of_file[element].split()]
            Matrix.append(Matrix_row)
        return Matrix
    except FileNotFoundError:
        return "No file with the corresponding name found."
    
# These functions below cheack if the Matricies or lists are valid 
def matrix_problem_cheacker(Matrix_A):
    if len(Matrix_A) == 0:
        return True
    
    if len(Matrix_A[0]) == 0:
        return True

def list_problem_cheacker(List_A):
    if len(List_A) == 0:
        return True