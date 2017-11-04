#   !/usr/bin/env python
"""
Provides the gcd and s, t of Euclidian algorithim for a given m, n

The algorithim states that the GCD of 2 numbers is equal to a product
of the one of the numbers and a coefficient, s added with the product
of the remaining number and a coefficient, t.
"""

def gcd(m,n,buffer):
    """Returns the GCD through recursion, and the quotient buffer"""
    if ((m % n) == 0):
        return n
    else:
        buffer.append(-1*(m // n))
        return gcd(n, (m % n), buffer)

def euclid(s,t,buffer):
    """ Returns s and t after recursion """
    if (len(buffer) == 0):
        return s,t
    else:
        t1 = s + t * buffer[len(buffer)-1]
        del buffer[len(buffer)-1]
        return euclid(t, t1, buffer)

def fn(m,n):
    """ Initilizes, and prints, the GCD and S and T values"""
    buffer = []
    if (m > n):
        large = m
        small = n
        gcd_ = gcd(m,n,buffer)
    else:
        large = n
        small = m
        gcd_ = gcd(n,m,buffer)
    s_t = euclid(1, buffer[len(buffer)-1], buffer[:len(buffer)-1])
    print("The GCD is {:d}".format(gcd_))
    if (s_t[0] > s_t[1]):
        print("{:d} = {:d} * {:d} - {:d} * {:d}".format(
            gcd_, s_t[0], large, -1*s_t[1], small))
    else:
        print("{:d} = {:d} * {:d} - {:d} * {:d}".format(
            gcd_, s_t[1], small, -1*s_t[0], large))
    if (large == m):
        print("S is {:d} and T is {:d}".format(s_t[0], s_t[1]))
    else:
        print("S is {:d} and T is {:d}".format(s_t[1], s_t[0]))

UserInput1 = int(input("Enter a pair of numbers: \n"))
UserInput2 = int(input())
fn(UserInput1,UserInput2)
input("Press enter to quit")
