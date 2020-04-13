'''
Author : lky
Date   : 2020/04/10

題目: 
    實現一個具有getMin功能的stack，且時間是O(n)
做法:
    實作兩個stack 分別功能是：存入當前資料進去stack，純粹的data，
    另外的stack是存minStack，如果當前資料比minStack的top元素小，
    則入stack，否則不存入stack。
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minStack) == 0 or x <= self.minStack[len(self.minStack) - 1]:
            self.minStack.append(x)

    def pop(self) -> None:
        if len(self.stack):
            if self.getMin() == self.stack[len(self.stack) - 1]:
                self.minStack.pop()
            self.stack.pop()
        else:
            return None

    def top(self) -> int:
        if len(self.stack):
            return self.stack[len(self.stack) - 1]
        return None
    
    def getMin(self) -> int:
        if len(self.minStack):
            return self.minStack[len(self.minStack) - 1]
        return None