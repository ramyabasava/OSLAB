def display(fr):

print("\n")

for i in range(3):

if fr[i] != -1: print(f"(fr[i]}\t", end="")

else:

print("\t", end="")

print()

def main():

fr = [-1, -1, -1] # Initialize the frame with 1 (indicating empty)

page [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 21 # Page reference string

pf = 0 # Page faults

frsize 3 #Frame size

top = 0 # Pointer for replacement

for j in range (len(page)):

flagl = 0 # Page is found in frame flag2 = 0 # Empty slot found or replacement

#Check if page is already in the frame

for i in range(frsize):

if fr[i] == page [j]:

flagl = 1

flag2 = 1

break

# If page is not already in the frame, try to insert in an empty slot

if flagl == 0:

for i in range(frsize):

if fr[i] = -1:

fr[i] = page[j]

flag2 = 1

break

# If no empty slot, replace using FIFO (circular queue)

if flag2=0:

fr [top] = page [j]

top += 1

pf += 1

if top >= frsize:

top = 0

display (fr)

print (f"Number of page faults: (pf + frsize}")

if name main":

main()