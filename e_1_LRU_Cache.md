1. Problem explanation
We set the fixed size of capacity. 
If the elements numbers are more than capacity, we want to remove item which is least recently used (LRU).

Example: capacity = 5

1 2 3 4 5
the most recently -> the least recently

We want to add (prepend) 0 to the front of it like 0 1 2 3 4 5. But it can't be like that because the capacity should be 5. So we want to move 4 (the least recently used) before adding 0 to the front.

2. Complexity explanation
get() Time complexity: O(1) constant time --> fast lookup: use hash table (dictionary).
: if we store key and the node as a value in the hash table (dictionary), we can access the node in O(1) time.

set() Time complexity: O(1) constant time --> fast removal: use doubly linked list.
If we remove the last used node fastly, we need to know the previous node and next node.
Otherwise, like when we use a sinlgy linked list, we need to traverse the list in order to find the previous node O(n). If we use an array, we need to shift all the elements after removing the element. That's why it takes O(n).




