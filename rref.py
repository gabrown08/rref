#rref

#Created by Greg Brown on 11/9/2019
#version 2.8, 3/14/2020: added ability to save matrices to hard drive and load them into program
#version 2.7, 3/8/2020: accuracy of rationals with large components fixed
#version 2.6, 3/5/2020: rref and inverse work for rationals and ints/floats
#version 2.5, 2/29/2020: added support for rational numbers
#version 2.0, 2/1/2020: added command prompt functionality

#a linear algebra program and python module with functionality to generate random matrices, define user-submitted matrices,
#transform a matrix into rref, compute the product of matrices, and more.

#TODO:make recursive determinant calculator

#TODO:class of matrices

#TODO:ability to save Rationals to database

#import modules
from rationals import Rational
import datetime
import random
import json

#list of commands for the user
def help():
  print()
  print('  ' + u"\u2588"*82)
  print('  rref will execute python commands as well as the following rref-specific commands:')
  print('  ' + u"\u2588"*82)
  print()
  print(u"\u2588"*2 + 'matrix generating functions:')
  print('  enter "I = identity(n)" to store the nxn identity matrix as I')
  print('  enter "A = matrix(m, n) to store random m by n matrix of rational whole numbers as A')
  print('  enter "A = matrix(m, n, a, b, c, d)" to store random m by n matrix of rationals\n\
    whose numerators range from a to b and denominator ranges from c to d as A')
  print('  enter "A = randMatrix(m, n)" to store random m by n matrix of integers between 0 and 9 as A')
  print('  enter "A = randMatrix(m, n, a, b)" to store random m by n matrix of integers between a and b as A')
  print('  enter "A = rationalMatrix(m,n)" to store a user-submitted m by n matrix of rationals as A')
  print('  enter "A = intMatrix(m, n)" to store user-submitted m by n matrix of integers as A')
  print('  enter "A = floatMatrix(m, n)" to store user-submitted m by n matrix of floats as A')
  print()
  print(u"\u2588"*2 + 'matrix operations:')  
  print('  enter "T = transpose(A)" to store the transpose of matrix A as matrix T')
  print('  enter "P = product(A, B)" to store the product of stored matrices A and B as new matrix P')
  print('  enter "R = rref(A)" to store the reduced row echelon form of matrix A as matrix R')
  print('  enter "B = inverse(A)" to store the inverse of matrix A as B')
  print()
  print(u"\u2588"*2 + 'other commands:')
  print('  enter "rounded(A)" to round the float or rational entries in matrix A to the nearest integer') 
  print('  enter "floated(A)" to convert rational entries of A into decimal approximations')
  print('  enter "display(A)" to display matrix A') 
  print('  enter "print(A)" to print matrix A as a list of lists')
  print('  enter "exit()" to close the program')
  print()
  print(u"\u2588"*2 + 'saving matrices:')
  print('  enter "save(A, matrixname, filename)" to save matrix matrixname to file filename in working directory')
  print('  enter "load(matrixname, filename) to load matrix matrixname from file filename')
  print('  enter "database(filename)" display all contents of database filename')
  print()
  print(u"\u2588"*2 + 'note: arguments a, b, c, d, m, n above must be integers, arguments A and B must be matrices,\n\
    and arguments matrixname and filename must be strings')
  print(u"\u2588"*2 + 'note: matrixname defaults to "untitled" and filename defaults to "matrix_database.json"')
  print()
  print('  ' + u"\u2588"*30)
  print('  rref was created by Greg Brown')
  print('  ' + u"\u2588"*30)
  print()
  return

#displays each nested list as a row
def display(A):
  for row in A:
    print(row)
  print()
  return

#round entries with scientific notation and .999999999
def rounded(A):
  for i in range(len(A)):
    for j in range(len(A[0])):
      A[i][j] = round(A[i][j])
  display(A)
  return A

#convert rational entries to floats
def floated(A):
  for i in range(len(A)):
    for j in range(len(A[0])):
      A[i][j] = A[i][j].decimal
  display(A)
  return A

#save matrix to json file
def save(A, matrix_name='untitled', file_name='matrix_database.json'):
  try:
    with open(file_name, 'r') as f:
      data = json.loads(f.read())
    try:
      data[matrix_name]
      print(f'matrix "{matrix_name}" already stored.')
    except:
      data[matrix_name] = A
      with open(file_name, 'w') as f:
        f.write(str(json.dumps(data)))    
      print(f'matrix "{matrix_name}" saved in "{file_name}".')
  except:
    data = {matrix_name:A}
    with open(file_name, 'w') as f:
      f.write(str(json.dumps(data)))
    print(f'matrix "{matrix_name}" saved in "{file_name}".')
  print()
  return

