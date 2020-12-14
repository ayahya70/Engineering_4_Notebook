from math import sqrt  # you need to import math to be able to square root

# greeting messages
print("Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + c + = 0")


# finding the discriminat given the coefficants
def find_discriminant(a, b, c):
    return b ** 2 - (4 * a * c)


# given roots
def solve(a, b, c):
    roots = [None, None]
    roots[0] = (-b + sqrt(find_discriminant(a, b, c))) / (2 * a)
    roots[1] = (-b - sqrt(find_discriminant(a, b, c))) / (2 * a)
    return roots


# allows to input numbers
user_a = int(input("a: "))
user_b = int(input("b: "))
user_c = int(input("c: "))
# made a variable so i dont have to type that really long word
discriminant = find_discriminant(user_a, user_b, user_c)
#  if its zero then its not reall if it is then solve
if discriminant < 0:
    print("No real roots")
else:
    print(solve(user_a, user_b, user_c))
