1. Problem explanations
The goal is to implement the union and intersection functions.
You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.
By using a pre-built node and linked list, The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

2. Complexity explanations
Time Complexity: O(n) since we use the prepend method (not using the append method) to add the nodes to the set.
Space Complexity: O(n) since we use set() for each node in total n length.