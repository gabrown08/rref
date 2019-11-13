#rref
#version 1.3, 11/12/2019
#by Greg Brown
#11/9/2019
#practice for Daugherty University Assessment Day 11/15/2019

#rref() function calculates the rref of a matrix.

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

#bugs 1, 2, 4 were fixed by allowing for a row-swapping, column-skipping pivot counter.
#This was completed on 11/12/2019.

#import modules
import random
import datetime

#list of commands for the user
def help():
  print('enter "A = randMatrix(m, n)" to store new random m by n matrix as A')
  print('enter "A = userMatrix(m, n)" to store user-submitted m by n matrix of integers as A')
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

#stores a user defined matrix 
def userMatrix(m, n):
  #intial matrix A
  A = []

  #append each entry of matrix A
  #input must be an integer
  for i in range(m):
    print("enter each entry for row " + str(i + 1) + ' of matrix A:')
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
  print('copy-pastable:')
  print(A)
  print()

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
  print('copy-pastable:')
  print(A)
  print()

  return A



#calculates the rref of a matrix
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

      #let b be the leading coefficient of the row
      b = a[i][j] 

      #if leading term is not 0, turn it into 1, then turn every number below it into 0
      if a[i][j] != 0:
        #divide every entry in entire row by leading coefficient to create leading 1
        for h in range(len(a[0])):   
          a[i][h] = round(float(a[i][h]/b), 10)
          #round -0.0 to 0
          if a[i][h] == -0:
            a[i][h] = 0
          #round 1.0 to 1
          if a[i][h] == 1.0:
            a[i][h] = 1
        #subtract leading coefficient of row times row with leading 1 from each row below row with leading 1
        for h in range(len(a)):
          if h > i:
            b = a[h][j]
            for k in range(len(a[0])):
              a[h][k] = round(float(a[h][k] - b*a[i][k]), 9)
              #round -0 to 0
              if a[h][k] == -0:
                a[h][k] = 0
              #round 1.0 to 1
              if a[h][k] == 1.0:
                a[h][k] = 1

      #if pivot counter is at the last column, quit
      if j == len(a[0])-1:
        break
      else:
        j += 1


  #the backward phase:
  #back-substitution
  while i >= 0:
      #if leading term in each row is 1, turn every term above it into 0
      for J in range(j+1):
        if a[i][J] == 1:
          j = J
          for h in range(len(a)):
            if h < i:
              b = a[i-h-1][j]
              for k in range(len(a[0])):
                a[i-h-1][k] = round(float(a[i-h-1][k] - b*a[i][k]), 9)
                #round -0 to 0
                if a[i-h-1][k] == -0:
                  a[i-h-1][k] = 0
                #round 1.0 to 1
                if a[i-h-1][k] == 1:
                  a[i-h-1][k] = 1
          break
      i -= 1

  #print rref(matrix)
  for i in a:
    print(i)
  print()
  print('copy-pastable:')
  print(a)
  print()

  return 


#beginning command prompt
print('enter "help()" for a list of commands.')
print()