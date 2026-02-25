#Priority Queue

#removes element based on the priority ijnsead of order

#Higer priority removed first
#not normal FIFO
#smaller number = higher priority

#task-->1
#task-->2
#task-->3
# HOSPITAL EMERGENCY ROOM
# cpu task scheduling
# network pocket routing
# printer task priority

# normal queue vs priority queue

#Heap
#smallest number = higer priority
#Automatic sorting
#Uses heap module

#Pseduocode
#  insert
# import heapq 
# create empty priority queue
# insert element with priority
# heap arrange automatically

# remove
# remove smallest priority element


# import heapq

# pq=[]
# heapq.heappush(pq,3)     
# heapq.heappush(pq,1)     
# heapq.heappush(pq,2)     

# print("Priority Queue",pq)

# print("Removed",heapq.heappop(pq))
# print("Removed",heapq.heappop(pq))
# print("Removed",heapq.heappop(pq))

import heapq

pq=[]

heapq.heappush(2,"Medium task")
heapq.heappush(1,"High task")
heapq.heappush(3,"low task")

while pq:
    priority,task=heapq.heappop(pq)
    print(priority,task)