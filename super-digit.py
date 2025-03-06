def super_digit(n):
    if n < 10:
        return n
    digit_sum = sum(int(digit) for digit in str(n))
    return super_digit(digit_sum)

num = input("Enter a number: ")

if num.isdigit() and len(num) <= 18:
    num = int(num)
    result = super_digit(num)
    print(f"{result} is the super digit.")
else:
    print("Invalid input.")
