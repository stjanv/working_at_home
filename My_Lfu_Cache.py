import time


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class Val:
    def __init__(self, value, count_usage):
        self.value = value
        self.count_usage = count_usage

    def __call__(self, *args, **kwargs):
        taple = (self.value, self.count_usage)
        return taple

    def __str__(self):
        return '{}'.format(self.__call__())


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
            time.sleep(1)
            return print('Cached...{} {}'.format(args, self.cache[args]))
        if len(self.cache) == self.cache_size:
            node = self.sort()
            self.remove(node)
            del self.cache[node.key]
        res = self.func(*args, **kwargs)
        value = Val(res, 1)
        self.cache[args] = value
        node = Node(args, value)
        self.add(node)
        #ok=self.sort()
        return print(value)

    def sort(self):
        current1 = self.head
        current2 = current1.next
        while current2.next is not None:
            if current1.val.count_usage > current2.val.count_usage :
                current1=current2
                current2=current2.next
                node=current1
            else:
                current1 = current2
                current2 = current2.next
                node=current2

        return node




    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def update(self, node):
        node.val.count_usage += 1

    def llist(self, args):
        current = self.head
        while True:
            if current.key == args:
                node = current
                self.update(node)
                break
            else:
                current = current.next


@My_Lru_Cache
def func(n):
    print('Computing...{}^4'.format(n))
    time.sleep(1)
    res = n ** 4
    return res


func(2)
func(2)
func(2)
func(2)
func(3)
func(3)
func(6)
func(6)
func(6)
func(6)
func(6)
func(5)
func(2)
