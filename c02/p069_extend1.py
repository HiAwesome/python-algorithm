"""
Python列表解析式
https://codingpy.com/article/python-list-comprehensions-explained-visually/
"""
numbers = [1, 2, 3, 4, 5]

# 如果你熟悉函数式编程（functional programming），你可以把列表解析式看作为结合了filter函数与map函数功能的语法糖：
a_list = list(map(lambda n: n * 2, filter(lambda n: n % 2 == 1, numbers)))
b_list = [n * 2 for n in numbers if n % 2 == 1]

print(a_list, b_list, a_list == b_list, '\n')

"""
每个列表解析式都可以重写为for循环，但不是每个for循环都能重写为列表解析式。
掌握列表解析式使用时机的关键，在于不断练习识别那些看上去像列表解析式的问题
（practice identifying problems that smell like list comprehensions）。
如果你能将自己的代码改写成类似下面这个for循环的形式，那么你也就可以将其改写为列表解析式：
:::python
new_things = []
for ITEM in old_things:
    if condition_based_on(ITEM):
        new_things.append("something with " + ITEM)

你可以将上面的for循环改写成这样的列表解析式：

:::python
new_things = ["something with " + ITEM for ITEM in old_things if condition_based_on(ITEM)]
"""

c_list = []
for n in numbers:
    c_list.append(n * 2)

d_list = [n * 2 for n in numbers]

print(c_list, d_list, c_list == d_list, '\n')

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

e_list = []
for row in matrix:
    for n in row:
        e_list.append(n)
# 如果要在列表解析式中处理嵌套循环，请记住for循环子句的顺序与我们原来for循环的顺序是一致的。
f_list = [n for row in matrix for n in row]

print(e_list, f_list, e_list == f_list, '\n')

words = ['tom', 'smith', 'jack']

a_set = set()
for w in words:
    a_set.add(w[0])

b_set = {w[0] for w in words}

print(a_set, b_set, a_set == b_set, '\n')

source_map = {'tom': 88, 'jack': 72, 'jenny': 99}

a_map = {}
for k, v in source_map.items():
    a_map[v] = k

b_map = {v: k for k, v in source_map.items()}

print(a_map, b_map, a_map == b_map, '\n')

"""
还要注意可读性
你有没有发现上面的列表解析式读起来很困难？
我经常发现，如果较长的列表解析式写成一行代码，那么阅读起来就非常困难。

不过，还好Python支持在括号和花括号之间断行。
"""

b_list_easy_to_read = [
    n * 2
    for n in numbers
    if n % 2 == 1
]
print(b_list_easy_to_read, '\n')

f_list_easy_to_read = [
    n
    for row in matrix
    for n in row
]
print(f_list_easy_to_read, '\n')

b_set_easy_to_read = {
    w[0]
    for w in words
}
print(b_set_easy_to_read, '\n')

b_map_easy_to_read = {
    v: k
    for k, v in source_map.items()
}
print(b_map_easy_to_read, '\n')

"""
[2, 6, 10] [2, 6, 10] True 

[2, 4, 6, 8, 10] [2, 4, 6, 8, 10] True 

[1, 2, 3, 4, 5, 6, 7, 8, 9] [1, 2, 3, 4, 5, 6, 7, 8, 9] True 

{'j', 't', 's'} {'j', 't', 's'} True 

{88: 'tom', 72: 'jack', 99: 'jenny'} {88: 'tom', 72: 'jack', 99: 'jenny'} True

[2, 6, 10] 

[1, 2, 3, 4, 5, 6, 7, 8, 9] 

{'t', 's', 'j'} 

{88: 'tom', 72: 'jack', 99: 'jenny'} 
"""
