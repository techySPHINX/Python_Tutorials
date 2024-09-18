import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
def calculate_frequency(string):
    frequency = defaultdict(int)
    for char in string:
        frequency[char] += 1
    return frequency

def build_heap(frequency):
    heap = []
    for key in frequency:
        node = Node(key, frequency[key])
        heapq.heappush(heap, node)
    return heap


def merge_nodes(heap):
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)
        
def build_codes_helper(root, current_code, codes):
    if root == None:
        return

    if root.char != None:
        codes[root.char] = current_code

    build_codes_helper(root.left, current_code + "0", codes)
    build_codes_helper(root.right, current_code + "1", codes)
    
def build_codes(root):
    codes = {}
    build_codes_helper(root, "", codes)
    return codes


def huffman_encoding(string):
    frequency = calculate_frequency(string)
    heap = build_heap(frequency)
    merge_nodes(heap)

    root = heap[0]
    codes = build_codes(root)

    encoded_string = ""
    for char in string:
        encoded_string += codes[char]

    return encoded_string, root

def huffman_decoding(encoded_string, root):
    decoded_string = ""
    current_node = root

    for bit in encoded_string:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char != None:
            decoded_string += current_node.char
            current_node = root

    return decoded_string
