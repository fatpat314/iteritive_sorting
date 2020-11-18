# function take in a number and exponent
def raise_power(num, exp):
    # check if exponent is 1. (base case)
    if exp == 1:
        # 1 * X == X
        return num
    # exponent is not 1
    else:
        # multiply our number by the exp
        # but decrement the exponent value
        # on each recursion until base case is reached.
        return(num*raise_power(num, exp-1))

num = 4
exp = 4
solution = num ** exp
print(raise_power(num, exp))
