from collections import deque

# Queue for RRA

class RRAQueue:
    def __init__(self):
        self.queue = deque()
        print("RRA Queue Initialized")

    def add_person(self, name):
        self.queue.append(name)
        print(f"Added to RRA queue: {name}")

    def serve_two(self):
        if self.queue:
            for _ in range(2):
                if self.queue:
                    served = self.queue.popleft()
                    print(f"Served: {served}")
        else:
            print("No one in the queue to serve.")

    def next_person(self):
        if self.queue:
            return f"Next in RRA queue: {self.queue[0]}"
        return "No one in RRA queue."


# ---------------------------
# Queue for BK ATM
# ---------------------------
class BKQueue:
    def __init__(self):
        self.queue = deque()
        print("BK ATM Queue Initialized")

    def add_client(self, name):
        self.queue.append(name)
        print(f"Added to BK ATM queue: {name}")

    def third_served(self):
        if len(self.queue) >= 3:
            return f"The third client to be served is: {self.queue[2]}"
        return "Less than 3 clients in the queue."

    def show_queue(self):
        return f"Current BK ATM queue: {list(self.queue)}"


# ---------------------------
# Circular Queue for Buses
# ---------------------------
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        print("Circular Queue for Nyabugogo buses Initialized")

    def enqueue(self, bus):
        if (self.rear + 1) % self.size == self.front:
            return "Queue is full! No space for another bus."
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = bus
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = bus
        return f"Bus {bus} added."

    def dequeue(self):
        if self.front == -1:
            return "Queue is empty! No bus to remove."
        removed_bus = self.queue[self.front]
        if self.front == self.rear:  # only one bus left
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return f"Bus {removed_bus} removed."

    def display(self):
        if self.front == -1:
            return "Queue is empty."
        elements = []
        i = self.front
        while True:
            elements.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        return f"Buses in queue: {elements}"


# ---------------------------
# Example Usage
# ---------------------------

# RRA Queue
rra = RRAQueue()
rra.add_person("people1")
rra.add_person("people2")
rra.add_person("people3")
rra.add_person("people4")
rra.add_person("people5")
print(rra.next_person())
rra.serve_two()
print(rra.next_person(), "\n")

# BK ATM Queue
bk = BKQueue()
bk.add_client("client1")
bk.add_client("client2")
bk.add_client("client3")
bk.add_client("client4")
bk.add_client("client5")
bk.add_client("client6")
print(bk.show_queue())
print(bk.third_served(), "\n")

# Circular Queue for Nyabugogo Buses
cq = CircularQueue(4)
print(cq.enqueue("Bus 1"))
print(cq.enqueue("Bus 2"))
print(cq.enqueue("Bus 3"))
print(cq.enqueue("Bus 4"))  # Queue full here
print(cq.display())
print(cq.dequeue())
print(cq.enqueue("Bus 5"))  # Bus 5 takes free space
print(cq.display())
