1. Problem explanations
The goal is to write code for finding all files under a directory (and all directories beneath it) that end with '.C'

2. Complexity explanations
Time complexity: 
Building PriorityList: O(n^2)
Building Huffman Tree: O(n^2)
Huffman_codes dictionary building: O(n)
Encoding with dictionary: O(n)
Decoding: Assume that the number of unique characters is m, the tree depth will be O(log m). Thus, total 
time complexity is O(n log m).

Space complexity: O(n) when the string size is n.