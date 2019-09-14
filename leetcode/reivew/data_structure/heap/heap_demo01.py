# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/13 20:59 
"""
from pprint import pprint as pp
import heapq
"""Heap queue algorithm (a.k.a. priority queue).

Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
all k, counting elements from 0.  For the sake of comparison,
non-existing elements are considered to be infinite.  The interesting
property of a heap is that a[0] is always its smallest element.

Usage:

heap = []            # creates an empty heap
heappush(heap, item) # pushes a new item on the heap
item = heappop(heap) # pops the smallest item from the heap
item = heap[0]       # smallest item on the heap without popping it
heapify(x)           # transforms list into a heap, in-place, in linear time
item = heapreplace(heap, item) # pops and returns smallest item, and adds
                               # new item; the heap size is unchanged

Our API differs from textbook heap algorithms as follows:

- We use 0-based indexing.  This makes the relationship between the
  index for a node and the indexes for its children slightly less
  obvious, but is more suitable since Python uses 0-based indexing.

- Our heappop() method returns the smallest item, not the largest.

These two make it possible to view the heap as a regular Python list
without surprises: heap[0] is the smallest item, and heap.sort()
maintains the heap invariant!
"""

h = []
heapq.heappush(h, 2)
heapq.heappush(h, 0)
heapq.heappush(h, 1)
heapq.heappush(h, 4)
heapq.heappush(h, 3)
heapq.heappush(h, 5)
heapq.heappush(h, 2)

l = len(h)
id_h = [(i,h[i]) for i in range(l)]
print(id_h)
# [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3), (5, 5), (6, 2)]

sorted_h = []
while h:
    i = heapq.heappop(h)
    sorted_h.append(i)

print(sorted_h)

# heapfiy a list

l1 = [2,3,5,1,0,9,10,12]
heapq.heapify(l1) # return None
print('heapfied:', l1)

print('The four biggest item:', heapq.nlargest(4, l1))
print('The four smallest item:',heapq.nsmallest(4, l1))
print('heap before poped one item:', l1)
item = heapq.heappop(l1)
print('poped item:', item)
print('heap after poped one item:', l1)








