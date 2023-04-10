# FizzBuzz Program

def fizzBuzz(upTo):
    for i in range(1, upTo + 1):
        if (i % 3 == 0):
            if(i % 5 == 0):
                print("FizzBuzz")
            else:
                print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)

num = int(input("Please enter a value: "))
fizzBuzz(num)
    
    