#rref
#Created by Greg Brown on 11/9/2019
#version 2.0, 2/1/2020: added command prompt functionality
#version 1.5, 1/29/2020

#a linear algebra program and python module with functionality to generate random matrices, define user-submitted matrices,
#transform a matrix into rref, compute the product of matrices, and more

#import modules
import random
import datetime

#list of commands for the user
def help():
  print()
  print('welcome to rref version 2.0, a linear algebra command line suite')
  print()
  print('enter "A = randMatrix(m, n)" to store new random m by n matrix of integers as A')
  print('enter "A = userMatrix(m, n)" to store user-submitted m by n matrix of integers as A')
  print('enter "A = realUserMatrix(m, n)" to store user-submitted m by n matrix of floats as A')
  print('enter "P = product(A, B)" to store the product of stored matrices A and B as new matrix P')
  print('enter "T = transpose(A)" to store the transpose of matrix A as matrix T')
  print('enter "rref(A)" to transform matrix A into reduced row echelon form')
  print('enter "display(A)" to display matrix A')
  print('enter "A" to print matrix A as a list of lists')
  print()
  return

#displays each nested list as a row
def display(A):
  for row in A:
    print(row)
  print()
  return

#generates a user defined integer matrix 
def userMatrix(m, n):
  #intial matrix A
  A = []
  #append each entry of matrix A
  for i in range(m):
    print("enter each entry for row " + str(i + 1) + ' of matrix:')
    row = []
    for j in range(n):
        entry = input()
        #input must be an integer
        while type(entry) != int:
            try:
                entry = int(entry)
            except ValueError:
                print()
                print("error: the input was not an integer. enter an integer.")
                entry = input()
        row.append(int(entry))
    A.append(row)
    print()
  #display matrix
  print('matrix =')
  for row in A:
    print(row)
  print()
  return A

#generates a user defined real matrix 
def realUserMatrix(m, n):
  #intial matrix A
  A = []
  #append each entry of matrix A
  for i in range(m):
    print("enter each entry for row " + str(i + 1) + ' of matrix:')
    row = []
    for j in range(n):
        entry = input()
        #input must be an integer
        while type(entry) != float:
            try:
                entry = float(entry)
            except ValueError:
                print()
                print("error: the input was not a number. enter a number.")
                entry = input()
        row.append(entry)
    A.append(row)
    print()
  #display matrix
  print('matrix =')
  for row in A:
    print(row)
  print()
  return A

#generate a matrix with random integer entries
def randMatrix(m, n):
  #use current time to randomize seed
  time = str(datetime.datetime.now())
  seed = int(time[17:19] + time[14:16] + time[11:13] + time[8:10] + time[5:7] + time[0:4])
  random.seed(seed)
  #print seed
  #print()
  #print('seed ', seed)
  #print()
  #generate a list of lists (matrix) with random integer entries
  A = [[random.randint(0, 9) for i in range(n)] for j in range(m)]
  #print random matrix
  #print('matrix =')
  for row in A:
    print(row)
  print()
  return A

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
  for row in B:
    print(row)
  print()
  return B

#calculates the product of two matrices
def product(a, b):
  #check if multiplication is defined
  if len(a[0]) != len(b):
    print('multiplication undefined. dimensions mismatch.')
    print()
    return
  #store number of columns of each matrix
  n = len(a[0])
  p = len(b[0])
  #generate blank matrix for b transpose
  B = [[0 for i in range(n)] for j in range(p)]
  #generate b transpose
  for i in range(p):
	  for j in range(n):
		  B[i][j] = b[j][i]				
  #calculate product of a and b by pairing rows in a with rows in b transpose (columns of b)
  product = [[sum([a * b for a, b in zip(a[i], B[j])]) for j in range(len(B))] for i in range(len(a))]
  #print product matrix
  for row in product:
    print(row)
  print()
  return product

#transform matrix into reduced row echelon form
def rref(a):
  #initiate pivot counter
  j = 0
  #the forward phase:
  #gaussian-elimination
  for i in range(len(a)):
      #if leading term is 0, swap the row with the next non-zero row, if no non zero leading term in rest of column, move pivot counter to next column and try again.
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
  for row in a:
    print(row)
  print()
  return a

#command prompt
if __name__ == '__main__':
  print()
  print(' ', u"\u2588"*47)
  print(' ', u"\u2588"*2 + ' '*43 + u"\u2588"*2)
  print(' ', u"\u2588"*2 + '   welcome to rref!' + ' '*8 +'by Greg Brown   ' + u"\u2588"*2)
  print(' ', u"\u2588"*2 + ' '*43 + u"\u2588"*2)
  print(' ', u"\u2588"*2 + '   enter "help()" for a list of commands   ' + u"\u2588"*2)
  print(' ', u"\u2588"*2 + ' '*43 + u"\u2588"*2)
  print(' ', u"\u2588"*47)
  print()
  while True:
    try:
      exec(input(u"\u222B" + ' '))
    except(SystemExit):
      raise
    except:
      pass

#TODO:
#create a class of objects called rational numbers, define operations using dunder methods, create rref algorithm for rational numbers
#will require gcd function to reduce fractions

#TODO:
#make recursive determinant function and a matrix inverse calculator

#TODO:
#read and write matrices from json and/or txt file in working directory

#TODO:
#need error handling to ensure arguments in matrix generating functions are integers