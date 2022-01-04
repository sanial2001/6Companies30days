def FirstKelements(arr,size,k):

	minHeap = []
	for i in range(k):
		minHeap.append(arr[i])
	
	for i in range(k, size):
		minHeap.sort()
    
    if (minHeap[0] > arr[i]):
      continue
			
		else:
			minHeap.pop(0)
			minHeap.append(arr[i])
			
	for i in minHeap:
		print(i, end = " ")
