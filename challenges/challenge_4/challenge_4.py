from functools import wraps
def memoize(func):
    cache = func.cache = {}
    @wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memoized_func


@memoize
def knapsack(max_weight, items, n):
    ''' A  method to determine the maximum value of the items included in the knapsack 
    without exceeding the capacity  C

        Parameters: 
        max_Weight = 50
        items = (("boot", 10, 60),
            ("tent", 20, 100),
            ("water", 30, 120),
            ("first aid", 15, 70))
        Returns: max value
    Credit to GEEKS FOR GEEKS for the algorithm
    '''
    # This code is contributed by Nikhil Kumar Singh
    if (n == 0 or max_weight == 0):
        return 0
    
    if (items[n-1][1] > max_weight):
        # print(items[n-1][1])
        return knapsack(max_weight, items, n-1)

    else:
        return max(items[n-1][2] + knapsack(max_weight - items[n-1][1], items, n-1 ), 
                    knapsack(max_weight, items, n-1))

if __name__ == "__main__":
    max_weight = 50
    items = (("boot", 10, 60),
        ("tent", 20, 100),
        ("water", 30, 120),
        ("first aid", 15, 70))
    n = len(items)

    print(knapsack(max_weight, items, n))