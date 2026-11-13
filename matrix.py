import os

def transpose(S1): #Preforms the transpose operation of a matrix of any type
    try:
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
    except ValueError:
        return "Did not submit a valid Matrix"


def inverse(S1): #Preforms the inverse operation on a matrix, (only takes type 2x2 matrices)
    try:
        determinant_of_Matrix = S1[0][0] * S1[1][1] - S1[0][1] * S1[1][0]
        if determinant_of_Matrix == 0:
            return "Could not preform inverse operation, determinant = 0"
        inverse_Matrix = [
            [S1[1][1]/determinant_of_Matrix, -(S1[1][0]/determinant_of_Matrix)], 
            [-(S1[0][1]/determinant_of_Matrix), S1[0][0]/determinant_of_Matrix]
        ]
        return inverse_Matrix
    except ValueError:
        return "Did not submit a valid Matrix"

def matmul(S1, S2): #Preforms the matrix multiplication operation for acceptable types of matrices
    try:
        New_Matrix = []
        Placeholder_List = []
        
        if len(S1[0]) == len(S2):
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
            
        else:
            return "Error"
    except ValueError:
        return "Did not submit a valid Matrix"
        
#Takes each element of a list to the power of each number in the range(start_power end_power)
#Exaple:
# L1 = [1,2] , start_power = 1, end_power = 3
# => Matrix = [[1**1, 1**2, 1**3], [2**1, 2**2, 2**3]]
def powers(L1, start_power, end_power): 
    try:
        Placeholder_List = []

        Matrix = [] # Transpose of matrix M

        for list_index in range(0, len(L1)):
            for power in range(start_power, end_power + 1):
                power_element = L1[list_index] ** power
                Placeholder_List.append(power_element)
            Matrix.append(Placeholder_List)
            Placeholder_List = []
            
        return Matrix
    except ValueError:
        return "Did not submit a valid List"
        
#Creats a Matrix from data in an .txt file.
def loadtxt(F1):
    try:
        Matrix = []

        Matrix_file = open(F1, "r")

        Lines_of_file = Matrix_file.readlines()

        for element in range(0, len(Lines_of_file)):
            Matrix_row = [float(x) for x in Lines_of_file[element].split()]
            Matrix.append(Matrix_row)
        return Matrix
    except FileNotFoundError:
        return "No file with the corresponding name found."

#Gives you the options of chosing what operation to do.
def main():
    Operator = input("Choose 1, 2, 3, 4, 5 For Matrix Operator, 'Help' for Help and Q for quit:\n------------------------------------\n1: Transpose\n2: Inverse, (Only 2x2)\n3: Matrix Multiplication\n4: powers\n5: Load .txt file\nHelp: 'Help'\nExit: 'Q'\n------------------------------------\nOperator: ").upper()
    
    if Operator != "Q" and Operator != "HELP":
        # The input takes the format of a,b;c,d where a,b,c,d can be converted to float/int.
        # Example: 1,2,3;3,2,1 => [[1,2,3], [3,2,1]] and 1,2;3,4;5,6 => [[1,2], [3,4], [5,6]]
        if Operator == "1":
            print(transpose([[float(x) for x in row.split(",")] for row in input("Enter Matrix: ").split(";")]))

                    
        elif Operator == "2":
            print(inverse([[float(x) for x in row.split(",")] for row in input("Enter Matrix: ").split(";")]))
        
        elif Operator == "3":
            print(matmul(
                [[float(x) for x in row.split(",")] for row in input("Enter Matrix 1: ").split(";")],
                [[float(x) for x in row.split(",")] for row in input("Enter Matrix 2: ").split(";")]
            )) 

        # Takes a similar input as above, however just as one line
        # Example 1,2,3,4 => [1,2,3,4] and 1,2;3,2 => Error
        elif Operator == "4":
            print(powers([float(x) for x in input("Enter List: ").split(",")], int(input("Starting power: ")), int(input("Ending power: "))))
            
        # Takes the input of a files name
        elif Operator == "5":
            print(loadtxt(input("Name of file: ")))

        else:
            print("Could not process choice, please enter: 1,2,3,4, 5\n")
            main()
            
    elif Operator == "HELP":
        print("\nFormating:\nMatricis: a,b,c;d,e,f => [[a,b,c], [d,e,f]] when they are int/floats\nLists: a,b,c,d => [a,b,c,d] when they are int/floats")
        input("\nPress Enter when done: ")
        os.system("cls" if os.name == "nt" else "clear")
        main()
        
    else:
        print("Exited program")
        
# Initilizes main()
if __name__ == "__main__":
    main()
