
def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.max_stack[-1]:
            self.max_stack.pop()
        return value

    def get_max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]


class MaxQueue:
    def __init__(self):
        self.enqueue_stack = MaxStack()
        self.dequeue_stack = MaxStack()

    def enqueue(self, value):
        self.enqueue_stack.push(value)

    def dequeue(self):
        if not self.dequeue_stack.stack:
            while self.enqueue_stack.stack:
                self.dequeue_stack.push(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def get_max(self):
        max_enq = self.enqueue_stack.get_max()
        max_deq = self.dequeue_stack.get_max()

        if max_enq is None and max_deq is None:
            return None
        elif max_enq is None:
            return max_deq
        elif max_deq is None:
            return max_enq
        else:
            return max(max_enq, max_deq)


def max_in_sliding_window(sequence, m):
    result = []
    queue = MaxQueue()

    for i in range(len(sequence)):
        queue.enqueue(sequence[i])

        if i >= m - 1:
            result.append(queue.get_max())
            queue.dequeue()

    return result


# Example usage:
sequence = [1, 3, -1, -3, 5, 3, 6, 7]
m = 3
result = max_in_sliding_window(sequence, m)
print(result)

    
if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))
