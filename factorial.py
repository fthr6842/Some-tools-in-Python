def factorial (k):
    if  k == 1: return 1
    else: return k*factorial(k-1)

if __name__ == "__main__":
    print("5!: ", factorial(5))
