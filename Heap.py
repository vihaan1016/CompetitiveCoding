import heapq

li =  [5, 7, 9, 4, 3]
# Converting the list to a heap
heapq.heapify(li)

print(li)

# Adding 1 to the heap
heapq.heappush(li, 1)
print("The modified heap is: ", list(li))

# popping the smallest and first element
print(heapq.heappop(li))

# pushpop(list, value) adds the entered value to the heap and
# also pops the smallest value after adding the new value to the list
print(heapq.heappushpop(li, 9))

# nlargest gives k largest numbers in the heap
print(heapq.nlargest(3, li))

#nsmallest gives k number of smalles numbers in the heap
print(heapq.nsmallest(3, li))