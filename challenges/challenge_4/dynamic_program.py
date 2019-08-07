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
def dist_count(dist):
  '''Given a distance, count the total number
    of ways to cover the distance with 1 , 2 and 3 steps
  '''
  count = [0] * (dist + 1)

  # initialize base values
  # there is 1 way to cover 0 and 1
  # and 2 ways to cover 2 distances
  count[0] = 1
  count[1] = 1
  count[2] = 2

  # fill in bottom up manner
  for i in range(3, dist + 1):
    count[i] = count[i - 1] + count[i - 2] + count[i - 3]
  
  return count[dist]

if __name__ == "__main__":
  # for this input 
  dist = 5
  # the return value of this should be 7
  print(dist_count(dist))