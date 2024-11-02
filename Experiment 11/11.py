def one():
    pos = 0
    print("\nAllow one philosopher to eat at any time\n")
    for i in range(howhung):
        print(f"\nP {philname[hu[pos]]} is granted to eat")
        for x in range(pos, howhung):
            print(f"P {philname[hu[x]]} is waiting")
        pos += 1

def two():
    s = 0
    print("\nAllow two philosophers to eat at the same time\n")
    for i in range(howhung):
        for j in range(i + 1, howhung):
            if abs(hu[i] - hu[j]) >= 1 and abs(hu[i] - hu[j]) != 4:
                print(f"\n\nCombination {s + 1}")
                t = hu[i]
                r = hu[j]
                s += 1
                print(f"P {philname[hu[i]]} and P {philname[hu[j]]} are granted to eat")
                for x in range(howhung):
                    if hu[x] != t and hu[x] != r:
                        print(f"P {philname[hu[x]]} is waiting")

# Main logic
tph = int(input("\n\nDINING PHILOSOPHER PROBLEM\nEnter the total number of philosophers: "))
philname = list(range(1, tph + 1))
status = [1] * tph

howhung = int(input("How many are hungry: "))
if howhung == tph:
    print("\nAll are hungry..\nDeadlock stage will occur")
    print("Exiting")
else:
    hu = []
    for i in range(howhung):
        hu.append(int(input(f"Enter philosopher {i + 1} position: ")) - 1)
        status[hu[-1]] = 2

    while True:
        print("\n1. One can eat at a time\n2. Two can eat at a time\n3. Exit")
        cho = int(input("Enter your choice: "))
        if cho == 1:
            one()
        elif cho == 2:
            two()
        elif cho == 3:
            print("Exiting program.")
            break
        else:
            print("\nInvalid option.")
