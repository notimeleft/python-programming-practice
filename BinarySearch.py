
#binary search on a list of sorted values. 

def BinarySearch(start, end, list, target):
		
	index = (start+end)/2
	
	if start==end: return -1

	if target < list[index]:
		return BinarySearch(start,index,list,target)
	elif target > list[index]:
		return BinarySearch(index+1,end,list,target)
	else:		
		return index


list = [1]
target = 1
k = len(list)
print BinarySearch(0,k,list,target)		