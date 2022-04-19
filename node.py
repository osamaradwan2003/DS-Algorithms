# crate node datatype

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        self.iter = None

    def type(self):
        return type(self.data)

    def __str__(self) -> str:
        return str(self.data)

    def __len__(self) -> int:
        if hasattr(self.data, "__iter__"):
            return len(self.data)
        return len(str(self.data))
