
def make_matrix(number):
    
    """
        This function is used to make any number of matrix
        use this function as make_matrix(number)
        number --> The number of matrices to make
    """
    
    matrices = []
    for i in range(number):
        n = int(input("\n Enter number of rows : "))
        m = int(input("\n Enter number of columns : "))
        matrix = []
        for _ in range(n):
            a = []
            for _ in range(m):
                a.append(int(input("\n Number : ")))
            matrix.append(a)
        matrices.append(matrix)
    return matrices



def matrix_add(m1,m2):
    """
        It is used to perform addition on two matrices 
        if matrix m1 is of dimension nxm 
        and dimension of m2 is n1xm2
        then n==n1 and m==m2
    """
    add = []
    if (len(m1) == len(m2)) and (len(m1[0]) == len(m2[0])): #check number of rows and number of column
        #print(len(m1[0]),len(m2[0]))
        for i in range(len(m1)):
            a = []
            for j in range(len(m1[0])):
                a.append(m1[i][j] + m2[i][j])
            add.append(a)
        return add
    else:
        return "Dimension does not match"
