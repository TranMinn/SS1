
class Huffman:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}

    #Calculate freq of characters in text
    def freq_dict(text):
        freq = {}
        for char in text:
            if not char in freq:
                freq[char] = 0
            freq[char] += 1
        return freq

    class MinHeap:
        def __init__(self, val, freq):
            self.val = val
            self.freq = freq
            self.left = None
            self.right = None

    #Build a min heap
    def build_heap(self, freq):



    #Select 2 min nodes and merge
    def merge_codes(self):


    #Assign code to character
    def assign_codes(self):





