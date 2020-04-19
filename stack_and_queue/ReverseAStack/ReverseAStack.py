'''
Author : lky
Date   : 2020/04/17

題目: 
    利用Recursive 逆序一個stack，不借助別的資料結構。
做法:
    ->把最底下的人拿出來返回，然後“最後”push進去stack
    這邊有兩件事要做
    1. 最下面要返回上來，依次返回，所以其實返回過後就要刪除此元素。
    2. 如何把返回的元素，”最後才push“？
        其實這就是遞歸的思想->把動作1 一直recursive 就會得到最上層要返回的人 依次push進去。
    
    實現兩個recursive
    recursive 1:
        把stack最底下元素刪除， 並且返回該元素。
    recursive 2:
        把recursive 1的值先保存，然後少了最下層元素的stack繼續recursive 1 直到Stack為空push進去stack
'''

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack):
            return self.stack.pop()
        else:
            return None
            
    def top(self) -> int:
        if len(self.stack):
            return self.stack[len(self.stack) - 1]
        return None
    def empty(self)->bool:
        return False if len(self.stack) else True
     
def getAndRemoveLastElement(stack):
    res = stack.pop()
    if stack.empty():
        return res
    last = getAndRemoveLastElement(stack)
    stack.push(res)
    return last
    
def reverse(stack):
    if stack.empty():
        return
    i = getAndRemoveLastElement(stack)
    reverse(stack)
    stack.push(i)
                
stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)

reverse(stack)

print (stack.top())