class Node(object):
    def __init__(self, element=-1):
        self.element = element
        self.next = None
    def __repr__(self):
        return str(self.element)

"""
链表
存取是 O(1)
插入删除也是 O(1)

python list 有两个部件
    数组 存储数据在链表中的地址
    链表 实际存储数据
"""
class LinkedList(object):
    def __init__(self):
        self.head = None

    def log_list(self):
        node = self.head
        s = ''
        while node is not None:
            s += (str(node.element) + ' > ')
            node = node.next
        print(s)

    # O(1)
    def is_empty(self):
        return self.head is None

    def length(self):
        index = 0
        node = self.head
        while node is not None:
            index += 1
            node = node.next
        return index

    def find(self, element):
        node = self.head
        while node is not None:
            if node.element == element:
                break
            node = node.next
        return node

    def _node_at_index(self, index):
        i = 0
        node = self.head
        while node is not None:
            if i == index:
                return node
            node = node.next
            i += 1
        return None

    def element_at_index(self, index):
        node = self._node_at_index(index)
        return node.element

    # O(n)
    def insert_before_index(self, position, element):
        before_node = self._node_at_index(position-1)
        cur_node =  self._node_at_index(position)
        # 在中间
        if before_node is not None:
            node = Node(element)
            node.next = cur_node
            before_node.next = node
        else:
            node = Node(element)
            node.next = cur_node
            
        return node

    # O(n)
    def insert_after_index(self, position, element):
        cur_node =  self._node_at_index(position)
        after_node = self._node_at_index(position+1)
        if after_node is not None:
            node = Node(element)
            cur_node.next = node
            node.next = after_node
        else:
            node = Node(element)
            cur_node.next = node

        return node

    # O(1)
    def first_object(self):
        node = self._node_at_index(0)
        return node

    # O(n)
    def last_object(self):
        node = self._node_at_index(self.length()-1)
        return node

    # O(n)
    def append(self, element):
        node = Node(element)
        if self.head is None:
            self.head.next = node
        else:
            last_node = self.last_object()
            last_node.next = node
            node.front = last_node

def test():
    li = LinkedList()
    li.head = Node(1)
    for i in range(2, 6):
        li.append(i)
    li.log_list()
    print('first_object', li.first_object())
    print('last_object', li.last_object())
    
    li.insert_after_index(2,8)
    print('insert_after_index')
    li.log_list()

    li.insert_before_index(2,9)
    print('insert_before_index')
    li.log_list()
    
    print('element_at_index',  li.element_at_index(2))

    print('find',  li.find(8))

    print('length',  li.length())

    print('is_empty', li.is_empty())
    

if __name__ == '__main__':
    test()
