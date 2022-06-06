from lab10.node import Node


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def add_node_to_back(self, data) -> None:
        new_node = Node(data)
        last = self.head
        new_node.next = None
        if self.head is None:
            new_node.previous = None
            self.head = new_node
            return
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def sort_by_selection(self) -> None:
        tmp = self.head
        while tmp is not None:
            tmp1 = tmp.next
            while tmp1 is not None:
                if tmp1.data.current_max < tmp.data.current_max:
                    tmp1.data.current_max, tmp.data.current_max = tmp.data.current_max, tmp1.data.current_max
                tmp1 = tmp1.next
            tmp = tmp.next

    def print_by_model(self, model: str) -> None:
        node = self.head
        while node is not None:
            if node.data.model == model:
                print(node.data)
            node = node.next

    def add_node(self, data) -> None:
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def print_list(self) -> None:
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def find_by_key(self, key) -> bool:
        node = self.head
        while node is not None:
            if node.data == key:
                return True
            node = node.next
        return False

    def delete_node_at_start(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.prev_node = None

    def delete_list(self):
        node = self.head
        if self.head is None:
            print("List is empty")
            return

        while node is not None:
            node.data = None
            node = node.next
