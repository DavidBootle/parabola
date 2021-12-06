# parabola
A python library for calculating various parabola information using a parabola equation in standard form.

You can run the script directly or import it. Running it will ask for an equation as input, then print out the parabola information. Importing it gives you access to the Parabola class.

## The `Parabola` Class
### Constructor
The constructor for Parabola takes a string argument, which is the equation of the parabola in standard form. This is written using `^` as an exponent character. Custom regex is used to extract information, and is designed to be flexible with parsing the inputs. Adding whitespace is allowed between terms (`x + 3` instead of `x+3` for example), but not between the left terms and the exponent (`x ^2` is invalid). The program can properly accept both `(x-h)^2=a(y-k)` and `(y-k)^2=a(x-h)` parabola equations, but `(x-h)^2=a(y-k)` will be used for the following examples. All variations are interchangable between the two forms. The left side can have the following variations:
- `(x-h)^2`
- `x^2`

while the right side can have the following variations:
- `a(y-k)`
- `ay`
- `(y-k)`

The program can properly interpret any combination of these variations.

In case you are interested, the regex used for data extraction is shown below with the regex for `(x-h)^2=a(y-k)` on the top and `(y-k)^2=a(x-h)` on the bottom.

```regex
^ *(?:(?:\( *x(-|\+)(\d+) *\))|x)\^2 *= *(?:(-?)(\d+)[ \*]*)?(?:(?:\(y *(-|\+) *(\d) *\))|y) *$
```
```regex
^ *(?:(?:\( *y(-|\+)(\d+) *\))|y)\^2 *= *(?:(-?)(\d+)[ \*]*)?(?:(?:\(x *(-|\+) *(\d) *\))|x) *$
```

#### Example
```python
>>> from parabola import Parabola
>>> a = Parabola('(x-2)^2=2y')
>>> print(a)
# <Parabola [(x-2)^2=2y]>

>>> a.print_info()
# Vertex: (2, 0)
# Focus: (2, 0.5)
# Other Point: (4, 2)
# Directrix: y=-0.5
# Opening Direction: up
```

### Properties and Methods
The `h`, `k`, and `p` values of a parabola can all be accessed directly and will be either float or int values.

The `vertex` and `focus` can also be accessed directly and will return a 2-tuple of int or float type, where the first value is the x value, and the second is the y value. Example: `(-5, 2.5)`

The directrix can be accessed with the `directrix` property, and is a 2-tuple. The first item in the tuple is a string and is either `x` or `y`, and the second item is either an int or float. The first item should be paired with the second in order to make a line equation. For example `('x', 5)` is x=5.

The `other_int_point` property is a point along the parabola where both the x and y values are integers. This is useful for computations that require the vertex and another point. This computation is not always perfect and may sometimes return ridiculously large numbers or simply the vertex. However, it usually works as intended.

The `OPENS` property is the direction that the parabola opens, and can be `up`, `down`, `left`, or `right`.

 The `x` method takes one parameter (`y`) and can be used to find x for a given y value on the parabola. The program currently does not take into account multiple correct values, and will only give you the positive one. This may be changed in the future. The returned value can be either a int, float, or complex number. Make sure to have handling for complex numbers!
 
 The `y` method does the same thing as the `x` method but finds y for a given x value on the parabola.
 
 The `print_info` method prints the `vertex`, `focus`, `other_int_point`, `directrix`, and `OPENS` properties for convient reading.

#### Example
```python
>>> from parabola import Parabola
>>> a = Parabola('(x+1)^2=4(y-3)')
>>> a.h
# -1
>>> a.k
# 3
>>> a.p
# 1
>>> a.vertex
# (-1, 3)
>>> a.focus
# (-1, 4)
>>> a.directrix
# ('y', 2)
>>> a.other_int_point
# (1, 4)
>>> a.OPENS
# 'up'
>>> a.x(10)
# 4.291502622129181
>>> a.y(10)
# 33.25
>>> a.print_info()
# Vertex: (-1, 3)
# Focus: (-1, 4)
# Other Point: (1, 4)
# Directrix: y=2
# Opening Direction: up
```
