num = int(input("Enter a number: "))
odd_even = ["even" if i % 2 == 0 else "odd" for i in range(1, num + 1)]
print(odd_even)