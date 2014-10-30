from __future__ import division

__author__ = "Anung Ariwibowo"


def logmap(n, x0, r):
    x = x0
    for i in range(0,n):
        x = r * x * (1-x)
    return x


if __name__ == "__main__":
    y = logmap(10, 0.2, 2.6)
    print y

