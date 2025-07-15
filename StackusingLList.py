class StackNode:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedListStack:
    def __init__(self):
        self.top=None

    def is_empty(self):
        return self.top is None

    def push(self,value):
        new_node = StackNode(value)
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop from empty stack!")
        popped_value=self.top.value
        self.top=self.top.next
        return popped_value

    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek on empty stack!")
        return self.top.value

    def display(self):
        current=self.top
        values=[]
        while current:
            values.append(str(current.value))
            current = current.next
        print("Stack from top to bottom:","->".join(values))

if __name__ == "__main__":
    stack_ll= LinkedListStack()
    stack_ll.push(5)
    stack_ll.push(10)
    stack_ll.push(15)

    stack_ll.display()

    print("Peek top:",stack_ll.peek())

    print("Pop:",stack_ll.pop())
    stack_ll.display()


