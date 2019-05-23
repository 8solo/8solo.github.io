- data model,
- len,
- magic method/dunder method,
- __getitem__,
- with 上下文管理,
- collections,
- collections.namedtuple,
- __init__,
- __len__,
- __getitem__,
- difference between method and function,
- class,

- method_descriptor and builtin_function_or_method 描述符是什么?
答:未实例化对象方法的 type 是method_descriptor, 实例化对象方法的 type 是builtin_function_or_method.
example:
```Shell
In [1]: t = tuple # 未实例化 tuple 对象

In [2]: type(t)
Out[2]: type

In [3]: t.count?
Docstring: T.count(value) -> integer -- return number of occurrences of value
Type:      method_descriptor

In [4]: t = tuple([1,2,3])

In [5]: type(t)
Out[5]: tuple

In [6]: t.count?
Docstring: T.count(value) -> integer -- return number of occurrences of value
Type:      builtin_function_or_method
```

- 属性和方法?

- collections.namedtuple 用来构建只有*少数属性*但是没有*方法*的*对象*, 比如数据库条目.(page4)
namedtuple 有方法的呀,为何这么说?
答:

- __getitem__ 方法和 index 的关系是什么?
答:
```Shell
In [10]: tuple.__getitem__?
Signature:      tuple.__getitem__(self, key, /)
Call signature: tuple.__getitem__(*args, **kwargs)
Type:           wrapper_descriptor
String form:    <slot wrapper '__getitem__' of 'tuple' objects>
Namespace:      Python builtin
Docstring:      Return self[key].

In [12]: t
Out[12]: (1, 2, 3)

In [13]: t.__getitem__?
Signature:      t.__getitem__(key, /)
Call signature: t.__getitem__(*args, **kwargs)
Type:           method-wrapper
String form:    <method-wrapper '__getitem__' of tuple object at 0x108330d80>
Docstring:      Return self[key].
```
从上述 doc 内容可以看出,  实例化后 self[index] 实际调用的 method 为self.__getitem__(index) 方法.

- <slot wrapper> 和 <method-wrapper> 的区别?
答:

- 支持 indexing 的数据模型,数据模型元素命名技巧:
法一, 给 indexing 的 数字设置别名,  如下 NAME = 0
```Shell
In [33]: NAME
Out[33]: 0

In [34]: NAME, AGE, = 0, 1

In [35]: user01[0]
Out[35]: 'haha'

In [36]: user01[NAME]
Out[36]: 'haha'

In [37]: NAME
Out[37]: 0

In [38]: 0
Out[38]: 0
```
法二, 使用collections.namedtuple
待续

- map的用法：
Init signature: map(self, /, *args, **kwargs)
Docstring:
map(func, *iterables) --> map object

Make an iterator that computes the function using arguments from
each of the iterables.  Stops when the shortest iterable is exhausted.
Type:           type
Subclasses:
example:
```Shell
In [4]: a = [1,2,3]

In [5]: def ad(d):
   ...:     return 1+d
   ...:

In [6]: b = map(ad, a)

In [7]: for i in b:
   ...:     print(i, type(i))
   ...:
2 <class 'int'>
3 <class 'int'>
4 <class 'int'>

In [8]: b = map(str, a)

In [9]: for i in b:
   ...:     print(i, type(i))
   ...:
1 <class 'str'>
2 <class 'str'>
3 <class 'str'>
```

- sys.intern用法:
intern(string) -> string

``Intern'' the given string.  This enters the string in the (global)
table of interned strings whose purpose is to speed up dictionary lookups.
Return the string itself or the previously interned string object with the
same value.
Type:      builtin_function_or_method
将特定的 string 转化为全局范围内的内建字符串,以加速字典查询.

- __slot__用法:


- __new__用法:
