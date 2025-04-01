def fibonacci(n):
    if n < 3:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
def main():
    for i in range(1,10):
        print(fibonacci(i))
if __name__=="__main__":
    main()
