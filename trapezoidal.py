# 1 Calculating area under a curve using trapezoidal rule for points within a set interval

# Recall trapezoidal rule = h/2((y0 + yn) + 2(y1+y2 ... yn-1))
def area():
    return 2/2 * ((4 + 5) + 2 * (6 + 6 + 4 + 4))


print("The area under the curve is {}". format(area()))


# 2 Proper way to calculate the area under a curve using the trapezoidal rule with a defined f(x)

# define f(x) here i.e if f(x) = x raised to power 4 - 7
def f(x): return x**4 - 7


# define x limits of curve and intervals
a = 0
b = 10
n = 5


# Recall trapezoidal rule = (dx/2) \sum_{k=1}^N (f(x_k) + f(x_{k-1})) where x_k = a + k*dx and dx = (b - a)/N.
def trapezoidal(f, a, b, n):
    h = float(b - a) / n
    f_sum = 0.0
    for i in range(1, n, 1):
        f_sum += f(a + i*h)
    return h*(0.5*f(a) + f_sum+0.5*f(b))

# Line commented out to prevent running as f(x) was not provided in the question
#print("The area under the curve is {}". format(trapezoidal(f, a, b, n)))
