# python 赋值的顺序
## 原来的验证方法
```python
class Node:
    def __init__(self, value):
        self.val = value
        self.pre = self.next = None

# 生成一些对象
ojs = list()
for i in range(5):
    ojs.append(Node(i))
# 将对象的尾部相连
for i in range(4):
    ojs[i].next = ojs[i+1]
# 将对象的头部相连
for i in range(1, 5):
    ojs[i].pre = ojs[i-1]

d = Node(666)

ojs[4].pre.pre = ojs[4].pre = d 
print(ojs[4].pre.pre == d.pre == None) # true

ojs[4].pre = ojs[4].pre.pre = d 
print(ojs[4].pre.pre == d) # true

```
- 结论:
  -  从左到右

## 重新整理的验证方法
1. 猜测赋值顺序
   - 把值赋给最右边的变量，然后从右到左逐个赋值
   - 把值赋给最左边的变量，然后从左到右逐个赋值

2. 第一次尝试
```Python
a = b = c = 1
```
- 结论：
  - 不能排除任何猜测

3. 第二次尝试
```Python
L = L[len(L):]=L[len(L):] = [4]
```
- 在没有给L赋值的情况下，也能运行`len(L)`,说明是从右到左
- 最后L = [4, 4, 4, 4]
- 可以通过dis查看
  ```Python
  In [9]: import dis
  
  In [10]: dis.dis("L = L[len(L):]=L[len(L):] = [4]")
  1           0 LOAD_CONST               0 (4)
              2 BUILD_LIST               1
              4 DUP_TOP
              6 STORE_NAME               0 (L)
              8 DUP_TOP
             10 LOAD_NAME                0 (L)
             12 LOAD_NAME                1 (len)
             14 LOAD_NAME                0 (L)
             16 CALL_FUNCTION            1
             18 LOAD_CONST               1 (None)
             20 BUILD_SLICE              2
             22 STORE_SUBSCR
             24 LOAD_NAME                0 (L)
             26 LOAD_NAME                1 (len)
             28 LOAD_NAME                0 (L)
             30 CALL_FUNCTION            1
             32 LOAD_CONST               1 (None)
             34 BUILD_SLICE              2
             36 STORE_SUBSCR
             38 LOAD_CONST               1 (None)
             40 RETURN_VALUE
  ```
  - dis:
    - LOAD_CONST(consti): Pushes co_consts[consti] onto the stack.
    - BUILD_LIST(count): Creates a list.
    - DUP_TOP——Duplicates the reference on top of the stack.


---
### references:
- [Python 的赋值坑 ， a=b=c=1???](https://www.v2ex.com/amp/t/443384)
- [dis的一些说明](https://docs.python.org/3/library/dis.html)