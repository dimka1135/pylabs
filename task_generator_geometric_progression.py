def geometric_progression_generator(b, q):
    if b == 0:
        raise ArithmeticError('The first term is zero')
    if q == 0:
         raise ArithmeticError('The denominator is zero')
    
    while 1:
        yield  b
        b *= q 