#load matrix in database into program
def load(matrix_name='untitled', file_name='matrix_database.json'):
  try:
    with open(file_name, 'r') as f:
      data = json.loads(f.read())
    try:
      A = data[matrix_name]
      display(A)
      return A
    except:
      print(f'matrix "{matrix_name}" does not exist in "{file_name}"')
  except:
    print(f'{file_name} does not exist in working directory')
  print()
  return

#display all entries in database
def database(file_name='matrix_database.json'):
  try:
    with open(file_name, 'r') as f:
      data = json.loads(f.read())
    for key in data.keys():
      print(key)
      display(data[key])
      print()
    return data
  except:
    print(f'"{file_name}" does not exist in working directory')
    print()
    return

#generates a user defined rational matrix 
def rationalMatrix(m, n):
  #intial matrix A
  A = []
  #append each entry of matrix A
  for i in range(m):
    print(f'enter each entry as "integer/integer" or just "integer" for row {str(i+1)} of matrix:')
    row = []
    for _ in range(n):
      entry = input()
      entry = entry.split('/')
      try:
        if len(entry) == 1:
          ratio = Rational(int(entry[0]))
        elif len(entry) > 1:
          ratio = Rational(int(entry[0]),int(entry[1]))
      except:
        ratio = Rational()
      row.append(ratio)
    A.append(row)
    print()
  #display matrix
  print('matrix =')
  display(A)
  return A

#generates a user defined integer matrix 
def intMatrix(m, n):
  #intial matrix A
  A = []
  #append each entry of matrix A
  for i in range(m):
    print(f'enter each entry for row {str(i+1)} of matrix:')
    row = []
    for _ in range(n):
      entry = input()
      #input must be an integer
      while type(entry) != int:
        try:
          entry = int(entry)
        except ValueError:
          entry = input("the input was not an integer. enter an integer: ")
      row.append(int(entry))
    A.append(row)
    print()
  #display matrix
  print('matrix =')
  display(A)
  return A

#generates a user defined real matrix 
def floatMatrix(m, n):
  #intial matrix A
  A = []
  #append each entry of matrix A
  for i in range(m):
    print(f'enter each entry for row {str(i+1)} of matrix:')
    row = []
    for _ in range(n):
      entry = input()
      #input must be an integer
      while type(entry) != float:
        try:
          entry = float(entry)
        except ValueError:
          entry = input("the input was not an integer. enter an integer: ")
      row.append(entry)
    A.append(row)
    print()
  #display matrix
  print('matrix =')
  display(A)
  return A

#generate a matrix with random integer entries
def randMatrix(m, n, a=0, b=9):
  #use current time to randomize seed
  time = str(datetime.datetime.now())
  #print(time)
  seed = int(time[20:26] + time[17:19] + time[14:16] \
        + time[11:13] + time[8:10] + time[5:7] + time[0:4])
  random.seed(seed)
  #print seed
  #print()
  #print('seed ', seed)
  #print()
  #generate a list of lists (matrix) with random integer entries
  A = [[random.randint(a, b) for i in range(n)] for j in range(m)]
  #print random matrix
  #print('matrix =')
  display(A)
  return A

#generate a matrix with random rational entries
def matrix(m, n, a=0, b=9, c=1, d=1):
  #use current time to randomize seed
  time = str(datetime.datetime.now())
  seed = int(time[20:26] + time[17:19] + time[14:16] \
        + time[11:13] + time[8:10] + time[5:7] + time[0:4])
  random.seed(seed)
  #generate a list of lists (matrix) with rational entries
  A = [[Rational(random.randint(a, b), random.randint(c,d)) for i in range(n)] for j in range(m)]
  #print random matrix
  display(A)
  return A

#generate nxn identity matrix
def identity(n):
  #initiate matrix
  I = [[] for i in range(n)]
  #insert 1's along main diagonal and 0's everywhere else
  for i in range(n):
    for j in range(n):
      if i == j:
        I[i].append(1)
      elif i != j:
        I[i].append(0)
  #display nxn identity matrix
  display(I)
  return I

#return the tranpose of given matrix
def transpose(A):
  m = len(A)
  n = len(A[0])
  #placeholder matrix
  B = [[0 for i in range(m)] for j in range(n)]
  #store transpose of A into placeholder matrix
  for i in range(n):
    for j in range(m):
      B[i][j] = A[j][i]
  #display transpose
  display(B)
  return B

#calculates the product of two matrices
def product(a, b):
  #check if multiplication is defined
  if len(a[0]) != len(b):
    print('multiplication undefined. dimensions mismatch.')
    print()
    return
  #store b transpose as B
  m = len(b)
  n = len(b[0])
  #placeholder matrix
  B = [[0 for i in range(m)] for j in range(n)]
  #store transpose of A into placeholder matrix
  for i in range(n):
    for j in range(m):
      B[i][j] = b[j][i]
  #calculate product of a and b by pairing rows in a with rows in b transpose (columns of b)
  product = [[sum(a*b for a, b in zip(a[i], B[j])) for j in range(len(B))] for i in range(len(a))]
  #print product matrix
  display(product)
  return product

