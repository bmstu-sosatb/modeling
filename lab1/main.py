from math import sqrt, trunc
eps = 1e-6
def print_table(xbeg, xend, step, p3, p4, yavn, neyavn):
    print("{:15}|{:15}|{:15}|{:15}|{:15}".format("x", "Пикар 3", "Пикар 4", "Явная схема", "Неявная схема"))
    print("-" * 80)
    i = 0
    x = xbeg
    while (x < xend):
        if yavn[i] == '-' and neyavn[i] == '-':
            print("{:15.5f}|{:15.5f}|{:15.5f}|{:>15s}|{:>15s}".format(x, p3[i], p4[i], yavn[i], neyavn[i]))
        elif yavn[i] == '-':
            print("{:15.5f}|{:15.5f}|{:15.5f}|{:>15s}|{:15.5f}".format(x, p3[i], p4[i], yavn[i], neyavn[i]))
        elif neyavn[i] == '-':
            print("{:15.5f}|{:15.5f}|{:15.5f}|{:15.5f}|{:>15s}".format(x, p3[i], p4[i], yavn[i], neyavn[i]))
        else:
            print("{:15.5f}|{:15.5f}|{:15.5f}|{:15.5f}|{:15.5f}".format(x, p3[i], p4[i], yavn[i], neyavn[i]))
        i +=1
        x += step

def f(x, u):
    return x**2 + u**2

def pikar(xbeg, xend, step, etta):
    p3 = []
    p4 = []
    x = xbeg
    while (x < xend):
        y3 = etta + 1/3 * x**3 + 1/63 * x**7 + 2/2079 * x**11 + 1/59535 * x**15
        y4 = y3 + 4/93555 * x**15 + (2/2488563 + 2/3393495) * x**19 + (4/99411543 + 1/86266215) * x**23 + 4/371319795 * x**27 + 1/109876902975 * x**31
        p3.append(y3)
        p4.append(y4)
        x += step
    return p3, p4

def yavniy(xbeg, xend, realstep, writestep, y0):
    yarr = [y0]
    y = y0
    summ = 0
    x = xbeg
    while (x < xend):
        try:
            y += realstep * f(x, y)
            if (abs(summ - writestep) < eps):
                yarr.append(y)
                summ = 0
            summ += realstep
            x += realstep
        except:
            n = trunc((xend - x)/realstep)
            for i in range(n):
                yarr.append('-')
            break
    return yarr

def neyavniy(xbeg, xend, realstep, writestep, y0):
    yarr = [y0]
    y = y0
    summ = 0
    x = xbeg + realstep
    while (x < xend + realstep):
        d = 1 - 4*realstep * (realstep * x**2 + y)
        if  d < 0:
            n = trunc((xend - x) / realstep)
            for i in range(n):
                yarr.append('-')
            break
        y = (1 - sqrt(d)) / (2 * realstep)
        if (abs(summ - writestep) < eps):
            yarr.append(y)
            summ = 0
        summ += realstep
        x += realstep
    return yarr

ws = 0.1
rs = 10 ** -5
xb = 0
xe = 2.6
etta = 0
y0 = 0
p3, p4 = pikar(xb, xe, ws, etta)
yavn = yavniy(xb, xe, rs, ws, y0)
neyavn = neyavniy(xb, xe, rs, ws, y0)
#print(p3,'\n', p4, '\n', yavn, '\n', neyavn)
print_table(xb, xe, ws, p3, p4, yavn, neyavn)