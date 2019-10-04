def sum(zeroDiv):
    return 45 / zeroDiv

try:
    print(sum(3))
    print(sum(5))
    print(sum(0))
    print(sum(9))
    print(sum(1))
except ZeroDivisionError:
    print('Invalid input.')
