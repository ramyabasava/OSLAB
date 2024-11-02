def main():
    # Input the total memory available
    ms = int(input("\nEnter the total memory available (in Bytes)-- "))
    temp = ms
    mp = []
    n = 0
    ch = 'y'

    i = 0
    while ch == 'y':
        n += 1
        i += 1
        memory_required = int(input(f"\nEnter memory required for process {i} (in Bytes) -- "))
        mp.append(memory_required)

        if memory_required <= temp:
            print(f"\nMemory is allocated for Process {i}")
            temp -= memory_required
        else:
            print("\nMemory is Full")
            break

        ch = input("\nDo you want to continue(y/n) -- ").strip().lower()

    print(f"\n\nTotal Memory Available -- {ms}")
    print("\n\n\tPROCESS\t\t MEMORY ALLOCATED")
    for i in range(n):
        print(f"\n \t{i + 1}\t\t{mp[i]}")

    print(f"\n\nTotal Memory Allocated is {ms - temp}")
    print(f"Total External Fragmentation is {temp}")

if __name__ == "__main__":
    main()
