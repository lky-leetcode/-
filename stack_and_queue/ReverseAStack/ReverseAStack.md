![Language](https://img.shields.io/badge/Language-Python%20%26%20C-orange) ![Update](https://img.shields.io/badge/Update-daily-brightgreen) 

# 《僅用Recursive Function Reverse A Stack》
* 利用Recursive 逆序一個stack，不借助別的資料結構。

想法
---

    把最底下的人拿出來返回，然後“最後”push進去stack
    這邊有兩件事要做
    1. 最下面要返回上來，依次返回，所以其實返回過後就要刪除此元素。
    2. 如何把返回的元素，”最後才push“？
        其實這就是遞歸的思想->把動作1 一直recursive 就會得到最上層要返回的人 依次push進去。
    
    實現兩個recursive
    recursive 1:
        把stack最底下元素刪除， 並且返回該元素。
    recursive 2:
        把recursive 1的值先保存，然後少了最下層元素的stack繼續recursive 1 直到Stack為空push進去stack

訪問Stack最末端

![](./ReverseAStack.png)

solution 
---

### [Python solution ](./ReverseAStack.py)

### [C++ solution](./)
