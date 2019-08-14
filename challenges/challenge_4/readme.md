### knapsack problem

# Given a backpack with max weigth n pack as many items in the backppack to calcualte the max value

# Resource
  Class Material/ Geeks for Geeks

# Five Steps
1. Consider each permutation of possible combinations
2. Consider the first item in array as first choice, and consider having that item vs not having that item
3. return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1))
4. memoization to optimise
5. function considers all possible permeations that gives max backpack value

### Problem 2

# Given a distance 'dist' Count the total number of ways to cover the distance

## Resource 
 Geeks for Geeks

 # The Five steps applied for this problem 
 1. sub problem here is that the ways could be repeated similar to the fibinacci dynamic problem
 2. First choice is to start at 3 there are 4 ways to cover the disance 3
 3. Not a recursive solution
 4. memomize to optimise
 5. find all permeations of ways to cover a given distance
