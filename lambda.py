n = int(input("Enter number of elements: "))
elements = [int(input(f"Element {i + 1}: "))for i in range(n)]
minimum_element = (lambda lst: min(lst))(elements) #takes a list (lst) as the input, returns the minimum of that list min(lst), and uses the elements list as the parameter
print(f"Max element: {minimum_element}")