def is_super_digit(n):
    if n < 10: #base case, if a number is a single digit number, then the super digit is the number itself
        return n
    digit_sum = sum(int(digit) for digit in str(n)) #iterate through the number and get the sum of all digits
    return is_super_digit(digit_sum) #pass the number through the function until it reaches base case

num = int(input("Enter a number: "))

result = is_super_digit(num)
print(f"The super digit is: {result}")