# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.nodes = {}
                for i in range(self.n):
                    self.nodes[i] = []
                for i in range(self.n):
                    if self.parent[i]!=-1:
                        self.nodes[self.parent[i]]+=[i]
                        
        def compute_height(self):
            root = self.parent.index(-1)
            queue = []
            queue.append(root)
            height = 0
            while True:
                nodecount = len(queue)
                if nodecount==0:
                    return height
                height+=1
                while nodecount>0:
                    node = queue[0]
                    queue.pop(0)
                    queue.extend(self.nodes[node])
                    nodecount-=1
                
            
        # def compute_height(self):
        #         # Replace this code with a faster implementation
        #         maxHeight = 0
        #         for vertex in range(self.n):
        #                 height = 0
        #                 i = vertex
        #                 while i != -1:
        #                         height += 1
        #                         i = self.parent[i]
        #                 maxHeight = max(maxHeight, height);
        #         return maxHeight;

def main():
  tree = TreeHeight()
  tree.read()
#   print(tree.nodes)
  print(tree.compute_height())

threading.Thread(target=main).start()