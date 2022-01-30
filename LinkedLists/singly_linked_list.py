class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, "--->", end=" ")
            temp = temp.next

    def middle(self):
        if self.head is None:
            print("Singly linked list is empty")
            return
        i = self.head
        j = self.head
        while j and j.next is not None:
            i = i.next
            j = j.next.next
        return i.data

    def middle_2(self):
        if self.head is None:
            return
        total = 0
        n = self.head
        while n is not None:
            total += 1
            n = n.next
        middle = total // 2
        return middle

    def remove_middle(self, node):
        node.data = node.next.data
        node.next = node.next.next


def list_into_linked_list(input_list):
    empty_list = SinglyLinkedList()
    for item in input_list:
        empty_list.insert(item)
    return empty_list


def main():
    lll = list_into_linked_list(["a", "e", "d", "c", "b"])
    lll.remove_middle(lll.head.next.next)
    lll.print_list()


if __name__ == "__main__":
    main()
