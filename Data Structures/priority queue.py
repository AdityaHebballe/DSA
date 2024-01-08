class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def Parent(i):
        return i//2
    def LeftChild(i):
        return 2*i+1
    def RightChild(i):
        return 2*i+1