l = 10
T0 = 300
R = 0.5
F0 = 50
def get_consts():
    k0 = 0.4
    kN = 0.1
    alpha0 = 0.05
    alphaN = 0.01
    '''
    k0 = float(input("k0 = "))
    kN = float(input("kN = "))
    alpha0 = float(input("alpha0 = "))
    alphaN = float(input("alphaN = "))
    '''
    a = (-k0*kN*l)/(kN-k0)
    b = (kN*l)/(kN-k0)
    c = (-alpha0*alphaN*l)/(alphaN-alpha0)
    d = (alphaN*l)/(alphaN-alpha0)
    return a, b, c, d

def k(x):
    return a/(x-b)
def alpha(x):
    return c/(x-d)

def hi(i,h):
    k1 = k((i-0.5)*h)
    k2 = k((i+0.5)*h)
    return (2*k1*k2)/(k1+k2)

def progonka(h, N):
    znam = hi(0.5,h) + (h**2 * (alpha(0)+alpha(h))) / (8*R) + (h**2 * alpha(0)) / (4*R)
    ksi1 = (hi(0.5,h) - (h**2 * (alpha(0)+alpha(h))) / (8*R)) / znam
    etta1 = (h*F0 + (h**2*T0*(3*alpha(0)+alpha(h)) / (4*R))) / znam
    ksi = [ksi1]
    etta = [etta1]
    for n in range(1,N):
        A = hi(n+0.5,h)/h
        C = hi(n-0.5,h)/h
        B = A+C + 2*alpha(n*h)*h/R
        D = 2*T0*alpha(n*h)*h/R
        znam = B-A*ksi[n-1]
        ksi.append(C/(znam))
        etta.append((D+A*etta[n-1])/znam)
    return ksi, etta

def go_back(ksi, etta, N, h):
    yarr = [0]*(N+1)
    xarr = [0]*(N+1)
    xarr[N] = l
    znam = (h**2 * (alpha(xarr[N]) + alpha(xarr[N]-h)) / (8*R)) - hi(N-0.5,h)
    m1 = (h*alpha(xarr[N])+hi(N-0.5,h)+h**2*alpha(xarr[N])/2/R + h**2*(alpha(xarr[N])+alpha(xarr[N]-h))/(8*R)) / znam
    m2 = (h*alpha(xarr[N])*T0 + T0*h**2*(3*alpha(xarr[N])+alpha(xarr[N]-h))/4/R) / znam
    yarr[N] = (m2 - etta[N-1])/(ksi[N-1] + m1)
    for n in range(N,0,-1):
        xarr[n-1] = xarr[n]-h
        yarr[n-1] = yarr[n]*ksi[n-1] + etta[n-1]
    return xarr, yarr

def work(h):
    global a, b, c, d
    a, b, c, d = get_consts()
    N = int(l/h + 1)
    ksi, etta = progonka(h, N)
    xarr, yarr = go_back(ksi, etta, N, h)
    return xarr, yarr
