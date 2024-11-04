def display(fr):

print("\n")

for i in range (3):

if fr[i]

!= -1:

print(f"\tfr[i])", end="")

else: print("\t-", end="")

print()

def main():

fr = [-1, -1, -1] # Initialize the frame with 1 (indicating empty)

p [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 21 # Page reference string

fs = [0, 0, 01 # Auxiliary list for future use in page replacement

frsize 3 #Frame size

pf = 0 # Page faults

index = -1 # Index for replacement

for j in range (len(p)):

flagl = 0 # Indicates if page is already in frame

flag2= 0 # Indicates if page is placed in an empty frame slot

for i in range (frsize):

if fr[i] = p[j]:

flagl = 1

flag2 = 1

break

if flagi == 0:

for i in range(frsize):

if fr[i] == -1:

fr[i] = p[j]

break

flag2 = 1 if flag2==0: fs = [0] frsize k=j-1 for 1 in range(1, frsize): for i in range(frsize): if fr[i] = p[k]: fs[i] = 1 k = 1 for i in range(frsize): if fs[i] == 0: index = i fr [index] = p[j] pf += 1

display (fr)

print(f"\nNumber of page faults: (pf + frsize}")

name = "main":

main()