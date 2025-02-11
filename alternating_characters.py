first_character = input("First Character: ")
second_character = input("Second Character: ")
size = int(input("Enter size: "))

for x in range(1, size + 1):
    print ("-" * (x - 1), end="")
    if x % 2 != 0:
        print(first_character)
    else:
        print(second_character)
