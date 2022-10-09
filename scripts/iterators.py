class InvalidOperationError(Exception):
    def __str__(self):
        return "Method not allowed on empty collection"


class Queue:

    def __init__(self, front=None, rear=None, collection=None):
        self.front = front
        self.rear = rear
        self.collection = collection
        self.len_ = 0
        if collection:
            for item in collection:
                self.enqueue(item)

    def __iter__(self):

        def value_generator():
            for i in range(len(self.collection)):
                curr = self.dequeue()
                self.enqueue(curr.value)
                yield curr.value

        return value_generator()

    def __eq__(self, other):

        return list(self) == list(other)

    def __str__(self):
        output = ""
        for value in self:
            # needs to be in reversed order originally to display properly later
            output += f" ) {value} ( >= "

        # output string needs to be reversed with slicing to display queue order properly
        return "Rear " + output[:len(output) - 3][::-1] + " Front"

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node

        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        self.len_ += 1

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError
        temp = self.front
        if self.front.next:
            self.front = self.front.next
            temp.next = None
        else:
            self.front = None
        self.len_ -= 1
        return temp


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


if __name__ == "__main__":
    q = Queue(collection=[1, 2, 3, 4])
    print(q)
