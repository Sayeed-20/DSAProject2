class Node:
    def __init__(self, val):
        self.val = val

    def setRelatives(self, left, right, parent):
        self.left = left
        self.right = right
        self.parent = parent





class Heap:

    def __init__(self, arr):
        self.arr = arr


    def insert(self, val):
        newNode = Node(val)
        self.arr.append(newNode);
        nodeIndex = len(self.arr) - 1;
        self.arr.append(0);
        self.arr.append(0);
        newNode.setRelatives(self.arr[-2], self.arr[-1], self.arr[(nodeIndex - 1) / 2])



    def heapify(self):


def heapSort():
    # For item in arr, add to new heap



