
# coding: utf-8

# **Student Name: Mark Murnane **
# 
# **Student ID: 18195326 **

# First part is to build a function that can parse an equation term for us

# In[8]:


import re

def parse_term (equation_term, differential):
    """Parses a string with an algebraic term (e.g. 5x^2) and returns the coefficient and exponent parts of the term.
    
    If multiple variables are present in the term, and they have exponents, they should be separated using *.  This
    allows for multiple exponents to be present in the term.
    
    Args: 
        equation_term (str):    A string with an algebraic term (e.g. 5x^2)
        differential (str):     A single character identifying the variable of the term being differentiated.
        
    Returns:
        (tuple) The coefficient and exponent of the<differential part of the term
    """
    
    # TODO: Some test assesertions and parameter checking
    equation_term
    
    
    if differential not in equation_term:
        coefficient = equation_term
        exponent = 0
    else:
        components = equation_term.split(differential)
        coefficient = components[0]
        exponent = components[1][1:]            # Strip off the exponent
    
    return (coefficient, int(exponent))  


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
    


# Second part is to have a function that implements the Power Rule

def apply_power_rule(equation_term, differential):
    """ Applies the Differential Calculus Power Rule to an algebraic term, e.g. f'(5x^2) = 10x.
    
    Args:
        equation_term (str)    The algebraic term (single equation element) for which the derivative is to be calculated.
        differential (str)     The variable which derivative will be calculated for
        
    Returns:
        str                    The first derivative of term with respect to the differential
    """
    
    components = parse_term(equation_term, differential)
    
    coefficient = ''
    exponent = components[1]    
    
    # Handle the different possibilities
    #  a) No existing coefficient
    #  b) A numeric co-efficient
    #  c) A composite co-efficient
    if not components[0]:
        coefficient = exponent    
    elif is_number(components[0]):
        coefficient = number_to_string(float(components[0]) * exponent)
    else:
        numeric_coefficient = 1.0

        parts = re.split("([a-z]+)", components[0])
        for coeff_part in parts:                
            if is_number(coeff_part):
                numeric_coefficient = float(coeff_part) * exponent
            else:
                coefficient += coeff_part
             
        # If there were no constants in the coefficient then still need to add in the (exponent - 1) 
        if numeric_coefficient == 1.0:
            numeric_coefficient *= exponent
            
        coefficient = number_to_string(numeric_coefficient) + coefficient
                                
    exponent -= 1
    
    return (coefficient, exponent)


# Now for some differentiation and application of rules

# In[11]:


def differentiate_term(equation_term, differential):
    
    """ Calculates the first derivative of an algebraic term, e.g. f'(5x^2) = 10x.
    
    This function currently applies the Power Rule only.
    Future extension will be added to handle the Chain Rule also.
    
    Args:
        equation_term (str)    The algebraic term (single equation element) for which the derivative is to be calculated.
        differential (str)     The variable which derivative will be calculated for
        
    Returns:
        str                    The first derivative of term with respect to the differential
    """
    
    # If the differential is not here, this resolves to a constant which is always 0
    if differential not in equation_term:
        return ("0")
    
    diff_coeff, diff_exp = apply_power_rule (equation_term, differential)
    
    diff_term = ''
    
    if diff_exp == 0:
        diff_term = "{0}".format(diff_coeff)
    if diff_exp == 1:
        diff_term = "{0}{1}".format(diff_coeff, differential)
    else:
        diff_term = "{0}{1}^{2}".format(diff_coeff, differential, diff_exp)
    
    return diff_term


# In[12]:
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
            diff_equation += differentiate_term(term.strip(), differential)
    
    return diff_equation


print(differentiate_polynomial ("x^501 + 3x^7 - 0.5x^6 + x^5 + 2x^3 + 3x^2 - 1", 'x'))
print(differentiate_polynomial ("3x^2", 'x'))
print(differentiate_polynomial ("ax^3 + 0.5x^8", 'x'))
print(differentiate_polynomial ("5ax^3 + 0.5x^7 - 4bx^2", 'x'))
