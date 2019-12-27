"""
Module: 'math' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

e = 2.718282
"""base of the natural logarithm"""

pi = 3.141593
"""the ratio of a circle’s circumference to its diameter"""

def acos(x):
    """
    Return the inverse cosine of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.acos

    """
    pass

def acosh(x):
    """
    Return the inverse hyperbolic cosine of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.acosh

    """
    pass

def asin(x):
    """
    Return the inverse sine of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.asin

    """
    pass

def asinh(x):
    """
    Return the inverse hyperbolic sine of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.asinh

    """
    pass

def atan(x):
    """
    Return the inverse tangent of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.atan

    """
    pass

def atan2(y, x):
    """
    Return the principal value of the inverse tangent of y/x.

    Parameters
    ----------
    - y
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.atan2

    """
    pass

def atanh(x):
    """
    Return the inverse hyperbolic tangent of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.atanh

    """
    pass

def ceil(x) -> int:
    """
    Return an integer, being x rounded towards positive infinity.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.ceil

    """
    pass

def copysign(x, y):
    """
    Return x with the sign of y.

    Parameters
    ----------
    - x
    - y

    http://docs.micropython.org/en/latest/library/math.html#math.copysign
    
    """
    pass

def cos(x):
    """
    Return the cosine of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.cos

    """
    pass

def cosh(x):
    """
    Return the hyperbolic cosine of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.cosh

    """
    pass

def degrees(x):
    """
    Return radians x converted to degrees.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.degrees

    """
    pass

def erf(x):
    """
    Return the error function of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.erf

    """
    pass

def erfc(x):
    """
    Return the complementary error function of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.erfc

    """
    pass

def exp(x):
    """
    Return the exponential of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.exp

    """
    pass

def expm1(x):
    """
    Return exp(x) - 1.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.expm1

    """
    pass

def fabs(x):
    """
    Return the absolute value of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.fabs

    """
    pass

def floor(x) -> int:
    """
    Return an integer, being x rounded towards negative infinity.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.floor

    """
    pass

def fmod(x, y):
    """
    Return the remainder of x/y.

    Parameters
    ----------
    - x
    - y

    http://docs.micropython.org/en/latest/library/math.html#math.fmod

    """
    pass

def frexp(x):
    """
    Decomposes a floating-point number into its mantissa and exponent. The returned value is the tuple (m, e) such that x == m * 2**e exactly. If x == 0 then the function returns (0.0, 0), otherwise the relation 0.5 <= abs(m) < 1 holds.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.frexp

    """
    pass

def gamma(x):
    """
    Return the gamma function of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.gamma

    """
    pass

def isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0) -> bool:
    """
    Return True if the values a and b are close to each other and False otherwise.

    Parameters
    ----------
    - a
    - b
    - *
    - rel_tol=1e-09
    - abs_tol=0.0

    Whether or not two values are considered close is determined according to given absolute and relative tolerances.

    rel_tol is the relative tolerance – it is the maximum allowed difference between a and b, relative to the larger absolute value of a or b. For example, to set a tolerance of 5%, pass rel_tol=0.05. The default tolerance is 1e-09, which assures that the two values are the same within about 9 decimal digits. rel_tol must be greater than zero.

    abs_tol is the minimum absolute tolerance – useful for comparisons near zero. abs_tol must be at least zero.

    If no errors occur, the result will be: abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol).

    The IEEE 754 special values of NaN, inf, and -inf will be handled according to IEEE rules. Specifically, NaN is not considered close to any other value, including NaN. inf and -inf are only considered close to themselves.

    https://docs.python.org/3/library/math.html#math.isclose

    """
    pass

def isfinite(x) -> bool:
    """
    Return True if x is finite.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.isfinite

    """
    pass

def isinf(x) -> bool:
    """
    Return True if x is infinite.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.isinf
    
    """
    pass

def isnan(x) -> bool:
    """
    Return True if x is not-a-number

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.isnan
    """
    pass

def ldexp(x):
    """
    Return x * (2**exp).

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.ldexp

    """
    pass

def lgamma(x):
    """
    Return the natural logarithm of the gamma function of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.lgamma

    """
    pass

def log(x):
    """
    Return the natural logarithm of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.log

    """
    pass

def log10(x):
    """
    Return the base-10 logarithm of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.log10

    """
    pass

def log2(x):
    """
    Return the base-2 logarithm of x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.log2

    """
    pass

def modf(x) -> tuple:
    """
    Return a tuple of two floats, being the fractional and integral parts of x. Both return values have the same sign as x.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.modf

    """
    pass

def pow(x, y):
    """
    Returns x to the power of y.

    Parameters
    ----------
    - x
    - y

    http://docs.micropython.org/en/latest/library/math.html#math.pow

    """
    pass

def radians(x):
    """
    Return degrees x converted to radians.

    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.radians

    """
    pass

def sin(x):
    """
    Return the sine of x.
    
    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.sin

    """
    pass

def sinh(x):
    """
    Return the hyperbolic sine of x.
    
    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.sinh

    """
    pass

def sqrt(x):
    """
    Return the square root of x.
    
    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.sqrt

    """
    pass

def tan(x):
    """
    Return the tangent of x.
    
    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.tan

    """
    pass

def tanh(x):
    """
    Return the hyperbolic tangent of x.
    
    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.tanh

    """
    pass

def trunc(x):
    """
    Return an integer, being x rounded towards 0.
    
    Parameters
    ----------
    - x

    http://docs.micropython.org/en/latest/library/math.html#math.trunc

    """
    pass

