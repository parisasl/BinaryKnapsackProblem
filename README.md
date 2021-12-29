# BinaryKnapsackProblem
Knapsack Problem: Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).

In a DP[][] table I considered all the possible weights from ‘1’ to ‘W’ as the columns and weights that can be kept as the rows. 

The state DP[i][j] will denote maximum value of ‘i-weight’ considering all values from ‘1 to jth’. So if we consider ‘wi’ (weight in ‘ith’ row) we can fill it in all columns which have ‘W > wi’. Now two possibilities can take place: 

- Fill ‘wi’ in the given row.
- Do not fill ‘wi’ in the given row.


Now we have to take a maximum of these two possibilities, formally if we do not fill ‘ith’ weight in ‘jth’ column then DP[i][j] state will be same as DP[i-1][j] but if we fill the weight, DP[i][j] will be equal to the value of ‘vi’+ value of the column weighing ‘j-wi’ in the previous row. So we take the maximum of these two possibilities to fill the current state.
