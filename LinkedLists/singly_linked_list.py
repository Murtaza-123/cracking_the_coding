class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singly_linked_list:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data,"--->",end = " ")
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
            total +=1
            n = n.next
        middle = total//2-1
        return middle

def list_into_linked_list(input_list):
    empty_list = singly_linked_list()
    for item in input_list:
        empty_list.insert(item)
    return empty_list




print(list_into_linked_list([]).middle_2())
print(list_into_linked_list([1,2]).middle_2())
print(list_into_linked_list([1,2,3,4]).middle_2())
print(list_into_linked_list([1,2,3,4,5,6]).middle_2())
print(list_into_linked_list([15,2,30,4,5,87,34,65]).middle_2())
print(list_into_linked_list([15,2,30,4,5,23,45,77,21,43,65,88]).middle_2())

