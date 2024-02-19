'''
Your task is to implement push and pop methods for a Stack structure.

The push method will accept a value as parameter and adds a new (class) Node at the top of
the stack with the given value. The pointers and size should be updated accordingly.
This method does not return anything.

The pop method will remove the top Node element from the stack and return its value. The
pointers and size should be updated accordingly. This method does not accept any
parameters. If the stack is empty, the method should return None.

You'll need to only modify the push() and pop() methods. Everything else should
remain as is.
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        current_node = self._top
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Stack ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        """
        Add a Node element containing data to the stack. This method creates the class Node
        element and store the data.

        Parameters:
        - 'data': Value/data being added

        Returns: None
        """
        # YOUR CODE GOES HERE
        return

    def pop(self):
        """
        Remove the top Node from the stack and return its content. This method removes the
        class Node element from the stack and returns the data stored in the Node element.

        Parameters: None

        Returns: The value/data of the Node or None if stack is empty
        """
        # YOUR CODE GOES HERE
        return

def main():
    mystack = Stack()
    for c in 'ABCDEFG':
        mystack.push(c)
        print(mystack)
    for _ in 'ABC':
        val = mystack.pop()
        print(val, mystack)
    for c in 'HIJ':
        mystack.push(c)
        print(mystack)
    for _ in 'DEFGHIJK':
        val = mystack.pop()
        print(val, mystack)

if __name__ == "__main__":
    main()