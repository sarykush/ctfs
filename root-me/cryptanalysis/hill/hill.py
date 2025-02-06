import math
from os.path import join

################### functions ###################

# 3х3 matrix from array
def nums_to_matrix(arr):
    mass = []
    count=0
    for i in range(3):
        tmp = []
        for k in range(3):
            tmp.append(arr[count])
            count=count+1
        mass.append(tmp)
    return mass
    
# array from cipher_m element
def num_arr(arr):
    numbers_arr = []
    for i in range(9):
        for k in range(67):
            if alph[k][0] == arr[i]:
                numbers_arr.append(alph[k][1])
    return numbers_arr    

# minor matrix
def minor_matrix(arr):
    tmp=[]
    for i in range(3):
        for j in range(3):
            tmp.append(get_minor(arr,i,j))
    min_matr=nums_to_matrix(tmp)
    return min_matr

def get_minor(arr,row,col):
    tmp=[]
    for i in range(3):
        for j in range(3):
            if i!=row and j!=col:
                tmp_num=arr[i][j]
                tmp.append(tmp_num)
    minor=(tmp[0]*tmp[3])-(tmp[1]*tmp[2])
    if ((row+col)%2==1):
        minor=minor*(-1)
    return minor
  
# inverted matrix mod 67
# x**-1 mod n = x**n-2 mod n; mod = (minor*(determinant**65))%67 I GUESS this should work
def inv_matrix(arr):
    d = determinant(arr)
    minor_arr = transpose(minor_matrix(arr))
    inverse = []
    for i in range(len(arr)):
        tmp = []
        for j in range(len(arr)):
            num = (minor_arr[i][j]*(d**65)%67)
            tmp.append(num)
        inverse.append(tmp)
    return inverse

# matrix*column mod 67
def matr_col_mult(key,vect):
    res_vect = []
    for i in range(len(key)):
        res=0
        for j in range(len(key)):
            res+=(key[i][j]*vect[j])
        res_vect.append(res)
    for i in range(len(res_vect)):
        res_vect[i]=res_vect[i]%67
    return(res_vect)

# vector to string
def vect_to_string(vect):
    tmp_vect = []
    for i in range(len(vect)):
        for j in range(len(alph)):
            if alph[j][1] == vect[i]:
                tmp_vect.append(alph[j][0])
    res_string=''.join(map(str, tmp_vect))
    return res_string

# matrix functions by ThomIves: https://github.com/ThomIves/MatrixInverse
def determinant(A, total=0):
    indices = list(range(len(A)))
    
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    for fc in indices:
        As = copy_matrix(A)
        As = As[1:]
        height = len(As)
        builder = 0

        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc+1:]

        sign = (-1) ** (fc % 2)
        sub_det = determinant(As)
        total += A[0][fc] * sign * sub_det

    return total

def check_non_singular(A):
    det = determinant(A)
    if det != 0:
        return det
    else:
        raise ArithmeticError("Singular Matrix!")
        
def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have

        :returns: list of lists that form the matrix.
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M

def identity_matrix(n):
    """
    Creates and returns an identity matrix.
        :param n: the square size of the matrix

        :returns: a square identity matrix
    """
    I = zeros_matrix(n, n)
    for i in range(n):
        I[i][i] = 1.0

    return I

def copy_matrix(M):
    """
    Creates and returns a copy of a matrix.
        :param M: The matrix to be copied

        :return: The copy of the given matrix
    """
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC

def print_matrix(M):
    """
    docstring here
        :param M: The matrix to be printed
    """
    for row in M:
        print([round(x,3)+0 for x in row])

def transpose(M):
    """
    Creates and returns a transpose of a matrix.
        :param M: The matrix to be transposed

        :return: the transpose of the given matrix
    """
    rows = len(M)
    cols = len(M[0])

    MT = zeros_matrix(cols, rows)

    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]

    return MT

