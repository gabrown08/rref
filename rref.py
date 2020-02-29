#rref
#Created by Greg Brown on 11/9/2019
#version 2.5, 2/29/2020: added support for rational numbers
#version 2.0, 2/1/2020: added command prompt functionality

#a linear algebra program and python module with functionality to generate random matrices, define user-submitted matrices,
#transform a matrix into rref, compute the product of matrices, and more

#import modules
from rationals import *
import datetime
import random

#list of commands for the user
def help():
  print()
  print('welcome to rref version 2.0, a linear algebra command line suite.')
  print()
  print('rref will execute python commands as well as the following rref-specific commands:')
  print()
  print('enter "I = identity(n)" to store the nxn identity matrix as I')
  print('enter "A = Matrix(m, n)" to store random m by n matrix of rationals as A')
  print('enter "A = randMatrix(m, n)" to store random m by n matrix of integers between 0 and 9 as A')
  print('enter "A = randMatrix(m, n, a, b)" to store random m by n matrix of integers between a and b as A')
  print('enter "A = intMatrix(m, n)" to store user-submitted m by n matrix of integers as A')
  print('enter "A = floatMatrix(m, n)" to store user-submitted m by n matrix of floats as A')
  print('enter "T = transpose(A)" to store the transpose of matrix A as matrix T')
  print('enter "P = product(A, B)" to store the product of stored matrices A and B as new matrix P')
  print('enter "R = rref(A)" to store the reduced row echelon form of matrix A as matrix R')
  print('enter "R = rref2(A)" to store reduced row echelon form of matrix of rationals A as R')
  print('enter "B = inverse(A)" to store the inverse of matrix A as B')
  print('enter "B = inverse2(A)" to store the inverse of matrix of rationals A as B')
  print('enter "display(A)" to display matrix A')
  print('enter "print(A)" to print matrix A as a list of lists')
  print('enter "exit()" to close the program')
  print()
  print('note: arguments a, b, m, n above must be integers and arguments A and B must be matrices.')
  print()
  print('rref was created by Greg Brown')
  print()
  return

#displays each nested list as a row
def display(A):
  for row in A:
    print(row)
  print()
  return
  
#generates a user defined rational matrix 
def matrix(m, n):
  #intial matrix A
  A = []
  #append each entry of matrix A
  for i in range(m):
    print(f'enter each entry as "integer/integer" or just "integer" for row {str(i+1)} of matrix:')
    row = []
    for _ in range(n):
      entry = input()
      entry = entry.split('/')
      if len(entry) == 1:
        ratio = Rational(int(entry[0]))
      if len(entry) == 2:
        ratio = Rational(int(entry[0]),int(entry[1]))
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

#generate a matrix with random integer entries
def Matrix(m, n, a=0, b=9, c=1, d=9):
  #use current time to randomize seed
  time = str(datetime.datetime.now())
  #print(time)
  seed = int(time[20:26] + time[17:19] + time[14:16] \
        + time[11:13] + time[8:10] + time[5:7] + time[0:4])
  random.seed(seed)
  #generate a list of lists (matrix) with rational entries
  A = [[Rational(random.randint(a, b), random.randint(c,d)).reduced() for i in range(n)] for j in range(m)]
  #print random matrix
  #print('matrix =')
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

#transform matrix into reduced row echelon form
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
          a[i][h] = round(float(a[i][h]/b), 10)
          #round -0.0 to 0, 1.0 to 1, 2.0 to 2, etc.
          if a[i][h] == int(a[i][h]):
            a[i][h] = int(a[i][h])
        #subtract leading coefficient of row times row with leading 1 from entire row for each row below row with leading 1
        for h in range(len(a)):
          if h > i:
            b = a[h][j]
            for k in range(len(a[0])):
              a[h][k] = round(float(a[h][k] - b*a[i][k]), 9)
              #round -0.0 to 0, 1.0 to 1, 2.0 to 2, etc.
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
                a[i-h-1][k] = round(float(a[i-h-1][k] - b*a[i][k]), 9)
                #round -0.0 to 0, 1.0 to 1, 2.0 to 2, etc.
                if a[i-h-1][k] == int(a[i-h-1][k]):
                  a[i-h-1][k] = int(a[i-h-1][k])
          break
      i -= 1
  #print rref(matrix)
  display(a)
  return a

#transform matrix into reduced row echelon form
def rref2(A):
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
          if not isinstance(a[i][h], Rational):
            a[i][h] = round(a[i][h], 9)
            #round -0.0 to 0, 1.0 to 1, 2.0 to 2, etc.
            if a[i][h] == int(a[i][h]):
              a[i][h] = int(a[i][h])
        #subtract leading coefficient of row times row with leading 1 from entire row for each row below row with leading 1
        for h in range(len(a)):
          if h > i:
            b = a[h][j]
            for k in range(len(a[0])):
              a[h][k] = a[h][k] - b*a[i][k]
              if not isinstance(a[h][k], Rational):
                a[h][k] = round(a[h][k], 9)
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
                if not isinstance(a[i-h-1][k], Rational):
                  a[i-h-1][k] = round(a[i-h-1][k], 9)
                #round -0.0 to 0, 1.0 to 1, 2.0 to 2, etc.
                  if a[i-h-1][k] == int(a[i-h-1][k]):
                    a[i-h-1][k] = int(a[i-h-1][k])
          break
      i -= 1
  #print rref(matrix)
  display(a)
  return a

#calculates the inverse of a matrix
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
  #display augmented matrix
  display(a)
  #rref augmented matrix
  R = rref(a)
  #store solution to rref as new matrix
  inverse = [row[len(A):] for row in R]
  #print inverse matrix
  display(inverse)
  return inverse

  #calculates the inverse of a matrix
def inverse2(A):
  #copy matrix A before transformations begin in order to preserve matrix A
  a = [[A[i][j] for j in range(len(A[i]))] for i in range(len(A))]
  #join matrix A with identity matrix to form augmented matrix
  for i in range(len(A)):
    for j in range(len(A[i])):
      if i == j:
        a[i].append(Rational(1))
      elif i != j:
        a[i].append(Rational(0))
  #display augmented matrix
  display(a)
  #rref augmented matrix
  R = rref2(a)
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
      exec(input(u"\u222B" + ' '))
    except(SystemExit, KeyboardInterrupt):
      raise
    #except:
    #  pass

#TODO:
#create/modify rref algorithm for rational numbers

#TODO:
#make recursive determinant calculator

#TODO:
#read and write matrices from json and/or txt file in working directory