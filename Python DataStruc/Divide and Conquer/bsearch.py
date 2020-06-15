import time

def bsearch(arr,len, value):
	length = len - 1
	index0 = 0
	indexend = length
	while(index0 <= indexend):
		mid = (index0 + indexend)//2 #integer point div

		if(arr[mid] == value):
			print("Found")
		if(value > arr[mid]):
			index0 = mid + 1
		else:
			indexend = mid - 1

	if index0 > indexend:
		return None

arr = [23,43,56,66,78,98]
arr_len = len(arr)
num_search = int(input("Enter num to search:\n"))
tic = time.perf_counter()
bsearch(arr,arr_len, num_search)
toc = time.perf_counter()
time_diff = toc-tic
print("Time:",time_diff)
