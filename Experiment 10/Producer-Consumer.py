# Initialize variables
buffer = [0] * 10
bufsize = 10
in_index = 0
out_index = 0
choice = 0

while choice != 3:
    print("\n1. Produce \t 2. Consume \t3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if (in_index + 1) % bufsize == out_index:
            print("\nBuffer is Full")
        else:
            produce = int(input("Enter the value: "))
            buffer[in_index] = produce
            in_index = (in_index + 1) % bufsize

    elif choice == 2:
        if in_index == out_index:
            print("\nBuffer is Empty")
        else:
            consume = buffer[out_index]
            print(f"\nThe consumed value is {consume}")
            out_index = (out_index + 1) % bufsize

    elif choice == 3:
        print("Exiting...")

    else:
        print("Invalid choice, please choose again.")
