
def do_math(number_one, number_two, operation):
    '''
    Do some math
    :param number_one: the first number
    :param number_two: the second number
    :param operation: the number representing the operation to be done
    :return: will return numberOne (operation) numberTwo
    '''
    # Initialize an empty array with five values
    answer = [None, None, None, None, None] # sum, diff, quotient, mod

    # Do all the calculations
    # If statements are too slow
    answer[0] = number_one + number_two # sum
    answer[1] = number_one - number_two # diff
    answer[2] = number_one * number_two # product
    answer[3] = round(number_one / number_two, 2) # quotient
    answer[4] = number_one % number_two # modulo

    return answer[operation - 1] # Return the operation, substract by one because arrays are 0-indexed


a = 5
b = 3

if __name__ == '__main__':
    print("Sum:\t\t" + str(do_math(a, b, 1)))
    print("Difference:\t" + str(do_math(a, b, 2)))
    print("Product:\t" + str(do_math(a, b, 3)))
    print("Quotient:\t" + str(do_math(a, b, 4)))
    print("Modulo:\t\t" + str(do_math(a, b, 5)))
