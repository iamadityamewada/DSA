# def find_fib(n):
#     # series = [0]
#     def fib(n):
#         if n <= 1:
#             return 1
#         return fib(n-1) + fib(n-2)
#     find_fib(n)
    
#     # if n == 0:
#     #     return 0
    
#     # return n + find_fib(n-1)


def fib(n):
     if n == 1:
        return 1
     elif n == 0:
        return 0
     return fib(n-1) + fib(n-2)
  
print(fib(5))
# Recursion Tree

    #                              __________________ fib(5)_________________
    #                         fib(4)                                          fib(3)
    #              fib(3)               fib(2)                        f(2)               f(1)
    #       f(2)         f(1)      f(1)        f(0)              f(1)      f(0) 
    # f(1)       f(0)                      
