def gcd(m,n,k):
    if ((m % n) == 0):
        return n
    else:
        k.append(-1*(m // n))
        return gcd(n, (m % n), k)

def euclid(s,t,k):
    if (len(k) == 0):
        return s,t
    else:
        t1 = s + t * k[len(k)-1]
        del k[len(k)-1]
        return euclid(t, t1, k)

def fn(m,n):
    k = []
    if (m > n):
        large = m
        small = n
        gcd_ = gcd(m,n,k)
    else:
        large = n
        small = m
        gcd_ = gcd(n,m,k)
    s_t = euclid(1, k[len(k)-1], k[:len(k)-1])
    print("The GCD is {:d}".format(gcd_))
    if (s_t[0] > s_t[1]):
        print("{:d} = {:d} * {:d} - {:d} * {:d}".format(gcd_, s_t[0], large, -1*s_t[1], small))
    else:
        print("{:d} = {:d} * {:d} - {:d} * {:d}".format(gcd_, s_t[1], small, -1*s_t[0], large))
    if (large == m):
        print("S is {:d} and T is {:d}".format(s_t[0], s_t[1]))
    else:
        print("S is {:d} and T is {:d}".format(s_t[1], s_t[0]))

UserInput1 = int(input("Enter a pair of numbers: \n"))
UserInput2 = int(input())
fn(UserInput1,UserInput2)
input("Press enter to quit")
