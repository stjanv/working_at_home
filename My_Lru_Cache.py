import time
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class My_Lru_Cache:
    cache_size = 3

    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __call__(self, *args, **kwargs):
        if args in self.cache:
            self.llist(args)
            return print('Cached...{} {}'.format(args,self.cache[args]))
        if len(self.cache) == self.cache_size:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]
        res = self.func(*args,**kwargs)
        self.cache[args] = res
        node = Node(args,res)
        self.add(node)
        return res


    def remove(self,node):
        p=node.prev
        n=node.next
        p.next = n
        n.prev = p

    def add(self,node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


    def llist(self,args):
        current = self.head
        while True:
            if current.key == args:
                node = current
                self.remove(node)
                self.add(node)
                break
            else:
                current = current.next

@My_Lru_Cache
def func(n):
    print('Computing...{}^4'.format(n))
    res = n**4
    return res


func(2)
func(4)
func(5)
func(2)
func(3)
func(1)
func(6)
func(6)
func(3)
func(5)