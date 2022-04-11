import sys
import time

def fibo(n):
    if n<=2:
        return 1

    return fibo(n-1) + fibo(n-2)

def fiboimproved(n):
    alfa = (1+5**(1/2))/2
    beta = (1-5**(1/2))/2
    k1 = 1/2 + (5**(1/2))/10
    k2 = 1/2 - (5**(1/2))/10

    factor1 = k1*alfa**(n-1)
    factor2 = k2*beta**(n-1)

    return int(factor1 + factor2)

if __name__ == "__main__":
    index = 35 
    if len(sys.argv) > 1:
        try:
            index = int(sys.argv[1])
        except Exception as e:
            print(e)
    start = time.time()
    fibo(index)
    end = time.time()

    print(f"Recursion method")
    print('took {:.20f} seconds\n'.format(end-start))

    start = time.time()
    fiboimproved(index)
    end = time.time()
    print("Discrete math tricks")
    print('took {:.20f} seconds\n'.format(end-start))
