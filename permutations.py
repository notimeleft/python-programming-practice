from math import factorial    
	'''
	given a list of items 1 and 2, we compute the number of possible orderings, i.e permutations, by the formula (x+y)!/(x!)(y!) where x is the number of 1s and y is the number of 2s. 

	More detailed formula is here: 

	http://codereview.stackexchange.com/questions/132704/counting-permutations-without-repetitions-for-a-number-or-a-string
    '''
    def permutations(self,one,two):
        if one==0 or two==0:
            return 1
        k = math.factorial(one+two)
        f = math.factorial(one)*math.factorial(two)
        return k/f