#rref calculator
#version 1.4, 11/30/2019
#Created by Greg Brown on 11/9/2019


#use "A = randMatrix(m, n)" to store a random m by n matrix of integers as A,
#or just type the nested lists manually.
#then enter "rref(A)" to display the rref of the matrix.


#import modules
import random
import datetime


#list of commands for the user
def help():
  print('enter "A = randMatrix(m, n)" to store new random m by n matrix as A')
  print('enter "A = userMatrix(m, n)" to store user-submitted m by n matrix of integers as A')
  print('enter "A = realUserMatrix(m, n)" to store user-submitted m by n matrix of floats as A')
  print('enter "P = product(A, B)" to store the product of stored matrices A and B as new matrix P')
  print('enter "rref(A)" to transform matrix A into row echelon form')
  print('enter "display(A)" to display matrix A')
  print()
  return


#displays each nested list as a row
def display(a):
  for i in a:
    print(i)
  print()
  return


#generates a user defined integer matrix 
def userMatrix(m, n):
  #intial matrix A
  A = []

  #append each entry of matrix A
  #input must be an integer
  for i in range(m):
    print("enter each entry for row " + str(i + 1) + ' of matrix:')
    row = []
    for j in range(n):
        entry = input()
        while type(entry) != type(1):
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
  for i in A:
    print(i)
  print()
  #print('copy-pastable:')
  #print(A)
  #print()

  return A


#generates a user defined real matrix 
def realUserMatrix(m, n):
  #intial matrix A
  A = []

  #append each entry of matrix A
  #input must be an integer
  for i in range(m):
    print("enter each entry for row " + str(i + 1) + ' of matrix:')
    row = []
    for j in range(n):
        entry = input()
        while type(entry) != type(1.1):
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
  for i in A:
    print(i)
  print()
  #print('copy-pastable:')
  #print(A)
  #print()

  return A


#generate a matrix with random integer entries
def randMatrix(m, n):
  #use current time to randomize seed
  time = str(datetime.datetime.now())
  seed = int(time[17:19] + time[14:16] + time[11:13] + time[8:10] + time[5:7] + time[0:4])
  random.seed(seed)

  #debug code
  #print seed
  #print()
  #print('seed ', seed)
  #print()

  #generate a list of lists (matrix) with random integer entries
  A = [[random.randint(0, 9) for i in range(n)] for j in range(m)]

  #print random matrix
  #print('matrix =')
  for i in A:
	  print(i)
  print()
  #print('copy-pastable:')
  #print(A)
  #print()

  return A


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
  for i in product:
	  print(i)
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
  for i in a:
    print(i)
  print()
  #print('copy-pastable:')
  #print(a)
  #print()

  return 


#beginning command prompt
print('enter "help()" for a list of commands.')
print()




#practice for Daugherty University Assessment Day 11/15/2019

#known bugs:
#need error handling to ensure arguments in matrix generating functions are integers

#fixed bugs:
#1. domain error if number of rows greater than number of columns fixed 11/12/19
#2. if free variables between pivot points, only calculates ref not rref.
#   fixed by comletely changing the way that the pivot counter moves on 11/12/19
#3. does not round some infinitesimally small negative differences from -0 to just 0
#   technically -0 and 0 are the same, so it is still correct, it just doesn't look nice
#   fixed 11/12/19
#4. error if very first entry is 0 fixed 11/11/19 by adding first version of row-swapping

#***bugs 1, 2, 4 were fixed by allowing for a row-swapping, column-skipping pivot counter.
#This was completed on 11/12/2019.