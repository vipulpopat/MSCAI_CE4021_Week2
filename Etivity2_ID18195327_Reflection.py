import re
import unittest

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

def parse_term (equation_term, differential):
    """Parses a string with an algebraic term (e.g. 5x^2) and returns the coefficient and exponent parts of the term.
    
    Args: 
        equation_term (str):    A string with an algebraic term (e.g. 5x^2)
        differential (str):     A single character identifying the variable of the term being differentiated.
        
    Returns:
        (tuple)                 The coefficient and exponent of the<differential part of the term
    """
   
    if equation_term == '' or differential == '':
        return None
    
    components = equation_term.split(differential)      
    coefficient = exponent = 0
      
    if differential not in equation_term:
        coefficient = float(equation_term)
    else:
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

def print_term(equation_term, differential):

    """Formats a polynomial algebraic term from it's tuple representation into a string.
    
    Args:
        equation_term        Tuple containing the (coefficient, exponent) of the term.
        differential (str)   The variable in the polynomial term.
        
    Returns:   
        (str)                The formatted string <coefficient><differential>^<exponent>."""
  
    if equation_term == None or differential == None:
        return ''
    
    coefficient, exponent = equation_term        # Unpacks the tuple
    diff_term = ''
    
    coefficient_str = number_to_string(coefficient)

    # If there is no exponent, then just print the coefficient.  O
    # Otherwise format the string with the coefficient and exponent (both only if > 1)    
    if exponent == 0:
        diff_term = "{0}".format(coefficient_str)
    else:
        diff_term = str(differential)        
        if coefficient > 1:
            diff_term = "{0}{1}".format(coefficient_str, diff_term)
            
        if exponent > 1:
            diff_term = "{0}{1}^{2}".format(coefficient_str, differential, exponent)
    
    return diff_term


def apply_power_rule(equation_term):
    """ Applies the Differential Calculus Power Rule to an algebraic term, i.e. a*x^n = (n*a)x^n-1.
     
    Args:
        equation_term        Tuple containing the (coefficient, exponent) of the term.
         
    Returns:
        tuple                The first derivative values of term.  Returns None if equation_term is invalid.
    """   
    if equation_term == () or equation_term == None:
        return None
   
    coefficient, exponent = equation_term
    
    # If the exponent is positive, then apply the power rule.  
    if exponent > 0:
        return (coefficient * exponent, exponent - 1)
    else:
        return (0,0)

def differentiate_polynomial (equation, differential):
     
    """ Calculates the first derivative of a simple polynomial equation. 
     
    The function handles basic operators such as +, -, / for division and * for multiplication.
     
    Powers should be added using the '^' symbol, e.g. x^3 is x-cubed.
     
    
    Args:
        equation (str)         An algebraic equation for which the derivative is to be calculated.
        differential (str)     The variable which derivative will be calculated for
         
    Returns:
        str                    The first derivative of the equation with respect to the differential
    """
    
    operators = re.compile("(\*|\/|\+|\-)")
       
    # Split the equation, returning terms and operators
    equation_terms = re.split(operators, equation)
     
    diff_equation = ''
         
    for term in equation_terms:
        if re.match(operators, term):
            diff_equation += f' {term} '
        else:
            # Broken out for clarity
            src_term = parse_term(term.strip(), differential)
            diff_term = apply_power_rule(src_term)
            diff_equation += print_term(diff_term, differential)
     
    return diff_equation

class TestPolynomialEtivity2(unittest.TestCase):
    
    def test_parse_term_simple_coefficient(self):
        # Checks that the parsing is correct for simple coefficient
        expected = (16,1)
        result = parse_term("16x", 'x')
        self.assertEqual(result, expected)
        
    def test_parse_term_basic(self):
        # Checks that parsing is correct for basic, individual term (no explicit power or coefficient)
        expected = (1,1)
        result = parse_term("x", 'x')
        self.assertEqual(result, expected)
        
    def test_parse_term_constant(self):
        # Checks that parsing is correct for constants
        expected = (12, 0)
        result = parse_term("12", 'x')
        self.assertEqual(result, expected)
        
    def test_parse_term_with_power(self):
        # Checks that terms with power are handled
        expected = (1,2)
        result = parse_term("x^2", 'x')
        self.assertEqual(result, expected)
        
    def test_parse_term_with_coefficient_and_power(self):
        # Checks that terms with both a coefficient and power are handled
        expected = (8,2)
        result = parse_term("8x^2", 'x')
        self.assertEqual(result, expected)
        
    def test_parse_term_empty(self):
        expected = None
        result = parse_term("", "")
        self.assertEqual(result, expected)
        
    def test_power_rule_simple(self):
        expected = (24,3)
        result = apply_power_rule((6,4))
        self.assertEqual(result, expected)
        
    def test_power_rule_constant(self):
        expected = (0,0)
        result = apply_power_rule((6,0))
        self.assertEqual(result, expected)

    def test_etivity_fx(self):
        expected = "6x"
        result = differentiate_polynomial("3x^2", 'x')
        self.assertEqual(result, expected)

    def test_power_rule_gx(self):
        expected = "2x + 16 + 0"
        result = differentiate_polynomial("x^2 + 16x + 64", 'x')
        self.assertEqual(result, expected)

    def test_power_rule_kx(self):
        expected = "501x^500 + 21x^6 - 3x^5 + 5x^4 + 6x^2 + 6x - 0"
        result = differentiate_polynomial("x^501 + 3x^7 - 0.5x^6 + x^5 + 2x^3 + 3x^2 - 1", 'x')
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)