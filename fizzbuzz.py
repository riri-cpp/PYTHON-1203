for each in range(1, 16):
    if each % 3 == 0 and each % 5 == 0:
        print("FizzBuzz")
    elif each % 3 == 0:
        print("Fizz")
    elif each % 5 == 0:
        print("Buzz")
    else:
        print(each)