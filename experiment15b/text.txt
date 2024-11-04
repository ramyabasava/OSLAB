class Directory:
    def __init__(self, dname):
        self.dname = dname
        self.fname = []
        self.fcnt = 0

def main():
    dirs = []
    dcnt = 0

    while True:
        print("\n\n1. Create Directory\t2. Create File\t3. Delete File")
        print("4. Search File\t\t5. Display\t6. Exit")
        ch = int(input("Enter your choice -- "))

        if ch == 1:
            dname = input("\nEnter name of directory -- ")
            dirs.append(Directory(dname))
            dcnt += 1
            print("Directory created")

        elif ch == 2:
            d = input("\nEnter name of the directory -- ")
            for dir in dirs:
                if dir.dname == d:
                    f = input("Enter name of the file -- ")
                    dir.fname.append(f)
                    dir.fcnt += 1
                    print("File created")
                    break
            else:
                print(f"Directory {d} not found")

        elif ch == 3:
            d = input("\nEnter name of the directory -- ")
            for dir in dirs:
                if dir.dname == d:
                    f = input("Enter name of the file -- ")
                    for k in range(dir.fcnt):
                        if dir.fname[k] == f:
                            print(f"File {f} is deleted")
                            dir.fcnt -= 1
                            dir.fname.pop(k)
                            break
                    else:
                        print(f"File {f} not found")
                    break
            else:
                print(f"Directory {d} not found")

        elif ch == 4:
            d = input("\nEnter name of the directory -- ")
            for dir in dirs:
                if dir.dname == d:
                    f = input("Enter the name of the file -- ")
                    if f in dir.fname:
                        print(f"File {f} is found")
                    else:
                        print(f"File {f} not found")
                    break
            else:
                print(f"Directory {d} not found")

        elif ch == 5:
            if dcnt == 0:
                print("\nNo Directories")
            else:
                print("\nDirectory\tFiles")
                for dir in dirs:
                    print(f"\n{dir.dname}\t\t", end="")
                    for f in dir.fname:
                        print(f"\t{f}", end="")
                print()

        elif ch == 6:
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
