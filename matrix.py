
def transpose():
    Matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
    ]

    Placeholder_List = [] # Used to create lists

    Matrix_Transpose = [] # Transpose of matrix M

    matrix_column_element = 0
    matrix_row_element = 0

    for n in range(0, len(Matrix) * len(Matrix[0])): # Iterrate through all combinations of row * colum 
        Placeholder_List.append(Matrix[matrix_row_element][matrix_column_element])
        matrix_row_element = matrix_row_element + 1
        
        if matrix_row_element == len(Matrix):
            Matrix_Transpose.append(Placeholder_List)
            Placeholder_List = []
            matrix_column_element = matrix_column_element + 1
            matrix_row_element = 0
        
    return Matrix_Transpose

def matmul(S1, S2):
    New_Matrix = []
    Placeholder_List = []
    
    if len(S1[0]) == len(S2):
        print("Preforming Matrix Multiplication...")
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
        print(f"New Matrix: {New_Matrix}\n")
    
    else:
        print("Could not preform Matrix Multiplication")

def powers():
    List = [2, 3, 4]

    Placeholder_List = []

    start_power = 0
    end_power = 2

    Matrix = [] # Transpose of matrix M

    for list_index in range(0, len(List)):
        for power in range(start_power, end_power + 1):
            power_element = List[list_index] ** power
            Placeholder_List.append(power_element)
        Matrix.append(Placeholder_List)
        Placeholder_List = []
        
    return Matrix

def main():
    Operator = int(input("Choose 1, 2, 3, 4 For Matrix Operator:\n------------------------------------\n1: Transpose\n2: Inverse\n3: Matrix Multiplication\n4: powers\n------------------------------------\nOperator: "))
    if Operator == 1:
        New_Matrix_Transpose = transpose()
        print(f"Awnser: {New_Matrix_Transpose}")
    
    elif Operator == 3:
        New_Matrix = matmul(
            [[float(x) for x in row.split(",")] for row in input("Enter Matrix 1: ").split(";")],
            [[float(x) for x in row.split(",")] for row in input("Enter Matrix 2: ").split(";")]
        )    
        
    elif Operator == 4:
        New_Matrix = powers()
        print(f"Awnser: {New_Matrix}")     
        

if __name__ == "__main__":
    main()