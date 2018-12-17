"""
pop 是 stack 的两个操作之一
push 入栈
pop 出栈

现在我们有这么 3 个函数
append 添加一个元素到末尾
prepend 添加一个元素到开头
pop 删除并返回末尾的元素

prepend + pop 就实现了 队列 的 入队(enqueue)和出队(dequeue)操作
append + pop 就实现了 栈 的 入栈(push) 和 出栈(pop)操作
"""

class Node():
    def __init__(self, element=None):
        self.e = element
        self.next = None

def append(node, element):
    """
    我们往 node 的末尾插入一个元素
    :param node: 是一个 Node 实例
    :param element: 任意类型的元素
    """
    n = node
    # 这里不应该使用 while n.next: 这样的隐含类型转换来判定
    while n.next is not None:
        n = n.next
    # n 现在是最后一个元素
    new_node = Node(element)
    n.next = new_node

def prepend(head, element):
    """
    往 node 的前面插入一个元素
    """
    n = Node(element)
    n.next = head.next
    head.next = n

def pop(head):
    """
    删除并返回末尾的元素
    """
    tail = head 
    while tail.next is not None:
        tail = tail.next
    # 现在 tail 是最后一个元素了
    n = head
    while n.next is not tail:
        n = n.next
    # 现在 n 是 tail 之前的元素了
    n.next = None
    return tail.e


def log_list(node):
    n = node
    s = ''
    while n is not None:
        s += (str(n.e) + ' > ')
        n = n.next
    print(s)


# 组成队列
head = Node()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3
head.next = n1
log_list(n1)

# 测试
append(n1, 'abc')
log_list(n1)

prepend(head, 'hello')
log_list(head)

print('pop head ', pop(head))
log_list(head)