def matrix_multiply(A,B):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix

        :return: The product of the two matrices
    """
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        raise ArithmeticError('Number of A columns must equal number of B rows.')

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += (A[i][ii] * B[ii][j])%67
            C[i][j] = total

    return C

# let's hope it works
def decrypt(numb):
    print(f"Iteration number: {numb}")
    cipher=nums_to_matrix(numbers_arr[numb])
    inv_plain=inv_matrix(Hill_matrix)
    key=matrix_multiply(inv_plain,cipher)
    for i in range (len(key)):
        for j in range (len(key)):
            key[i][j]=key[i][j]%67
    inv_key=inv_matrix(transpose(key))
    res_vect=[]
    for i in range(len(vect_arr)):
        res_vect.append((vect_to_string(matr_col_mult(inv_key,vect_arr[i]))))
    res_string=''.join(map(str, res_vect))
    print(res_string)
#################################################

# alphabet used
alph = [['b', 0], ['0', 1], ['f', 2], ['5', 3], ['h', 4], ['L', 5], ['.', 6], ['1', 7], ['!', 8], ['G', 9], ['i', 10], ['m', 11], ['o', 12], ['8', 13], ['g', 14], ['T', 15],  ['B', 16], ['W', 17], ['R', 18], ['n', 19], ['u', 20], ['M', 21], ['S', 22], ['F', 23], ['q', 24], ['a', 25],  ['P', 26], ['t', 27], ['l', 28], ['I', 29], ['e', 30], ['E', 31], ['H', 32], ['d', 33], ['3', 34], ['A', 35], ['w', 36], ['2', 37], ['c', 38], ['j', 39], ['Q', 40], ['N', 41],  [' ', 42], ['7', 43], ['v', 44], ['Y', 45], ['s', 46], ['4', 47],  ['x', 48], ['p', 49], ['Z', 50], ['U', 51], ['O', 52], ['J', 53], ['9', 54],  ['K', 55], ['y', 56], ['C', 57], [',', 58], ['k', 59],   ['?', 60], ['r', 61], ['V', 62],  ['6', 63], ['D', 64], ['z', 65], ['X', 66]]
# ciphertext
cipher_string = "EgiMbrC7AbHOTyCiRJTU4eWlQwfgK4?fGQvzcjXBBw?NpxK6rv3OsObp?N9vjIqzHC?O9WwOT1VVtu32my2CzNNkHTozl5W,nE7Lm4rBJucP8XezREIuzgl0C7ANnn.561s9jBIYgECq!8XezREBDQ6sOG2i44iQIligvf9.Auk5hgNMuzREcjXzvPWrieWlQwfgK4km0xS?o0tuPB7VJo0t,nOwCUZAyxYyf0LvcfrIFmbPJDoAs9xaJA!cQF8?ffkln7SKO.h CVdc?JqPiAK9c8jt5Ck9ZAyrVP.y13pyC6OdvrN1dkHTseEgnDHQGEfKjBIf90KjAyFNBBwtXMaTZpbycC3HiqFp07SK44inxH5YAvEEml?CKjNQoCJwzNNbHOTyCnE7Lm4uZFCir"
# ciphertext chars array
cipher_whole=[char for char in cipher_string]

# array of strings which possibly encode 'Hill ciph'
# 3х3 matrix. The message, written in English, seems to talk about the method used.
cipher_m = []
for off in range(397):
    str_tmp = []
    for i in range(off, off+9):
        str_tmp.append(cipher_string[i])
    cipher_m.append(str_tmp)
    
# 'Hill cipher' numbers array
Hill_str = "Hill ciph"
Hill_chars = [char for char in Hill_str]
Hill_nums = []
for i in range(9):
    for k in range(67):
        if alph[k][0] == Hill_chars[i]:
            Hill_nums.append(alph[k][1])
          
# матрица Hill ciph выглядит как сифилис ей-богу
Hill_matrix=nums_to_matrix(Hill_nums)
print (Hill_matrix)

# strings from cipher_m to alphabetic numbers  
numbers_arr=[]
for i in range(len(cipher_m)):
    tmp_arr=num_arr(cipher_m[i])
    numbers_arr.append(tmp_arr)

# vectors for decoding  
vect_arr = []
off=0
for i in range(int(len(cipher_whole)/3)):
    vect_tmp = []
    for j in range(off, off+3):
        vect_tmp.append(cipher_whole[j])
    vect_arr.append(vect_tmp)
    off=off+3
for i in range(len(vect_arr)):
    for j in range(len(vect_arr[i])):
        for k in range(67):
            if alph[k][0] == vect_arr[i][j]:
                vect_arr[i][j]=alph[k][1]

for i in range(len(numbers_arr)):
    decrypt(i)

# num = (1304*(34823**65))%67 this little one right here was the guinea pig so let him stay where he is
