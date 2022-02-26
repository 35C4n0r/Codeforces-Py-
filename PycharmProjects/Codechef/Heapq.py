import heapq
arr = [6, 7, 9, 4, 3, 5, 8, 10, 1]
heapq.heapify(arr)
print(arr)
heapq.heappush(arr, 2)
print(arr)
print(arr[1])