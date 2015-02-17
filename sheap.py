from operator import lt, gt


class MinHeap: pass
class MaxHeap: pass


class SHeap:
    def __init__(self, iterable=[], key=lambda x: x, kind=MinHeap):
        self.array = []
        self.index = {}
        self.push_many(iterable)
        self.key = key
        self.kind = kind

    def __get_parent_pos__(self, i):
        if i == 0:
            return -1
        else:
            return int((i - 1) / 2)


    def __get_child_pos__(self, i):
        left_child_pos, right_child_pos = 2 * i + 1, 2 * i + 2
        l_ok = left_child_pos < len(self.array)
        r_ok = right_child_pos < len(self.array)
        both_ok = l_ok and r_ok
        if l_ok and not r_ok:
            return left_child_pos
        elif r_ok and not l_ok:
            return right_child_pos
        elif both_ok:
            cmp_func = lt if self.kind == MinHeap else gt
            left_key_val, right_key_val = self.key(self.array[left_child_pos]), self.key(self.array[right_child_pos])
            if cmp_func(self.array[left_child_pos], self.array[right_child_pos]):
                return left_child_pos
            else:
                return right_child_pos
        return -1


    def __swap__(self, pos, otherPos):
        self.array[pos], self.array[otherPos] = self.array[otherPos], self.array[pos]
        temp = self.index[self.array[pos]]
        self.index[self.array[pos]] = self.index[self.array[otherPos]]
        self.index[self.array[otherPos]] = temp

    def __str__(self):
        return str(self.array)


    def __bubble_up__(self):
        pos = len(self.array) - 1
        self.__bubble__(pos, self.__get_parent_pos__, lt if self.kind == MinHeap else gt)

    def __bubble_down__(self):
        pos = 0
        self.__bubble__(pos, self.__get_child_pos__, gt if self.kind == MinHeap else lt)


    def __bubble__(self, pos, bubble_func, cmp_func):
        otherPos = bubble_func(pos)
        while otherPos != -1 and cmp_func(self.key(self.array[pos]), self.key(self.array[otherPos])):
            self.__swap__(pos, otherPos)
            pos = otherPos
            otherPos = bubble_func(pos)

    def push(self, node):
        self.array.append(node)
        self.index[node] = len(self.array) - 1
        self.__bubble_up__()


    def push_many(self, l):
        for el in l:
            self.push(el)

    def pop(self):
        if len(self.array) == 0:
            return
        node = self.array[0]
        last_node = self.array[-1]
        del self.index[node]
        self.array[0] = last_node
        self.index[last_node] = 0
        del self.array[-1]
        self.__bubble_down__()
        return node

    def update(self, node, newNode):
        pos = self.index[node]
        old_key_val = self.key(node)
        new_key_val = self.key(newNode)
        if new_key_val != old_key_val:
            self.array[pos] = newNode
            del self.index[node]
            self.index[newNode] = pos
        if self.kind == MinHeap:
            if new_key_val > old_key_val:
                self.__bubble__(pos, self.__get_child_pos__, gt)
            elif new_key_val < old_key_val:
                self.__bubble__(pos, self.__get_parent_pos__, lt)
        elif self.kind == MaxHeap:
            if new_key_val > old_key_val:
                self.__bubble__(pos, self.__get_parent_pos__, gt)
            elif new_key_val < old_key_val:
                self.__bubble__(pos, self.__get_child_pos__, lt)