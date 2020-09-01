1. Problem explanations
This problem implements ls command in command line tool.
There are one directory 'path' and it can have another subdirectories which are no limitation in depth.

2. Complexity explanations
Time complexity: 
O(nlogn) if n is all children files. 
Since the procedure uses sorted() function for an alphabetical order, it takes O(logn).
If we take sorted() function out of the procedure, it will take O(n) simply.

Space complexity: 
O(n). Since it's a recursive implementation, the space complexity is not very clearly seen but you will see it more clearly as O(n)
by using result [] array.

