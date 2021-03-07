def fizzBuzz():
    output = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            output.append('Fizz')
            print('Fizz')

        elif i % 3 != 0 and i % 5 == 0:
            output.append('Buzz')
            print('Buzz')

        elif i % 3 == 0 and i % 5 == 0:
            output.append('FizzBuzz')
            print('FizzBuzz')
            
        else:
            output.append(i)
            print(i)

    return output