#calculate the reduced row echelon form of a matrix
#this function will yield decimal approximation if the type of entries are ints are floats,
#and reduced fractions if the entries of the matrix are rational
def rref(A):
  #copy matrix A before transformations begin in order to preserve matrix A
  a = [[A[i][j] for j in range(len(A[i]))] for i in range(len(A))]
  #initiate pivot counter
  j = 0
  #the forward phase:
  #gaussian-elimination
  for i in range(len(a)):
      #if leading term is 0, swap the row with the next non-zero row.
      #if no non-zero leading term in rest of column, move pivot counter to next column and try again.
      while a[i][j] == 0:
        for I in range(len(a)-i):
          if a[i+I][j] != 0:
            rowSwap = a[i]
            a[i] = a[i+I]
            a[i+I] = rowSwap
            break
        #if found nonzero leading term in loop, quit and move to next part
        if a[i][j] != 0:
          break
        # if arrive at last column, quit
        if j == len(a[0])-1:
          break
        j += 1
      #if leading term is not 0, turn it into 1, then turn every number below it into 0
      if a[i][j] != 0:
        #let the leading coefficient of the row remain constant as b
        b = a[i][j]
        #divide every entry in entire row by leading coefficient to create leading 1
        for h in range(len(a[0])):   
          a[i][h] = a[i][h]/b
          #round -0.0 to 0, 1.0 to 1, 2.0 to 2, etc.
          if type(a[i][h]) is float:
            if a[i][h] == int(a[i][h]):
              a[i][h] = int(a[i][h])
        #subtract leading coefficient of row times row with leading 1 from entire row for each row below row with leading 1
        for h in range(len(a)):
          if h > i:
            b = a[h][j]
            for k in range(len(a[0])):
              a[h][k] = a[h][k] - b*a[i][k]
              #round -0.0 to 0, 1.0 to 1, 2.0 to 2, etc.
              if type(a[h][k]) is float:
                if a[h][k] == int(a[h][k]):
                  a[h][k] = int(a[h][k])
      #if pivot counter is at the last column, quit. otherwise, continue finding pivots.
      if j == len(a[0])-1:
        break
      else:
        j += 1
  #the backward phase:
  #back-substitution
  while i >= 0:
      #starting on the last row, find the leading 1, and turn every term above it into 0
      for J in range(j+1):
        if a[i][J] == 1:
          j = J
          #subtract the entry above pivot point times the entire pivot row from every row
          for h in range(len(a)):
            if h < i:
              b = a[i-h-1][j]
              for k in range(len(a[0])):
                a[i-h-1][k] = a[i-h-1][k] - b*a[i][k]
                #round -0.0 to 0, 1.0 to 1, 2.0 to 2, etc.
                if type(a[i-h-1][k]) is float:
                  if a[i-h-1][k] == int(a[i-h-1][k]):
                    a[i-h-1][k] = int(a[i-h-1][k])
          break
      i -= 1
  #print rref(matrix) only if the user did not call inverse function
  if 'inverse' not in COMMAND:
    display(a)
  return a

#calculates the inverse of a matrix
#this function will yield decimal approximation if the type of entries are ints are floats,
#and reduced fractions if the entries of the matrix are rational
def inverse(A):
  #copy matrix A before transformations begin in order to preserve matrix A
  a = [[A[i][j] for j in range(len(A[i]))] for i in range(len(A))]
  #join matrix A with identity matrix to form augmented matrix
  for i in range(len(A)):
    for j in range(len(A[i])):
      if i == j:
        a[i].append(1)
      elif i != j:
        a[i].append(0)
  #rref augmented matrix
  R = rref(a)
  #store solution to rref as new matrix
  inverse = [row[len(A):] for row in R]
  #print inverse matrix
  display(inverse)
  return inverse

#command prompt
if __name__ == '__main__':
  print()
  print(' ', u"\u2588"*47)
  print(' ', u"\u2588"*2 + ' '*43 + u"\u2588"*2)
  print(' ', u"\u2588"*2 + '   welcome to rref!' + ' '*24 + u"\u2588"*2)
  print(' ', u"\u2588"*2 + ' '*43 + u"\u2588"*2)
  print(' ', u"\u2588"*2 + '   enter "help()" for a list of commands   ' + u"\u2588"*2)
  print(' ', u"\u2588"*2 + ' '*43 + u"\u2588"*2)
  print(' ', u"\u2588"*47)
  print()
  while True:
    try:
      exec(COMMAND:=input(u"\u222B" + ' '))
    except(SystemExit, KeyboardInterrupt):
      raise
    except:
      print('error. try again.')
      print()
      pass