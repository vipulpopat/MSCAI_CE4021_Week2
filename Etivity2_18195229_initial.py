# Student: Gerard Kerley ID:18195229

def get_derivative(coefficients):
    """Calculate derivate of equation where the coefficients are passed as a list.
    The exponent on x is implied by the position in the list from greatest to least.
    Args:
        param1 (list of ints): list of coefficients
    Return:
        derivatives: a list of tuples

    """
    # Reverse the coefficients list
    coefficients.reverse()
    # Create a new list to hold the derivative
    derivatives = []
    n = 0 # index counter representing the exponent
    # Iterate across each of the coefficients
    for coefficient in coefficients:
        # multiply the coefficient by the exponent
        coefficient = (coefficients[n]) * n
        # reduce the exponent by one
        exponent = n - 1
        # add the result to the derivatives list
        derivatives.append((coefficient, exponent))
        # increment the exponent counter
        n += 1
    # reverse the new list to return to original order
    derivatives.reverse()
    # discard the last element as it derives to zero
    derivatives.pop()
    # return the new list of derivatives
    return derivatives


# TESTS
# 5x^3+7x^2+3x+6 -> [5,7,3,6]
print(get_derivative([5,7,3,6]))
# expected answer 15x^2 + 14x + 3
#
# 2x^4-6x^3+3x^2+8x+9 as [2,-6,3,8,9]
print(getDerivative([2,-6,3,8,9]))
# expected answer 8x^3-18x^2+6x+8