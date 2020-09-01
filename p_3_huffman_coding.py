'''
Data Compression - Huffman Coding, lossless
# Huffman Encoding
input str: AAAAAAABBBCCCCCCCDDEEEEEE (25 characters)
output binary code: 1010101010101000100100111111111111111000000010101010101
'''
# 1. Build the Huffman Tree (bottom up)
'''
1. determine the frequency of each character in the message.
'''

import sys

class TreeNode:
    def __init__(self, key, freq):
        self.key = key
        self.freq = freq
        self.left = None
        self.right = None

class PriorityNode:
    def __init__(self, tree_node):
        self.tree_node = tree_node
        self.next = None

class PriorityList:
    def __init__(self):
        self.head = None

    def print(self):
        node = self.head
        while node:
            print(' ({}, {})'.format(node.tree_node.key, node.tree_node.freq), end='')
            node = node.next
        print()

    def push(self, tree_node):
        new_node = PriorityNode(tree_node)
        if self.head is None:
            self.head = new_node
            return
        
        cur_node = self.head
        prev_node = None
        while cur_node and new_node.tree_node.freq > cur_node.tree_node.freq:
            prev_node = cur_node
            cur_node = cur_node.next
        if prev_node:
            prev_node.next = new_node
        else:
            self.head = new_node
        new_node.next = cur_node    

    def pop(self):
        if self.head is None:
            return None
        result = self.head
        self.head = self.head.next
        return result

o = PriorityList()
o.push(TreeNode('A', 5))
o.print()
o.push(TreeNode('D', 6))
o.print()
o.push(TreeNode('B', 3))
o.print()
o.push(TreeNode('C', 7))
o.print()
print(o.pop().tree_node.key)
print(o.pop().tree_node.key)

def huffman_encoding(data):
    # 0. Build the prioritylist
    d = {}
    for c in data:
        d[c] = d.get(c, 0) + 1
    q = PriorityList()
    for key in d:
        q.push(TreeNode(key, d[key]))
    q.print()

    # 1. Build the Huffman Tree
    if q.head is None:
        return

    while q.head.next is not None:
        f_node = q.pop()
        s_node = q.pop()
        n_node = TreeNode(key=None, freq=f_node.tree_node.freq + s_node.tree_node.freq)
        n_node.left = f_node.tree_node
        n_node.right = s_node.tree_node
        q.push(n_node)
    
    tree = q.head.tree_node

    # 2. Generate the Encoded Data
    huffman_codes = {}
    def traverse(node, code):
        if node is None:
            return
        if node.key:
            # insert to dictionary
            huffman_codes[node.key] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')

    traverse(q.head.tree_node, '')
    encoded_data = ''
    for c in data:
        encoded_data += huffman_codes[c]
    return encoded_data, tree

def huffman_decoding(data, tree):
    result = ''
    node = tree
    for c in data:
        if c == '0':
            node = node.left
        if c == '1':
            node = node.right
        if node.key:
            result += node.key
            node = tree
    return result

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
