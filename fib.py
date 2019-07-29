def memoize(f):
    memo = {0:0, 1:1}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
         return fib(n-1) + fib(n-2)




if __name__ == "__main__":
    print(fib(40))