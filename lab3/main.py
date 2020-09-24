from calc import work
import matplotlib.pyplot as plt

if __name__ == '__main__':
    h = 1e-4
    xarr, yarr = work(h)
    plt.plot(xarr, [300]*len(xarr))
    plt.plot(xarr, yarr)
    plt.xlabel("x")
    plt.ylabel("T")
    plt.show()