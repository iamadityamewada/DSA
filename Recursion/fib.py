def find_fib(n):
    # series = [0]
    def fib(n):
        if n == 0 or n==1:
            return 0
        return fib(n) + fib(n-1)
    
    find_fib()
    
    # if n == 0:
    #     return 0
    
    # return n + find_fib(n-1)

print(find_fib(7))