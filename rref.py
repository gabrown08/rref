#rref
#version 1.0
#by Greg Brown
#11/9/2019

#rref() function calculates the rref of a matrix
#works for linearly independent rows

#import modules
import random
import datetime

def help():
  print('enter "A = randMatrix(m, n)" to store new random m by n matrix A')
  print('enter "A = userMatrix(m, n)" to store user-submitted m by n matrix of integers A')
  print('enter "rref(A)" to convert matrix A into row echelon form')
  print('enter "display(A)" to display matrix A')
  print()
  return

def display(a):
  for i in a:
    print(i)
  print()
  return


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

  print('matrix =')
  for i in A:
    print(i)
  print()
  print('copy-pastable:')
  print(A)
  print()

  return A


def randMatrix(m, n):
  #use current time to randomize seed
  time = str(datetime.datetime.now())
  seed = int(time[17:19] + time[14:16] + time[11:13] + time[8:10] + time[5:7] + time[0:4])
  random.seed(seed)

  #print seed
  print()
  print('seed ', seed)
  print()

  #generate a random m by n matrix as a
  A = [[random.randint(0, 9) for i in range(n)] for j in range(m)]

  #print a
  print('matrix =')
  for i in A:
	  print(i)
  print()
  print('copy-pastable:')
  print(A)
  print()

  return A


def rref(a):
  #pivot counter
  j = 0
  
  #gaussian-elimination
  for i in range(len(a)):
      b = a[i][j]  
      if a[i][j] != 0:
        for h in range(len(a[0])):   
          a[i][h] = round(a[i][h]/b, 10)
        for h in range(len(a)):
          if h > i:
            b = a[h][j]
            for k in range(len(a[0])):
              a[h][k] = round(a[h][k] - b*a[i][k], 8)
      j += 1
  
  #undo last increment
  j -= 1

  #debug printing
  #print(i)
  #print(j)

  #back-substitution
  for I in range(len(a)):
      for h in range(len(a)):
        if h < i:
          b = a[i-h-1][j]
          for k in range(len(a[0])):
            a[i-h-1][k] = round(a[i-h-1][k] - b*a[i][k], 8)
      j -= 1
      i -= 1

  for i in a:
    print(i)
  print()
  print('copy-pastable:')
  print(a)
  print()

  return 


print('enter "help()" for a list of commands.')
print()
