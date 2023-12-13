import heapq
import os

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(data):
    frequency = {}
    for char in data:
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1
    return frequency

def build_huffman_tree(frequency):
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merge_node = HuffmanNode(None, left.freq + right.freq)
        merge_node.left = left
        merge_node.right = right

        heapq.heappush(priority_queue, merge_node)

    return priority_queue[0]

def build_huffman_codes(root, current_code, huffman_codes):
    if root is None:
        return

    if root.char is not None:
        huffman_codes[root.char] = current_code
        return

    build_huffman_codes(root.left, current_code + '0', huffman_codes)
    build_huffman_codes(root.right, current_code + '1', huffman_codes)

def encode(data, huffman_codes):
    encoded_data = ''
    for char in data:
        encoded_data += huffman_codes[char]
    return encoded_data

def compress(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read()
        frequency = build_frequency_table(data)
        huffman_tree = build_huffman_tree(frequency)
        huffman_codes = {}
        build_huffman_codes(huffman_tree, '', huffman_codes)
        encoded_data = encode(data, huffman_codes)

        with open(output_file, 'w') as output:
            for char in encoded_data:
                output.write(char)

input_file = '/Users/elizavetabalura/prog_ing/algos/input.txt'
output_file = '/Users/elizavetabalura/prog_ing/algos/compressed.txt'

compress(input_file, output_file)
