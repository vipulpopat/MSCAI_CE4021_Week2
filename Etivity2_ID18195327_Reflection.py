# **Student Name: Mark Murnane **
# 
# **Student ID: 18195326 **

# First part is to build a function that can parse an equation term for us

import re


def is_number(value):
     
    """ Simple function to determine if a string value is a number (integer or float).
     
    Args:
        value (str)    String value to be tested to see if it is numeric
         
    Returns:
        bool:          True if value is a number.  False otherwise
    """
     
    try:
        float(value)
    except ValueError:
        return False
     
    return True
     
     
def number_to_string (value):
      
    """ Simple function that takes a string representing a number and formats it for display.
     
    Integer values are returned with no decimal place.  Float values are returned rounded to 2 decimal places (no trailing zeroes).
     
    Args:
        value (str)        Value representing a number
         
    Returns:
        str                Formatted string value, or empty string if the input is not a number.
    """
      
    number_string = ''
      
    if is_number(value):
        val = float(value)
        if val.is_integer():
            number_string = str(int(val))
        else:
            number_string = str(round(val, 2))
             
    return number_string

# Need to take in text and parse it into a tuple list
# No need for a differentiate term function : use a lamba to call f'(term)
# Similar for parse funciton
# Text is handled by a print function on top of the parse function
#    Consider using the console pretty print capabilities highlighted by Fergus?
# Test assertions
# Test class with polynomials from question
# Test class with edge cases such as f'(x) where there is no x, x^1 and combination terms

def parse_term (equation_term, differential):
    """Parses a string with an algebraic term (e.g. 5x^2) and returns the coefficient and exponent parts of the term.
    
    If multiple variables are present in the term, and they have exponents, they should be separated using *.  This
    allows for multiple exponents to be present in the term.
    
    Args: 
        equation_term (str):    A string with an algebraic term (e.g. 5x^2)
        differential (str):     A single character identifying the variable of the term being differentiated.
        
    Returns:
        (tuple)                 The coefficient and exponent of the<differential part of the term
    """
    
    # Need to return (coefficient, power) and then expand to include ([coefficients], power)
    # May need to recurse in here to handle any other variable coefficients
    
    # Do the simple case first
        
    # Split the equation_term on the differential
    # Then have coefficient and power
    
    if equation_term == '' or differential == '':
        return None
    
    coefficient = exponent = 0
    
    
    # Simple case is             
    if differential not in equation_term:
        coefficient = float(equation_term)
    else:
        # Here instead of splitting on the differential, could split on the exponent value
        # May need to consider using maxsplit == 1 (differential should only appear once) and then parse term inside this
        
        components = equation_term.split(differential)              
        
        # Left part is the coefficient
        if components[0] == '':
            coefficient = 1
        else:
            coefficient = float(components[0])       
                
        # Now need to check if an exponent value was included
        if components[1] == '':
            exponent = 1
        else:
            exponent = int(components[1][1::])
    
    return (coefficient, exponent)

print ("Parsing tests ...")

print(parse_term("16x", 'x'))
print(parse_term("3x^2", 'x'))
print(parse_term('x', 'x'))
print(parse_term('12', 'x'))
print(parse_term('', 'x'))

#print(parse_term("ax^3", 'x')


def print_term(equation_term, differential):
  
    if equation_term == "" or equation_term == None:
        return ''
    elif differential == "" or equation_term == None:
        return ''
    
    coefficient, exponent = equation_term    
    
    diff_term = ''
    coefficient_str = number_to_string(coefficient)
    
    if exponent == 0:
        diff_term = "{0}".format(coefficient_str)
    else:
        if coefficient == 1:
            coefficient_str = ''
            
        if exponent == 1:
            diff_term = "{0}{1}".format(coefficient_str, differential)
        else:
            diff_term = "{0}{1}^{2}".format(coefficient_str, differential, exponent)
    
    return diff_term

print(print_term(parse_term("16x", 'x'), 'x'))
print(print_term(parse_term("3x^2", 'x'), 'x'))
print(print_term(parse_term('x', 'x'), 'x'))
print(print_term(parse_term('12', 'x'), 'x'))
print(print_term(parse_term('1', 'x'), 'x'))
print(print_term(parse_term('', 'x'), 'x'))

  
# 
# 

