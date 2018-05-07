"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

#draw Quadratic type 1 curve
def koch(t, n):
    """Draws a koch curve with length n."""
    if n<3:
        fd(t, n)  #Moves the turtle foward by the given distance.
        return
    m = n/3.0
    koch(t, m)
    lt(t, 90) #Turns left by the given angle.
    koch(t, m)
    rt(t, 90) #Turns right by the given angle.
    koch(t, m)
    rt(t, 90) # Turns right by the given angle.
    koch(t, m)
    lt(t, 90) #Turns left by the given angle.
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    # for i in range(3): #执行3次，画出最大的三角形
    koch(t, n)
        # rt(t, 120)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0

bob.x = -150
bob.y = 30
bob.redraw()

snowflake(bob, 300)

world.mainloop()
