import cmath

'''
1. 把f(x)作用在list的每一个元素并把结果生成一个新的list

  list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

2. reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

   reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

3 filter 用于过滤   和map类似，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

4 sort  排序


          sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：reverse表示反向
          sorted([36, 5, -12, 9, -21], key=abs  ，reverse=True)
'''


#   闭包

def count():
    L = []
    '''当外函数执行到内函数时,把 内函数当作   一个对象  而已 ，所以会把外面的循环执行完'''
    for i in range(1, 4):
        def click():
            return i * i
    L.append(click())
    return L


# 所以无论如何结果都是9
f1 = count()

print(f1)

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


''' 需求 ： 每调用一次 返回count + 1'''


def count2():
    def fs():
        i=0
        while True:
            i = i + 1
            yield i

    it = fs()
    def count3():
        return next(it)
    return count3


f5 = count2()
f4 = count2()
print(f4())
print(f5())



