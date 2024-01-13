#Name: Jack Wyeth
def DPknapsack(wi,vi,W,n):
    dp = [[0 for w in range(W + 1)] for i in range(n + 1)]

# Build the table using the given formula
    for i in range(1, n + 1):
     for w in range(1, W + 1):
        if wi[i - 1] <= w:
            dp[i][w] = max(vi[i - 1] + dp[i - 1][w - wi[i - 1]], dp[i - 1][w])
        else:
            dp[i][w] = dp[i - 1][w]

# Print the result
    for i in range(n+1): print(dp[i][W])
def main():
   num_items=int(input())
   weights=[]
   values=[]

   var_weights=input()
   var_weights=var_weights.split()
   for num in var_weights:
       weights.append(int(num))

   var_value=input()
   var_value=var_value.split()
   for num in var_value:
       values.append(int(num))
   capacity=int(input())

   DPknapsack(weights,values,capacity,num_items)

if __name__=="__main__": 
    
    main() 
