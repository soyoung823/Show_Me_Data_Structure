1. Problem explanations
Our goal is to design a data structure, a Least Recently Used (LRU) cache, which is
a type of cache in which we remove the least recently used entry when the cache memory reaches
its limit. 
The lookup operation get() and set() shoud be fast for a cache memory.
All operations must take O(1) time.

2. Complexity explanations
Time complexity:
get(): O(1) constant time --> fast lookup: use hash table (dictionary).
: if we store key and the node as a value in the hash table (dictionary), we can access the node in O(1) time.

set(): O(1) constant time --> fast removal: use doubly linked list.
If we remove the last used node fastly, we need to know the previous node and next node.
Otherwise, like when we use a sinlgy linked list, we need to traverse the list in order to find the previous node O(n). If we use an array, we need to shift all the elements after removing the element. That's why it takes O(n).

Space complexity: O(n) since the implementation uses n numbers dictionary and doubly linked list.


