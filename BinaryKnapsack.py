'''
To solve the binary knapcksack problem, I have employed dynamic programming approach.
A matrix is defined. In each element of this matrix, the most accessible value is calculated considering the value of items and 
the weight of items and the pack. 
The last element of the matrix is the optimal(best) answer(value). 
wi is the weight for item i 
W is the maximum weight the pack can handle
V is the value of picking particular items 
n is the number of items
'''
def knapsackSolver(W, wi, V, n ):
    # at first the elements are defined as zero.
	matrix = [[0 for weight in range(W + 1)] 
			for item in range(n + 1)] 
	for i in range(n + 1): 
		for w in range(W + 1): 
			if i == 0 or w == 0: 
				matrix[i][w] = 0
			elif wi[i - 1] <= w:
            # if adding the new item do not result in exceeding the weight of the pack, the optimal value is calculated :
				matrix[i][w] = max(V[i - 1] + matrix[i - 1][w - wi[i - 1]],matrix[i - 1][w]) 
			else: # if adding the new item result in exceeding the pack's weight, the value of previous element will remain in the new element
				matrix[i][w] = matrix[i - 1][w]
    # the last element of the matrix is the accessibale optimal(best) answer(value) 
	maximum = matrix[n][W] 
	print("maximum value:" + str(maximum)  + "\nitems are:") 
	w = W 
 # returning the items that have lead us to the best value (we picked)
	for i in range(n, 0, -1): 
		if maximum <= 0: 
			break
		if maximum == matrix[i - 1][w]: 
			continue
		else: 
			print(i) 
			
			maximum = maximum - V[i - 1] 
			w = w - wi[i - 1] 

# test case 1
# V = [1, 3, 4, 2] 
# wi = [1, 1, 3, 2] 
# W = 5

# test case 2
# V = [15, 17, 20, 10]
# wi = [40, 37, 45, 30]
# W = 80

# test case 3
V = [2, 4, 3]
wi = [3, 2, 1]
W = 5


n = len(V) 	
knapsackSolver(W, wi, V, n) 