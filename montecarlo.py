import math as m
import random as r
def montecarlo(n):
    diana = 0
    for _ in range(n):
        x = r.random()
        y = r.random()
        hyp = m.sqrt(m.pow(x,2) + m.pow(y,2))
        if hyp < 1:
            diana += 1
    return 4*diana/n
def main():
    for i in range(1,10):
        print(montecarlo(10000))
if __name__=="__main__":
    main()
