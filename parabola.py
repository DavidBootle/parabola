'''Calculates all parameters of a Parabola with an input of a parabola equation in standard form'''

import re
import cmath

# constants
X_FIRST_REGEX = r'^ *(?:(?:\( *x(-|\+)(\d+) *\))|x)\^2 *= *(?:(-?)(\d+)[ \*]*)?(?:(?:\(y *(-|\+) *(\d) *\))|y) *$'
Y_FIRST_REGEX = r'^ *(?:(?:\( *y(-|\+)(\d+) *\))|y)\^2 *= *(?:(-?)(\d+)[ \*]*)?(?:(?:\(x *(-|\+) *(\d) *\))|x) *$'
GET_HK = lambda num, sign: float(num) if sign == '-' else -1 * float(num)
GET_MULTIPLIER = lambda num, sign: float(num) if sign != '-' else -1 * float(num)
GET_INT_OR_FLOAT = lambda num: int(num) if num.is_integer() else num

# parabola class
class Parabola():
    '''A parabola represented in standard form.'''

    def __init__(self, equation):
        '''Calculate parabola information from a parabola equation in standard form.'''
        self.equation = equation

        x_first_match = re.match(X_FIRST_REGEX, equation)
        y_first_match = re.match(Y_FIRST_REGEX, equation)

        # calculate parabola information
        if x_first_match:
            groups = x_first_match.groups()
            h_sign = groups[0] or '-'
            h_unsigned = groups[1] or '0'
            multiplier_sign = groups[2] or '+'
            multiplier_unsigned = groups[3] or '1'
            multiplier = GET_MULTIPLIER(multiplier_unsigned, multiplier_sign)
            k_sign = groups[4] or '-'
            k_unsigned = groups[5] or '0'
            h = GET_INT_OR_FLOAT(GET_HK(h_unsigned, h_sign))
            k = GET_INT_OR_FLOAT(GET_HK(k_unsigned, k_sign))
            p = GET_INT_OR_FLOAT(float(multiplier) / 4)

            vertex = (h, k)
            focus = (h, k + p)
            directrix = ('y', k - p)
            OPENS = 'up' if p >= 0 else 'down'
            def solve_for_x(y):
                result = cmath.sqrt(4*p*(y-k))+h
                return GET_INT_OR_FLOAT(float(result.real)) if result.imag == 0 else result
            solve_for_y = lambda x: GET_INT_OR_FLOAT(((x-h)**2/(4* p))+k)

            other_point = (0.1,0.1)
            other_y = focus[1]
            while not (float(other_point[0]).is_integer() and float(other_point[1]).is_integer()):
                other_point = (solve_for_x(other_y), other_y)
                other_y *= 2
            other_point = (int(other_point[0]), int(other_point[1]))

        elif y_first_match:
            groups = y_first_match.groups()
            k_sign = groups[0] or '-'
            k_unsigned = groups[1] or '0'
            multiplier_sign = groups[2] or '+'
            multiplier_unsigned = groups[3] or '1'
            multiplier = GET_MULTIPLIER(multiplier_unsigned, multiplier_sign)
            h_sign = groups[4] or '-'
            h_unsigned = groups[5] or '0'
            h = GET_INT_OR_FLOAT(GET_HK(h_unsigned, h_sign))
            k = GET_INT_OR_FLOAT(GET_HK(k_unsigned, k_sign))
            p = GET_INT_OR_FLOAT(float(multiplier) / 4)

            vertex = (h, k)
            focus = (h + p, k)
            directrix = ('x', h - p)
            OPENS = 'left' if p >= 0 else 'right'
            def solve_for_y(x):
                result = cmath.sqrt(4*p*(x-h))+k
                return GET_INT_OR_FLOAT(float(result.real)) if result.imag == 0 else result
            solve_for_x = lambda y: GET_INT_OR_FLOAT(((y-k)**2/(4* p))+h)
            
            other_point = (0.1,0.1)
            other_x = focus[0]
            while not (float(other_point[0]).is_integer() and float(other_point[1]).is_integer()):
                other_point = (solve_for_x(other_x), other_x)
                other_x *= 2
            other_point = (int(other_point[0]), int(other_point[1]))

        else:
            raise ValueError('Not a valid parabola equation.')
        
        # save parabola information to object
        self.h = h
        self.k = k
        self.p = p
        self.vertex = vertex
        self.focus = focus
        self.directrix = directrix
        self.other_int_point = other_point
        self.OPENS = OPENS
        self.x = solve_for_x
        self.y = solve_for_y

    def print_info(self):
        print('Vertex:', self.vertex)
        print('Focus:', self.focus)
        print('Other Point:', self.other_int_point)
        print('Directrix:', f'{self.directrix[0]}={str(self.directrix[1])}')
        print('Opening Direction:', self.OPENS)
    
    def __repr__(self):
        display_equation = self.equation.replace(' ', '')
        return f'<Parabola [{display_equation}]>'
        
if __name__ == '__main__':
    equation = input('Equation: ')
    try:
        parabola = Parabola(equation)
        parabola.print_info()
    except ValueError:
        print('Sorry, not a valid parabola equation in standard form.')