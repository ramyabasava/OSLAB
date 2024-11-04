class Directory:
    def __init__(self):
        self.dname = ""
        self.fname = []
        self.fcnt = 0

dir = Directory()

def create_file():
    file_name = input("Enter the name of the file -- ")
    dir.fname.append(file_name)
    dir.fcnt += 1

def delete_file():
    file_name = input("Enter the name of the file -- ")
    if file_name in dir.fname:
        dir.fname.remove(file_name)
        dir.fcnt -= 1
        print(f"File {file_name} is deleted")
    else:
        print(f"File {file_name} not found")

def search_file():
    file_name = input("Enter the name of the file -- ")
    if file_name in dir.fname:
        print(f"File {file_name} is found")
    else:
        print(f"File {file_name} not found")

def display_files():
    if dir.fcnt == 0:
        print("\nDirectory Empty")
    else:
        print("\nThe Files are -- ")
        for file in dir.fname:
            print(f"\t{file}")

def main():
    dir.dname = input("Enter name of directory -- ")

    while True:
        print("\n\n1. Create File\t2. Delete File\t3. Search File\n4. Display Files\t5. Exit")
        choice = int(input("Enter your choice -- "))

        if choice == 1:
            create_file()
        elif choice == 2:
            delete_file()
        elif choice == 3:
            search_file()
        elif choice == 4:
            display_files()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