#     
# 
# 
# # Second part is to have a function that implements the Power Rule
# Don't need to know differentiator.  The parse functin takes care of giving back f'(x) wrt to x
def apply_power_rule(equation_term):
    """ Applies the Differential Calculus Power Rule to an algebraic term, i.e. a*x^n = (n*a)x^n-1.
     
    Args:
        equation_term (tuple)    The algebraic term (single equation element) for which the derivative is to be calculated.
        differential (str)     The variable which derivative will be calculated for
         
    Returns:
        str                    The first derivative of term with respect to the differential
    """
   
#     calculated_derivative = [0,0]
#     if power > 0:
#         calculated_derivative = [value*power, power - 1]
# 
#     return calculated_derivative 
    if equation_term == () or equation_term == None:
        return None
   
    coefficient, exponent = equation_term
    
    # If the exponent is positive, then this will be 
    if exponent > 0:
        return (coefficient * exponent, exponent - 1)
    else:
        return (0,0)

print ("\n\nPower rule tests ...")

print(apply_power_rule(parse_term("16x", 'x')))
print(apply_power_rule(parse_term("3x^2", 'x')))
print(apply_power_rule(parse_term('x', 'x')))
print(apply_power_rule(parse_term('12', 'x')))
print(apply_power_rule(parse_term('', 'x')))



# # Now for some differentiation and application of rules
# 
# # In[11]:
# 
# 
# def differentiate_term(equation_term, differential):
#     
#     """ Calculates the first derivative of an algebraic term, e.g. f'(5x^2) = 10x.
#     
#     This function currently applies the Power Rule only.
#     Future extension will be added to handle the Chain Rule also.
#     
#     Args:
#         equation_term (str)    The algebraic term (single equation element) for which the derivative is to be calculated.
#         differential (str)     The variable which derivative will be calculated for
#         
#     Returns:
#         str                    The first derivative of term with respect to the differential
#     """
#     
#     # If the differential is not here, this resolves to a constant which is always 0
#     if differential not in equation_term:
#         return ("0")
#     
#     diff_coeff, diff_exp = apply_power_rule (equation_term, differential)
#     
#     diff_term = ''
#     
#     if diff_exp == 0:
#         diff_term = "{0}".format(diff_coeff)
#     if diff_exp == 1:
#         diff_term = "{0}{1}".format(diff_coeff, differential)
#     else:
#         diff_term = "{0}{1}^{2}".format(diff_coeff, differential, diff_exp)
#     
#     return diff_term
# 
# 
# # In[12]:
def differentiate_polynomial (equation, differential):
     
    """ Calculates the first derivative of a simple polynomial equation. 
     
    The function handles basic operators such as +, -, / for division and * for multiplication.
     
    Powers should be added using the '^' symbol, e.g. x^3 is x-cubed.
     
    
    Args:
        equation (str)    An algebraic equation for which the derivative is to be calculated.
        differential (str)     The variable which derivative will be calculated for
         
    Returns:
        str                    The first derivative of the equation with respect to the differential
    """
     
    operators = re.compile("(\*|\/|\+|\-)")
       
    # Iterate over the equation
    equation_terms = re.split(operators, equation)
     
    diff_equation = ''
         
    for term in equation_terms:
        if re.match(operators, term):
            diff_equation += f' {term} '
        else:
            src_term = parse_term(term.strip(), differential)
            diff_equation += print_term(apply_power_rule(src_term), differential)
     
    return diff_equation

print ("\n\nDifferentiation tests ...")

print(differentiate_polynomial("16x", 'x'))
print(differentiate_polynomial("3x^2", 'x'))
print(differentiate_polynomial("x", 'x'))
print(differentiate_polynomial("12", 'x'))
print(differentiate_polynomial("", 'x'))
# 
# 
print(differentiate_polynomial ("x^501 + 3x^7 - 0.5x^6 + x^5 + 2x^3 + 3x^2 - 1", 'x'))
print(differentiate_polynomial ("3x^2", 'x'))
# print(differentiate_polynomial ("ax^3 + 0.5x^8", 'x'))
# print(differentiate_polynomial ("5ax^3 + 0.5x^7 - 4bx^2", 'x'))
print(differentiate_polynomial ("6x", 'x'))
print(differentiate_polynomial ("16", 'x'))
print(differentiate_polynomial('0', 'x'))
