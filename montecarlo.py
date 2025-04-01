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
    r.seed(88)
    for i in range(1,10):
        print(montecarlo(100000))
if __name__=="__main__":
    main()
