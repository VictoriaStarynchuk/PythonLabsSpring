from transistor import Transistor
from doubly_linked_list import DoublyLinkedList

if __name__ == '__main__':
    list = DoublyLinkedList()
    list.add_node(Transistor("p-n-p", "GBQ", 200, 200))
    list.add_node_to_back(Transistor("p-n-p-n", "GBQ", 100, 100))
    list.add_node_to_back(Transistor("p-n-p-n", "DIY", 150, 10))
    list.print_list()
    print()
    print("Transistors with certain model: \n")
    list.print_by_model("GBQ")
    print()
    list.sort_by_selection()
    print("Transistors sorted by type and current max: \n")
    list.print_list()
    print()
    list.delete_node_at_start()
    print("List after node deleting : \n")
    list.print_list()




