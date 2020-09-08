1. Problem explanations
The goal is to implement a blockchain which is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash and the Greenwich Mean Time when the block was created, and test strings as the data.

Since we need to include all informations in each block (node) and connect each other, we need to implement a block chain with linked list.

2. Complexity explanations
Time complexity: 
append(): O(1) since a tail pointer is used.

Space complexity: O(n) since we assume that the number of blocks are n, we use a lilnked list to build a block chain. 